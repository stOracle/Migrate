add_library('sound')
from editor import *
from Music import *
notes = []
wheelbuttons = []

def setup():
    size(825, 600)   
    
    editSongs = RectButton()
    editSongs.position(650, 30) \
          .size(140, 40) \
          .textSize(20) \
          .name("EditorButton") \
          .text("Song Editor") \
          .onClick(setupEditor)
          
    song1 = Song('C', 'Demo.txt')
    progression1 = song1.chords 
    
def draw():
    background(200)
    strokeWeight(5)
    wheel.displayWheel()        
    wheel.makeLines()
    displayGUI()
    
def keyPressed():
    if (key == 'a'):
        pass    
    
def mousePressed():
    handleGUImousePress()
    
def mouseReleased():
    handleGUImouseRelease()
    
def mouseMoved():
    handleGUImouseMove()

###### MusicWheel class begins here ######

middlehz = [262, 277, 294, 311, 330, 349, 370, 392, 415, 440, 466, 494]
circlebuttons = [[400, 550],[275, 517],[183, 425],[150, 300],[183, 175],[275, 83],[400, 50],[525, 83],[617, 175],[650, 300],[617, 425],[525, 517]]

class Tone(object):
    
    def __init__(self):
        self.tone = TriOsc(this)
        self.isPlaying = False
    
class MusicWheel(object):
    
    def __init__(self):
        self.order = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        
        self.note1 = Tone()
        notes.append(self.note1)        
        note1 = RoundButton()
        wheelbuttons.append(note1)
        note1.position(400, 550) \
          .radius(30) \
          .textSize(30) \
          .text(self.order[0]) \
          .onClick(lambda: self.playSound(self.note1, middlehz[0], note1))
        
        self.note2 = Tone()
        notes.append(self.note2) 
        note2 = RoundButton()
        wheelbuttons.append(note2)
        note2.position(275, 517) \
          .radius(30) \
          .textSize(30) \
          .text(self.order[1]) \
          .onClick(lambda: self.playSound(self.note2, middlehz[1], note2))
        
        self.note3 = Tone()
        notes.append(self.note3)
        note3 = RoundButton()
        wheelbuttons.append(note3)
        note3.position(183, 425) \
          .radius(30) \
          .textSize(30) \
          .text(self.order[2]) \
          .onClick(lambda: self.playSound(self.note3, middlehz[2], note3))
          
        self.note4 = Tone()
        notes.append(self.note4)        
        note4 = RoundButton()
        wheelbuttons.append(note4)
        note4.position(150, 300) \
          .radius(30) \
          .textSize(30) \
          .text(self.order[3]) \
          .onClick(lambda: self.playSound(self.note4, middlehz[3], note4))
          
        self.note5 = Tone()
        notes.append(self.note5)        
        note5 = RoundButton()
        wheelbuttons.append(note5)
        note5.position(183, 175) \
          .radius(30) \
          .textSize(30) \
          .text(self.order[4]) \
          .onClick(lambda: self.playSound(self.note5, middlehz[4], note5))
          
        self.note6 = Tone()
        notes.append(self.note6)
        note6 = RoundButton()
        wheelbuttons.append(note6)
        note6.position(275, 83) \
          .radius(30) \
          .textSize(30) \
          .text(self.order[5]) \
          .onClick(lambda: self.playSound(self.note6, middlehz[5], note6))
        
        self.note7 = Tone()
        notes.append(self.note7)
        note7 = RoundButton()
        wheelbuttons.append(note7)
        note7.position(400, 50) \
          .radius(30) \
          .textSize(30) \
          .text(self.order[6]) \
          .onClick(lambda: self.playSound(self.note7, middlehz[6], note7))
          
        self.note8 = Tone()
        notes.append(self.note8)
        note8 = RoundButton()
        wheelbuttons.append(note8)
        note8.position(525, 83) \
          .radius(30) \
          .textSize(30) \
          .text(self.order[7]) \
          .onClick(lambda: self.playSound(self.note8, middlehz[7], note8))
          
        self.note9 = Tone()
        notes.append(self.note9)
        note9 = RoundButton()
        wheelbuttons.append(note9)
        note9.position(617, 175) \
          .radius(30) \
          .textSize(30) \
          .text(self.order[8]) \
          .onClick(lambda: self.playSound(self.note9, middlehz[8], note9))
          
        self.note10 = Tone()
        notes.append(self.note10)
        note10 = RoundButton()
        wheelbuttons.append(note10)
        note10.position(650, 300) \
          .radius(30) \
          .textSize(30) \
          .text(self.order[9]) \
          .onClick(lambda: self.playSound(self.note10, middlehz[9], note10))
        
        self.note11 = Tone()
        notes.append(self.note11)
        note11 = RoundButton()
        wheelbuttons.append(note11)
        note11.position(617, 425) \
          .radius(30) \
          .textSize(30) \
          .text(self.order[10]) \
          .onClick(lambda: self.playSound(self.note11, middlehz[10], note11))
          
        self.note12 = Tone()
        notes.append(self.note12)
        note12 = RoundButton()
        wheelbuttons.append(note12)
        note12.position(525, 517) \
          .radius(30) \
          .textSize(30) \
          .text(self.order[11]) \
          .onClick(lambda: self.playSound(self.note12, middlehz[11], note12))
          
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
        for note in notes:            
            note.tone.stop()
            note.isPlaying = False
                
        for note in wheelbuttons:
            note.fill = '#FFFFFF'       
        
    def changeOrder(self, circularList):
        pass
        
    def displayWheel(self):
        noFill()
        ellipse(400, 300, 500, 500)        
        
    def playSound(self, note, frequency, button):
        if (note.isPlaying):
            note.tone.stop()
            note.isPlaying = False
            button.fill = '#FFFFFF'            
        else:
            note.tone.freq(frequency)
            note.tone.play()
            note.isPlaying = True
            button.fill = "#4CB5FA"
                 
    def makeLines(self):
        playingButtons = []
        for i in range(len(notes)):
            if notes[i].isPlaying:
                playingButtons.append(circlebuttons[i])
        if len(playingButtons) > 1:            
            for i in range(len(playingButtons) - 1):
                line(playingButtons[i][0], playingButtons[i][1], playingButtons[i+1][0], playingButtons[i+1][1])
            line(playingButtons[0][0], playingButtons[0][1], playingButtons[-1][0], playingButtons[-1][1])
                
wheel = MusicWheel()