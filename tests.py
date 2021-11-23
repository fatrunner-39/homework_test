import unittest
import re

from main import *
from yandex_api import YaUploader, TOKEN

class TestFunctions(unittest.TestCase):
    # def test_show_document_info(self):
    #     r = r'[a-z]+\s"\d+(-|\s)?(\d+)?"\s"[A-я]+\s[A-я]+"'
    #     self.assertRegex(show_document_info(documents[2]), r)
    #
    # def test_add_new_doc(self):
    #     self.assertEqual(len(documents)+1, len(add_new_doc('multipassport', '1234',
    #                                                          'Tisha Scotisha')))

    # def test_delete_doc(self):
    #     self.assertEqual(len(documents)-1, len(delete_doc()))

    def test_create_folder(self):
        ya = YaUploader(token=TOKEN)
        self.assertEqual(ya.create_folder('None'), 201)

    @unittest.expectedFailure
    def test_error_create_folder(self):
        ya = YaUploader(token=TOKEN)
        self.assertEqual(ya.create_folder('None'), 201)


if __name__ == '__main__':
    unittest.main()