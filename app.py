import os
import json
import requests

from config import Config

def app(config):
    # print(config)


    headers_auth = {'content-type': 'application/json'}
    data ={"username": config['username'], "password": config['password']}
    
    try:
        r = requests.post(url=config['url_auth'], data=json.dumps(data), headers=headers_auth)

        token = "JWT " + r.json()['access_token']
    except Exception:
        print('Auth error')

    for dates in config['dates']: 
        headers_connect = {'content-type': 'application/json', 'Authorization': token}
        data ={"date": dates}
        try:
            r = requests.get(url=config['url_connect'], data=json.dumps(data), headers=headers_connect)
            
            result = r.json()
            # print(result)
            directory_path =os.path.join('.','Results', dates)
            os.makedirs(directory_path, exist_ok=True)
            with open(os.path.join(directory_path, dates+'.json'), 'w') as json_file:
                json.dump(result,json_file)
        except Exception:
            print('Wrong date')
        

if __name__== '__main__':
    config = Config('config.yaml')
    app(config.getconfig('config_app'))