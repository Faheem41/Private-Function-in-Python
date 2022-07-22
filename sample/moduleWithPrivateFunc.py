
from private import PrivateFunc
privatefunc = PrivateFunc("moduleWithPrivateFunc")

@privatefunc.private
def prvt_func():
    print("working...")
    
def non_prvt_func():
    prvt_func()
