import subprocess
p1 = subprocess.run(['ls'], text = True , capture_output = True)
print(p1.stdout)

