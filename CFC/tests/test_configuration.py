import unittest
import CFC.configuration as configuration

class TestConfiguration(unittest.TestCase):

    def test_load_tf(self):
        tf = configuration.tf
        assert configuration.tf