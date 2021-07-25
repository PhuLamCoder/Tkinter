path = 'database.txt'
def savefile(line) :
    try:
        file = open(path, 'a', encoding='utf-8')
        file.writelines(line)
        file.writelines('\n')
        file.close()
    except:
        pass
def readfile():
    arrbook = []
    try :
        file = open(path, 'r', encoding='utf-8')
        for line in file:
            data=line.strip()
            arr = data.split(';')
            arrbook.append(arr)
        file.close()
    except:
        pass
    return arrbook