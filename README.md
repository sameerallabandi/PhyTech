![WhatsApp Image 2023-04-14 at 10 47 16 PM](https://user-images.githubusercontent.com/75690804/232215711-ead46f57-e4ad-4eb3-9e20-995c3891f284.jpeg)
![WhatsApp Image 2023-04-14 at 10 47 15 PM](https://user-images.githubusercontent.com/75690804/232216346-0f076efc-4441-45cb-a1b1-138935bdac50.jpeg)


# PhyTech
### Your one-stop solution for agriculture automation, plant identification, and monitoring insights!

#### Overview:
The goal of this project is to create a system that automatically waters plants based on the soil moisture level and tracks the change in water usage over different seasons using temperature and humidity data. The project will use data science techniques to analyze the collected data and optimize the watering process for maximum plant growth and health. Additionally, an android app will be developed to display the data insights to the user, and a plant identifying classifier model will be added to assist smaller scale plant parents.
##### Main Components:
1. IOT Device
2. Android App
3. Plant Identifying CNN

#### 1. IOT Device:
To achieve the goal of the project, we will use a microcontroller, sensors, and a water pump to automate the watering process. The microcontroller will read data from the soil moisture sensor, temperature sensor, and humidity sensor, and use this data to determine when to water the plants. If the soil moisture level is too low, the microcontroller will activate the water pump to water the plants.
 
In addition to the watering process, the system will also collect data on temperature and humidity levels. This data will be used to analyze the change in water usage over different seasons. By understanding how temperature and humidity affect water usage, we can optimize the watering process to conserve water while still providing the plants with the necessary moisture they need to grow.
 
To analyze the collected data, we will use various data science techniques such as data visualization and statistical analysis. Data visualization techniques will help us to understand the relationship between soil moisture levels, temperature, and humidity. We can use statistical analysis to determine the optimal moisture level for each plant and adjust the watering process accordingly.

##### Parts Used:
1. Arduin Nano 33 iot
2. DHT 11 - Temperature and Humidity sensor
3. Capacitive Soil Moisture Sensor
4. L293D Motor Driver
5. 9V Battery
6. 9V Water pump

##### Live Setup Diagram:
![IMG_4828](https://user-images.githubusercontent.com/75690804/232213147-29679003-757f-4f5f-a691-b64d71db6ac2.jpeg)

#### 2. Android App:
To display the data insights to the user and control the hardware, we will develop an android app. The app will display real-time data on the soil moisture level, temperature, humidity, trigger level and pump status. The app will also display graphs and charts to visualize the change in water usage over different seasons. The user can use this data to adjust the watering process for their plants or to monitor the health of their plants.

#### 3. Plant Identifying CNN:
To assist smaller scale plant parents, we will also integrate a plant identifying classifier model. This feature will allow users to upload an image of their plant to the app and get a short description of plant care details. The plant identifying classifier model will use a CNN to identify the plant species and provide information on how to care for that specific plant. This will be especially helpful for new plant owners who may not be familiar with the specific care requirements for their plants. This model is hosted on the GCloud AMD compute engine.
