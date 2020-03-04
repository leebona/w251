# Homework 3
## Containers in Jetson
  * Create a User-Defined Bridge
    - `docker network create --driver bridge hw03`
### 1. Face Detector
  * [Dockerfile](https://github.com/leebona/w251/tree/master/HW3/Dockerfile.faces)
  * Commands
    * Build a Docker Image
      - `sudo docker build -t imagesaver -f Dockerfile.app .`
    * Build a Docker Container
      - `sudo docker run --privileged --name facedetector --network hw03 -v "$PWD":/tmp/hw3 --device=/dev/video1:/dev/video1 --env="DISPLAY" -it facedetector bash`
    * Run a Python Script for Face Detection
      - `python3 hw3/face_detector.py`

### 2. MQTT Broker
  * [Dockerfile](https://github.com/leebona/w251/tree/master/HW3/Dockerfile.mosquitto)
  * Commands
    * Build a Docker Image
      - `sudo docker build -t mosquitto -f Dockerfile.mosquitto .`
    * Build a Docker Container
      - `sudo docker run --privileged --name mqtt-broker --network hw03 -p 1883:1883 -it mosquitto sh`
    * Run Mosquitto
      - `/usr/sbin/mosquitto`

### 3. MQTT Message Forwarder
* [Dockerfile](https://github.com/leebona/w251/tree/master/HW3/Dockerfile.forwarder)
* Commands
  * Build a Docker Image
    - `sudo docker build -t forwarder -f Dockerfile.forwarder .`
  * Build a Docker Container
    - `sudo docker run --privileged --name forwarder --network hw03 -it -v "$PWD":/tmp/hw3 forwarder sh`
  * Run a Python Script to Forward the Messages to the MQTT Broker in Cloud
    - `python3 hw3/message_forwarder.py`

* Inspect Network
  - `sudo docker network inspect hw03`
