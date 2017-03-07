#!/usr/bin/env python
PKG='task'

import unittest

from task import plotting


class TestPlotting(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.start = 0
        cls.end = 10
        cls.x_vals = [0, 1, 2, 3, 4]
        cls.y_vals = [1, 2, 3, 4, 5]
        cls.ordinary_x = 10     # not a startpoint or endpoint

    def test_travel_begins_when_coordinate_is_startpoint(self):
        _, x_vals, y_vals = plotting.travel(self.start, self.end, self.start, \
                0, [], [])
        self.assertEqual(x_vals, [self.start])
        self.assertEqual(y_vals, [0])
    
    def test_travel_does_not_begin_when_coordinate_is_not_startpoint(self):
        _, x_vals, y_vals = plotting.travel(self.start, self.end, \
                self.ordinary_x,  0, [], [])
        self.assertEqual(x_vals, [])
        self.assertEqual(y_vals, [])

    def test_travel_is_complete_when_coordinate_is_endpoint(self):
        # When the x-coord of the input position is equal to the end, travel
        # should return that the path is complete.
        complete, _, _ = plotting.travel(self.start, self.end, self.end, 0, \
                self.x_vals, self.y_vals)
        self.assertTrue(complete)

if __name__ == '__main__':
    import rosunit
    rosunit.unitrun(PKG, 'test_plotting', TestPlotting)
