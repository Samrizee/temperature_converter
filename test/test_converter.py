import unittest
from temperature_converter.converter import celisus_to_farhaniet
class TestConverter(unittest.TestCase):
    def test_conversion(self):
        self.assertEqual(celisus_to_farhaniet(0), 32)
        self.assertEqual(celisus_to_farhaniet(100), 212)
        self.assertEqual(celisus_to_farhaniet(25.5), 77.9, places=2)

if __name__ == '__main__':
    unittest.main()
    
       
