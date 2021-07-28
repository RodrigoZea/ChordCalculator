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
    for i in range(0, len(majorKey)):
        chordPos = [i, i+2, i+4]
        chord = []

        for pos in chordPos:
            chord.append(majorKey[pos%7])

        print(chord)  

def main():
    startingNote = input("Ingrese la nota inicial (0: Do, 1: Do, ..., 11: Si): ")

    if (int(startingNote) < 12):
        print("ESCALA MAYOR:")
        majorKey = generateMajorKey(int(startingNote))
        print(majorKey)

        print("ACORDES:")
        chords = generateChords(majorKey)

main()