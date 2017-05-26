# Pyglish 


[![codebeat badge](https://codebeat.co/badges/e86a8bfe-3ad9-4d4e-98b6-b5a4e46852f1)](https://codebeat.co/projects/github-com-d-kiss-pyglish-master)

Pyglish is a free and open-source programming language developed and maintained by d-kiss. It is a verbose syntactical superset of Python, and adds english-like syntax to the language. 

# Have a look at this python code:
This code snippet is a generator for prime numbers
```python
def primes():
    x = 1
    while True:
        was_divided = False
        x+= 1
        for y in xrange(2, x):
            if x % y == 0:
                was divided = True
        
        if not was_divided:
            yield x
```

# This is how we do it 
```python
def primes():
    yield every natural x if there is no y from 2 to x where x is divided by y
```
or, if you prefer:
```python
def primes():
    yield x for every number x from 1 to inifinity if there is no number y from 2 to x  where x divides y
```

Some of Pyglish's important features as we keep in mind are
  - 100% full backwards compatability with python.
  - Easy to use and intuitive.
  - Very elagant syntax
 - Strong tests for easy refactoring

# Supports:
  * Unittests
  * Comparisons
  * Loops

# Future Support:
 * ~~Unittests~~
  * ~~Comparisons~~
  * ~~Loops~~
 * Conditions
 * Exit codes
 * Strong typing 
 * File I/O
 * Socket I/O
 * Threading
 * Waits (Explicit, Conditions, Implicit)
 * Math
 * Logging
 * Dates
 * [Strangle](http://www.github.com/d-kiss/strangle)
 * Abstract classing
 * Interfaces
 * Equation Return value
 * Switch-case
 * Elegant Hex Usage
 * Event-based programming
 * [Monoikers](http://www.yegor256.com/2017/05/16/monikers.html)
 * Then-Success-Failure angular-like promise
 * pyglish ignore.



# Usage
#### Loops
| Pyglish | Python Equivalent |
|:-------:|:-------------------:|
| ```until password is equal to '123':```|```while password != '123':```|
|```as long as user.is_connected(): ```| ```while user.is_connected():```|
|```10 times: print "Hello"```|``` for _ in xrange(10): print "Hello"```|
|```for each user in group: print user.age```| ```for user in group: print user.age```
|```for every user in group: print user.name```| ```for user in group: print user.name```
|```foreach user in group: print user.address```| ```for user in group: print user.address```

#### Comparisons
| Pyglish | Python Equivalent |
|:-------:|:-------------------:|
| ```if a is equal to b:```|```if a == b:```|
| ```if a is not equal to b:```|```if a != b:```|
| ```if a is greater than or equal to b:```|```if a >= b:```|
| ```if a is greater than or equal to b:```|```if a > b:```|
| ```if a is less than or equal to b:```|```if a <= b:```|
| ```if a is less than b:```|```if a < b:```|
| ```if a is between b and c:```|```if b <= a <= c:```|

#### Unit Testing
| Pyglish | Python Equivalent |
|:-------:|:-------------------:|
| ```assert that user.is_connected()```|```self.assertTrue(user.is_connected())```|
| ```user.name should be "Dan"```|```assert user.name == "Dan"```|
| ```user.name should not be "Daniel"```|```assert user.name != "Daniel"```|
| ```assert that sock.connect raises socket.error```|```self.assertRaises(sock.connect, socket.error)```|
| ```assert raises NotImplementedError: a = AbstractClass()```|```with self.assertRaises(NotImplementedError): a = AbstractClass()```|

