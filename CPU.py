import psutil


def _CPU_():
    summcpu = {}
    cpu_data = psutil.cpu_times()
    summcpu.update(user_time=cpu_data.user, system_time=cpu_data.system, nice_time=cpu_data.nice, idle_time=cpu_data.idle)
    return summcpu


def _Memory_():
    summmem = {}
    memory_data = psutil.virtual_memory()
    summmem.update(total_mem=memory_data.total // 1E+6, available_mem=memory_data.available // 1E+6,
        used_mem=memory_data.used // 1E+6, cached_mem=memory_data.cached // 1E+6) 
    return summmem


def _Disk_():
    summdisk = {}
    disk_data = psutil.disk_usage('/')
    summdisk.update(total_disk=disk_data.total // 1E+6, used_disk=disk_data.used // 1E+6,
        free_disk=disk_data.free // 1E+6, percent_disk=disk_data.percent)
    return summdisk


def show(cpu=None, mem=None, disk=None):
    cpu_sh = "/// {:<38} /// {:^21} /// {:^22} /// {:>13} ///"
    cpu_template = "/// {user_time} /// {system_time} /// {nice_time} /// {idle_time} ///"
    cpu_end = "{}"
    mem_sh = "\\\\\\\ {:<28} \\\\\\\ {:^24} \\\\\\\ {:^24} \\\\\\\ {:>33} "
    memory_template = "\\\\\\\ {total_mem} \\\\\\\ {available_mem} \\\\\\\ {used_mem} \\\\\\ {cached_mem} \\\\\\\ "
    mem_end = "{}"
    disk_template = "///// {total_disk} ///// {used_disk} ///// {free_disk} ///// {percent_disk} /////"
    disk_sh ="///// {:>22} ///// {:^23} ///// {:^20} ///// {:<16} /////"
    disk_end = "{}"
    print(cpu_sh.format("Время затрачиваемое обычными процессами", "Процессы в режиме ядра", "Проприетарные процессы", "Время простоя")
    )
    print(cpu_template.format(**cpu)
    )
    print(cpu_end.format("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    )
    print(mem_sh.format("Общая физическая память (MB)", "Память под процессы (MB)" ,"Используемая память (MB)" ,"Неиспользуемая память вообще (MB)")
    )        
    print(memory_template.format(**mem)
    )
    print(mem_end.format(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    )
    print(disk_sh.format("Общий объём диска (MB)", "Используемый объём (MB)", "Свободный объём (MB)" ,"Использование(%)")
    )
    print(disk_template.format(**disk)
    )
    print(disk_end.format("====================================================================================================================")
    )


def main():
    _cpu_ = _CPU_()
    _memory_ = _Memory_()
    _disk_ = _Disk_()
    show(cpu=_cpu_,mem=_memory_, disk=_disk_)


if __name__ == "__main__":
    main()
