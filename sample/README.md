Sample Code Example:..........

Here a demo code will be shown where we will see the practical implementation of the private.py</br>
file. We will learn how to create a private function, and implement it. This code piece actually</br>
is the proof of whether the code works or not.</br>
..............................</br>


Description of the files......</br>
private.py&emsp&emsp&ensp              : the module with the class, which is used to make functions private</br>
moduleWithPrivateFunc.py: here a private function prvt_func() is created, also another function</br>
                            <t>non_prvt_func() is there, which just calls prvt_func()</br>
runme.py                : this is the current file; it contains prvt_func_caller() and non_prvt_func_caller(),</br>
                            which calls prvt_func() and non_prvt_func() respectively</br>
..............................</br>


Description of the functions..</br>
>> prvt_func() | imported     | this is a private function as described in moduleWithPrivateFunc.py,
                                so it would raise error if called
>> non_prvt_func() | imported | it is a native function to prvt_func() and calls prvt_func(), which is
                                a private function, internally, but, since non_prvt_func() itself is not
                                a private function, so it should work under any circumstances
>> prvt_func_caller()         | calls prvt_func(), but, since it isn't a native function to it, it should raise an error
>> non_prvt_func_caller()     | calls non_prvt_func(), which is a non native function to it, but not private, so
                                non_prvt_func_caller() should work
..............................


"""  Run the runme.py file to get the details understanding of the project  """
