# Face recognition based smart attendance managment system using dlib.
Here we aim at automating the traditional way of taking attendances at school's and college's.

# Let's get started.

## Firstly clone this repository.

## In case if you need the installer/executable just to mail me.

## Download the [IP Webcam](https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en_IN "IP Webcam") app from play store.

## For better user experience try the installer.

## Once after downloading the installer / cloning the repository.

## Note : Before proceeding further.

Make sure you have enabled allow Less Secure Apps from your google account.

![permission](https://user-images.githubusercontent.com/39863022/58754172-541d5b80-84e8-11e9-8887-9c5a720879b8.png)

Though its not recomended , you can turn it off once after running the application

Link : https://myaccount.google.com/security

# Once after completing the above step's.

## Execute either REGISTER.py or register.exe and the following output will be obtained.

![register](https://user-images.githubusercontent.com/39863022/59695717-4d8d2480-9208-11e9-82c1-492c1027ca32.png)

## Upon successful registeration.

![register success](https://user-images.githubusercontent.com/39863022/59696054-e58b0e00-9208-11e9-8d87-f635586cf4d3.png)

## After registring with your mail execute either RUN.py or RUN.exe [Attendance Marker.lnk] and the following output will be obtained.

## Select option 1 (Perform training) if running for the first time.

![run1](https://user-images.githubusercontent.com/39863022/59696801-52eb6e80-920a-11e9-86b3-aa284a2256c1.png)

## Follow the specified instruction's and then click Start.

![run2](https://user-images.githubusercontent.com/39863022/59696809-57b02280-920a-11e9-8c42-c7692be94869.png)

## As mentioned in the instructions store the user images in DATASETS directory.

![train1](https://user-images.githubusercontent.com/39863022/59698962-58e34e80-920e-11e9-8b57-67e3edc8e36a.png)

## Then click start to begin training.

<img src="https://user-images.githubusercontent.com/39863022/59703396-6a7d2400-9217-11e9-843a-e26abff7e823.gif" width=778 height=265>
Note : Once training is completed all the images are deleted to maintain privacy.

## Provide the Mail-ID's of all the new users.

<img src="https://user-images.githubusercontent.com/39863022/59704049-df9d2900-9218-11e9-9257-3aeff23a7908.gif" width=599 height=302>

### Launch the IP Webcam mobile app and select start server.
### Make sure your system and device are connected through a same network.
  

## After completing the above step's execute RUN.py or RUN.exe [Attendance Marker.lnk] again and select option 2 (Detect Faces).

## The following output will be obtained.

![ip](https://user-images.githubusercontent.com/39863022/59719942-39164f80-923b-11e9-9983-61640ffdd5ea.png)

### The threshold value is used as a reference to declare weather a user is absent or not.

## Moment of truth.

![hold](https://user-images.githubusercontent.com/39863022/59720670-18e79000-923d-11e9-8ca2-43e5c104affb.png)

## Press q to close the video stream.
### Here we purposefully sent one of our friend to move away from the camera view.
### In order to test the proper functionality of the application.
## Success.
![mno](https://user-images.githubusercontent.com/39863022/59721773-af1cb580-923f-11e9-94e7-1eac025bfa0e.png)
### The system was able to successfully detect the user who was not available in the frame.
## Mail received by the student.
![mail](https://user-images.githubusercontent.com/39863022/59722084-79c49780-9240-11e9-9932-aad090a06572.png)
### Thanks to @ageitgey and @davisking for their awesome work.
