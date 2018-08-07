import base64
import sys

import cv2
import zmq

from constants import PORT, SERVER_ADDRESS


class Streamer:

    def __init__(self, server_address=SERVER_ADDRESS, port=PORT):
        print("Connecting to ", server_address, "at", port)
        context = zmq.Context()
        self.footage_socket = context.socket(zmq.PUB)
        self.footage_socket.connect('tcp://' + server_address + ':' + port)

    def start(self, camera_mode=0):
        print("Streaming Started...")
        camera = cv2.VideoCapture(camera_mode)  # TODO Abstract Camera
        while self.footage_socket:
            try:
                grabbed, frame = camera.read()  # grab the current frame
                encoded, buffer = cv2.imencode('.jpg', frame)
                jpg_as_text = base64.b64encode(buffer)
                self.footage_socket.send(jpg_as_text)

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
