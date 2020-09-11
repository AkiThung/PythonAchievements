Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6

PS C:\Users\akith> py
Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 2 + 2
4
>>> 3 * 10
30
>>> 100 - 10
90
>>> 25 / 5
5.0
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
>>> print('mijn naam is Aki')
mijn naam is Aki
>>> naam = 'Aki'
>>> print(naam)
Aki
>>> print(naam.upper())
AKI
>>> print(naam[0:2])
Ak
>>> print(naam[::-1])
ikA
>>> leeftijd = 17
>>> print('hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?'
...
... leeftijd = leeftijd + 1
  File "<stdin>", line 3
    leeftijd = leeftijd + 1
    ^
SyntaxError: invalid syntax
>>> print('hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?'
...
...
... leeftijd = leeftijd + 1
  File "<stdin>", line 4
    leeftijd = leeftijd + 1
    ^
SyntaxError: invalid syntax
>>> print('hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
hallo Aki ben je al 17 jaar?
>>> leeftijd = leeftijd + 1
>>> leeftijd
18
>>> leeftijd-=1
>>> leeftijd
17
>>> if leeftijd < 18:
... hoelang_tot18jaar = 18 -leeftijd
  File "<stdin>", line 2
    hoelang_tot18jaar = 18 -leeftijd
    ^
IndentationError: expected an indented block
>>> if leeftijd < 18:
... hoelang_tot18jaar = 18 - leeftijd
  File "<stdin>", line 2
    hoelang_tot18jaar = 18 - leeftijd
    ^
IndentationError: expected an indented block
>>> if leeftijd < 18:
...     hoelang_tot18jaar = 18 -leeftijd
...     print('Over ' +  str(hoelang_tot18jaar) + 'jaar wordt je 18')
... elif leeftijd > 18:
...     hoelang_al18jaar =leeftijd - 18
...     print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
... else:
...     print ('Je bent precies ' + str(leeftijd) + ' jaar ')
... leeftijd
  File "<stdin>", line 9
    leeftijd
    ^
SyntaxError: invalid syntax
>>> leeftijd
17
>>> if leeftijd < 18:
... hoelang_tot18jaar = 18 - leeftijd
  File "<stdin>", line 2
    hoelang_tot18jaar = 18 - leeftijd
    ^
IndentationError: expected an indented block
>>> if leeftijd < 18:
... hoelang_tot18jaar = 18 - leeftijd
  File "<stdin>", line 2
    hoelang_tot18jaar = 18 - leeftijd
    ^
IndentationError: expected an indented block
>>> if leeftijd < 18:
...     hoelang_tot18jaar = 18 - leeftijd
...     print('Over ' +  str(hoelang_tot18jaar) + 'jaar wordt je 18')
... elif leeftijd > 18:
...     hoelang_al18jaar =leeftijd - 18
...     print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
... else:
...     print ('Je bent precies ' + str(leeftijd) + ' jaar ')
... from random import randint
  File "<stdin>", line 9
    from random import randint
    ^
SyntaxError: invalid syntax
>>> if leeftijd < 18:
...     hoelang_tot18jaar = 18 - leeftijd
...     print('Over ' +  str(hoelang_tot18jaar) + 'jaar wordt je 18')
... elif leeftijd > 18:
...     hoelang_al18jaar =leeftijd - 18
...     print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
... else:
...     print ('Je bent precies ' + str(leeftijd) + ' jaar ')
...
Over 1jaar wordt je 18
>>>
>>> from random import randint
>>> randint(0,1000)
960
>>> willekeurig_getal = randint (0,1000)
>>> willekeurig_getal
353
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal)
...
...
... print(naam[::-1])
  File "<stdin>", line 4
    print(naam[::-1])
    ^
SyntaxError: invalid syntax
>>> print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))
Willekeurig getal tussen 0 en 1000: 353
>>> from datetime import datetime
>>> datum = datetime.now()
>>> print(datum)
2020-09-11 14:59:46.844035
>>> datum.strftime('%A %d %B %Y')
'Friday 11 September 2020'
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
'it_IT'
>>> datum.strftime('%A %d %B %Y')
'venerdì 11 settembre 2020'
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime('%A %d %B %Y')
'vrijdag 11 september 2020'
>>> if leeftijd < 18:
...     hoelang_tot18jaar = 18 - leeftijd
...     print('Over ' +  str(hoelang_tot18jaar) + 'jaar wordt je 18')
... elif leeftijd > 18:
...     hoelang_al18jaar =leeftijd - 18
...     print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
... else:
...     print ('Je bent precies ' + str(leeftijd) + ' jaar ')
...
Over 1jaar wordt je 18
>>> locale.setlocale(locale.LC_TIME, 'es_ES')
'es_ES'
>>> datum.strftime('%A %d %B %Y')
'viernes 11 septiembre 2020'
>>>print(naam)
	  
SyntaxError: invalid syntax
>>> naam = "Aki"
>>> print(naam[::-1])
ikA
>>> print(naam[::-2])
iA
>>> 