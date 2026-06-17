from calculator import square as s
import pytest as pyt

def test_pawsitive():
#assert - if the condition is false, it will raise an AssertionError and stop the program. 
# If the condition is true, it does nothing and continues to the next line of code.
    assert s(2) == 4, "2 squared was NOT 4."
    assert s(3) == 9, "3 squared was NOT 9."
    assert s(1.5) == 2.25, "1.5 squared was NOT 2.25."
    assert s(100) == 10000, "100 squared was NOT 10000."

def test_negative():
    assert s(-2) == 4, "-2 squared was NOT 4."
    assert s(-3) == 9, "-3 squared was NOT 9."
    assert s(-1.5) == 2.25, "-1.5 squared was NOT 2.25."
    assert s(-100) == 10000, "-100 squared was NOT 10000."

def test_zero():
    assert s(0) == 0, "0 squared was NOT 0."

def test_str():
    #raises - is used to check if a specific exception is raised when executing a block of code.
    with pyt.raises(TypeError):
        s("string")
        

#pytest - is a testing framework for Python that allows you to write simple and scalable test cases. 
# It provides a powerful and flexible way to write tests, including support for fixtures, parameterized
# tests, and more. You can run your tests using the pytest command in the terminal, 
# and it will automatically discover and execute all test functions in your code.




#AssertionError - is an exception that is raised when an assert statement fails. 
# It indicates that the condition being tested was not met, 
# and it can include an optional message to provide more information about the failure.
#try block is used to wrap code that may raise an exception, for e.g AssertionError, 
# allowing you to handle the exception gracefully without crashing the program.
