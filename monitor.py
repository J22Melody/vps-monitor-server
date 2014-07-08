import platform, os, time

class Monitor(object):
    def get_os_type(self):
        return platform.platform()

    def get_cpu_usage(self):
        # free cpu usage rate
        return os.popen('top -bi -n 2 -d 0.02').read().split('\n\n\n')[1].split('\n')[2].split(',')[3][:-2]

    def get_memory_usage(self):
        result = os.popen('free -m').read().split('\n')[1]
        return {'total': result.split()[1]+'M', 'used': result.split()[2]+'M'}

    def get_disk_usage(self):
        result = os.popen('df -h').read().split('\n')[1]
        return {'total': result.split()[1], 'used': result.split()[2]}

if __name__ == '__main__':
    monitor = Monitor()
    print monitor.get_os_type() 
    print monitor.get_cpu_usage() 
    print monitor.get_memory_usage()
    print monitor.get_disk_usage()
