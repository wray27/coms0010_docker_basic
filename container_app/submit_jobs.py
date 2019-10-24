import time

from container_app.tasks import add

if __name__ == '__main__':
    start_time = time.time()
    for i in range(100):
        result = add.delay(i, 1)

    result_output = result.wait(timeout=None, interval=0.5)
    print(f'Last scheduled task result: {result_output}')
    elapsed_time = time.time() - start_time
    print(f"elapsed time: {elapsed_time}")
