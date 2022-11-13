# s

westernScale = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']

def importTextTab(filename):
    importTab = ''
    with open(filename) as f:
        importTab = f.read()
        importTab = str(importTab).split('\n')
    return importTab

def determinStringTuning(tab):
    """Determins the scale in a tab. Not really useful for how the program turned out"""
    stringTuning = []
    for i in tab:
       stringTuning.append(i[0])
    return stringTuning

def guitarStringScaleCreator(note):
    """Generates an interable scale from an input of a note
    and starts the scale from the input"""
    initalNote = westernScale.index(note.upper())
    string = []
    for i in westernScale:
        convertedNote = (westernScale.index(i)+initalNote)
        if convertedNote < 12:
            string.append(westernScale[convertedNote])
        if convertedNote >= 12 and convertedNote <= 24:
            string.append(westernScale[convertedNote-12])
    return string
    
def convertor(stringScale,note):
    """Takes an input of a number (between 0-24 aka poition on a guitar fret)
    and outputs a western scale note"""
    if int(note) < 12:
        return(stringScale[note])
    elif int(note) >= 12 and int(note) <= 24:
        return(stringScale[note-12])
    
def breakDownNotes(oldTab):
    newTab = []
    for string in oldTab:
        try: #Error checks for bad input
            if str(string[0]).upper() not in westernScale:
                newTab.append(string)
                continue
        except IndexError:
            continue
        scale = guitarStringScaleCreator(string[0])
        
        for note in string.split('-'):
            if note.isdigit():
                convertedNote = convertor(scale,int(note))
                if len(note) == len(convertedNote):
                    newString = string.replace(note, convertedNote)
                elif len(note) > len(convertedNote):
                    newString = string.replace(note, convertedNote + '-')       
                elif len(note) < len(convertedNote):
                    newString = string.replace(note + '-', convertedNote,1)
                string = newString
        
        newTab.append(string)
        
    return newTab  

def manualTabInput():
    userInputTab = []
    numOfStrings = int(input('How many strings?: '))
    while numOfStrings > 0:
        x = str(input('Input string ' + str(numOfStrings) + ' : '))
        userInputTab.append(x)
        numOfStrings -= 1
    return userInputTab

def run(tab):
    x = breakDownNotes(tab)
    for i in x:
        print(i)    
        
def removeTxt(input_):
    length = len(input_)
    output_ = input_[:length - 4]
    return output_
        
def runWrite(tab,filename):
    newFileName = removeTxt(filename) + '_ttn.txt' #NEEDS FIX
    with open(newFileName, "a") as f:
        f.write('\nTab to Notes:\n')
        x = breakDownNotes(tab)
        for i in x:
            f.write(i+ '\n') 
        f.write('\n2022 ttn tory sciacca c0')
    print(f'File: {newFileName} successfully created.')

def runUserInput():
    userInputTab = userInput() 
    x = breakDownNotes(manualTabInput)
    for i in x:
        print(i)

def manualfileInput():
    while True:
        try:
            filename = input('Please input file name...\n').strip() #user input
            importTextTab(filename) #file import
            print('Import successful.\nCreating File...')
            runWrite(importTextTab(filename),filename)
            print('Program closing...')
            break
        except Exception as e:
            print(f'{e}, try again\n')
        finally:
            pass

manualfileInput()