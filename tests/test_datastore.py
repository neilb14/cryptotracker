import unittest, io
from unittest.mock import patch
from unittest.mock import MagicMock
from cryptotracker import datastore

class TestDatastore(unittest.TestCase):
    def test_append_record_to_file(self):
        with patch('builtins.open', create=True) as mock_open:
            mock_open.return_value = MagicMock(spec=io.IOBase)
            datastore.save('asdf')
        file_handle = mock_open.return_value.__enter__.return_value
        file_handle.write.assert_called_with('asdf')

if __name__ == '__main__':
    unittest.main()