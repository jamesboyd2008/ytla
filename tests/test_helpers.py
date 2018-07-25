# This file contains test(s) for the helper fucntions.

import unittest

class TestHelpers(unittest.TestCase):

    import sys
    sys.path.append('.')

    def test_timerator(self):
        from timerator import timerator
        self.assertEqual(timerator("01/23/2019 12:27 PM"),"2019-01-23 12:27:00")
        self.assertEqual(timerator("01/23/2019 12:27 AM"),"2019-01-23 00:27:00")
        self.assertEqual(timerator("01/23/2019 08:27 PM"),"2019-01-23 20:27:00")
        self.assertEqual(timerator("01/23/2019 03:27 AM"),"2019-01-23 03:27:00")
        self.assertEqual(timerator("01/23/2019 3:27 AM"), "2019-01-23 03:27:00")

if __name__ == '__main__':
    unittest.main()
