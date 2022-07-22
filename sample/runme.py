# this is the main file of the sample code
# run this file


from moduleWithPrivateFunc import prvt_func, non_prvt_func


def prvt_func_caller():
    prvt_func()


def non_prvt_func_caller():
    non_prvt_func()


if __name__ == '__main__':

    print("\n________module_description________")
    print(
        "# private.py: the module with the class, which is used to make functions private\n# moduleWithPrivateFunc.py: "
        "here a private function prvt_func() is created, also another function non_prvt_func() is there, which just "
        "calls prvt_func()\n# runme.py: this is the current file; it contains prvt_func_caller() and"
        " non_prvt_func_caller(), which calls prvt_func() and non_prvt_func() respectively")
    print("_" * 34)
    print(
        "\n\nHere, in runme.py, prvt_func() and non_prvt_func() are imported from moduleWithPrivateFunc.py, and"
        " prvt_func_caller() and non_prvt_func_caller() are native functions to runme.py\n\n")
    print("__function_description__")
    print(
        ">> prvt_func() | imported     |this is a private function as described in moduleWithPrivateFunc.py, so it would"
        " raise error if called\n>> non_prvt_func() | imported | it is a native function to prvt_func() and calls "
        "prvt_func(), which is a private function, internally, but, since non_prvt_func() itself is not a private "
        "function, so it should work under any circumstances\n>> prvt_func_caller()         | calls prvt_func(), but, "
        "since it isn't a native function to it, it should raise an error\n>> non_prvt_func_caller()     | calls "
        "non_prvt_func(), which is a non native function to it, but not private, so non_prvt_func_caller() should work")
    print("_" * 34)
    print("\n\n\nfunctions of file0.py running.....\n")

    try:
        print("| The private function from moduleWithPrivateFunc.py says    : ", end="")
        prvt_func()
    except:
        print("The private function from moduleWithPrivateFunc.py is raising error")

    try:
        print("| The non-private function from moduleWithPrivateFunc.py says: ", end="")
        non_prvt_func()
    except:
        print("The non-private function from moduleWithPrivateFunc.py is raising error")
    try:
        print("| The native function which calls the private function from moduleWithPrivateFunc.py says    : ", end="")
        prvt_func_caller()
    except:
        print("The native function which calls the private function from moduleWithPrivateFunc.py is raising error")

    try:
        print("| The native function which calls the non-private function from moduleWithPrivateFunc.py says: ", end="")
        non_prvt_func_caller()
    except:
        print("The native function which calls the non-private function from moduleWithPrivateFunc.py is raising error")

    print("\nResult: In this simple test, all the functions worked as expected\n\nTHANKS!")
    x = input()
