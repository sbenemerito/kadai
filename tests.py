import os
import unittest

from core.constants import INDEX_FILE_DIR
from core.indexer import generate_index_file
from core.searcher import query_data

TEST_INDEX_FILE = os.path.join(os.path.dirname(__file__), 'test_index.pickle')


class TestApp(unittest.TestCase):
    """
    Unit tests for the whole app, based on the original data source
    """

    @classmethod
    def setUpClass(cls):
        generate_index_file(index_dir=TEST_INDEX_FILE)

    def test_generate_index(self):
        index_file_exists = os.path.isfile(TEST_INDEX_FILE)
        self.assertTrue(index_file_exists, "Should create index file")

    def test_search_shibuya(self):
        # Output should be similar to sample output when searching '渋谷'
        search_term = '渋谷'
        match_counter = 0
        sample_outputs = ['9870113', '0101642', '6050874']
        special_value = ('常盤町（東大路通渋谷上る、渋谷通東大路東入、'
                         '渋谷通東大路東入２丁目、東大路五条下る）')

        query_result = query_data(
            search_term=search_term,
            index_dir=TEST_INDEX_FILE
        )

        for row in query_result:
            if row[0] in sample_outputs:
                match_counter = match_counter + 1

            if row[0] == '6050874':
                with self.subTest():
                    self.assertEqual(row[3], special_value,
                                        'Split rows should be joined')

            if match_counter == 3:
                break

        with self.subTest():
            self.assertEqual(match_counter, 3,
                             'Should match all three sample outputs')

    @classmethod
    def tearDownClass(cls):
        if os.path.isfile(TEST_INDEX_FILE):
            os.remove(TEST_INDEX_FILE)


if __name__ == '__main__':
   unittest.main()
