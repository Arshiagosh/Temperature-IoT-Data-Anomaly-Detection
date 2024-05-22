# Temperature IoT Data Anomaly Detection

## Abstract
This project focuses on implementing an IoT system for temperature data anomaly detection using machine learning techniques. The goal is to enhance IoT security and efficiency in various applications, including industrial automation, energy management, healthcare, agriculture, and food safety.

## Introduction
The IoT Capstone Project aims to develop a comprehensive solution that can collect temperature data from IoT sensors, analyze it using machine learning algorithms to detect anomalies and provide real-time insights and actionable alerts. This report outlines the key components, implementation steps, and technical details of the project.

## Applications of Anomaly Detection in IoT
The project explores the following applications of temperature anomaly detection in IoT:

1. **Industrial Automation**: Early identification of equipment malfunctions or overheating in industrial settings.
2. **Energy Management**: Optimizing energy consumption by identifying anomalies in temperature patterns in smart buildings and facilities.
3. **Healthcare**: Ensuring proper storage conditions for pharmaceuticals and medical supplies.
4. **Agriculture & Food Safety**: Early detection of climate-related anomalies affecting crop growth, and ensuring the correct storage temperature for perishable goods during transportation and storage.

## System Diagram
The IoT system consists of the following key components:

1. **Edge Device**: An ESP32 microcontroller connected to a DHT11 temperature sensor for data collection.
2. **Gateway**: A Raspberry Pi 4 that receives data from the edge device via Bluetooth, encrypts it using the RC4 algorithm, and transmits it to the cloud via MQTT.
3. **Cloud Database**: A MongoDB database hosted in the cloud to store the collected temperature data.
4. **Real-Time Analysis and Dashboard**: A dashboard that provides real-time monitoring and visualization of the temperature data, as well as anomaly detection using unsupervised machine learning algorithms.

## Implementation Steps
The project implementation involves the following steps:

1. **Design, Hardware, and Sensors**: Connecting the DHT11 temperature sensor to the ESP32 microcontroller and developing the necessary scripts to collect and transmit the data.
2. **Communications**: Sending the sensor data from the ESP32 to the Raspberry Pi gateway via Bluetooth, encrypting the data using the RC4 algorithm, and transmitting it to the cloud using MQTT.
3. **Dashboard and Monitoring**: Developing a real-time dashboard to visualize the temperature data and the detected anomalies.
4. **Cloud Database**: Storing the temperature data in a MongoDB cloud database for long-term storage and analysis.
5. **Encryption and Decryption**: Implementing the RC4 algorithm for secure data transmission between the edge device, gateway, and cloud.
6. **Gateway**: Utilizing the Raspberry Pi 4 as the gateway to collect, encrypt, and transmit the sensor data to the cloud.
7. **ML Anomaly Detection**: Applying an unsupervised machine learning algorithm (e.g., Isolation Forest) to detect temperature anomalies in the collected data.

## Conclusion
The IoT Capstone Project demonstrates the implementation of a temperature anomaly detection system using machine learning techniques. By leveraging IoT sensors, secure communication protocols, cloud infrastructure, and advanced analytics, this project aims to enhance the security and efficiency of various IoT applications, ultimately contributing to the advancement of the IoT ecosystem.
