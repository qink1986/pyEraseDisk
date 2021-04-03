'''
Author: qink-dell
Date: 2021-03-25 10:55:16
LastEditors: qink-dell
LastEditTime: 2021-04-03 11:01:24
Description:  
'''

import sys
import os
import psutil

def erase_empty_disk(path, num):
    print('erase ' + path + ' ' + str(num) + ' times')
    for i_num in range(num):
        try :
            f = open(path+'/temp_file.tmp', 'w')
            sdiskusage = psutil.disk_usage(path)
            print(str(sdiskusage.free))
            print(str(sdiskusage.percent))
            size = sdiskusage.free
            bSize = 1e9
            while size > bSize:
                f.write('0' * int(bSize))
                f.flush()
                size -= bSize
            sSize = 1e3
            while size > sSize : # also can be 0, set 1 to avoid a rarely bug
                f.write('0' * int(size - sSize))
                f.flush()
                size -= size - sSize
        finally :
            f.close()
            os.remove(path+'/temp_file.tmp')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('usage: ./earase_empyt_disk disk_root_path [num_erases]')
        sys.exit(1)
    if len(sys.argv) < 3:
        num = 1
    else :
        num = int(sys.argv[2])
    path = sys.argv[1]
    erase_empty_disk(path, num)