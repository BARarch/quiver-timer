import time

def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print("timing-" + method.__name__.ljust(30, '-'), end= " ")
            print ("{:.2f} ms".format((te - ts) * 1000))
        return result
    return timed

def howfast_will_it_update():
    return None
    
