#if the results need to be stored in cache with the procedure name,this cache procedure can be used:

def cached_execution(cache, proc, proc_input):
    if proc in cache:
        if proc_input in cache[proc]:
            return cache[proc][proc_input]
    cache[proc]={proc_input:proc(proc_input)}
    return proc(proc_input)