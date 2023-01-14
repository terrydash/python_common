# coding=utf-8
import json
import os

import rsa

from common.convert import Config
from common.convert import dict2class
from enviroment import project_dir

config_name = project_dir + os.sep + "config" + os.sep + "config.json"
rsa_dir = project_dir + os.sep + "config" + os.sep


# #print(config_name)
def read_config():
    config = object()
    if os.path.exists(config_name) == True:
        with open(config_name, 'r') as load_f:
            if load_f != None:
                jsondict = json.load(load_f)
                config = dict2class(jsondict)

        if os.path.exists(rsa_dir + r'public.pem') and os.path.exists(rsa_dir + r'private.pem'):
            config.rsa=Config()
            with open(rsa_dir + r'public.pem', 'r') as f:
                config.rsa.__setattr__('publickey', rsa.PublicKey.load_pkcs1(f.read().encode()))
            with open(rsa_dir + r'private.pem', 'r') as f:
                config.rsa.__setattr__('privatekey', rsa.PrivateKey.load_pkcs1(f.read().encode()))
        else:
            raise Exception('RSA加密文件不存在！')
    else:
        raise Exception('config文件不存在！')
    return config


init_config = read_config()
