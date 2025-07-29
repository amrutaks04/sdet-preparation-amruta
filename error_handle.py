import requests

def safe_web_request(url,timeout=3):
    try:
        res=requests.get(url,timeout=timeout)
        res.raise_for_status()
        print("Request success")
        return res.json()
    except requests.exceptions.MissingSchema:
        print('Invalid URL format')
    except requests.exceptions.ConnectionError:
        print('Failed to establish a connection')
    except requests.exceptions.ConnectTimeout:
        print('Connection attempt timed out')
    except requests.exceptions.Timeout:
        print('The request timed out')
    except requests.exceptions.JSONDecodeError:
        print("Not in JSON format")

    except Exception as e:
        print(e)


data=safe_web_request("https//google.com")
if(data):
    print(data)