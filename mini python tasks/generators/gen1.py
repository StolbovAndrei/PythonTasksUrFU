from decorators.dec_t2 import is_prime


def take(n):
    def decorator(gen_func):
        def wrapper(*args, **kwargs):
            gen = gen_func(*args, **kwargs)
            count = 0
            while True:
                if n >= 0 and count >= n:
                    break
                yield next(gen)
                count += 1
        return wrapper
    return decorator

@take(10)
def gen_prime():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

if __name__ == "__main__":
    for num in gen_prime():
       print(num)