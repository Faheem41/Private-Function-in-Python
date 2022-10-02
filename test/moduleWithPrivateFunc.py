# this file contains two functions- one private and the other non-private
# the private.py file contains the src/private.py
# the runme.py is the file which one should run


from privatefunc import PrivateFunc
privatefunc = PrivateFunc("moduleWithPrivateFunc")


@privatefunc.private
def prvt_func():
    print("working...")
  

def non_prvt_func():
    prvt_func()
