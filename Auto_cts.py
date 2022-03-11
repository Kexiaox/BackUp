import os
import time

def read_result(result):
    res = ''
    file = open('/home/media/Downloads/android-cts/results/latest', 'r')
    for i in file:
        if 'Total Tests' in i:
            tmp = i.split(':')
            res = tmp[1] + ', '
        if 'PASSED' in i:
            tmp = i.split(':')
            res += tmp[1] +', '
        if 'FAILED' in i:
            tmp = i.split(':')
            res += tmp[1]
    result.append(res)

def write_result(result):
    file = open('/home/media/result.txt', 'a')
    file.write(result)


os.chdir("/home/media/Downloads/android-cts/tools")
result = []
file = open('/home/media/case.txt','r')
for i in file:
    cmd = './cts-tradefed run commandAndExit cts --abi x86_64 -m CtsMediaTestCases -t ' + i + ' --skip-all-system-status-check --dynamic-config-url="" --skip-device-info --disable-reboot'
    print(cmd)
    os.system(cmd)
    read_result(result)
    write_result(result)
