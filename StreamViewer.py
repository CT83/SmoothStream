import base64
import sys

import cv2
import numpy as np
import zmq

from constants import PORT, SERVER_ADDRESS


class StreamViewer:
    def __init__(self, port=PORT):
        context = zmq.Context()
        self.footage_socket = context.socket(zmq.SUB)
        self.footage_socket.bind('tcp://*:' + port)
        self.footage_socket.setsockopt_string(zmq.SUBSCRIBE, np.unicode(''))

    def start_listening_for_incoming_stream(self):
        while self.footage_socket:
            try:
                frame = self.footage_socket.recv_string()
                img = base64.b64decode(frame)
                npimg = np.fromstring(img, dtype=np.uint8)
                source = cv2.imdecode(npimg, 1)
                cv2.imshow("Stream", source)
                cv2.waitKey(1)

            except KeyboardInterrupt:
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

    stream_viewer = StreamViewer(port)
    stream_viewer.start_listening_for_incoming_stream()


if __name__ == '__main__':
    main()
