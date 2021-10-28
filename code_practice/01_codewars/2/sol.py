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
    """Версия 2 - вывод в список списков"""
    def func_iter(combos, iter_cnt, values, num_obj):
        if iter_cnt == num_obj:
            return combos
        new_combos = []
        for i in combos:
            for j in values:
                new_combos.append(i+[j])
        return func_iter(new_combos, iter_cnt+1, values, num_obj)

    assert type(values)==type([])

    combos = []
    if num_obj == 0:
        return combos
    for i in values:
        assert type(i)==type('string')
        combos.append([i])
    return func_iter(combos, 1, values, num_obj)

def max_expr_val(args, sig_combos):
    assert type(args)==type([])
    for i in args:
        assert type(i)==type('string')
    assert type(sig_combos)==type([])
    expressions = {}
    for i in range(1,len(args)):
        head = 0
        tail = i
        while tail < len(args):
            args_tmp = args.copy()
            args_tmp[head] = "".join(("(", args_tmp[head]))
            args_tmp[tail] = "".join((args_tmp[tail], ")"))
            for k in sig_combos:
                draft = args_tmp.copy()
                cnt = 1
                for j in k:
                    draft.insert(cnt, j)
                    cnt += 2
                expr = "".join(draft)
                expressions[expr] = eval(expr)
            head += 1
            tail += 1
    print(expressions.keys())
    return max(expressions.values())

#def expression_matter(a, b, c):
