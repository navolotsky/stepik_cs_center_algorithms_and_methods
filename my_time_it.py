def time_it(func):
    import time
    def wrapper(*args, **kwargs):
        print("Args:", *args)
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        print('Time spent: {}'.format(time.time()-start_time))
        return result
    return wrapper