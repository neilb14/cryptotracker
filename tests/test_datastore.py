import unittest, io
from unittest.mock import patch, MagicMock
from cryptotracker.datastore import Datastore

class TestDatastore(unittest.TestCase):
    def test_append_record_to_file(self):
        datastore = Datastore('./data')
        with patch('builtins.open', create=True) as mock_open:
            mock_open.return_value = MagicMock(spec=io.IOBase)
            datastore.save('a s d f'.split())
        file_handle = mock_open.return_value.__enter__.return_value
        file_handle.write.assert_called_with('a,s,d,f\r\n')

if __name__ == '__main__':
    unittest.main()