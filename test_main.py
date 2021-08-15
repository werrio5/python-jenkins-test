import unittest
from main import Main

class Main_test(unittest.TestCase):
    def test_main(self):
        main = Main()
        self.assertEqual(main.hello(), 'hello world!')

    @unittest.expectedFailure
    def test_fail(self):
        self.assertTrue(False)
        
if __name__ == '__main__':
    unittest.main()