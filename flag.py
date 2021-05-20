import hashlib
import os
from dotenv import load_dotenv
import random 

def check_flag_validity(question, flag):
    if(len(flag)!=64): return False
    for i in range(0, 255):
        result = hashlib.sha256((str(question)+str(i)).encode())
        if( result.hexdigest() == flag ): return True
    return False

def gen_flag(question):
    random_int = int(random.randint(0, 255))
    flag = hashlib.sha256( (str(question)+str(random_int)).encode('utf-8') )
    return (flag.hexdigest()+"\n").encode('utf-8')