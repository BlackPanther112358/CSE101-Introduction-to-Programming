#Declaring global variables
notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

#Defining functions
def clearFiles():
    with open(r'scaleMinor.txt', 'w') as f_write:
        f_write.write('')
    with open(r'scaleMajor.txt', 'w') as f_write:
        f_write.write('')
    return

def inputRoot()->str:
    try_cnt = 0
    while try_cnt < 3:
        try_cnt += 1
        try:
            inpt = input('Please enter the root note for the scale: ').strip()
            if inpt in notes:
                return inpt
            else:
                print('Please enter a valid note as input.')
        except Exception:
            print('Please provide input in correct input.')
            continue
    print('Program terminated due to multiple incorrect inputs.')
    return False

def inputScale()->str:
    try_cnt = 0
    while try_cnt < 3:
        try_cnt += 1
        try:
            inpt = input('Please enter the required scale of the root note (Major/Minor): ').strip()
            inpt = inpt.lower()
            if inpt == 'minor':
                return 'Minor'
            elif inpt == 'major':
                return 'Major'
            else:
                print('Please enter \'Minor\' or \'Major\' as the input.')
        except Exception:
            print('Please provide input in correct input.')
            continue
    print('Program terminated due to multiple incorrect inputs.')
    return False

def minorScale(root:str)->str:     
    step = 'WHWWHWWW'   #Added a W to avoid indexing error, it doesn't effect the output
    itr = notes.index(root)
    ans = ''
    for i in range(8):
        ans += notes[itr%12]
        ans += ('\'')*(itr//12)
        ans += ' '
        if step[i] == 'W':
            itr += 2
        else:
            itr += 1
    return ans

def majorScale(root:str)->str:    
    step = 'WWHWWWHW'   #Added a W to avoid indexing error, it doesn't effect the output
    itr = notes.index(root)
    ans = ''
    for i in range(8):
        ans += notes[itr%12]
        ans += ('\'')*(itr//12)
        ans += ' '
        if step[i] == 'W':
            itr += 2
        else:
            itr += 1
    return ans

def noteCreate():
    clearFiles()
    for note in notes:
        minorscale = minorScale(note)
        with open(r'scaleMinor.txt', 'a') as f_write:
            f_write.write(minorscale + '\n')
        majorscale = majorScale(note)
        with open(r'scaleMajor.txt', 'a') as f_write:
            f_write.write(majorscale + '\n')
    return

def majorNotes(root:str)->str:
    with open(r'scaleMajor.txt', 'r') as f_read:
        for _ in range(notes.index(root)):
            data = f_read.readline()
        data = f_read.readline()
        data.strip(r'\n')
        print(f'The Major scale in the key of {root} is:')
        print(data)
    return 

def minorNotes(root:str)->str:
    with open(r'scaleMinor.txt', 'r') as f_read:
        for _ in range(notes.index(root)):
            data = f_read.readline()
        data = f_read.readline()
        data.strip(r'\n')
        print(f'The Major scale in the key of {root} is:')
        print(data)
    return

def main():
    noteCreate()
    root = inputRoot()
    if root is False:
        return
    scale = inputScale()
    if scale is False:
        return
    if scale == 'Major':
        majorNotes(root)
    else:
        minorNotes(root)
    return

#Driver code
if __name__ == '__main__':
    print('-'*100)
    main()
    print('-'*100)