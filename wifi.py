# we can use this code to find passwords of wifis that we conect to them befor 
import subprocess


names = []
all = subprocess.check_output("netsh wlan show profiles")
all = all.decode("utf-8", "backslashreplace")
all = all.split("\n")
for i in all:
    if "All User Profile" in i:
        s = i.split(": ")[1].strip()
        names.append(s)

data = []
lost = []
message = ""
for i in names:
    try:
      d = subprocess.check_output(f"""netsh wlan show profiles name={i} key=clear""")
    except:
        lost.append(i+" : lost")
        continue
    data = d.decode("utf-8", "backslashreplace")
    data = data.split("\n")
    t = 0
    for z in data:
        if "Key Content" in z:
            t += 1
            message = message + i + " : " + z.split(": ")[1] + "\n"
    if t == 0:
        lost.append(i+" : lost")
for i in lost:
    message = message + i + "\n"
print(message[:-1])