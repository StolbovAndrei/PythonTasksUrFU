import time
import functools
import random


def retry(max_attempts=3, default_delay=1, default_factor=2, exceptions=(Exception,)):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            delay = default_delay
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as error:
                    attempts +=1
                    if attempts == max_attempts:
                        raise
                    print(f"Exceptions {error}, function will try again afterr a delay {delay} seconds")
                    time.sleep(delay)
                    delay *= default_factor
        return wrapper
    return decorator


@retry(exceptions=(ValueError,))
def demonstration_func():
    num = random.random()
    if num < 0.5:
        raise ValueError("ValueError")
    print("The function worked successfully!")
    return "Success"

if __name__ == "__main__":
    try:
        result = demonstration_func()
        print(f"Result: {result}")
    except ValueError as error:
        print(f"All retries failed: {error}")