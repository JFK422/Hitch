import create, time

class compiler:

    def __init__(self):
        print("compiler; compiler; init: INIT_CALLED")

    def compile(self, mode):
        print(print("compiler; compiler; compile: Compiling"))
        
        create.switchCompStatus("compiling")
        time.sleep(3)
        create.switchCompStatus("compiled")
        time.sleep(3)
        create.switchCompStatus("error")
        time.sleep(3)
        create.switchCompStatus("leftovers")