"""
Expressions Matter 

---

== Instructions ==


Given three integers a ,b ,c. 
Return the largest number obtained after inserting +, *, ()
In other words , try every combination of a,b,c with [*+()] , and return the Maximum Obtained

----------------------------------------------------------
Suggested solutions:
https://www.codewars.com/kata/5ae62fcf252e66d44d00008e/solutions/python

Я слишком запарился.
Однако получить решение для общего случая (n аргументов) - полезно.

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
    return max(expressions.values())

def expression_matter(a, b, c):
    args = [str(a), str(b), str(c)]
    signs = ['+', '*']
    sig_combos = get_combos(len(args)-1, signs)
    return max_expr_val(args, sig_combos)
