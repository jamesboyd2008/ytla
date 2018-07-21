# This file contains test(s) for the helper fucntions.

import unittest

class TestHelpers(unittest.TestCase):

    import sys
    sys.path.append('.')

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_timerator(self):
        from timerator import timerator
        self.assertEqual(timerator("01/23/2019 12:27 PM"), "01/23/2019 12:27")
        self.assertEqual(timerator("01/23/2019 12:27 AM"), "01/23/2019 00:27")
        self.assertEqual(timerator("01/23/2019 08:27 PM"), "01/23/2019 20:27")
        self.assertEqual(timerator("01/23/2019 03:27 AM"), "01/23/2019 03:27")

if __name__ == '__main__':
    unittest.main()
