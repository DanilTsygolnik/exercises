Вывел и сгруппировал массивы данных.

```
0 []  1 [0]    4 [0, 3]    9  [0, 3, 8]    16 [0, 3, 8, 15]
      2 [0]    5 [0, 3]    10 [0, 3, 8]    17 [0, 3, 8, 15]
      3 [0]    6 [0, 3]    11 [0, 3, 8]    18 [0, 3, 8, 15]
               7 [0, 3]    12 [0, 3, 8]    19 [0, 3, 8, 15]
               8 [0, 3]    13 [0, 3, 8]    20 [0, 3, 8, 15]
                           14 [0, 3, 8]    21 [0, 3, 8, 15]
                           15 [0, 3, 8]    22 [0, 3, 8, 15]
                                           23 [0, 3, 8, 15]
                                           24 [0, 3, 8, 15]

25 [0, 3, 8, 15, 24]    36 [0, 3, 8, 15, 24, 35]    49 [0, 3, 8, 15, 24, 35, 48]
26 [0, 3, 8, 15, 24]    37 [0, 3, 8, 15, 24, 35]    50 [0, 3, 8, 15, 24, 35, 48]
27 [0, 3, 8, 15, 24]    38 [0, 3, 8, 15, 24, 35]    51 [0, 3, 8, 15, 24, 35, 48]
28 [0, 3, 8, 15, 24]    39 [0, 3, 8, 15, 24, 35]    52 [0, 3, 8, 15, 24, 35, 48]
29 [0, 3, 8, 15, 24]    40 [0, 3, 8, 15, 24, 35]    53 [0, 3, 8, 15, 24, 35, 48]
30 [0, 3, 8, 15, 24]    41 [0, 3, 8, 15, 24, 35]    54 [0, 3, 8, 15, 24, 35, 48]
31 [0, 3, 8, 15, 24]    42 [0, 3, 8, 15, 24, 35]    55 [0, 3, 8, 15, 24, 35, 48]
32 [0, 3, 8, 15, 24]    43 [0, 3, 8, 15, 24, 35]    56 [0, 3, 8, 15, 24, 35, 48]
33 [0, 3, 8, 15, 24]    44 [0, 3, 8, 15, 24, 35]    57 [0, 3, 8, 15, 24, 35, 48]
34 [0, 3, 8, 15, 24]    45 [0, 3, 8, 15, 24, 35]    58 [0, 3, 8, 15, 24, 35, 48]
35 [0, 3, 8, 15, 24]    46 [0, 3, 8, 15, 24, 35]    59 [0, 3, 8, 15, 24, 35, 48]
                        47 [0, 3, 8, 15, 24, 35]    60 [0, 3, 8, 15, 24, 35, 48]
                        48 [0, 3, 8, 15, 24, 35]    61 [0, 3, 8, 15, 24, 35, 48]
                                                    62 [0, 3, 8, 15, 24, 35, 48]
                                                    63 [0, 3, 8, 15, 24, 35, 48]

64 [0, 3, 8, 15, 24, 35, 48, 63]    81 [0, 3, 8, 15, 24, 35, 48, 63, 80]
65 [0, 3, 8, 15, 24, 35, 48, 63]    82 [0, 3, 8, 15, 24, 35, 48, 63, 80]
66 [0, 3, 8, 15, 24, 35, 48, 63]    83 [0, 3, 8, 15, 24, 35, 48, 63, 80]
67 [0, 3, 8, 15, 24, 35, 48, 63]    84 [0, 3, 8, 15, 24, 35, 48, 63, 80]
68 [0, 3, 8, 15, 24, 35, 48, 63]    85 [0, 3, 8, 15, 24, 35, 48, 63, 80]
69 [0, 3, 8, 15, 24, 35, 48, 63]    86 [0, 3, 8, 15, 24, 35, 48, 63, 80]
70 [0, 3, 8, 15, 24, 35, 48, 63]    87 [0, 3, 8, 15, 24, 35, 48, 63, 80]
71 [0, 3, 8, 15, 24, 35, 48, 63]    88 [0, 3, 8, 15, 24, 35, 48, 63, 80]
72 [0, 3, 8, 15, 24, 35, 48, 63]    89 [0, 3, 8, 15, 24, 35, 48, 63, 80]
73 [0, 3, 8, 15, 24, 35, 48, 63]    90 [0, 3, 8, 15, 24, 35, 48, 63, 80]
74 [0, 3, 8, 15, 24, 35, 48, 63]    91 [0, 3, 8, 15, 24, 35, 48, 63, 80]
75 [0, 3, 8, 15, 24, 35, 48, 63]    92 [0, 3, 8, 15, 24, 35, 48, 63, 80]
76 [0, 3, 8, 15, 24, 35, 48, 63]    93 [0, 3, 8, 15, 24, 35, 48, 63, 80]
77 [0, 3, 8, 15, 24, 35, 48, 63]    94 [0, 3, 8, 15, 24, 35, 48, 63, 80]
78 [0, 3, 8, 15, 24, 35, 48, 63]    95 [0, 3, 8, 15, 24, 35, 48, 63, 80]
79 [0, 3, 8, 15, 24, 35, 48, 63]    96 [0, 3, 8, 15, 24, 35, 48, 63, 80]
80 [0, 3, 8, 15, 24, 35, 48, 63]    97 [0, 3, 8, 15, 24, 35, 48, 63, 80]
                                    98 [0, 3, 8, 15, 24, 35, 48, 63, 80]
                                    99 [0, 3, 8, 15, 24, 35, 48, 63, 80]
```

