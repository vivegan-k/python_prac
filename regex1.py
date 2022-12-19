# Your previous Plain Text content is preserved below:

# This is just a simple shared plaintext pad, with no execution capabilities.

# When you know what language you'd like to use for your interview,
# simply choose it from the dots menu on the tab, or add a new language
# tab with the + button.

# You can also change the default language your pads are created with
# in your account settings: https://app.coderpad.io/settings

# Enjoy your interview!

'''
A number is said to be a magic number, if the sum of its digits are calculated till a single digit recursively by adding the sum of the digits after every addition. If the single digit comes out to be 1,then the number is a magic number. 

For example- 
Number= 50113 
=> 5+0+1+1+3=10 
=> 1+0=1 
This is a Magic Number 

Input : 1234
Output : Magic Number

Input  : 12345
Output : Not a magic Number
'''
'''
def recursive_sum(num, sum1=0):        
    #val = num % 10
    for val in str(num):
        sum1 += int(val)
    print(sum1)
    
    if len(str(sum1)) > 1:
        return recursive_sum(sum1)
    else:
        if sum1 == 1:
            return 'Magic Number'
        else:
            return 'Not a magic number'
    
    
print(recursive_sum(1234))

'''
from collections import defaultdict

logs="""
[2021-12-09 13:31:45: INFO/ForkPoolWorker-3] Waiting for update
[2021-12-09 13:31:09: INFO/ForkPoolWorker-2] Preparing for execution of work
[2021-12-09 13:31:28: INFO/ForkPoolWorker-4] Waiting for update
[2021-12-09 13:31:28: INFO/ForkPoolWorker-1] Received update. Execution completed.
[2021-12-09 13:31:31: INFO/ForkPoolWorker-3] Waiting for update
[2021-12-09 13:31:25: INFO/ForkPoolWorker-2] Waiting for update
[2021-12-09 13:31:27: INFO/ForkPoolWorker-4] Waiting for update
[2021-12-09 13:31:12: INFO/ForkPoolWorker-2] Starting execution
[2021-12-09 13:31:29: INFO/ForkPoolWorker-3] Preparing for execution of work
[2021-12-09 13:31:45: INFO/ForkPoolWorker-4] Received update. Execution completed.
[2021-12-09 13:31:30: INFO/ForkPoolWorker-3] Starting execution
[2021-12-09 13:31:24: INFO/ForkPoolWorker-2] Waiting for update
[2021-12-09 13:31:22: INFO/ForkPoolWorker-4] Preparing for execution of work
[2021-12-09 13:31:46: INFO/ForkPoolWorker-3] Received update. Execution completed.
[2021-12-09 13:31:13: INFO/ForkPoolWorker-2] Waiting for update
[2021-12-09 13:31:24: INFO/ForkPoolWorker-4] Starting execution
[2021-12-09 13:31:38: INFO/ForkPoolWorker-2] Received update. Execution completed.
[2021-12-09 13:31:25: INFO/ForkPoolWorker-1] Preparing for execution of work
[2021-12-09 13:31:27: INFO/ForkPoolWorker-1] Waiting for update
[2021-12-09 13:31:26: INFO/ForkPoolWorker-1] Starting execution
[2021-12-09 13:31:29: INFO/ForkPoolWorker-4] Waiting for update
"""

import re

logs = logs.strip().split("\n")
worker_strings = []
di = defaultdict(list)
di2 = defaultdict(dict)
for log in  logs:
    worker_string = re.findall(r"\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:(\d{2}):\s\w+\/\w+\-(\d+)\]\s([\w|\s]+)", log)
    #\d{4}-d{2}-d{2}\sd{2}:d{2}:d{2}: INFO\/ForkPoolWorker\-?(\d+)
    print(worker_string[0][0])
    di[worker_string[0][1]].append(worker_string[0][0])
    di2[worker_string[0][1]][worker_string[0][0]] = log
    worker_string.append(log)
print(di)
print(di2)
for key in sorted(di.keys()):
    for val in sorted(di[key]):
        print(di2[key][val])

'''
worker_ids = []
for string in worker_strings:
    worker_ids.append(string.split('-')[-1])

worker_ids = sorted(worker_ids)
''' 



'''
import collections

log_lines = logs.split("\n")
d = collections.defaultdict(list)
for line in log_lines:
    
    if line != '':
        id = line.split(']')[0].split('-')[-1]
        seconds = line.split(':')[2]
        d[id].append(seconds)
print(d)

new_d = collections.defaultdict(list)
new_val = set()
worker_ids = sorted(d.keys())
for key in worker_ids:
    print(key)
    for val in sorted(d[key]):
        #print(val)
        for line in log_lines:
            if val in line and f'ForkPoolWorker-{key}' in line:
                print(line)
'''