import json
from json.decoder import JSONDecodeError

def create_test_user_data():
    data={
        'name':'amruta',
        'email':'amruta.ks2022cse@sece.ac.in',
        'password':'123',
        'age':'21',
        'role':'sdet'
        }
    return data

def validate_email_format(email):
    if '@' in email and '.' in email:
        return True
    else:
        return False

def read_test_data_from_json():
    try:
        with open('sample_data.json','r') as file:
            data=json.load(file)
        print(data)
    except FileNotFoundError:
        print("File Not Found")
    except JSONDecodeError:
        print('Not a valid JSON format')
    except Exception as e:
        print(e) 

print(create_test_user_data())
print(validate_email_format('amruta@gmailcom'))
read_test_data_from_json()