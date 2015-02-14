Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:15:05) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 2+2
4
>>> 5+5
10
>>> 2*9
18

>>> "my name is" = "bilal"
SyntaxError: can't assign to literal
>>> name = "bilal"
>>> "my name is" + name
'my name isbilal'
>>> "my name is" + " " + name
'my name is bilal'
>>> "bilal" + " onal"
'bilal onal'
>>> "bilal" + " " + "onal"
'bilal onal'
>>> "Hello" + 1
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    "Hello" + 1
TypeError: Can't convert 'int' object to str implicitly
>>> "Hello" + "1"
'Hello1'
>>> type(1)
<class 'int'>
>>> type("1")
<class 'str'>
>>> "Hello" + str(1)
'Hello1'
>>> len("Hello")
5
>>> len(welcome)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    len(welcome)
NameError: name 'welcome' is not defined
>>> len("welcome")
7
>>> "The length of my name is " + str(len(name))
'The length of my name is 5'
>>> "hello"
'hello'
>>> 'hello'
'hello'
>>> "A" * 40
'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
>>> 'A' * 40
'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
>>> h = "happy"
>>> b = "Birthday"
>>> h + " " + b
'happy Birthday'
>>> (h+b)*10
'happyBirthdayhappyBirthdayhappyBirthdayhappyBirthdayhappyBirthdayhappyBirthdayhappyBirthdayhappyBirthdayhappyBirthdayhappyBirthday'
>>> (h + " " + b+" ") *40
'happy Birthday happy Birthday happy Birthday happy Birthday happy Birthday happy Birthday happy Birthday happy Birthday happy Birthday happy Birthday happy Birthday happy Birthday happy Birthday happy Birthday happy Birthday happy Birthday happy Birthday happy Birthday happy Birthday happy Birthday happy Birthday happy Birthday happy Birthday happy Birthday happy Birthday happy Birthday happy Birthday happy Birthday happy Birthday happy Birthday happy Birthday happy Birthday happy Birthday happy Birthday happy Birthday happy Birthday happy Birthday happy Birthday happy Birthday happy Birthday '
>>> (h + " " + b+",") *40
'happy Birthday,happy Birthday,happy Birthday,happy Birthday,happy Birthday,happy Birthday,happy Birthday,happy Birthday,happy Birthday,happy Birthday,happy Birthday,happy Birthday,happy Birthday,happy Birthday,happy Birthday,happy Birthday,happy Birthday,happy Birthday,happy Birthday,happy Birthday,happy Birthday,happy Birthday,happy Birthday,happy Birthday,happy Birthday,happy Birthday,happy Birthday,happy Birthday,happy Birthday,happy Birthday,happy Birthday,happy Birthday,happy Birthday,happy Birthday,happy Birthday,happy Birthday,happy Birthday,happy Birthday,happy Birthday,happy Birthday,'
>>> (h + " " + b+ ,) *40
SyntaxError: invalid syntax
>>> h = "Happy"
>>> (h + " " + b+ ,) *40
SyntaxError: invalid syntax
(h + " " + b+ ,) *40
>>> (h + " " + b+",") *40
'Happy Birthday,Happy Birthday,Happy Birthday,Happy Birthday,Happy Birthday,Happy Birthday,Happy Birthday,Happy Birthday,Happy Birthday,Happy Birthday,Happy Birthday,Happy Birthday,Happy Birthday,Happy Birthday,Happy Birthday,Happy Birthday,Happy Birthday,Happy Birthday,Happy Birthday,Happy Birthday,Happy Birthday,Happy Birthday,Happy Birthday,Happy Birthday,Happy Birthday,Happy Birthday,Happy Birthday,Happy Birthday,Happy Birthday,Happy Birthday,Happy Birthday,Happy Birthday,Happy Birthday,Happy Birthday,Happy Birthday,Happy Birthday,Happy Birthday,Happy Birthday,Happy Birthday,Happy Birthday,'
>>> (h + " " + b+", ") *40
'Happy Birthday, Happy Birthday, Happy Birthday, Happy Birthday, Happy Birthday, Happy Birthday, Happy Birthday, Happy Birthday, Happy Birthday, Happy Birthday, Happy Birthday, Happy Birthday, Happy Birthday, Happy Birthday, Happy Birthday, Happy Birthday, Happy Birthday, Happy Birthday, Happy Birthday, Happy Birthday, Happy Birthday, Happy Birthday, Happy Birthday, Happy Birthday, Happy Birthday, Happy Birthday, Happy Birthday, Happy Birthday, Happy Birthday, Happy Birthday, Happy Birthday, Happy Birthday, Happy Birthday, Happy Birthday, Happy Birthday, Happy Birthday, Happy Birthday, Happy Birthday, Happy Birthday, Happy Birthday, '
>>> print("Hello")
Hello
>>> 9**9
387420489
>>> 9**2
81
>>> type(1)
<class 'int'>
>>> type(1.0)
<class 'float'>
>>> type("1")
<class 'str'>
>>> True
True
>>> false
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    false
NameError: name 'false' is not defined
>>> False
False
>>> type(True)
<class 'bool'>
>>> type(true)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    type(true)
NameError: name 'true' is not defined
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
>>> name.capitalize()
'Bilal'
>>> name
'bilal'
>>> name.capitalize(-2)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    name.capitalize(-2)
TypeError: capitalize() takes no arguments (1 given)
>>> name.capitalize(1)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    name.capitalize(1)
TypeError: capitalize() takes no arguments (1 given)
>>> name.capitalize()
'Bilal'
>>> name.capitalize(0)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    name.capitalize(0)
TypeError: capitalize() takes no arguments (1 given)
>>> 0 == 0
True
>>> 1 == 0
False
>>> 1 == 2
False
>>> name == bilal
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    name == bilal
NameError: name 'bilal' is not defined
>>> name == "bilal"
True
>>> len(name)
5
>>> len(name) == 5
True
>>> len(name) == 6
False
>>> 
