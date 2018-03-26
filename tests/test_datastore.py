import unittest, io
from unittest.mock import patch, MagicMock
from cryptotracker.datastore import Datastore

class TestDatastore(unittest.TestCase):
    def test_append_record_to_file(self):
        datastore = Datastore('testdata')
        with patch('builtins.open', create=True) as mock_open:
            mock_open.return_value = MagicMock(spec=io.IOBase)
            datastore.save('a s d f'.split())
        file_handle = mock_open.return_value.__enter__.return_value
        file_handle.write.assert_called_with('a,s,d,f\r\n')

    def test_read_all_records(self):
        datastore = Datastore('testdata')
        lines = ['03/25/2018,Quadriga,BTC,CAD,0.1,1197,0.0025',
                 '03/25/2018,Quadriga,BTC,CAD,0.2,1190,0.005', 
                 '03/25/2018,Quadriga,BTC,CAD,0.3,1178,0.0025']
        fake_file = io.StringIO(initial_value='\r\n'.join(lines))
        with patch('builtins.open', create=True) as mock_open:
            mock_open.return_value = fake_file
            results = datastore.read_all()
        self.assertEqual(3, len(results))

if __name__ == '__main__':
    unittest.main()