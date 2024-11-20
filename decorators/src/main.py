# TODO: Create a decorator that calculates the execution time of any function.

# library used to calculate time
import time
# We will use the wrapper standard decorator to conserve the original function metadata. 
from functools import wraps

def log_execution_time(func):
    # With this we conserve the metadata of the function passed to the outer decorator
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"The function {func.__name__} executed in {end - start:.4f}")
        return result
    return wrapper

@log_execution_time
def simulate_compute():
    time.sleep(2)
    return "Task completed"

result = simulate_compute()
print(result)

