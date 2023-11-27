import os
import subprocess
import time

# run This !

cmd = "python3 frontend.py"
while True:
    proc = subprocess.Popen(cmd, shell=True)
    # delay for 10 seconds
    time.sleep(86400)
    # kill the process if not finished
    proc.kill()
