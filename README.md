# SmoothStream
Webcam and PiCamera Streaming over the Network with Python


## Getting Started

Streaming images from your Webcam over the network should be easy, right?
Nope. After pulling my hair out, searching on the internet for weeks, scavenging through old forum posts and digging through old StackOverflow questions, I came up empty handed. (Most of the code examples were outdated and worked only in Python 2)
Until I stumbled upon [this](https://stackoverflow.com/questions/43817161/how-to-send-opencv-video-footage-over-zeromq-sockets) StackOverflow Question.

I decided it was 'bout time someone did something about it.
This repo is a minimal example of Streaming Video smoothly over the network.
It currently has a dependency on ZeroMQ and I don't see a way around it.

PRs are always welcome.


### Prerequisites

1. Webcam (duh!)

### Installing

A step by step series of examples that tell you how to get a development env running

1. Install all the requirements

```
pip install -r requirements.txt
```


End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### What other alternatives did I try?
http://answers.opencv.org/question/19055/video-over-the-network/
https://github.com/yushuhuang/webcam
https://stackoverflow.com/questions/30988033/sending-live-video-frame-over-network-in-python-opencv
https://stackoverflow.com/questions/49084143/opencv-live-stream-video-over-socket-in-python-3
https://stackoverflow.com/questions/43299440/how-to-send-live-video-over-network-in-python
https://stackoverflow.com/questions/36265183/how-to-get-video-frame-by-frame-from-stream-using-opencv-and-python
https://stackoverflow.com/questions/29099839/opencv-stream-from-a-camera-connected-to-a-remote-machine
https://raspberrypi.stackexchange.com/questions/72308/how-to-stream-video-via-socket-using-opencv-and-picamera

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags).

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

