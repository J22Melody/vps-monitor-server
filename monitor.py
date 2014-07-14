import platform, os, time, re

class Monitor(object):
    
    def get_os_type(self):
        return platform.platform()

    def get_cpu_usage(self):
        # free cpu usage rate
        return os.popen('top -bi -n 2 -d 0.02').read().split('\n\n\n')[1].split('\n')[2].split(',')[3][:-2]

    def get_memory_usage(self):
        result = os.popen('free -m').read().split('\n')[1]
        return result.split()[2] + 'M/' + result.split()[1] + 'M'

    def get_disk_usage(self):
        result = os.popen('df -h').read().split('\n')[1]
        return result.split()[2] + '/' + result.split()[1]  

    def get_access_log(self):
        log_size = str(float(os.path.getsize('/var/log/httpd/access_log'))/1000) + 'k'
        log_file = open('/var/log/httpd/access_log')
        request_list = [] 
        for line in log_file.readlines():
            line_split = line.split()
            request_list.append({
                'ip': line_split[0],
                'identity': line_split[1],
                'userid': line_split[2],
                'time': re.findall(r'\s\[.*]\s', line)[0][2:-2],
                'request_head': re.findall(r'\s\"[^\"]*\"\s', line)[0][2:-2], 
                'status_code': re.findall(r'\s\d\d\d\s', line)[0][1:-1],
                'return_byte': re.findall(r'\s\d\d\d\s(\-|\d+)\s', line)[0],
                'referer': re.findall(r'\s\"[^\"]*\"\s', line)[1][2:-2],
                'user_agent': re.findall(r'\s\"[^\"]*\"$', line)[0][2:-1] 
            })
        total_request = len(request_list)
        return { 
            'log_size': log_size,
            'total_request': total_request,
            'request_list': request_list
        }

if __name__ == '__main__':
    monitor = Monitor()
    print monitor.get_os_type() 
    print monitor.get_cpu_usage() 
    print monitor.get_memory_usage()
    print monitor.get_disk_usage()
    print monitor.get_access_log()