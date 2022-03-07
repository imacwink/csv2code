# -*- utf-8 -*-
# -*- imacwink -*- 
import os 
import shutil
import re
import csv
import platform

sysType = platform.system()

ESC = chr(27)

# 字体
a_default  = 0
a_bold     = 1
a_italic   = 3
a_underline= 4

# 前景颜色
fg_black   = 30
fg_red     = 31
fg_green   = 32
fg_yellow  = 33
fg_blue    = 34
fg_magenta = 35
fg_cyan    = 36
fg_white   = 37

# 后景颜色
bg_black   = 40
bg_red     = 41
bg_green   = 42
bg_yellow  = 43
bg_blue    = 44
bg_magenta = 45
bg_cyan    = 46
bg_white   = 47
 
def color_code(a):
    return ESC + "[%dm" % a
    
def color_str(s, *args):
    if(sysType == "Windows"):
        return s
    cs = ""
    for a in args:
        cs += color_code(a)
    cs += s
    cs += color_code(a_default)
    return cs 

path = os.path.split(os.path.realpath(__file__))[0]

csvPath = path + "/Numeric/"
cSharpPath = path + "/CSharp/"
csvDataName = "CsvData"
csvDataManagerName = "CsvDataManager"

templatePath = path + "/Template/"
templateCSPath = templatePath + "TemplateClass.cs"
templateCsvDataManagerPath = templatePath + "TemplateCsvDataManager.cs"
templateCsvDataPath = templatePath + "TemplateCsvData.cs"

genCodeModel = "Model"

# sys info 
print("\n")
print(color_str("System: " + sysType, bg_blue, bg_cyan, a_bold))
print(color_str("Path: " + path, bg_blue, bg_cyan, a_bold))
print("\n")

classList = []

def genCsCodeFromLine(line):
    isItem = 0
    data = ''
    for i in range(len(line)):
        item = line[i]
        if item != '':
            isItem = 1
            data += '\"' + item + '\"'
            if i < len(line) - 1:
                data += ','
    if isItem == 0:
        return ''
    return data

def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
 
    if not isExists:
        # print path + ' OK'
        os.makedirs(path)
        return True
    else:
        # print path + 'OK'
        return False

def genCsCodeFromClass(name):
    code = "\t\t\t\tif(className == \"" + name +"\")\n\t\t\t\t{" + "\n\t\t\t\t\t" + "return " + name + ".getInstance();" + "\n\t\t\t\t}"
    return code

def genCode(rootDir): 
    print(color_str("Start...", fg_white, bg_green, a_italic))

    list_dirs = os.walk(rootDir)

    # remove old csharp
    isExists = os.path.exists(cSharpPath)
    if isExists:
        shutil.rmtree(cSharpPath)

    for root, dirs, files in list_dirs: 
        for f in files: 
            filePath = os.path.join(root, f) 
            fname, fextension = os.path.splitext(f)
            csharpFilePath = os.path.join(cSharpPath, genCodeModel + "/" + fname) + ".cs"
            if fextension == ".csv":
                # print(f)
                print(color_str(" -- " + f, fg_cyan, bg_black, a_bold))
                mkdir(cSharpPath + genCodeModel)
                # copy template.cs
                shutil.copy(templateCSPath, csharpFilePath)

                #add classList
                classList.append(fname)

                # compatible
                fp = None
                if(sysType == "Windows"):
                    fp = open(filePath, 'r', encoding = 'utf-8')
                    alllines = fp.readlines()
                    fp.close() 
                    fp = open(filePath, 'w', encoding = 'utf-8')
                else:
                    fp = open(filePath, 'r')
                    alllines = fp.readlines()
                    fp.close() 
                    fp = open(filePath, 'w') 

                # write start
                for eachline in alllines:
                    # compatible
                    a = re.sub(';', ',', eachline)
                    fp.writelines(a) 
                fp.close()
  
                if(sysType == "Windows"):
                    reader = csv.reader(open(filePath, 'rU', encoding = 'utf-8'), dialect = 'excel')
                else:
                    reader = csv.reader(open(filePath, 'rU'), dialect = 'excel')

                descKey = None
                key = None
                data = ''

                for line in reader:
                    if descKey is None:
                        descKey = genCsCodeFromLine(line)  # first line : csv desc
                    else:
                        if key is None:
                            key = genCsCodeFromLine(line)
                        else:
                            item = genCsCodeFromLine(line)
                            if item != '':
                                data = data + '{' + item + '}' + ',\n\t\t\t'
                # print(key)
                # print(data)
                # write *.cs
                # read lines
                fp = None

                if(sysType == "Windows"):
                    fp = open(csharpFilePath, 'r', encoding = 'utf-8')
                    alllines = fp.readlines()
                    fp.close() 
                    fp = open(csharpFilePath, 'w', encoding = 'utf-8')
                else:
                    fp = open(csharpFilePath, 'r')
                    alllines = fp.readlines()
                    fp.close() 
                    fp = open(csharpFilePath, 'w') 

                # write start
                for eachline in alllines:
                    # class name
                    a = re.sub('TemplateClass', fname, eachline)
                    # china key
                    a = re.sub('TemplateDescKey', descKey, a)
                    # allkey
                    a = re.sub('//TemplateRealKey', key, a)
                    # alldata
                    a = re.sub('//TemplateRealData', data, a)
                    # csvDataParent
                    a = re.sub('TemplateCsvData', csvDataName, a)
                    fp.writelines(a) 
                fp.close()

    # copy templateCsvDataManager.cs
    csvDataManagerPathPath = cSharpPath + csvDataManagerName + ".cs"
    shutil.copy(templateCsvDataManagerPath, csvDataManagerPathPath)

    fp = None
    for classItem in classList:
        if(sysType == "Windows"):
            fp = open(csvDataManagerPathPath, 'r', encoding = 'utf-8')
            alllines = fp.readlines()
            fp.close() 
            fp = open(csvDataManagerPathPath, 'w', encoding = 'utf-8')
        else:
            fp = open(csvDataManagerPathPath, 'r')
            alllines = fp.readlines()
            fp.close() 
            fp = open(csvDataManagerPathPath, 'w') 

        # write start
        for eachline in alllines:
            # class name
            a = re.sub('TemplateCsvDataManager', csvDataManagerName, eachline)
            a = re.sub('TemplateCsvData', csvDataName, a)
            a = re.sub('//genCode','//genCode\n' + genCsCodeFromClass(classItem), a)
            fp.writelines(a) 
        fp.close()
        
    # copy templateCsvData.cs
    csvDataPath = cSharpPath + csvDataName + ".cs"
    shutil.copy(templateCsvDataPath, csvDataPath)

    fp = None
    if(sysType == "Windows"):
        fp = open(csvDataPath, 'r', encoding = 'utf-8')
        alllines = fp.readlines()
        fp.close() 
        fp = open(csvDataPath, 'w', encoding = 'utf-8')
    else:
        fp = open(csvDataPath, 'r')
        alllines = fp.readlines()
        fp.close() 
        fp = open(csvDataPath, 'w') 

    # write start
    for eachline in alllines:
        # class name
        a = re.sub('TemplateCsvData', csvDataName, eachline)
        fp.writelines(a) 
    fp.close()

    # print(classList)
                
genCode(csvPath)
print(color_str("Finish", fg_white, bg_green, a_italic))