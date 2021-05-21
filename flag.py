import hashlib
import os
import random 

def check_flag_validity(question, flag):
    if(len(flag)!=64): return False
    for i in range(0, 255):
        result = hashlib.sha256((str(question)+str(i)).encode())
        if( result.hexdigest() == flag ): return True
    return False