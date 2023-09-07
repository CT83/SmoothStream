# SmoothStream [![Build Status](https://travis-ci.com/CT83/SmoothStream.svg?branch=master)](https://travis-ci.com/CT83/SmoothStream)
Webcam and PiCamera Streaming over the Network with Python


## Getting Started
SmoothStream is a Python Application which makes streaming video from webcams over the network a breeze.

Streaming images from your Webcam over the network should be easy, right?

Nope. After pulling my hair out, searching on the internet for weeks, scavenging through old forum posts and digging through old StackOverflow questions, I came up empty-handed. (Most of the code examples were outdated and worked only in Python 2)
Until I stumbled upon [this](https://stackoverflow.com/questions/43817161/how-to-send-opencv-video-footage-over-zeromq-sockets) StackOverflow Question.

I decided it was 'bout time someone did something about it.

The `StreamViewer` needs to start listening for incoming stream from the `Streamer`, once an incoming stream is detected it is displayed on the screen.

SmoothStream currently has a dependency on ZeroMQ and I don't see a way around it.

So, PRs are always welcome.


### Prerequisites

1. Webcam (duh!)

### Installing

A step by step series of examples that tell you how to get a development env running

1. Install all the requirements

```
pip install -r requirements.txt
```

2. Start the viewer, on the server.
```
python StreamViewer.py
```

3. On another machine connected to the same network, start the streamer, and enter the IP of the machine running the StreamViewer.
```
python Streamer.py -s 192.168.1.X
```

You will see the video being streamed across the network to your Viewer.

## Running the tests (WebCam Needed)
```
python -m unittest discover .
```

1. `test_camera.py` - Tests if camera can be detected with OpenCV

    `python -m unittest camera.test_camera`

2. `test_local_streaming.py` - Tests Streaming and Viewing silently locally

    `python -m unittest test_local_streaming`




### Alternatives from around the internet which failed to work.
http://answers.opencv.org/question/19055/video-over-the-network/
https://github.com/yushuhuang/webcam
https://stackoverflow.com/questions/30988033/sending-live-video-frame-over-network-in-python-opencv
https://stackoverflow.com/questions/49084143/opencv-live-stream-video-over-socket-in-python-3
https://stackoverflow.com/questions/43299440/how-to-send-live-video-over-network-in-python
https://stackoverflow.com/questions/36265183/how-to-get-video-frame-by-frame-from-stream-using-opencv-and-python
https://stackoverflow.com/questions/29099839/opencv-stream-from-a-camera-connected-to-a-remote-machine
https://raspberrypi.stackexchange.com/questions/72308/how-to-stream-video-via-socket-using-opencv-and-picamera



## Built With

* **[OpenCV](http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_setup/py_intro/py_intro.html)** - a library of programming functions mainly aimed at real-time computer vision.
* **[ZeroMQ](http://zeromq.org/bindings:python)** - a high-performance asynchronous messaging library, aimed at use in distributed or concurrent applications.


## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Rohan Sawant** [CT83](https://github.com/CT83)


## License
This project is licensed under the GPL-3.0 License - see the [LICENSE.md](LICENSE.md) file for details

# Thank You 👍
