from pysci import util
from unittest import TestCase

class UtilTest (TestCase):
    """Test the utility functions.
    """
    def test_rgb_to_bgr_int(self):
        """RGB tuples are correctly converted to BGR integers.
        """
        self.assertEqual(util.rgb_to_bgr_int((255, 128, 64)), 4227327)


    def test_bgr_int_to_rgb(self):
        """BGR integers are correctly converted to RGB tuples.
        """
        self.assertEqual(util.bgr_int_to_rgb(4227327), (255, 128, 64))


    def test_rgb_bgr_roundtrip(self):
        """RGB-to-BGR-to-RGB roundtrip conversion works correctly.
        """
        rgb_tuples = [
            (0, 0, 0),
            (64, 64, 64),
            (128, 128, 128),
            (255, 255, 255),
            (255, 0, 0),
            (0, 255, 0),
            (0, 0, 255),
            (255, 128, 0),
            (0, 255, 128),
            (128, 0, 255),
        ]
        for rgb in rgb_tuples:
            bgr_int = util.rgb_to_bgr_int(rgb)
            got_rgb = util.bgr_int_to_rgb(bgr_int)
            self.assertEqual(rgb, got_rgb)


