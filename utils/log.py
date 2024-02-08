import datetime

#coding:utf-8
PURPLE  = '\033[35m'
RED     = '\033[31m'
CYAN    = '\033[36m'
OKBLUE  = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL    = '\033[91m'
ENDC    = '\033[0m'


def getCurrentDatetime():    
    dt_now = datetime.datetime.now()
    today = dt_now.strftime('%Y/%m/%d/%H:%M:%S')
    return today


def success(message):
    print(OKGREEN + getCurrentDatetime() + "    " + message + ENDC)
    

def warning(message):
    print(WARNING + getCurrentDatetime() + "    " + message + ENDC)
    

def error(message):
    print(FAIL + getCurrentDatetime() + "    " + message + ENDC)
    

def normal(message):
    print(getCurrentDatetime() + "    " + message + ENDC)
    
    
    
    
if __name__ == "__main__":
    success("asdf")
    warning("asdf")
    error("asdf")
    normal("asdf")