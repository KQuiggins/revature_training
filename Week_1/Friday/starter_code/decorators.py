import time
from functools import wraps

def timer(func):
    """Decorator that measures and prints execution time.

    Output format: "⏱️ {func_name} completed in {seconds:.4f}s"
    """
    @wraps(func)
    def wrappper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        elapsed = end - start

        print(f"⏱️ {func.__name__} completed in {elapsed:.4f}s")

        return result

    return wrappper


@timer
def slow_operation():
    time.sleep(0.5)
    return "done"

result = slow_operation()
# Should print: ⏱️ slow_operation completed in 0.50XXs
assert result == "done"
assert slow_operation.__name__ == "slow_operation"  # @wraps preserves metadata

def retry(max_attempts=3, delay=0.5, exceptions=(Exception,)):
    """Parameterized decorator that retries on failure.

    Args:
        max_attempts: Maximum number of tries
        delay: Seconds between retries
        exceptions: Tuple of exception types to catch

    Prints progress: "⚠️ Attempt {n}/{max}: {error}. Retrying in {delay}s..."
    On final failure: "💥 {func_name} failed after {max} attempts"
    """
    pass  # TODO: Implement (3-layer nesting: factory → decorator → wrapper)


