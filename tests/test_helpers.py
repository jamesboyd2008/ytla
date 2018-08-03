# This file contains tests for the helper fucntions.

import unittest

class TestHelpers(unittest.TestCase):

    import sys
    sys.path.append('.')

    def test_timerator(self):
        from client.helpers.timerator import timerator
        self.assertEqual(timerator("01/23/2019 12:27 PM"),"2019-01-23_12:27")
        self.assertEqual(timerator("01/23/2019 12:27 AM"),"2019-01-23_00:27")
        self.assertEqual(timerator("01/23/2019 08:27 PM"),"2019-01-23_20:27")
        self.assertEqual(timerator("01/23/2019 03:27 AM"),"2019-01-23_03:27")
        self.assertEqual(timerator("01/23/2019 3:27 AM"), "2019-01-23_03:27")

    def test_make_an_hour(self):
        from client.helpers.make_an_hour import make_an_hour
        # Ensure that every hour contains 60 minutes.
        self.assertEqual( len(make_an_hour(0)), 60 )
        # Ensure that the maximum granularity of an hour is 5 seconds.
        self.assertEqual( len(make_an_hour(0)['0']), 12 )

if __name__ == '__main__':
    unittest.main()
