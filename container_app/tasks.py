import time

from .sellerie import app


@app.task
def add(a, b):
    time.sleep(3)
    result = a + b
    print(f"result of {a} + {b} = {result}")
    return result
