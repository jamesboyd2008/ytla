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

    def test_make_a_day(self):
        from client.helpers.make_a_day import make_a_day
        # Ensure that every day contains 24 hours.
        self.assertEqual( len(make_a_day(0)), 24 )
        # Ensure that every hour contains 60 miutes.
        self.assertEqual( len(make_a_day(0)['0']), 60 )

if __name__ == '__main__':
    unittest.main()
