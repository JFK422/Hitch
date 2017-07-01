

class Data:
    def __init__(self):
        print("workareaData; Data; init: INIT_CALLED")
    
    def readTemp(self):
        print("workareaData; Data; readTemp: Reading temp files")

        tempData = open("./Data/Temp/data.tmp", "r")

    def storeTemp(self, data):
        print("workareaData; Data; storeTemp: Storing temp files")