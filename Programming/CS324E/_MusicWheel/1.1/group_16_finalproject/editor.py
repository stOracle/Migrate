from gui import *

# Loads a song file
def loadSong(filename):
    file = open(filename, "r")
    rawSong = file.read().strip().split("\n")
    file.close()
    tempo = rawSong.pop(0)
    song = []
    for line in rawSong:
        song.append(line.split(","))
    return tempo, song

def setupEditor():
    global pos, song
    tempo, song = loadSong("song.txt")
    pos = len(song)

    # Updates the song by adding (or deleting) the given
    # note (str) from the current position of the head
    def addNote(note):
        # if this is a new chord, make it.
        if pos == len(song):
            song.append([note])
        # Delete note if it already exists in this chord
        elif note in song[pos]:
            delNote(note)
        elif note[0]+"#"+note[1] in song[pos]:
            delNote(note[0]+"#"+note[1])
        elif note[0]+"b"+note[1] in song[pos]:
            delNote(note[0]+"b"+note[1])
        # Else, add the note!
        else:
            song[pos].append(note)
        drawStaff()

    # Deletes the given note from the current chord.
    def delNote(note):
        song[pos].remove(note)
        # If the chord is now empty, remove it.
        if len(song[pos]) == 0:
            del song[pos]

    # Varies the sharpness/flatness of a note.
    # Natural -> Sharp -> Flat -> Natural
    # Input note is a string of the form: "C4#" for ex.
    def varyNote(note, chordNum):
        song[pos-chordNum].remove(note)
        if note[1] == "#": note = note.replace("#", "b")
        elif note[1] == "b": note = note.replace("b", "")
        else: note = note[0] + "#" + note[1]

        # Handle boundary cases so that we stay in the
        # range [C3 to B5]
        if note == "Cb3": note = "C3"
        elif note == "B#5": note = "Bb5"
        song[pos-chordNum].append(note)
        return note

    # Draws the given note (str) in the appropriate
    # chord field in the appropriate position.
    # Input note is a string of the form: "C4#" for ex.
    def drawNote(note, chordNum):
        noteButton = getGUI(note[0]+note[-1]+"button")
        x = noteButton.x + 22.5
        y = noteButton.y + 15
        noteImg = RoundButton(chordFields.children[chordNum])

        def action(noteImg=noteImg, chordNum=chordNum):
            note = noteImg.name()
            newNote = varyNote(note, chordNum)
            drawStaff()
            #noteImg.name(newNote) \
            #       .text(newNote[0] + newNote[2:])

        noteImg.position(x,y) \
               .radius(15) \
               .normalFill("#000000") \
               .pushedFill("#000000") \
               .textColor("#FFFFFF") \
               .textSize(16) \
               .name(note) \
               .text(note[0:len(note)-1]) \
               .onClick(action)

    # Redraws the staff based on the current state of song.
    # pos denotes position of the head. Can be in the range
    # [0, len(song)] inclusive
    def drawStaff():
        global pos
        # Clear out all the chord fields
        for i in range(7):
            chordFields.children[i].killChildren()

        # Draw the notes in each chord field for as many
        # as possible
        chordNum = 0
        for i in range(pos, max(pos-7, -1), -1):
            if i == len(song):
                chordNum += 1
                continue
            chord = song[i]
            for note in chord:
                drawNote(note, chordNum)
            chordNum += 1

    # Create main window object
    win = Window()
    win.position(25,25) \
       .size(width-50, height-50) \
       .strokeWeight(3)

    # Exit button
    exitButton = RectButton(win)
    exitButton.position(win.width()-30, 0) \
              .size(30, 30) \
              .strokeWeight(2) \
              .text("X") \
              .textSize(18) \
              .textColor("#FFFFFF") \
              .normalFill("#f9372b") \
              .pushedFill("#ae271e") \
              .onClick(lambda: win.kill())

    # Title text
    GUItext(win).text("Song Editor") \
                .position(win.width()/2.0, 10) \
                .textSize(28) \
                .textAlign(CENTER)

    # Staff
    staff = Window(win)
    staff.position(25, 105) \
         .size(win.width()-250, 360) \
         .strokeWeight(2) \
         .color("#FFFFFF")

    # Adjust window height according to staff height
    win.height(staff.height()+150)

    def scrollLeft():
        global pos
        if pos == 0: return
        pos -= 1
        drawStaff()
    # Staff scroll buttons
    scrollLeftButton = RectButton(staff)
    scrollLeftButton.position(staff.width()-225, staff.height()) \
                    .strokeWeight(2) \
                    .size(75, 30) \
                    .textSize(18) \
                    .text("<<<") \
                    .normalFill("#FFFF88") \
                    .pushedFill("#b9b963") \
                    .onClick(scrollLeft)

    def scrollRight():
        global pos
        if pos == len(song): return
        pos += 1
        drawStaff()
    scrollRightButton = RectButton(staff)
    scrollRightButton.position(staff.width()-150, \
                               staff.height()) \
                     .strokeWeight(2) \
                     .size(75, 30) \
                     .textSize(18) \
                     .text(">>>") \
                     .normalFill("#FFFF88") \
                     .pushedFill("#b9b963") \
                     .onClick(scrollRight)

    # Chord field group
    chordFields = GUI(staff)

    # New chord field
    newChordField = Window(chordFields)
    newChordField.position(staff.width()-75, 0) \
                 .strokeWeight(2) \
                 .size(75, staff.height()) \
                 .color("#abffab") \
                 .name("chordField0")

    # Other chord fields
    for i in range(1,7):
        Window(chordFields).position(staff.width()-75-i*75, 0) \
                           .name("chordField"+str(i)) \
                           .size(74, staff.height()) \
                           .color("#FFFFFF") \
                           .strokeWeight(0.5)

    # New note buttons
    noteButtons = GUI(staff)
    noteButtons.position(staff.width(), 0)
    def makeTrebleButtons():
        # Line notes
        B5 = RectButton(noteButtons)
        B5.position(0, 0) \
          .size(30, 30) \
          .textSize(16) \
          .name("B5button") \
          .text("B") \
          .onClick(lambda: addNote("B5"))
        G5 = RectButton(noteButtons)
        G5.position(0, 30) \
          .size(30, 30) \
          .textSize(16) \
          .name("G5button") \
          .text("G") \
          .onClick(lambda: addNote("G5"))
        E5 = RectButton(noteButtons)
        E5.position(0, 60) \
          .size(30, 30) \
          .textSize(16) \
          .name("E5button") \
          .text("E") \
          .onClick(lambda: addNote("E5"))
        C5 = RectButton(noteButtons)
        C5.position(0, 90) \
          .size(30, 30) \
          .textSize(16) \
          .name("C5button") \
          .text("C") \
          .onClick(lambda: addNote("C5"))
        # New octave
        A4 = RectButton(noteButtons)
        A4.position(0, 135) \
          .size(30, 30) \
          .textSize(16) \
          .name("A4button") \
          .text("A") \
          .onClick(lambda: addNote("A4"))
        F4 = RectButton(noteButtons)
        F4.position(0, 165) \
          .size(30, 30) \
          .textSize(16) \
          .name("F4button") \
          .text("F") \
          .onClick(lambda: addNote("F4"))
        D4 = RectButton(noteButtons)
        D4.position(0, 195) \
          .size(30, 30) \
          .textSize(16) \
          .name("D4button") \
          .text("D") \
          .onClick(lambda: addNote("D4"))
        # New octave
        B3 = RectButton(noteButtons)
        B3.position(0, 240) \
          .size(30, 30) \
          .textSize(16) \
          .name("B3button") \
          .text("B") \
          .onClick(lambda: addNote("B3"))
        G3 = RectButton(noteButtons)
        G3.position(0, 270) \
          .size(30, 30) \
          .textSize(16) \
          .name("G3button") \
          .text("G") \
          .onClick(lambda: addNote("G3"))
        E3 = RectButton(noteButtons)
        E3.position(0, 300) \
          .size(30, 30) \
          .textSize(16) \
          .name("E3button") \
          .text("E") \
          .onClick(lambda: addNote("E3"))
        C3 = RectButton(noteButtons)
        C3.position(0, 330) \
          .size(30, 30) \
          .textSize(16) \
          .name("C3button") \
          .text("C") \
          .onClick(lambda: addNote("C3"))

        # Space notes
        A5 = RectButton(noteButtons)
        A5.position(30, 15) \
          .size(30, 30) \
          .textSize(16) \
          .name("A5button") \
          .text("A") \
          .onClick(lambda: addNote("A5"))
        F5 = RectButton(noteButtons)
        F5.position(30, 45) \
          .size(30, 30) \
          .textSize(16) \
          .name("F5button") \
          .text("F") \
          .onClick(lambda: addNote("F5"))
        D5 = RectButton(noteButtons)
        D5.position(30, 75) \
          .size(30, 30) \
          .textSize(16) \
          .name("D5button") \
          .text("D") \
          .onClick(lambda: addNote("D5"))
        B4 = RectButton(noteButtons)
        B4.position(30, 120) \
          .size(30, 30) \
          .textSize(16) \
          .name("B4button") \
          .text("B") \
          .onClick(lambda: addNote("B4"))
        G4 = RectButton(noteButtons)
        G4.position(30, 150) \
          .size(30, 30) \
          .textSize(16) \
          .name("G4button") \
          .text("G") \
          .onClick(lambda: addNote("G4"))
        E4 = RectButton(noteButtons)
        E4.position(30, 180) \
          .size(30, 30) \
          .textSize(16) \
          .name("E4button") \
          .text("E") \
          .onClick(lambda: addNote("E4"))
        C4 = RectButton(noteButtons)
        C4.position(30, 210) \
          .size(30, 30) \
          .textSize(16) \
          .name("C4button") \
          .text("C") \
          .onClick(lambda: addNote("C4"))
        A3 = RectButton(noteButtons)
        A3.position(30, 255) \
          .size(30, 30) \
          .textSize(16) \
          .name("A3button") \
          .text("A") \
          .onClick(lambda: addNote("A3"))
        F3 = RectButton(noteButtons)
        F3.position(30, 285) \
          .size(30, 30) \
          .textSize(16) \
          .name("F3button") \
          .text("F") \
          .onClick(lambda: addNote("F3"))
        D3 = RectButton(noteButtons)
        D3.position(30, 315) \
          .size(30, 30) \
          .textSize(16) \
          .name("D3button") \
          .text("D") \
          .onClick(lambda: addNote("D3"))

    makeTrebleButtons()

    def clearChord():
        global pos
        if pos == len(song): return
        song.pop(pos)
        drawStaff()
    # Destroy highlighted chord button
    clearButton = RectButton(staff)
    clearButton.position(staff.width()-75, -30) \
               .strokeWeight(2) \
               .size(75, 30) \
               .textSize(18) \
               .text("Clear") \
               .textColor("#FFFFFF") \
               .normalFill("#ff4e4e") \
               .pushedFill("#832828") \
               .onClick(clearChord)
    '''
    # Play highlighted chord button
    # Plays as long as it is held (pushed)
    # Stops once user releases the mouse
    def playAction():
        global pos
        if pos == len(song): playChord([])
        else: playChord(song[pos])
    playButton = RectButton(staff)
    playButton.position(staff.width()-75, staff.height()) \
              .strokeWeight(2) \
              .size(75, 30) \
              .textSize(18) \
              .text("Play") \
              .normalFill("#33d157") \
              .pushedFill("#228d3b") \
              .onPush(playAction) \
              .onRelease(muteChord) \
              .onClick(muteChord)
    '''
    # Tempo radios
    # Tempo Title
    tempoTitle = GUItext(staff).hide()
    tempoTitle.position(staff.width()+75, -30) \
              .textSize(21) \
              .text("Tempo:")
    '''
    # Tempo radio group
    tempos = RadioGroup(tempoTitle)
    tempos.position(15, 45)

    # Tempo radios
    slowButton = RadioButton(tempos)
    slowButton.position(0, 60) \
              .radius(12.5) \
              .text("Slow") \
              .name("slow") \
              .clickZone(105)

    normButton = RadioButton(tempos)
    normButton.position(0, 30) \
              .radius(12.5) \
              .text("Normal") \
              .name("normal") \
              .clickZone(105)

    fastButton = RadioButton(tempos)
    fastButton.position(0, 0) \
              .radius(12.5) \
              .text("Fast") \
              .name("fast") \
              .clickZone(105)
    '''
    def saveSong():
        global song
        file = open("song.txt", "w")
        #file.write(tempos.activeChild.name())
        file.write("normal")  # Temporary hard-code
        file.write("\n")
        for chord in song:
            file.write(",".join(chord))
            file.write("\n")
        file.close()
        win.kill()

    # Save Button
    saveButton = RoundButton(tempoTitle)
    saveButton.radius(50) \
              .position(saveButton.radius()+10, 180) \
              .strokeWeight(3) \
              .normalFill("#0068ff") \
              .pushedFill("#003d97") \
              .textColor("#FFFFFF") \
              .textSize(24) \
              .text("Save!") \
              .onClick(saveSong)

    def revertSong():
        global pos, song
        tempo, song = loadSong("song.txt")
        pos = len(song)
        #getGUI(tempo).activate()
        drawStaff()
    # Revert Button
    revertButton = RectButton(tempoTitle)
    revertButton.position(25, 250) \
                .size(75, 30) \
                .strokeWeight(3) \
                .normalFill("#ffa500") \
                .pushedFill("#b97800") \
                .textColor("#000000") \
                .textSize(18) \
                .text("Revert") \
                .onClick(revertSong)
    '''
    # TEMP!!! Prints song to the console
    printSong = RectButton(tempoTitle)
    printSong.position(25, 300) \
             .size(75, 30) \
             .strokeWeight(3) \
             .text("Print song") \
             .textSize(13) \
             .onClick(lambda: printList(song))
    '''
    # Based on the tempo loaded in from song.txt,
    # Activate the correct radio button.
    #getGUI(tempo).activate()

    # Draw the staff for the first time
    drawStaff()

