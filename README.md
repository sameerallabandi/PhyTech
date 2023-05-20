![WhatsApp Image 2023-04-14 at 10 47 15 PM](https://user-images.githubusercontent.com/75690804/232216346-0f076efc-4441-45cb-a1b1-138935bdac50.jpeg)


# PhyTech
### Your one-stop solution for agriculture automation, plant identification, and monitoring insights!

#### Collaborators: 
1. Haseeb Kollorath
2. Sameera Rallabandi
3. Insaaf Sulaimaan
4. Jacob Charles Joy

#### INDEX:
1. Overview
2. Smart Plant Pot - Flaura
3. Android App
4. Plant Identifying CNN
5. Plant Disease Detection Model
6. Architecture
7. Logs
8. Conclusion

#### 1. Overview:
The goal of this project is to create a smart plant pot that automatically waters plants based on the soil moisture level and tracks the change in water usage over different seasons using temperature and humidity data. The project will use data science techniques to analyze the collected data and optimize the watering process for maximum plant growth and health. Additionally, an android app will be developed to display the data insights to the user, and a plant identifying classifier model and a plant disease detection model will be added to assist smaller scale plant parents.


#### 2. Smart Plant Pot (Flaura):
To achieve the goal of the project, we will use a microcontroller, sensors, and a water pump to automate the watering process. The microcontroller will read data from the soil moisture sensor, temperature sensor, and humidity sensor, and use this data to determine when to water the plants. If the soil moisture level is too low, the microcontroller will activate the water pump to water the plants.
 
In addition to the watering process, the system will also collect data on temperature and humidity levels. This data will be used to analyze the change in water usage over different seasons. By understanding how temperature and humidity affect water usage, we can optimize the watering process to conserve water while still providing the plants with the necessary moisture they need to grow.
 
To analyze the collected data, we will use various data science techniques such as data visualization and statistical analysis. Data visualization techniques will help us to understand the relationship between soil moisture levels, temperature, and humidity. We can use statistical analysis to determine the optimal moisture level for each plant and adjust the watering process accordingly.

##### Parts Used:
1. NodeMCU ESP32
2. DHT 11 - Temperature and Humidity sensor
3. Capacitive Soil Moisture Sensor
4. Mosfet
5. 3.7V Battery
6. 3.7V Water pump
7. 3D Printed Plant Pot
8. PVC Water Pipes

#### 3. Android App:
To display the data insights to the user and control the hardware, we will develop an android app. The app will display real-time data on the soil moisture level, temperature, humidity, trigger level and pump status. The app will also display graphs and charts to visualize the change in water usage over different seasons. The user can use this data to adjust the watering process for their plants or to monitor the health of their plants.

#### 4. Plant Identifying CNN:
To assist smaller scale plant parents, we will also integrate a plant identifying classifier model. This feature will allow users to upload an image of their plant to the app and get a short description of plant care details. The plant identifying classifier model will use a CNN to identify the plant species and provide information on how to care for that specific plant. This will be especially helpful for new plant owners who may not be familiar with the specific care requirements for their plants. 

- Methdology: 
In the proposed method we have integrated a pretrained inception_resnet_v2 model for plant classification. In the following model we scraped data of the 10 most common household plants, 3515 images were used for training and 386 images were used as test data. Before moving onto creating a model, a few preprocessing tasks were required. As the images were scraped from the internet, the images can be of different file formats. In order to get an accurate model we converted each image to a .jpeg file with the help of Python's in-built OS library (This is done as tensorflow only supports .jpeg,.bmp,.png files). Further, we checked for corrupted file formats by converting each image to a binary formmat and decode the imagee. If corrupted file formats are present, the image is removed from the file path. Further, data augmentation operations were performed in order to get more data and create an accurate model.

The model has 6 layers, 3 convolutional layers, a flattening layer and 2 dense layers. The model uses 'he_uniform' weight initialization method in order to make sure the weights are neither too small or too big. In the initial iterations of the model, the model seemed to get a very high accuracy(80%-90%), however when visualizing the accuracy and losses, the data was overfitted. In order to resolve this issue a L1 kernel regularizer was used with each layer and batch normalization layers were used.

In the app being created, the model would be used to predict what plant it is. The model is pushed to the AMD instance and with the following results, the app displays information on how to maintain the plant. Further, this is attatched to an IOT device that checks for soil moisture, humidity and temperature and these metrics will be displayed in the app

- Results: 
The following model for classification is able to get an accuracy of 60.7%. This is due to the low amounts of data we have used. We are looking to further improve the model by scraping for more images on the internet. However, although the accuracy is low, when using it for classification it seems to be making accurate predictions.

The model is hosted on GCP AMD compute engine. 

#### 5. Plant Disease Detection Model:
- To assist smaller scale plant parents, we will also integrate a plant disease detection model. This feature will allow users to upload an image of their plant to the app and get a short description of plant care details. The plant disease model will identify the plant disease and provide information on how to care for that specific plant. This will be especially helpful for new plant owners who may not be familiar with the specific care requirements for their plants. 

#### 6. Architecture:
- The android app has a camera feature that sends an image to the CNN model that is hosted on GCP AMD Compute engine. 
- An inference API script listens on the instance for any requests. 
- Upon getting a request, the saved model is used to make predictions on the plant type and this label is sent back as a response.
- The predcited plant can be added to the user's "virtual greenhouse". This is where the appropriate plant care details can be viewed and more importantly, the scarecrow can be attached to a plant.
- The scarecrow monitors the plant and sends the data to be visualized on the android app.

#### 7. LOGS:
##### 20/05/23: 

1. The IOT hardware is complete. features include :
- Temperature and humidity sensor.
- soil moisture sensor that tracks moisture to determine whether plants need to be watered.
- water pump that turns on depending on the trigger level set by the user. (defaulted to 30%).
- 3D printed plant pot is complete.

2. Android App:
- Login/Register page designed.
- Camera app setup to send plant image and get the relevant class label or disease back.
- Analytics page to display the response from the IOT device.
- Virtual greenhouse page has been setup.

3. Plant Identifying CNN model:
- model is able to predict plant classes.
- accuracy needs to be improved.

4.Plant Disease Detection
- model is able to detect the disease. Only general diseases have been included, plant specific diseases are going to be included in the future iterations.
- model is very accurate.

#### 8. Conclusion:
The benefits of this project are significant. By automating the watering process, we can save time and reduce the risk of overwatering or underwatering plants. This system will also help conserve water by providing the plants with the necessary moisture without wasting excess water. By tracking the change in water usage over different seasons and displaying the data insights to the user, we can optimize the watering process for maximum plant growth and health. Finally, the addition of the plant identifying classifier model will make plant care more accessible and easier for smaller scale plant parents.
 
Overall, this project will combine hardware, data science techniques, android app development, and machine learning to create a system that automates the watering process, tracks the change in water usage over different seasons, and provides plant care information to users. This system will not only save time and conserve water but also optimize the watering process for maximum plant growth and health while making plant care more accessible for everyone.

