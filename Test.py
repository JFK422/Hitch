testText = ["./Data/Temp/openFiles.tmp", "./Data/Temp/compileMode.tmp", "./Data/Temp/unsavedFiles.tmp"]

openFiles = open("./Data/Temp/openFiles.tmp", "r+")
tOpenFiles = openFiles.read()
print(tOpenFiles)
#print("{0}, {1}".format(tOpenFiles, "LOL"))
for i in range(3):
    tOpenFiles += testText[i]
    tOpenFiles += ";"
openFiles.write(tOpenFiles)
print(tOpenFiles)

openFiles.close()