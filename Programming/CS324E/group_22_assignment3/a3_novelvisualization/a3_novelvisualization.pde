String uniqueWords[];

void setup(){
  size(700,600);
  uniqueWords = loadStrings("uniquewords.txt"); //create list of words from unique words text file
  background(#F2F2E1);
  wordDraw(); //draw first set of words to screen  
}

void draw(){  
  //called so that void mouseClicked() is constantly checked for
}

void mouseClicked(){
  if (mouseX != 0 && mouseY != 0 && (mouseButton == LEFT)){ //draws a new set of words if the canvas is clicked
     wordDraw(); 
  }
}

void wordDraw(){ //draws words to the screen  
    
  int Xcursor = 10; int Ycursor = 30; //initialize location to draw text from
  StringList wordsUsed; wordsUsed = new StringList();//initialize list to track words used; needed to determine placement on screen
  int wordIndex = 0; //used for indexing wordsUsed
  int i; String newWord;
  background(#F2F2E1); //cleans canvas of previous words
  
  //first iteration
  wordsUsed.append(uniqueWords[int(random(uniqueWords.length))]);   
  color[] textColors = {#39AEEA, #643619, #299319, #FC8B00};  
  PFont font = createFont("Trajan Pro 3", 30);
  textFont(font);
  fill(#39AEEA);
  
  while (Ycursor < 600){ //loop that draws words and moves "cursors". 
    if (Xcursor + textWidth(wordsUsed.get(wordIndex)) >= 700){ //moves cursor to next line if next word would print horizontally off screen
      Ycursor += 35;
      Xcursor = 10;
    }    
    if (Ycursor >= 600){ 
      break;                  //exits loop when screen is full
    }
    
    int colorPicker = int(random(4));//color selection goes here. randomly chosen
    fill(textColors[colorPicker]);
    
    text(wordsUsed.get(wordIndex),Xcursor,Ycursor); //actual text drawing line
    Xcursor += 25 + textWidth(wordsUsed.get(wordIndex)); //moves cursor with spacing between words
    wordIndex ++;
    
    newWord = uniqueWords[int(random(uniqueWords.length))];
    //condtional to make sure the same word isnt used twice
    for (i = 0; i < wordsUsed.size(); i++){
       if (newWord == wordsUsed.get(i)){
          newWord = uniqueWords[int(random(uniqueWords.length))];
          i = 0;
       }
       if (Xcursor + textWidth(newWord) > 700 && 700 - Xcursor > 80){
          newWord = uniqueWords[int(random(uniqueWords.length))];
          i = 0;
       }
    }
    
    wordsUsed.append(newWord); //adds a new unique word
  
  }  
}