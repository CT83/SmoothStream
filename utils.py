import base64
import io



def is_raspberry_pi(raise_on_errors=False):
    """Checks if Raspberry PI.

    :return:
    """
    try:
        with io.open('/proc/cpuinfo', 'r') as cpuinfo:
            found = False
            for line in cpuinfo:
                if line.startswith('Hardware'):
                    found = True
                    label, value = line.strip().split(':', 1)
                    value = value.strip()
                    if value not in (
                            'BCM2708',
                            'BCM2709',
                            'BCM2835',
                            'BCM2836'
                    ):
                        if raise_on_errors:
                            raise ValueError(
                                'This system does not appear to be a '
                                'Raspberry Pi.'
                            )
                        else:
                            return False
            if not found:
                if raise_on_errors:
                    raise ValueError(
                        'Unable to determine if this system is a Raspberry Pi.'
                    )
                else:
                    return False
    except IOError:
        if raise_on_errors:
            raise ValueError('Unable to open `/proc/cpuinfo`.')
        else:
            return False

    return True


def preview_image(image, name="window", time=1000):
    import cv2
    cv2.imshow(name, image)
    if cv2.waitKey(time):
        cv2.destroyAllWindows()


def image_to_string(image):
    import cv2
    encoded, buffer = cv2.imencode('.jpg', image)
    return base64.b64encode(buffer)


def string_to_image(string):
    import numpy as np
    import cv2
    img = base64.b64decode(string)
    npimg = np.fromstring(img, dtype=np.uint8)
    return cv2.imdecode(npimg, 1)
