# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

add_library('sound')
from editor import *
from Music import *

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

global songPlaying
songPlaying = False

notes = [] #stores the 12 Tone objects that play sound
wheelbuttons = [] #stores the 12 wheel buttons on the screen
modes = ['Free', 'Instrument', 'Song']
mode = 'Free'

songList = []
chordNumber = 0
custom = False
allFrequencies = []
customNotes = []

# Lists of frequencies, button positions, and notes of those frequencies respectively
middlehz = [131, 139, 147, 156, 165, 175, 185, 196, 208, 220, 233, 247, 262, 277, 294, 311, 330, 349, 370, 392, 415, 440, 466, 494, 523, 554, 587, 622, 659, 698, 740, 784, 831, 880, 932, 988]
circlebuttons = [[400, 550],[275, 517],[183, 425],[150, 300],[183, 175],[275, 83],[400, 50],[525, 83],[617, 175],[650, 300],[617, 425],[525, 517]]
pitches = ['C3', 'C#3', 'D3', 'D#3', 'E3', 'F3', 'F#3', 'G3', 'G#3', 'A3', 'A#3', 'B3','C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4', 'G#4', 'A4', 'A#4', 'B4','C5', 'C#5', 'D5', 'D#5', 'E5', 'F5', 'F#5', 'G5', 'G#5', 'A5', 'A#5', 'B5']

for i in range(len(middlehz)):
    allFrequencies.append(TriOsc(this))
    allFrequencies[i].freq(middlehz[i])

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def setup():
    size(825, 600)

    editSongs = RectButton()
    editSongs.position(650, 30) \
          .size(140, 40) \
          .textSize(20) \
          .name("EditorButton") \
          .text("Song Editor") \
          .onClick(setupEditor)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    # Rotates between modes when clicking mode button
    def changeMode(modeButton):
        global mode
        for i in range(3):
            if mode == modes[i]:
                mode = modes[(i+1) % len(modes)]
                break
        modeButton.txt = 'Mode: ' + mode
        wheel.muteAll()

    modeButton = RectButton()
    modeButton.position(650, 70) \
              .size(140, 40) \
              .textSize(16) \
              .text('Mode: ' + mode) \
              .onClick(lambda: changeMode(modeButton))

    #song1 = Song('C', 'Demo.txt')
    #progression1 = song1.chords

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def draw():
    global songPlaying
    background(200)
    strokeWeight(5)
    wheel.displayWheel()
    wheel.makeLines()
    displayGUI()
    if songPlaying:
        callKeyPress("a", RIGHT)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def keyPressed():
    callKeyPress(key, keyCode)

def callKeyPress(key, keyCode):

    global chordNumber
    global customNotes

    if mode != 'Song':
        # transpose the circle a half-note up or down
        if (keyCode == LEFT):
            wheel.changeOrder('left')
        elif (keyCode == RIGHT):
            wheel.changeOrder('right')

        # transpose the circle an octave up or town
        elif (keyCode == UP):
            wheel.changeOrder('up')
        elif (keyCode == DOWN):
            wheel.changeOrder('down')

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    if mode == 'Song':
        if (key == ' ' and chordNumber == 0):
            wheel.playSong('Demo.txt')
            print (songList)
            wheel.changeOrder(songList[0][0])
            for note in songList[0]:
                for i in range(len(wheel.order)):
                    if note == wheel.order[i]:
                        wheel.playInstrument(notes[i], middlehz[wheel.keyStart + i], wheelbuttons[i])
                        break
            chordNumber += 1

        elif (keyCode == RIGHT and chordNumber != 0 and custom == False):
            wheel.muteSong()
            for note in songList[chordNumber % 5]:
                for i in range(len(wheel.order)):
                    if note == wheel.order[i]:
                        wheel.playInstrument(notes[i], middlehz[wheel.keyStart + i], wheelbuttons[i])
                        break
            chordNumber += 1

        elif (key == 'a' and chordNumber == 0):
            global songPlaying
            songPlaying = True
            frameRate(6)
            wheel.playSong('song.txt')
            for note in songList[0]:
                for i in range(len(pitches)):
                    if note == pitches[i]:
                        customNotes.append(allFrequencies[i])
                        customNotes[-1].play()
                        break
            chordNumber += 1

        elif (keyCode == RIGHT and chordNumber != 0 and custom):
            for osc in customNotes:
                osc.stop()
            customNotes = []
            for note in songList[chordNumber % len(songList)]:
                for i in range(len(pitches)):
                    if note == pitches[i]:
                        customNotes.append(allFrequencies[i])
                        customNotes[-1].play()
                        break
            chordNumber += 1




# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    #plays sound with the keyboard inputs when in instrument mode
    if (mode == 'Instrument'):
        if (keyPressed == False):
            wheel.muteAll()
        else:
            if (key == '1' and notes[0].isPlaying == False):
                wheel.playInstrument(notes[0], middlehz[0 + wheel.keyStart], wheelbuttons[0])
            if (key == '2' and notes[1].isPlaying == False):
                wheel.playInstrument(notes[1], middlehz[1 + wheel.keyStart], wheelbuttons[1])
            if (key == '3' and notes[2].isPlaying == False):
                wheel.playInstrument(notes[2], middlehz[2 + wheel.keyStart], wheelbuttons[2])
            if (key == '4' and notes[3].isPlaying == False):
                wheel.playInstrument(notes[3], middlehz[3 + wheel.keyStart], wheelbuttons[3])
            if (key == '5' and notes[4].isPlaying == False):
                wheel.playInstrument(notes[4], middlehz[4 + wheel.keyStart], wheelbuttons[4])
            if (key == '6' and notes[5].isPlaying == False):
                wheel.playInstrument(notes[5], middlehz[5 + wheel.keyStart], wheelbuttons[5])
            if (key == '7' and notes[6].isPlaying == False):
                wheel.playInstrument(notes[6], middlehz[6 + wheel.keyStart], wheelbuttons[6])
            if (key == '8' and notes[7].isPlaying == False):
                wheel.playInstrument(notes[7], middlehz[7 + wheel.keyStart], wheelbuttons[7])
            if (key == '9' and notes[8].isPlaying == False):
                wheel.playInstrument(notes[8], middlehz[8 + wheel.keyStart], wheelbuttons[8])
            if (key == '0' and notes[9].isPlaying == False):
                wheel.playInstrument(notes[9], middlehz[9 + wheel.keyStart], wheelbuttons[9])
            if (key == '-' and notes[10].isPlaying == False):
                wheel.playInstrument(notes[10], middlehz[10 + wheel.keyStart], wheelbuttons[10])
            if (key == '=' and notes[11].isPlaying == False):
                wheel.playInstrument(notes[11], middlehz[11 + wheel.keyStart], wheelbuttons[11])

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def keyReleased():
    #stops sound on key release during instrument mode
    if mode == 'Instrument':
        if (key == '1' and notes[0].isPlaying == True):
            wheel.playInstrument(notes[0], middlehz[0 + wheel.keyStart], wheelbuttons[0])
        if (key == '2' and notes[1].isPlaying == True):
            wheel.playInstrument(notes[1], middlehz[1 + wheel.keyStart], wheelbuttons[1])
        if (key == '3' and notes[2].isPlaying == True):
            wheel.playInstrument(notes[2], middlehz[2 + wheel.keyStart], wheelbuttons[2])
        if (key == '4' and notes[3].isPlaying == True):
            wheel.playInstrument(notes[3], middlehz[3 + wheel.keyStart], wheelbuttons[3])
        if (key == '5' and notes[4].isPlaying == True):
            wheel.playInstrument(notes[4], middlehz[4 + wheel.keyStart], wheelbuttons[4])
        if (key == '6' and notes[5].isPlaying == True):
            wheel.playInstrument(notes[5], middlehz[5 + wheel.keyStart], wheelbuttons[5])
        if (key == '7' and notes[6].isPlaying == True):
            wheel.playInstrument(notes[6], middlehz[6 + wheel.keyStart], wheelbuttons[6])
        if (key == '8' and notes[7].isPlaying == True):
            wheel.playInstrument(notes[7], middlehz[7 + wheel.keyStart], wheelbuttons[7])
        if (key == '9' and notes[8].isPlaying == True):
            wheel.playInstrument(notes[8], middlehz[8 + wheel.keyStart], wheelbuttons[8])
        if (key == '0' and notes[9].isPlaying == True):
            wheel.playInstrument(notes[9], middlehz[9 + wheel.keyStart], wheelbuttons[9])
        if (key == '-' and notes[10].isPlaying == True):
            wheel.playInstrument(notes[10], middlehz[10 + wheel.keyStart], wheelbuttons[10])
        if (key == '=' and notes[11].isPlaying == True):
            wheel.playInstrument(notes[11], middlehz[11 + wheel.keyStart], wheelbuttons[11])

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def mousePressed():
    handleGUImousePress()

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def mouseReleased():
    handleGUImouseRelease()

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def mouseMoved():
    handleGUImouseMove()

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

