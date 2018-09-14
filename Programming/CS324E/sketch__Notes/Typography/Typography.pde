//Typography

//Initializing Fonts
//Display all
//string[] fontlist = PFont.list();
//printArray(fontlist);

//converts PFont o desired font
//createfont()

//sets PFont as the text font type
//textFont()

//example

PFont courier;
void setup() {
  size(500, 500);
  courier = createFont("Courier", 32);
  textFont(courier);
}

void draw() {
  text("hello", 100, 100);
  
}

void draw() {
  //refresher
  background = (250);
}

void keyPressed() {
  if (key == BACKSPACE) {
    if (letters.length() > 0) {
      letters = letters.substring(0, letters.length() - 1);
    }
  } else if (textWidth(letters + key) < width) {
    letters = letters + key;
  }
}
  