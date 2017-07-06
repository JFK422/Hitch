testText = [["./Data/Temp/openFiles.tmp", "./Data/Temp/compileMode.tmp", "./Data/Temp/unsavedFiles.tmp"], ["LOL"], ["L"], ["./Data/Temp/openFiles.tmp", "./Data/Temp/compileMode.tmp", "./Data/Temp/unsavedFiles.tmp"]]

openFiles = open("../Data/Temp/EditorTemp.tmp", "r+")
tOpenFiles = openFiles.read()
print(tOpenFiles)
#print("{0}, {1}".format(tOpenFiles, "LOL"))
tOpenFiles += ";".join(testText[0])
tOpenFiles += ":"
tOpenFiles += ";".join(testText[1])
tOpenFiles += ":"
tOpenFiles += ";".join(testText[2])
tOpenFiles += ":"
tOpenFiles += ";".join(testText[3])
openFiles.write(tOpenFiles)
print(tOpenFiles)

openFiles.close()