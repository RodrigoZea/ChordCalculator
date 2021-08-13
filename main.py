# Chords program

notesArray = [
    "Do", #0, 12, 24
    "Do#", #1, 13, 25
    "Re", #2, 14, 26
    "Re#", #3, 15, 27
    "Mi", #4, 16, 28
    "Fa", #5, 17, 29
    "Fa#", #6, 18, 30
    "Sol", #7, 19, 31
    "Sol#", #8, 20, 32
    "La", #9, 21, 33
    "La#", #10, 22, 34
    "Si" #11, 23, 35
]

#TT 1/2T TT 1/2T
def generateMajorKey(rootNote):
    majorKey = []
    positions = [rootNote+2, rootNote+4, rootNote+5, rootNote+7, rootNote+9, rootNote+11]

    majorKey.append(notesArray[rootNote])
    for pos in positions:
        majorKey.append(notesArray[pos%12])

    return majorKey
         
def generateChords(majorKey):
    chords = []
    for i in range(0, len(majorKey)):
        chordPos = [i, i+2, i+4]
        chord = []

        for pos in chordPos:
            chord.append(majorKey[pos%7])
 
        chords.append(chord)

    return chords 


def generateQualityChords(chords):
    qualityChordsArray = []
    quality = ""
    for chord in chords:
        firstDistance = notesArray.index(chord[0]) - notesArray.index(chord[1])
        secondDistance = notesArray.index(chord[1]) - notesArray.index(chord[2])

        if firstDistance == 9:
            firstDistance = abs(firstDistance-12)
        if secondDistance == 9:
            secondDistance = abs(secondDistance-12)

        firstDistance = abs(firstDistance)
        secondDistance = abs(secondDistance)

        quality = getQuality(firstDistance, secondDistance)
        qualityChordsArray.append((chord, quality))
    
    return qualityChordsArray

def getQuality(firstDistance, secondDistance):
    quality = ""
    if (firstDistance == 4 and secondDistance == 3):
        quality = "Mayor"
    elif (firstDistance == 3 and secondDistance == 4):
        quality = "Menor"
    elif (firstDistance == 3 and secondDistance == 3):
        quality = "Disminuido"
    elif (firstDistance == 4 and secondDistance == 4):
        quality = "Aumentado"
    else:
        quality = "Ninguno"

    return quality

def getGrade(grade):
    # Re menor subdominante
    #1er 3er y 6to grados -> tonica
    #2do y 4to -> subdominante
    #5to y 7mo -> dominante
    gradeType = ""
    if (grade == 0 or grade == 2 or grade == 5):
        gradeType = "Tónica"
    elif (grade == 1 or grade == 3):
        gradeType = "Subdominante"
    elif (grade == 4 or grade == 6):
        gradeType = "Dominante"

    return gradeType

def main():
    startingNote = input("Ingrese la nota inicial (0: Do, 1: Do#, ..., 11: Si): ")

    if (int(startingNote) < 12):
        print("ESCALA MAYOR:")
        majorKey = generateMajorKey(int(startingNote))
        print(majorKey)

        print("----------------------------------------------------------")

        print("ACORDES:")
        chords = generateChords(majorKey)
        generateQualityChords(chords)


def returnGrade():
    grado = input("Ingrese el grado (1-7): ")
    #tonalidad

    if (int(grado) < 8):
        startingNote = input("Ingrese la nota inicial (0: Do, 1: Do#, ..., 11: Si): ")

        if (int(startingNote) < 12):
                gradoUse = int(grado)-1
                majorKey = generateMajorKey(int(startingNote))
                chords = generateChords(majorKey)
                qualityChords = generateQualityChords(chords)

                chordGrade = getGrade(gradoUse)
                chordOnIndex = qualityChords[gradoUse]

                print("NOTA: ", notesArray[int(startingNote)])
                print("ACORDE: ", chordOnIndex[0])
                print("CALIDAD: ", chordOnIndex[1])
                print("GRADO: ", chordGrade)
    
returnGrade()