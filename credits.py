from time import sleep
from termcolor import cprint
import os

f = open(os.getcwd() + '\\credits.txt', 'r')
for x in f:
    print(x)
    sleep(2.5)
