import psutil

print(psutil.cpu_count())

print(psutil.cpu_count(logical=False))

print(psutil.cpu_times())

print(psutil.virtual_memory())

print(psutil.net_io_counters())

print(psutil.net_if_stats())
