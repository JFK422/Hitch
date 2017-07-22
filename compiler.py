import time
from Components import create
from ProjectHandling import workareaData as wd

class compiler:

    def __init__(self):
        print("compiler; compiler; init: INIT_CALLED")

    def compile(self):
        print(print("compiler; compiler; compile: Compiling"))
        
        create.createUI.switchCompStatus(self, "compiling")