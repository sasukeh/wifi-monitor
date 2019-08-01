import pings
import subprocess as sp

command = ["ping","8.8.8.8"]

print(command)

sp.call(command)
