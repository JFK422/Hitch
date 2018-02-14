import time
from components import create

class compiler:

    def __init__(self):
        print("compiler; compiler; init: INIT_CALLED")

    def compile(self):
        print("compiler; compiler; compile: Compiling")
        
        create.CreateUI.switchCompStatus(self, "compiling")