class Tone(object):

    def __init__(self, pitch):
        self.tone = TriOsc(this) #the object that sound is played with
        self.isPlaying = False
        self.pitch = pitch #String version of pitch

# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////

class MusicWheel(object):

    def __init__(self):
        #the order starting from the bottom and going clockwise of the 12 wheel buttons. keyStart changes the starting place of this order from the main list of pitches
        self.order = ['C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4', 'G#4', 'A4', 'A#4', 'B4']
        self.keyStart = 12

        #the following chunks of code initialize all of the buttons and Tone objects for the wheel
        self.note1 = Tone('C4')
        notes.append(self.note1)
        note1 = RoundButton()
        wheelbuttons.append(note1)
        note1.position(400, 550) \
          .radius(30) \
          .textSize(30) \
          .text(self.order[0]) \
          .onClick(lambda: self.playSound(self.note1, middlehz[0+self.keyStart], note1))

        self.note2 = Tone('C#4')
        notes.append(self.note2)
        note2 = RoundButton()
        wheelbuttons.append(note2)
        note2.position(275, 517) \
          .radius(30) \
          .textSize(30) \
          .text(self.order[1]) \
          .onClick(lambda: self.playSound(self.note2, middlehz[1+self.keyStart], note2))

        self.note3 = Tone('D4')
        notes.append(self.note3)
        note3 = RoundButton()
        wheelbuttons.append(note3)
        note3.position(183, 425) \
          .radius(30) \
          .textSize(30) \
          .text(self.order[2]) \
          .onClick(lambda: self.playSound(self.note3, middlehz[2+self.keyStart], note3))

        self.note4 = Tone('D#4')
        notes.append(self.note4)
        note4 = RoundButton()
        wheelbuttons.append(note4)
        note4.position(150, 300) \
          .radius(30) \
          .textSize(30) \
          .text(self.order[3]) \
          .onClick(lambda: self.playSound(self.note4, middlehz[3+self.keyStart], note4))

        self.note5 = Tone('E#4')
        notes.append(self.note5)
        note5 = RoundButton()
        wheelbuttons.append(note5)
        note5.position(183, 175) \
          .radius(30) \
          .textSize(30) \
          .text(self.order[4]) \
          .onClick(lambda: self.playSound(self.note5, middlehz[4+self.keyStart], note5))

        self.note6 = Tone('F4')
        notes.append(self.note6)
        note6 = RoundButton()
        wheelbuttons.append(note6)
        note6.position(275, 83) \
          .radius(30) \
          .textSize(30) \
          .text(self.order[5]) \
          .onClick(lambda: self.playSound(self.note6, middlehz[5+self.keyStart], note6))

        self.note7 = Tone('F#4')
        notes.append(self.note7)
        note7 = RoundButton()
        wheelbuttons.append(note7)
        note7.position(400, 50) \
          .radius(30) \
          .textSize(30) \
          .text(self.order[6]) \
          .onClick(lambda: self.playSound(self.note7, middlehz[6+self.keyStart], note7))

        self.note8 = Tone('G4')
        notes.append(self.note8)
        note8 = RoundButton()
        wheelbuttons.append(note8)
        note8.position(525, 83) \
          .radius(30) \
          .textSize(30) \
          .text(self.order[7]) \
          .onClick(lambda: self.playSound(self.note8, middlehz[7+self.keyStart], note8))

        self.note9 = Tone('G#4')
        notes.append(self.note9)
        note9 = RoundButton()
        wheelbuttons.append(note9)
        note9.position(617, 175) \
          .radius(30) \
          .textSize(30) \
          .text(self.order[8]) \
          .onClick(lambda: self.playSound(self.note9, middlehz[8+self.keyStart], note9))

        self.note10 = Tone('A4')
        notes.append(self.note10)
        note10 = RoundButton()
        wheelbuttons.append(note10)
        note10.position(650, 300) \
          .radius(30) \
          .textSize(30) \
          .text(self.order[9]) \
          .onClick(lambda: self.playSound(self.note10, middlehz[9+self.keyStart], note10))

        self.note11 = Tone('A#4')
        notes.append(self.note11)
        note11 = RoundButton()
        wheelbuttons.append(note11)
        note11.position(617, 425) \
          .radius(30) \
          .textSize(30) \
          .text(self.order[10]) \
          .onClick(lambda: self.playSound(self.note11, middlehz[10+self.keyStart], note11))

        self.note12 = Tone('B4')
        notes.append(self.note12)
        note12 = RoundButton()
        wheelbuttons.append(note12)
        note12.position(525, 517) \
          .radius(30) \
          .textSize(30) \
          .text(self.order[11]) \
          .onClick(lambda: self.playSound(self.note12, middlehz[11+self.keyStart], note12))

        masterMute = RectButton()
        masterMute.position(650, 500) \
                  .size(150, 50) \
                  .textSize(25) \
                  .text('MUTE ALL') \
                  .onClick(lambda: self.muteAll())

    # def playSong(self, chords):
    #     for chord in chords:
    #         if chord.seventh == None:
    #             note1 = TriOsc()
    #             note1.freq(chord.root.pitch)

    def muteAll(self):
        global chordNumber, custom, mode, customNotes, songPlaying
        songPlaying = False
        frameRate(60)
        chordNumber = 0
        for note in notes:
            note.tone.stop()
            note.isPlaying = False

        for note in wheelbuttons:
            note.fill = '#FFFFFF'
            note.R = 30

        if (custom == True):
            for osc in customNotes:
                osc.stop()
            del customNotes[:]
            custom = False

    def muteSong(self):
        for note in notes:
            note.tone.stop()
            note.isPlaying = False

        for note in wheelbuttons:
            note.fill = '#FFFFFF'
            note.R = 30

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////

    #changes what appears and is available to be played on the wheel. could possibly add another if statement later for receieving any music key as input
    def changeOrder(self, input):
        if input == 'left':
            if (self.keyStart == 0):
                pass
            else:
                self.keyStart -= 1
                self.order = []
                for i in range(self.keyStart, self.keyStart+12):
                    self.order.append(pitches[i])
                for i in range(len(notes)):
                    notes[i].pitch = self.order[i]
                    notes[i].tone.stop()
                    wheelbuttons[i].txt = self.order[i]
                    if (notes[i].isPlaying):
                        notes[i].tone.freq(middlehz[i + self.keyStart])
                        notes[i].tone.play()

        elif input == 'right':
            if (self.keyStart == 24):
                pass
            else:
                self.keyStart += 1
                self.order = []
                for i in range(self.keyStart, self.keyStart+12):
                    self.order.append(pitches[i])
                for i in range(len(notes)):
                    notes[i].pitch = self.order[i]
                    notes[i].tone.stop()
                    wheelbuttons[i].txt = self.order[i]
                    if (notes[i].isPlaying):
                        notes[i].tone.freq(middlehz[i + self.keyStart])
                        notes[i].tone.play()

        # octave shift up - 12 half notes
        elif input == 'up':

            if (self.keyStart >= 12):
                self.keyStart = 24
            else:
                self.keyStart += 12

            self.order = []
            for i in range (self.keyStart, self.keyStart + 12):
                self.order.append(pitches[i])
            for i in range(len(notes)):
                notes[i].pitch = self.order[i]
                notes[i].tone.stop()
                wheelbuttons[i].txt = self.order[i]
                if (notes[i].isPlaying):
                    notes[i].tone.freq(middlehz[i + self.keyStart])
                    notes[i].tone.play()

        # octave shift down - 12 half notes
        elif input == 'down':

            if (self.keyStart <= 12):
                self.keyStart = 0
            else:
                self.keyStart -= 12

            self.order = []
            for i in range (self.keyStart, self.keyStart + 12):
                self.order.append(pitches[i])
            for i in range (len(notes)):
                notes[i].pitch = self.order[i]
                notes[i].tone.stop()
                wheelbuttons[i].txt = self.order[i]
                if (notes[i].isPlaying):
                    notes[i].tone.freq(middlehz[i + self.keyStart])
                    notes[i].tone.play()

        else:
            for i in range(len(pitches)):
                if input == pitches[i]:
                    self.keyStart = i
                    self.order = []
                    break
            for i in range (self.keyStart, self.keyStart + 12):
                self.order.append(pitches[i])
            for i in range (len(notes)):
                notes[i].pitch = self.order[i]
                notes[i].tone.stop()
                wheelbuttons[i].txt = self.order[i]



