import os
import subprocess
import time

cmd = "python frontend.py"
while True:
    proc = subprocess.Popen(cmd, shell=True)
    # delay for 10 seconds
    time.sleep(86400)
    # kill the process if not finished
    proc.kill()
