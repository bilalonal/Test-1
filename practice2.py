Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:15:05) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 0==0
True
>>> 1==0
False
,
>>> 
>>> float(10)
10.0
>>> int(10)
10
>>> int(10,2)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(10,2)
TypeError: int() can't convert non-string with explicit base
>>> int(10.2)
10
>>> int(10.6)
10
>>> int(10.11)
10
>>> int(10.0)
10
>>> name = "Bilal Faruk Onal"
>>> len(name)
16
>>> name.capitalize()
'Bilal faruk onal'
>>> name
'Bilal Faruk Onal'
>>> name.capitalize(2)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    name.capitalize(2)
TypeError: capitalize() takes no arguments (1 given)
>>> name2=veli
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    name2=veli
NameError: name 'veli' is not defined
>>> name2="veli"
>>> name2.capitalize()
'Veli'
>>> name3="Ali"
>>> name3.capitalize()
'Ali'
>>> 0 != 1
True
>>> "a" == "A"
False
>>> "a" != "A"
True
>>> "a" != "A"
True
>>> name4 = Enes
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    name4 = Enes
NameError: name 'Enes' is not defined
>>> name4 = "Enes"
>>> name5 = "enes"
>>> name4 = name5.capitalize()
>>> name5 = "enes"
>>> name4 = "Enes"
>>> name4 == name5.capitalize()
True
>>> 1<2
True
>>> 1!<2
SyntaxError: invalid syntax
>>> 1<!2
SyntaxError: invalid syntax
>>> 1<<2
4
>>> 1<<3
8
>>> 1<<4
16
>>> 2<1
False
>>> 2<=1
False
>>> 2>=2
True
>>> "b" in name
False
>>> "B" in name
True
>>> "k O" in name
True
>>> " " in name
True
>>> "E" in name5
False
>>> "E" in name5.capitalize()
True
>>> "a" not in "abcde"
False
>>> "B F O" in name
False
>>> "B F O" not in name
True
>>> type(True)
<class 'bool'>
>>> type("True")
<class 'str'>
>>> type(true)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    type(true)
NameError: name 'true' is not defined
>>> type(False)
<class 'bool'>
>>> type(in)
SyntaxError: invalid syntax
>>> type(not in)
SyntaxError: invalid syntax
>>> x = 4
>>> x==4
True
>>> type(x==4)
<class 'bool'>
>>> #wow
>>> if 6 > 5:
	print(wow)

	
Traceback (most recent call last):
  File "<pyshell#61>", line 2, in <module>
    print(wow)
NameError: name 'wow' is not defined
>>> if 6 > 5:
	print(name)

	
Bilal Faruk Onal
>>> if 6 > 6:
	print(name)

	
>>> if 6.2 >= 6.2
SyntaxError: invalid syntax
>>> if 6.2 >= 6.2:
	print("wow haram :D")

	
wow haram :D
>>> name4
'Enes'
>>> name5
'enes'
>>> if "E" in name5
SyntaxError: invalid syntax
>>> if "E" in name5:
	print("nice job")

	
>>> if "E" in name5.capitalize():
	print("nice job")

	
nice job
>>> brother = 15
>>> sister = 19
>>> if brother < sister:
	print("sister is older")
else:
	print("brother is older")

	
sister is older
>>> brother = 20
>>> if brother < sister:
	print("sister is older")
else:
	print("brother is older")

	
brother is older
>>> 1 > 0 and 1 < 2
True
>>> 1 > 2 and  1< 3
False
>>> 1 > 2 or  1< 3
True
>>> #mantık dersi gibi. ve yazdığında içlerinden 1 tanesi yanlış ise hepsi yanlış. ama veya yazdığında 1 tanesi doğruysa hepsi doğru.
>>> 1.2 =< 1.21 and "E" in name5.capitalize()
SyntaxError: invalid syntax
>>> 1.2 <= 1.21 and "E" in name5.capitalize()
True
>>> "a" in "abc" and "b" in "abc" and "c" in "abc" or "d" in "abc"
True

>>> "a" in "abc" and "b" in "abc" and "c" in "abc" and "d" in "abc"
False
>>> "a" in "abc" and "b" in "abc" and "c" in "abc"
True
>>> #Big one is coming :)
>>> temp = 32
>>> if temp > 60 and temp < 75:
	print("Nice and cozy")
else:
	print("Too extreme for me")

	
Too extreme for me
>>> temp = 70
>>> 
>>> if temp > 60 and temp < 75:
	print("Nice and cozy")
else:
	print("Too extreme for me")

	
Nice and cozy
>>> Sister is 15
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    Sister is 15
NameError: name 'Sister' is not defined
>>> sister = 15
>>> brother = 15
>>> if brother < sister:
	print("sister is older")
else:
	print("brother is older")
elif:
	
SyntaxError: invalid syntax
>>> if brother < sister:
	print("sister is older")
else:
	print("brother is older")
elif sister == brother:
	
SyntaxError: invalid syntax
>>> type(elif)
SyntaxError: invalid syntax
>>> if brother < sister:
	print("sister is older")
elif sister == brother:
	else:
	print("brother is older")
	
SyntaxError: invalid syntax
>>> if brother < sister:
	print("sister is older")
elif sister == brother:
	print("Twinsies!!")
else:
	print("brother is older")

	
Twinsies!!
>>> 