#///////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def displayWheel(self):
        noFill()
        ellipse(400, 300, 500, 500)

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////

    #for playing sound in Free mode
    def playSound(self, note, frequency, button):
        if mode == 'Free':
            if (note.isPlaying):
                note.tone.stop()
                note.isPlaying = False
                button.fill = '#FFFFFF'
                button.R = 30
            else:
                note.tone.freq(frequency)
                note.tone.play()
                note.isPlaying = True
                button.fill = "#4CB5FA"
                button.R = 35

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////

    #for playing sound in Instrument mode
    def playInstrument(self, note, frequency, button):
        if (note.isPlaying):
            note.tone.stop()
            note.isPlaying = False
            button.fill = '#FFFFFF'
            button.R = 30
        else:
            note.tone.freq(frequency)
            note.tone.play()
            note.isPlaying = True
            button.fill = "#4CB5FA"
            button.R = 35

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def playSong (self, file_name):
        global songList
        global custom
        songList = []

        if file_name == "Demo.txt":
            in_file = open("Demo.txt", "r")
            #numSongs = int(in_file.readline())
            for i in range (5):
                chord = in_file.readline().strip().split(',')
                # numChords = int(in_file.readline())
                # songKey = in_file.readline()
                # chordList = []
                # for j in range (numChords):
                #     chord = in_file.readline().strip().split()
                #     chordList.append(chord)
                #song = Song(songKey, chordList)
                songList.append(chord)

        if file_name == "song.txt":
            custom = True
            in_file = open('song.txt', 'r')
            for songchord in in_file:
                if songchord.strip() == 'normal':
                    continue
                chord = songchord.strip().split(',')
                songList.append(chord)


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////

    def makeLines(self):
        playingButtons = []
        for i in range(len(notes)):
            if notes[i].isPlaying:
                playingButtons.append(circlebuttons[i])
        if len(playingButtons) > 1:
            for i in range(len(playingButtons) - 1):
                line(playingButtons[i][0], playingButtons[i][1], playingButtons[i+1][0], playingButtons[i+1][1])
            line(playingButtons[0][0], playingButtons[0][1], playingButtons[-1][0], playingButtons[-1][1])

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////

wheel = MusicWheel()