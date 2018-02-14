from components import create

class fmgActions:
    
    #Called when a folder is opened or the breadcrumb points to a new location
    def changeLocation(self, newPos):
        print(newPos)

    #Called when a file needs to be opened
    def openFile(self, fileToOpen):
        print(fileToOpen)
    
    #The delete file method is in the directroyItem file!

    #Save every modyfied file
    def saveAll(self):
        print("saving everything")
