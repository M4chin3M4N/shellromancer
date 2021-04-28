import os
import sys

if os.getuid() != 0:
  print("[!]You must execute as root!!!!!")
  print("Say the magic word ")
  sys.exit()
  
step1 = f"chmod +x shellromancer.py"
step2 = f"cp shellromancer.py /usr/local/bin/shellromancer"
step3 = f"cp payload.py /usr/bin"

os.system(step1)
os.system(step2)
os.system(step3)

print("Done")