Данные группируются, поэтому пробую выявить закономерности в отношениях. Связка номер "группы" -- длина массива k -- индексы.
Различные пробы на бумаге и в текстовом редакторе.

```
      |- [0 ... 0] -|   -----  k=0   open doors indexes: []
     1|    ---->    |3  (1+2)
  +2  |- [1 ... 3] -|   -----  k=1   open doors indexes: [0]
     3|    ---->    |5  (3+2)
  +2  |- [4 ... 8] -|   -----  k=2   open doors indexes: [0,3]
     5|    ---->    |7  (5+2)
  +2  |- [9 .. 15] -|   -----  k=3   open doors indexes: [0,3,8]
     7|    ---->    |9  (7+2)
  +2  |- [16 . 24] -|   -----  k=4   open doors indexes: [0,3,8,15]
     9|    ---->    |11 (9+2)
  +2  |- [25 . 35] -|   ------ k=5   open doors indexes: [0,3,8,15,24]
    11|    ---->    |13 (11+2)
      |- [36 . 48] -|   ------ k=0   open doors indexes: [0,3,8,15,24,35]
   ...|             |...

      |- [0 ... 0] -|   -----  k=0   open doors indexes: []
     1|    ---->    |3  (1+2)
  +2  |- [1 ... 3] -|   -----  k=1   open doors indexes: [0]
     3|    ---->    |5  (1+2+2)
  +2  |- [4 ... 8] -|   -----  k=2   open doors indexes: [0,3]
     5|    ---->    |7  (1+2+2+2)
  +2  |- [9 .. 15] -|   -----  k=3   open doors indexes: [0,3,8]
     7|    ---->    |9  (1+2+2+2+2)
  +2  |- [16 . 24] -|   -----  k=4   open doors indexes: [0,3,8,15]
     9|    ---->    |11 (1+2+2+2+2+2)
  +2  |- [25 . 35] -|   ------ k=5   open doors indexes: [0,3,8,15,24]
    11|    ---->    |13 (1+2+2+2+2+2+2) = 2^0 + 3*2*2 = 2^0 + 3*2^2
      |- [36 . 48] -|   ------ k=0   open doors indexes: [0,3,8,15,24,35]
   ...|             |...


0
3 = 2^0+2^1
8 = 3+5 = (2^0+2^1)+(2^0+2^2)
15 = 3+5+7 = (2^0+2^1)+(2^0+2^2)+(2^0+2^1+2^2)
24 = 3+5+7+9 = (2^0+2^1)+(2^0+2^2)+(2^0+2^1+2^2)+(2^0+2^1+2^2)


[0 ... 0]  0-0=0            0 
[1 ... 3]  3-1=2      group 1    3 = 1+2        = (1+2) = 1х(1+2) + 0x2 = 1 + 1x1
[4 ... 8]  8-4=4      group 2    8 = 3+5        = 1х(1+2) + 0x2 + (1+2+2) = 2х(1+2) + 1x2 = 2 + 3x2
[9 .. 15]  15-9=6     group 3   15 = 3+5+7      = 2х(1+2) + 1x2 + (1+2+2+2) = 3х(1+2) + 3x2 = 3 + 6x2
[16 . 24]  24-16=8    group 4   24 = 3+5+7+9    = 3х(1+2) + 3x2 + (1+2+2+2+2) = 4х(1+2) + 6x2 = 4 + 10x2
[25 . 35]  35-25=10   group 5   35 = 3+5+7+9+11 = 4х(1+2) + 6x2 + (1+2+2+2+2+2) = 5х(1+2) + 10x2 = 5 + 20x2
[36 . 48]  48-36=12   group 6   48

-----------------------------

начало текущей группы = конец предыдущей + 1
конец текущей группы = начало текущей + 2 х номер шага
номер группы = кол-во открытых дверей = (всего дверей)^(1/2) x10 // 10 ; т.е. корень округленный к меньшему

Таким образом, кол-во открытых дверей (n), от общего кол-ва дверей (k) можно выразатить функцией:
n = f(k) = floor(sqrt(k))

Как рассчитать индексы на основе полученного n?
На что смотреть? Закономерность? -- Каждый индекс увеличивается на определенный шаг. Определить шаг....

....прикидывая варианты на клочке бумаги, заметил, что каждый индекс - это номер группы в степени 2 минус 1.

Таким образом, при i=[1...n] каждая открытая дверь располагается под  индексом ind(i) = i^2-1
```

На основе полученных обобщений `n = floor(sqrt(k))` и `ind(i) = i^2-1` написана функция для дополнительной части задания.

```python
def Keymaker_math(n):
    templ = n*[0]
    num_open = 10 * int(round(n**(1/2),1)) // 10
    for i in range(1, num_open+1):
        templ[i**2-1]=1
    return "".join(str(i) for i in templ)
```
