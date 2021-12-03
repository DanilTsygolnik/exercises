def raise_to_power(base, power):
    
    def iter_func(product, count, base, power):
        if count > abs(power):
            return product
        if power > 0:
            return iter_func(product*base, count+1, base, power)
        if base == 0:
            raise ZeroDivisionError("Can't divide by zero. Use another base or non-negative power.")
        return iter_func(product/base, count+1, base, power)

    return iter_func(1, 1, base, power)
