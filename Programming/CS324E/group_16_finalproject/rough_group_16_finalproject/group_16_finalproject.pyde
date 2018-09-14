#from RSS import *
from writer import *

def setup():
    size(825, 600)
    frameRate(45)
    noLoop()
    #setupFeeds()
    #RSS_GUI()
    setupEditor()

def draw():
    background(255)
    displayGUI()

def mousePressed():
    handleGUImousePress()

def mouseReleased():
    handleGUImouseRelease()

def mouseMoved():
    handleGUImouseMove()