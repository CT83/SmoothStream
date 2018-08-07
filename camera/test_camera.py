import unittest

import numpy

from camera.Camera import Camera


class TestCameraImage(unittest.TestCase):

    def test_camera_image(self):
        self.assertIsInstance(Camera().capture_image(), numpy.ndarray)

    def test_camera_image_not_null(self):
        self.assertIsNotNone(Camera().capture_image())


class TestCameraStream(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestCameraStream, cls).setUpClass()
        cls.camera = Camera()
        cls.camera.start_capture()

    def test_camera_stream(self):
        self.assertIsInstance(self.camera.current_frame.read(), numpy.ndarray)

    def test_camera_stream_not_null(self):
        self.assertIsNotNone(self.camera.current_frame.read())

    @classmethod
    def tearDownClass(cls):
        super(TestCameraStream, cls).tearDownClass()
        cls.camera.stop_capture()


if __name__ == '__main__':
    unittest.main()
