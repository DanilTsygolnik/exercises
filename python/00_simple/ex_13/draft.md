
def UFO(N, data, octal=True)

N - длина массива входных данных
data - массив входных данных
octal=True - числа в массиве data представлены в восьмеричной системе счисления ==> цифры 8 и 9 отсутствуют
octal=fasle - числа в массиве data представлены в шестнадцатиричной системе счисления

функция должна вывести массив из чисел, представленных в десятиричной системе счисления

-----

десятичная в восьмерчную `oct(X)`
десятичная в шестнадцатеричную `hex(X)`

из системы счисления в десятичную `int('number', base)`

bin(19) --> '0b10011'
int('0b10011', 2) --> 19


```python
def UFO(N, data, octal=True):
    integers = []
    index_cnt = 0
    while index_cnt < N:
        if octal:
            integers.append(int(str(data[index_cnt]), 8))
        else:
            integers.append(int(str(data[index_cnt]), 16))
        index_cnt += 1
    return integers
```
