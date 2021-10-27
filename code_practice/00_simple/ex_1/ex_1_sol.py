"""
Написать функцию squirrel(N), которая возвращает первую цифру факториала N!
"""
def squirrel(N):
    def fact(number):
        def fact_iter(prod, cnt, val):
            if val in (0, 1):
                return 1
            if cnt > val:
                return prod
            return fact_iter((prod * cnt), (cnt + 1), val)

        return fact_iter(1, 1, number)

    def emeralds(k):
        """Функция возвращает первую цифру факториала k!"""
        if k == 0:
            return 0
        if k < 10:
            return k
        return emeralds(k // 10)

    if N < 0:
        raise ValueError("N must be equal to or bigger than 0")
    if isinstance(N, type(1)) is False:
        raise ValueError("N must be integer")
    return emeralds(fact(N))
