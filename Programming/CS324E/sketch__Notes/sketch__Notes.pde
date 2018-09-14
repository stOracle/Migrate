//extract hue, sat, and brightness from a pixel:
hue(color c)
saturation(color c)
brightness(color c)

//example: sharper

float[][] matrix = {{0,-1,0},{-1,5,-1},{0,-1,0}};
float red, green, blue;
// code to access individual pixel location (x, y)
for (int i = 0; i < 3; i++) {
  for (int j = 0; j < 3; j++) {
    int index = (x + i - 1) + img.width*(y + j -1);
    red += red(img.pixels[index]) * matrix[i][j];
  }
}
red = constrain(abs(red), 0, 255);