import time
import unittest
from threading import Thread

import numpy

from StreamViewer import StreamViewer
from Streamer import Streamer


class TestLocalStreaming(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestLocalStreaming, cls).setUpClass()

        cls.stream_viewer = StreamViewer()
        Thread(target=lambda: cls.stream_viewer.receive_stream(display=False)).start()

        cls.streamer = Streamer()
        Thread(target=lambda: cls.streamer.start()).start()

        time.sleep(5)

    def test_camera_image(self):
        self.assertIsInstance(self.stream_viewer.current_frame, numpy.ndarray)

    def test_camera_image_not_null(self):
        self.assertIsNotNone(self.stream_viewer.current_frame)

    @classmethod
    def tearDownClass(cls):
        super(TestLocalStreaming, cls).tearDownClass()
        cls.streamer.stop()
        cls.stream_viewer.stop()


if __name__ == '__main__':
    unittest.main()
