###  Traffic-Light-Automation

The idea of the project is to help the patient’s needs inside a hospital, using Mediapipe, OpenCV and Arduino UNO. 
We have taken the idea of hand-tracking using the Mediapipe Library to count the number of  fingers to light up the LED's. 
Messages will be send on WhatsApp and Email accordingly based on the number of fingers captured by camera.


```
-Encoding
```
- 1 fingers--> Green Light --> The patient is okay but needs supplies like food and water or some daily medicines
- 2 fingers--> Yellow Light --> The patient needs to go to the bathroom for urination or excretion
- 3 fingers --> Red Light --> The patient is facing severe problems and needs instant medical attention
```
```

### What is Mediapipe?

**MediaPipe is a cross-platform framework for building multimodal applied machine learning pipelines. MediaPipe is a framework for building multimodal (eg. video, audio, any time series data), cross platform (i.e Android, iOS, web, edge devices) applied ML pipelines.**

### How to set up locally?

- Check if your system has python installed in it before!

- Fork the repository

- Git clone your forked repository

- Create virtual environment
```
- pip install --user virtualenv
- python -m venv env
- source env/bin/activate (Linux)
- env\Scripts\activate (Windows)
```

- Install dependencies
```
- pip install -r requirements.txt
```  

- Check dependencies
```
- pip list
```  

### Software Used:

- Language
```
- Python
```
- Libraries
```
- OpenCV
- Mediapipe
- pyfirmata
- controller
- pywhatkit
- date time
- SMTP
```

### Hardware Used:

```
- Arduino UNO
- Jumper Wires
- Breadboard
- LED light's Red,Green,Yellow

```

### Setup Picture:

<img src="images\setup.jpg"  width="900" height="600">


