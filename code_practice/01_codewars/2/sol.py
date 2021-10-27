"""
Expressions Matter 

---

== Instructions ==


Given three integers a ,b ,c. 
Return the largest number obtained after inserting +, *, ()
In other words , try every combination of a,b,c with [*+()] , and return the Maximum Obtained

----------------------------------------------------------
есть последовательность abc (может быть больше abcdef )

нужно перебирать группы эл-тов внутри
кол-во циклов - кол-во срезов от максимально большого -- срезa arr[0:len(arr)] до минимального arr[len(arr)-2:len(arr)]
k циклов где k=[0...len(arr)-2включительно]

внутри каждого цикла - циклы перестановки среза
первый цикл - срез находится в крайнем правом положении, R=len(arr), L=k
    в конце каждого цикла R-=1 L-=1 пока L>=0

Для каждой перестановки каждого среза нужно посчитать 2**(len(arr)-1) комбинаций -- знаки между цифрами

"""

def get_combos(num_obj, values):
    def func_iter(combos, iter_cnt, values, num_obj):
        if iter_cnt == num_obj:
            return combos
        new_combos = {}
        for i in combos.keys():
            for j in values:
                new_combos[i+j] = combos[i] + [j]
        return func_iter(new_combos, iter_cnt+1, values, num_obj)

    combos = {}
    for i in values:
        combos[i] = [i]
    return func_iter(combos, 1, values, num_obj)

def brackets(array):
    combos = []
    for i in range(1, len(array)):
        head = 0
        tail = i
        while tail < len(array):
            combos.append("".join(array[head:tail+1]))
            head += 1
            tail += 1
    return combos
