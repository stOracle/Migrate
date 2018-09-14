PImage img;
PImage orig;

void setup() {
 size (888, 500);
 surface.setResizable(true);
 img = loadImage("pinata.jpg");
 orig = loadImage("pinata.jpg");
 surface.setSize(img.width, img.height);
}

///////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////

void draw() {
  image(img, 0, 0);
 
}
 
void keyPressed() { 
 
 if ((keyPressed == true) && (key == '0')) {
   img.copy(orig, 0, 0, orig.width, orig.height, 0, 0, img.width, img.height);
   
 }
 
///////////////////////////////////////////////////////////////////
// Pressing '1' will apply Greyscale
 if ((keyPressed == true) && (key == '1')) {
   colorMode(RGB);
   orig.loadPixels();
   for (int x = 0; x < orig.width; x++) {
     for (int y = 0; y < orig.height; y++) {
       int loc = x + y * width;
       float r = red(orig.pixels[loc]);
       float g = green(orig.pixels[loc]);
       float b = blue(orig.pixels[loc]);
       int grey = (int)(r + g + b) / 3;
       img.pixels[loc] = color(grey); 
     }
   }
   img.updatePixels();
   image (img, 0, 0);
 }
 
 ///////////////////////////////////////////////////////////////////
 // Pressing '2' will apply higher contrast
 if ((keyPressed == true) && (key == '2')) {
   
   //colorMode(HSB);
   float threshold = 125;
   int adjust = 30;
   orig.loadPixels();
   for (int x = 0; x < orig.width; x++) {
     for (int y = 0; y < orig.height; y++) {
       int loc = x + y * width;
       float r = red (orig.pixels[loc]);
       float g = green (orig.pixels[loc]);
       float b = blue (orig.pixels[loc]);
       float bright = brightness(orig.pixels[loc]);
       if (bright >= threshold) {
         //orig.pixels[loc] += brightness((int)b);
         r += adjust;
         g += adjust; 
         b += adjust;
         r = constrain(r, 0, 255);
         g = constrain(g, 0, 255);
         b = constrain(b, 0, 255);
         color c = color(r,g,b);
         img.pixels[loc] = c;
       }  else {
         r -= adjust;
         g -= adjust; 
         b -= adjust;
         r = constrain(r, 0, 255);
         g = constrain(g, 0, 255);
         b = constrain(b, 0, 255);
         color c = color(r,g,b);
         img.pixels[loc] = c;
         
       }
     }
   }
 img.updatePixels();
 image (img,0,0);
 }
 
 /////////////////////////////////////////////////////////////////////
 // Pressing '3' will apply a Gaussian Blur
 if ((keyPressed == true) && (key == '3')) {
   float [][] matrix = {{0,-1,0}, {-1, 5, -1}, {0,-1, 0}};
   float [][] matrix2 = {{1, 1}, {1, 1}};
   float red;
   float green;
   float blue;
   red = 0;
   green = 0;
   blue = 0;
   
   for (int x = 0; x < orig.width; x++) {
     for (int y = 0; y < orig.height; y++) {
       
       if (((x == 0) || (y == 0)) && (x != orig.width) && (y != orig.height)) {
         for (int i = 0; i < 2; i++) {
           for (int j = 0; j < 2; j++) {
             int index = (x + i) + orig.width * (y + j);
             red += red(orig.pixels[index]) * matrix[i][j];
             green += green(orig.pixels[index]) * matrix[i][j];
             blue += blue(orig.pixels[index]) * matrix[i][j];
           }
         }
                  
       }
       if ((x == 0) && (y == orig.height)) {
         for (int i = 0; i < 2; i++) {
           for (int j = 0; j < 2; j++) {
             int index = (x + i) + orig.width * (y + j);
             red += red(orig.pixels[index]) * matrix[i][j];
             green += green(orig.pixels[index]) * matrix[i][j];
             blue += blue(orig.pixels[index]) * matrix[i][j];          
           }
         }                  
       }
       if ((x == orig.width) && (y == 0)) {
         for (int i = 0; i < 2; i++) {
           for (int j = 0; j < 2; j++) {
             int index = (x + i) + orig.width * (y + j);
             red += red(orig.pixels[index]) * matrix[i][j];
             green += green(orig.pixels[index]) * matrix[i][j];
             blue += blue(orig.pixels[index]) * matrix[i][j];
           }
         }         
       }
       if ((x == orig.width) && (y == orig.height)) {
         for (int i = 0; i < 2; i++) {
           for (int j = 0; j < 2; j++) {
             int index = (x + i) + orig.width * (y + j);
             red += red(orig.pixels[index]) * matrix[i][j];
             green += green(orig.pixels[index]) * matrix[i][j];
             blue += blue(orig.pixels[index]) * matrix[i][j];
           }
         }  
       }
       for (int i = 0; i < 3; i++) {
         for (int j = 0; j < 3; j++) {
           int index = (x + i - 1) + img.width * (y + j -1);           
           red += red(img.pixels[index]) * matrix[i][j];
           green += green(img.pixels[index]) * matrix[i][j];
           blue += blue(img.pixels[index]) * matrix[i][j];
         }         
       }
       red = constrain(abs(red), 0, 255);
       green = constrain(abs(green), 0, 255);
       blue = constrain(abs(blue), 0, 255);
     }
   }
 
   
 img.updatePixels();
 image (img,0,0);
 }
 /////////////////////////////////////////////////////////////////////
 // Pressing '4' will apply Edge Detection
 if ((keyPressed == true) && (key == '4')) {
   noTint();
   image (img, 0, 0);
 }
}