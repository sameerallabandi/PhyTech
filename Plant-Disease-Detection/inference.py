import torch
from torch import nn
from torchvision import models
import numpy as np
from PIL import Image
import albumentations as A
from albumentations.pytorch.transforms import ToTensorV2
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import io

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

LABELS = ['Powdery', 'Healthy', 'Rust']


class PlantDiseaseModel(nn.Module):
    def __init__(self, classes=2):
        super(PlantDiseaseModel, self).__init__()
        self.model = models.resnet34(pretrained=True)

        for parameter in self.model.parameters():
            parameter.require_grad = False

        in_features = self.model.fc.in_features
        self.model.fc = nn.Sequential(
            nn.Linear(in_features=in_features, out_features=classes),
            nn.Softmax(dim=1)
        )

    def forward(self, image):
        output = self.model(image)
        return output


def single_image_test(image):
    # Load the image as a numpy array
    # image = np.array(image.convert("RGB"))
    image = np.array(image)

    # Define the augmentation pipeline
    augmentations = A.Compose([
        A.Resize(width=256, height=256),
        ToTensorV2(),
    ])
    # Apply the augmentations to the image
    augmented = augmentations(image=image)
    # Extract the tensor from the augmented dictionary
    tensor = augmented['image']
    # Add a batch dimension to the tensor
    tensor = tensor.unsqueeze(0)
    # Return tensor
    return tensor


@app.post("/upload-image")
async def upload_image(image: bytes = File(...)):
    try:
        contents = io.BytesIO(image)
        pil_image = Image.open(contents).convert('RGB')
        # Create a new instance of your model
        model = PlantDiseaseModel(classes=len(LABELS))

        # Load the saved state dictionary into the model
        model.load_state_dict(torch.load("model_w_6.pt"))
        model.eval()  # Set the model to evaluation mode

        model.eval()  # Set the model to evaluation mode
        image_tensor = single_image_test(pil_image)
        output = model(image_tensor.float())

        predicted_class_index = torch.argmax(output).item()
        predicted_class_label = LABELS[predicted_class_index]
        print(predicted_class_label)
        return {"predicted_class_name": predicted_class_label}

    except Exception as e:
        # Return an error message if an exception occurs
        return {"error": str(e)}


@app.get("/ping")
async def ping():
    return {"message": "pong"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=1234)