def printList(a):
    for elem in a:
        print(elem)
    print("")

# Takes a note as a string of the form "Db4"
# and converts it into non-flat form.
# E.g. it will take "Db4" and convert it to "C#4".
# and takes "Fb4" and converts it to "E4"
# If note is natural (not sharp OR flat), simply
# returns the note unchanged.
def makeSharp(note):
    # If note is natural OR sharp, just return it.
    if len(note) == 2 or note[1] == "#":
        return note
    num = int(note[-1])
    local = note[0:len(note)-1]
    if local == "Ab": local = "G#"
    elif local == "Bb": local = "A#"
    elif local == "Cb":
        local = "B"
        num -= 1
    elif local == "Db": local = "C#"
    elif local == "Eb": local = "D#"
    elif local == "Fb": local = "E"
    elif local == "Gb": local = "F#"
    else:
        print("ERROR in makeSharp().", note, "not recognized!")
        1/0
    return local + str(num)

# Takes a chord (list of notes, where each note is a string of
# the form "Cb4") and plays it until muteChord() is called.
def playChord(chord):
    # Make a local copy of the chord,
    # and convert its flats to sharps.
    chord = chord[:]
    for i in range(len(chord)):
        chord[i] = makeSharp(chord[i])

    # Your code here:
    # P.S. Make sure that you handle the special case
    # that chord = [] (empty list)
    pass

# While in the editor GUI, stop playing the active chord
def muteChord():
    # Your code here:
    pass