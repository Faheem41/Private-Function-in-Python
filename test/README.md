<h6>
  <dl align="right">
    <dt><a href="https://github.com/Faheem41/Private-Function-in-Python" rel="noreferrer">Home</a></dt>
    <dt><a href="https://github.com/Faheem41/Private-Function-in-Python/blob/main/src/privatefunc.py" rel="noreferrer">Source</a></dt>
  </dl>
</h6>

#
----------------
<h3>Sample Code Example:..........</h3></br>
Here a demo code will be shown where we will see the practical implementation of the private.py</br>
file. We will learn how to create a private function, and implement it. This code piece actually</br>
is the proof of whether the code works or not.</br>
<h3>..............................</h3></br></br>


<h3>Description of the files......</h3></br>
<h4>private.py</h4>              : the module with the class, which is used to make functions private</br>
<h4>moduleWithPrivateFunc.py</h4>: here a private function prvt_func() is created, also another function</br>
                            <t>non_prvt_func() is there, which just calls prvt_func()</br>
<h4>runme.py</h4>                : this is the current file; it contains prvt_func_caller() and non_prvt_func_caller(),</br>
                            which calls prvt_func() and non_prvt_func() respectively</br>
<h3>..............................</h3></br>


<h3>Description of the functions..</h3></br>
>> <strong>prvt_func()</strong> | imported     | this is a private function as described in moduleWithPrivateFunc.py,
                                so it would raise error if called</br>
>> <strong>non_prvt_func()</strong> | imported | it is a native function to prvt_func() and calls prvt_func(), which is
                                a private function, internally, but, since non_prvt_func() itself is not
                                a private function, so it should work under any circumstances</br>
>> <strong>prvt_func_caller()</strong>         | calls prvt_func(), but, since it isn't a native function to it, it should raise an error</br>
>> <strong>non_prvt_func_caller()</strong>     | calls non_prvt_func(), which is a non native function to it, but not private, so
                                non_prvt_func_caller() should work</br>
<h3>..............................</h3></br></br>


<h5>"""  Run the runme.py file to get the details understanding of the project  """</h5>

#
----------------
<h6 align="center">© 2021-2023 Md. Faheem Hossain fmhossain2941@gmail.com</h6>
