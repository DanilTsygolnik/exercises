def MaximumDiscount(N, price):
    if N < 3:
        return 0
    else:
        price_sorted = price.copy()
        price_sorted.sort()

        cnt = 1
        max_discount = 0
        for i in price_sorted[N%3:]:
            if cnt == 1:
                max_discount += i
            if cnt == 3:
                cnt = 1
            else:
                cnt += 1
        return max_discount
