from gui import *

# Loads a song file
def loadSong(filename):
    file = open(filename, "r")
    song = []
    for line in file:
        song.append(line.strip().split(","))
    file.close()
    return song

def setupEditor():
    song = loadSong("song.txt")
    global song, pos
    pos = len(song)

    # Updates the song by adding (or deleting) the given
    # note (str) from the current position of the head
    def addNote(note):
        #return
        global song, pos
        # if this is a new chord, make it.
        if pos == len(song):
            song.append([note])
        # Delete note if it already exists in this chord
        elif note in song[pos]:
            delNote(note)
        # Else, add the note!
        else:
            song[pos].append(note)
        drawStaff()

    # Deletes the given note from the current chord.
    def delNote(note):
        global song, pos
        song[pos].remove(note)
        # If the chord is now empty, remove it.
        if len(song[pos]) == 0:
            del song[pos]

    # Draws the given note (str) in the appropriate
    # chord field in the appropriate position.
    def drawNote(note, chordNum):
        noteButton = getGUI(note)
        x = noteButton.x + 22.5
        y = noteButton.y + 15
        noteImg = RoundButton(chordFields.children[chordNum])
        noteImg.position(x,y) \
               .radius(15) \
               .normalFill("#000000") \
               .pushedFill("#000000") \
               .textColor("#FFFFFF") \
               .textSize(16) \
               .text(note[0])

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
        if pos == len(song):
            startPos = pos-1
            chordNum = 1
        else:
            startPos = pos
            chordNum = 0
        for i in range(startPos, max(startPos-7, -1), -1):
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
              .onClick(closeEditor)

    # Title text
    GUItext(win).text("Song Writer") \
                .position(win.width()/2.0, 10) \
                .textSize(28) \
                .textAlign(CENTER)

    # Staff
    staff = Window(win)
    staff.position(25, 105) \
         .size(win.width()-250, 180) \
         .strokeWeight(2) \
         .color("#FFFFFF")

    # Adjust window height according to staff height
    win.height(staff.height()+150)

    # Staff scroll buttons
    scrollLeftButton = RectButton(staff)
    scrollLeftButton.position(0, staff.height()) \
                    .strokeWeight(2) \
                    .size(75, 30) \
                    .textSize(18) \
                    .text("<<<") \
                    .normalFill("#FFFF88") \
                    .pushedFill("#b9b963")
    scrollRightButton = RectButton(staff)
    scrollRightButton.position(staff.width()-150, \
                               staff.height()) \
                     .strokeWeight(2) \
                     .size(75, 30) \
                     .textSize(18) \
                     .text(">>>") \
                     .normalFill("#FFFF88") \
                     .pushedFill("#b9b963")

    # Chord field group
    chordFields = GUI(staff)
    #staffChords = [ [], [], [], [], [], [], [] ]

    # New chord field
    newChordField = Window(chordFields)
    newChordField.position(staff.width()-75, 0) \
                 .strokeWeight(2) \
                 .size(75, staff.height()) \
                 .color("#abffab") \
                 .name("chordField0")

    # Other chord fields
    for i in range(1,7):
        GUI(chordFields).position(staff.width()-75-i*75, 0) \
                        .name("chordField"+str(i))

    # New note buttons
    noteButtons = GUI(staff)
    noteButtons.position(staff.width(), 0)
    def makeTrebleButtons():
        # Line notes
        F5 = RectButton(noteButtons)
        F5.position(0, 0) \
          .size(30, 30) \
          .textSize(16) \
          .name("F5") \
          .text("F") \
          .onClick(lambda: addNote("F5"))
        D5 = RectButton(noteButtons)
        D5.position(0, 30) \
          .size(30, 30) \
          .textSize(16) \
          .name("D5") \
          .text("D") \
          .onClick(lambda: addNote("D5"))
        B5 = RectButton(noteButtons)
        B5.position(0, 60) \
          .size(30, 30) \
          .textSize(16) \
          .name("B5") \
          .text("B") \
          .onClick(lambda: addNote("B5"))
        G4 = RectButton(noteButtons)
        G4.position(0, 90) \
          .size(30, 30) \
          .textSize(16) \
          .name("G4") \
          .text("G") \
          .onClick(lambda: addNote("G4"))
        E4 = RectButton(noteButtons)
        E4.position(0, 120) \
          .size(30, 30) \
          .textSize(16) \
          .name("E4") \
          .text("E") \
          .onClick(lambda: addNote("E4"))
        C4 = RectButton(noteButtons)
        C4.position(0, 150) \
          .size(30, 30) \
          .textSize(16) \
          .name("C4") \
          .text("C") \
          .onClick(lambda: addNote("C4"))
        # Space notes
        E5 = RectButton(noteButtons)
        E5.position(30, 15) \
          .size(30, 30) \
          .textSize(16) \
          .name("E5") \
          .text("E") \
          .onClick(lambda: addNote("E5"))
        C5 = RectButton(noteButtons)
        C5.position(30, 45) \
          .size(30, 30) \
          .textSize(16) \
          .name("C5") \
          .text("C") \
          .onClick(lambda: addNote("C5"))
        A5 = RectButton(noteButtons)
        A5.position(30, 75) \
          .size(30, 30) \
          .textSize(16) \
          .name("A5") \
          .text("A") \
          .onClick(lambda: addNote("A5"))
        F4 = RectButton(noteButtons)
        F4.position(30, 105) \
          .size(30, 30) \
          .textSize(16) \
          .name("F4") \
          .text("F") \
          .onClick(lambda: addNote("F4"))
        D4 = RectButton(noteButtons)
        D4.position(30, 135) \
          .size(30, 30) \
          .textSize(16) \
          .name("D4") \
          .text("D") \
          .onClick(lambda: addNote("D4"))

    makeTrebleButtons()
    '''
    # Add new chord button
    addButton = RectButton(staff)
    addButton.position(staff.width()-75, \
                        staff.height()) \
             .strokeWeight(2) \
             .size(75, 30) \
             .textSize(18) \
             .text("Add") \
             .normalFill("#ffb94b") \
             .pushedFill("#b38234")
    '''
    # Destroy highlighted chord button
    clearButton = RectButton(staff)
    clearButton.position(staff.width()-75, -30) \
               .strokeWeight(2) \
               .size(75, 30) \
               .textSize(18) \
               .text("Clear") \
               .textColor("#FFFFFF") \
               .normalFill("#ff4e4e") \
               .pushedFill("#832828")

    # Play highlighted chord button
    playButton = RectButton(staff)
    playButton.position(staff.width()-75, staff.height()) \
              .strokeWeight(2) \
              .size(75, 30) \
              .textSize(18) \
              .text("Play") \
              .normalFill("#33d157") \
              .pushedFill("#228d3b")

    # Tempo radios
    # Tempo Title
    tempoTitle = GUItext(staff)
    tempoTitle.position(staff.width()+75, -30) \
              .textSize(21) \
              .text("Tempo:")
    # Tempo radio group
    tempos = RadioGroup(tempoTitle)
    tempos.position(15, 45)

    # Tempo radios
    slowButton = RadioButton(tempos)
    slowButton.position(0, 60) \
              .radius(12.5) \
              .text("Slow") \
              .clickZone(105)

    normButton = RadioButton(tempos)
    normButton.position(0, 30) \
              .radius(12.5) \
              .text("Normal") \
              .clickZone(105) \
              .activate()

    fastButton = RadioButton(tempos)
    fastButton.position(0, 0) \
              .radius(12.5) \
              .text("Fast") \
              .clickZone(105)

    # Save Button
    saveButton = RoundButton(tempoTitle)
    saveButton.radius(50) \
              .position(saveButton.radius()+10, 180) \
              .strokeWeight(3) \
              .normalFill("#0068ff") \
              .pushedFill("#003d97") \
              .textColor("#FFFFFF") \
              .textSize(24) \
              .text("Save!")

    # Revert Button
    revertButton = RectButton(staff)
    revertButton.position(staff.width()-150, -30) \
                .size(75, 30) \
                .strokeWeight(3) \
                .normalFill("#ffa500") \
                .pushedFill("#b97800") \
                .textColor("#000000") \
                .textSize(18) \
                .text("Revert")

    drawStaff()

def closeEditor():
    exit()
