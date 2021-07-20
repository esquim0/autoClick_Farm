# Install python on windows
# then install pyautogui lib on cmd ( py -m pip install pyautogui ) 
# finally to execute the program write python name.py

#ref:
# https://pyautogui.readthedocs.io/en/latest/install.html
# https://www.python.org/downloads/windows/
# version choosed 3.6.8

import pyautogui as pg
import time

initial_exec_time = time.time()

print(pg.position())
pg.click(1616, 557)
initial_time = int(time.time())
count = 0
for i in range(10000):
    pg.drag(1,0)
    pg.drag(-1, 0)
    
    current_time = int(time.time())
    count = count + 2
    #time.sleep(1)
    #print( current_time - initial_time )
    if current_time - initial_time == 60 :
        initial_time = int(time.time())
        print(f"Per minute was pressed {count} times" )
        count = 0

final_exec_time = time.time() - initial_exec_time       
print( f"Execution time: {final_exec_time}")        

#pressed 20k in 34min.
