import os

fileDir = os.path.join(os.getcwd(),"Linux")
print(fileDir)

outDir = os.path.join(os.getcwd(),"L")
print(outDir)

fileList = os.listdir(fileDir)
print(fileList)

n = 0
for i in fileList:
    oldname = fileDir + os.sep + fileList[n]  # os.sep添加系统分隔符
    newname = fileDir + os.sep + 'a' + str(n+1) + '.jpg'
    os.rename(oldname, newname)
    print(oldname, "====>", newname)
    n += 1

