# -*- coding: utf-8 -*-

from .context import wiki_to_matrix

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_crowl(self):
        wiki_to_matrix.crowl("http://url_for_test", "/tmp")


if __name__ == '__main__':
    unittest.main()
