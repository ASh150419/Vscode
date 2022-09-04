import psutil


def CPU_info():
    summcpu = {}
    cpu_data = psutil.cpu_times()
    summcpu.update(user_time=cpu_data.user, system_time=cpu_data.system, nice_time=cpu_data.nice, idle_time=cpu_data.idle)
    return summcpu


def Memory_info():
    summmem = {}
    memory_data = psutil.virtual_memory()
    summmem.update(total_mem=memory_data.total // 1E+6, available_mem=memory_data.available // 1E+6,
        used_mem=memory_data.used // 1E+6, cached_mem=memory_data.cached // 1E+6) 
    return summmem


def Disk_info():
    summdisk = {}
    disk_data = psutil.disk_usage('/')
    summdisk.update(total_disk=disk_data.total // 1E+6, used_disk=disk_data.used // 1E+6,
        free_disk=disk_data.free // 1E+6, percent_disk=disk_data.percent)
    return summdisk


def show(cpu=None, mem=None, disk=None):
    cpu_template = "/// {:<38} /// {:^21} /// {:^22} /// {:>13} ///"
    cpu_template1 = "/// {user_time} /// {system_time} /// {nice_time} /// {idle_time} ///"
    cpu_template2 = "{}"
    mem_template = "\\\\\\\ {:<28} \\\\\\\ {:^24} \\\\\\\ {:^24} \\\\\\\ {:>33} "
    memory_template1 = "\\\\\\\ {total_mem} \\\\\\\ {available_mem} \\\\\\\ {used_mem} \\\\\\ {cached_mem} \\\\\\\ "
    mem_template2 = "{}"
    disk_template = "///// {total_disk} ///// {used_disk} ///// {free_disk} ///// {percent_disk} /////"
    disk_template1 ="///// {:>22} ///// {:^23} ///// {:^20} ///// {:<16} /////"
    disk_template2 = "{}"
    print(cpu_template.format("Время затрачиваемое обычными процессами", "Процессы в режиме ядра", "Проприетарные процессы", "Время простоя")
    )
    print(cpu_template1.format(**cpu)
    )
    print(cpu_template2.format("<" * 120)
    )
    print(mem_template.format("Общая физическая память (MB)", "Память под процессы (MB)" ,"Используемая память (MB)" ,"Неиспользуемая память вообще (MB)")
    )        
    print(memory_template1.format(**mem)
    )
    print(mem_template2.format(">" * 120)
    )
    print(disk_template1.format("Общий объём диска (MB)", "Используемый объём (MB)", "Свободный объём (MB)" ,"Использование(%)")
    )
    print(disk_template.format(**disk)
    )
    print(disk_template2.format("=" * 120)
    )


def main():
    cpu_main = CPU_info()
    memory_main = Memory_info()
    disk_main = Disk_info()
    show(cpu=cpu_main, mem=memory_main, disk=disk_main)


if __name__ == "__main__":
    main()
