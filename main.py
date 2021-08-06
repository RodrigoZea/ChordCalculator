# Chords program

notesArray = [
    "Do",
    "Do#",
    "Re",
    "Re#",
    "Mi",
    "Fa",
    "Fa#",
    "Sol",
    "Sol#",
    "La",
    "La#",
    "Si"
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
        print(chord, quality)

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

"""
['Do' - 4 - 'Mi' - 3 - 'Sol']
['Re' - 3 - 'Fa' - 4 - 'La']
['Mi' - 3 'Sol' - 4 - 'Si']
['Fa' - 4 - 'La' - 3 - 'Do']
['Sol' - 4 - 'Si' - 3 - 'Re']
['La' - 3 - 'Do' - 4 - 'Mi']
['Si' - 3 - 'Re' - 3 - 'Fa']
"""

def main():
    startingNote = input("Ingrese la nota inicial (0: Do, 1: Do, ..., 11: Si): ")

    if (int(startingNote) < 12):
        print("ESCALA MAYOR:")
        majorKey = generateMajorKey(int(startingNote))
        print(majorKey)

        print("----------------------------------------------------------")

        print("ACORDES:")
        chords = generateChords(majorKey)
        generateQualityChords(chords)

main()