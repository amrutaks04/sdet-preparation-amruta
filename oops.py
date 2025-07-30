from numpy import random
import json,re
from json.decoder import JSONDecodeError

class TestUser:
    def __init__(self,name,password,email):
        self.name=name
        self.password=password
        self.email=email
    def validate(self):
        if self.name==None or self.password==None or self.email==None:
            return False
        elif len(self.password)<6:
            return False
        pattern='^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.fullmatch(pattern,self.email):
            return False
        return True
    @classmethod
    def random_test_user(cls):
        name="User"+str(random.randint(1,1000))
        password="passw"+str(random.randint(200,40000))
        email=name.lower()+"@gmail.com"
        return cls(name,password,email) 
    
    def to_dict(self):
        return {
            "name":self.name,
            "password":self.password,
              "email":self.email
        }

class TestDataManager:
    def __init__(self,file_path):
        self.file_path=file_path
    def load_test_user(self):
        try:
            with open(self.file_path,'r') as file:
                data=json.load(file)
                return data
        except FileNotFoundError:
            print("File not found")
            return []
        except JSONDecodeError:
            print("Not a valid JSON format")
            return []
        except Exception as e:
            print(e)
            return []
    
    def save_to_file(self,data):
        try:
            with open(self.file_path,'w') as file:
                json.dump(data,file,indent=3)
            print('Saved')
        except Exception as e:
            print(e)     


user=TestUser.random_test_user()
print(user.name)
print(user.password)
print(user.email)

if user.validate():
    print('User data is valid')
else:
    print("Invalid")

manager=TestDataManager('sample_data.json')
existing=manager.load_test_user()
existing.append(user.to_dict())
manager.save_to_file(existing)


