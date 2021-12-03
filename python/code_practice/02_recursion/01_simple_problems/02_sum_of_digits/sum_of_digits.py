def get_digits_sum(number):
    
    def iter_func(product, number):
        if number == 0:
            return product
        return iter_func(product + number % 10, number // 10)

    return iter_func(number % 10, number // 10)
