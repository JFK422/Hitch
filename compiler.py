import time
from components import create
from projectHandling import workareaData as wd

class compiler:

    def __init__(self):
        print("compiler; compiler; init: INIT_CALLED")

    def compile(self):
        print(print("compiler; compiler; compile: Compiling"))
        
        create.CreateUI.switchCompStatus(self, "compiling")