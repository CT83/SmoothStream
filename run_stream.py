import base64
import sys

import cv2
import zmq

from constants import PORT, SERVER_ADDRESS


def connect_to_viewer(server_address, port):
    context = zmq.Context()
    footage_socket = context.socket(zmq.PUB)
    footage_socket.connect('tcp://' + server_address + ':' + port)
    return footage_socket


def start_streaming(footage_socket, camera_mode=0):
    print("Streaming Started...")
    camera = cv2.VideoCapture(camera_mode)  # init the camera
    while True:
        try:
            grabbed, frame = camera.read()  # grab the current frame
            encoded, buffer = cv2.imencode('.jpg', frame)
            jpg_as_text = base64.b64encode(buffer)
            footage_socket.send(jpg_as_text)

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

    sock = connect_to_viewer(server_address=server_address, port=port)
    start_streaming(sock)


if __name__ == '__main__':
    main()
