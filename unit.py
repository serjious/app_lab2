import unittest
from tandem import HTTP_requests_parser
from tandem import search_tandem_word 
from tandem import get_list_from_file

test_list = [
    "ТУСОВА",
    "ТАРТАР",
    "АРБУЗ",
    "МАМА",
    "ГАГА"
    ]

valid_list = [
    "ТАРТАР",
    "МАМА",
    "ГАГА"
    ]

valid_list_file = [
    "ТУСОВА",
    "ТАРТАР",
    "КАПКАН",
    "МАМА",
    "ГАГА"
    ]
    
class TestTandem(unittest.TestCase):
    def test_search_tandem_word(self):
        self.assertEqual(search_tandem_word(test_list), valid_list)
    
    def test_get_list_from_file(self):
        list_tandem = get_list_from_file("tandem.txt")
        self.assertEqual(list_tandem, valid_list_file)
        self.assertEqual(search_tandem_word(list_tandem), valid_list) 

if __name__ == "__main__":
    print("Hello")
