
123 231 312

132 213 321

----------------------------

2134
    - 213 132 321
    + 134 341 413

1324
    - 132 321 213
    - 324 243 432


---------------
3412 
    + 341 413 134y
    + 412 124y 241
4132
    + 413 134y 341
    - 132 321n 213
1342
    + 134y
    + 342 423 234y
1423
    - 142 421n 214
    + 423 234y 342
1234
    + 123y
    + 234y

2134 --> ?? --> 1234

------------------------------------ == 1.5 часа ==

Перебирать каждую тройку можно бесконечно, но для каждой тройки число уникальных комбинаций при перестановки одного эл-та по кругу - 3
Общее кол-во перестановок из 3-х элементов равно 3! = 6, причем имеем 2х3 группы: в одной содержатся отсортированные по возрастанию числа, в другой - по убыванию.

Вопрос: на сколько групп по 3 эл-та можно разбить ряд из N чисел? -- N-3+1 = N-2
При k >= N: N-(k+1) 


Если каждое из N чисел - единственное в ряду, общее кол-во операций (уникальных перестановок для каждой тройки) составит 6^(N-2) 






для каждой тройки точно нужно будет отслеживать индекс каждого из 3-х эл-тов в массиве
потому что:
например, есть 1324
перебор 132 к нужной (123) последотельности не приведет
но если взять 1 324
                243...124 3
                      241--412...412 3
                                 124 3...1 243
                                         1 432...143 2
                                                 431 2


------------------------------------ == 1:30 + 1:10 = 2:40 ==


```python
def rotate(inp_list): # len(inp_list) = 3
    src_list = inp_list
    cnt = 0
    while cnt < 3:
        curr_list = src_list.copy()
        curr_list[0] = src_list[1] # mid -> head
        curr_list[1] = src_list[2] # tail -> mid
        curr_list[2] = src_list[0] # head -> tail
        print(curr_list)
        src_list = curr_list.copy()
        cnt += 1
```

```
1234

lmM1   lmM2
123 -- 234 l2=m1 m2=M1 M2>=M1
       342
       423

1342

lmM    lmM
134 -- 342 min2>min1 mid2>=mid1 Max2>=Max1

---
обе тройки сортируются по возрастанию

3412
341 -- 412 max2=max1 mid2<mid1 min2=min1
413 -- 124 max2=max1 mid2<mid1 min2=min1
134 -- 241 max2=max1 mid2<mid1 min2=min1

mid2<mid1 - не вариант ==> переставляем 412->124
3124
312 -- 124 max2>max1 mid2=mid1 min2=min1
123 -- 234
231 -- 314


```

```python

def is_sort(data):
    cnt = 1
    while cnt < len(data):
        if data[cnt-1] <= data[cnt]:
            result = True
        else:
            result = False
            break
        cnt += 1
    return result

# func(list, index) -> list_rotated
def get_rotated(data, index):
    data_mod = data.copy()
    tmp_head = data[index]
    data_mod[index] = data[index+1] # mid -> head
    data_mod[index+1] = data[index+2] # tail -> mid
    data_mod[index+2] = tmp_head # head -> tail
    return data_mod

def MisterRobot(N, data): # N >= 4, len(data) = N
    val_list = []
    
    def brute_force(data, val_list):
        if is_sort:
            return True
        elif data in val_list:
            return False
        else:
            val_list.append(data)
            result = False
            for i in range(N-2):
                if brute_force(get_rotated(data, i), val_list): # if True
                    result = True
                    break
            return result
        
------------------------------------ == 5:57 ==


