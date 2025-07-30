import os
from oops import TestDataManager

file_path='test_file.json'

def test_load_and_check():
    sample_validusers=[
        {
      "name": "amruta",
      "email": "amruta.ks2022cse@gmail.com",
      "password": "123456"
   },
   {
      "name": "User132",
      "password": "passw31556",
      "email": "user132@gmail.com"
   }
    ]
    manager=TestDataManager(file_path)
    manager.save_to_file(sample_validusers)
    data=manager.load_test_user()
    assert data==sample_validusers
    os.remove('test_file.json')

def test_load_filenotfound():
    manager=TestDataManager('notafile.json')
    data=manager.load_test_user()
    assert data==[],"Empty list as file not found"