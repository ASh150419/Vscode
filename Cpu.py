import psutil


def _CPU_():
    summcpu = {}
    cpu_data = psutil.cpu_times()
    summcpu.update(user_time=cpu_data.user, system_time=cpu_data.system, nice_time=cpu_data.nice, idle_time=cpu_data.idle, iowait_time=cpu_data.iowait, softirq_time=cpu_data.softirq)
    return summcpu

def _Memory_():
    summmem = {}
    memory_data = psutil.virtual_memory()
    summmem.update(total_mem=memory_data.total, available_mem=memory_data.available, percent_mem=memory_data.percent, used_mem=memory_data.used, cached_mem=memory_data.cached)
    return summmem

def _Disk_():
    summdisk = {}
    disk_data = psutil.disk_usage('/')
    summdisk.update(total_disk=disk_data.total, used_disk=disk_data.used, free_disk=disk_data.free, percent_disk=disk_data.percent)
    return summdisk

def show(cpu=None, mem=None, disk=None):
    cpu_template = "{user_time} /// {system_time} /// {nice_time} /// {idle_time} /// {iowait_time} /// {softirq_time}"
    memory_template = "{total_mem} \\\\ {available_mem} \\\\ {percent_mem} \\\\ {used_mem} \\\\ {cached_mem}"
    disk_template = "{total_disk} ///// {used_disk} ///// {free_disk} ///// {percent_disk}"
    print(cpu_template.format(**cpu))
    print(memory_template.format(**mem))
    print(disk_template.format(**disk))

def main():
    _cpu_ = _CPU_()
    _memory_ = _Memory_()
    _disk_ = _Disk_()
    show(cpu=_cpu_,mem=_memory_, disk=_disk_)


if __name__ == "__main__":
    main()