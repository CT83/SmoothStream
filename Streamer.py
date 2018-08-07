import sys

import cv2
import zmq

from camera.Camera import Camera
from constants import PORT, SERVER_ADDRESS
from utils import image_to_string


class Streamer:

    def __init__(self, server_address=SERVER_ADDRESS, port=PORT):
        print("Connecting to ", server_address, "at", port)
        context = zmq.Context()
        self.footage_socket = context.socket(zmq.PUB)
        self.footage_socket.connect('tcp://' + server_address + ':' + port)

    def start(self):
        print("Streaming Started...")
        camera = Camera()
        camera.start_capture()

        while self.footage_socket:
            try:
                frame = camera.current_frame.read()  # grab the current frame
                image_as_string = image_to_string(frame)
                self.footage_socket.send(image_as_string)

            except KeyboardInterrupt:
                camera.release()
                cv2.destroyAllWindows()
                break


def main():
    port = PORT
    server_address = SERVER_ADDRESS

    try:
        if len(sys.argv) > 1:
            program_name = sys.argv[0]
            arguments = sys.argv[1:]
            count = len(arguments)
            server_address = arguments[0]
            port = arguments[1]
    except IndexError as ie:
        print("Loading default Server Address and Port.")

    streamer = Streamer(server_address, port)
    streamer.start()


if __name__ == '__main__':
    main()
