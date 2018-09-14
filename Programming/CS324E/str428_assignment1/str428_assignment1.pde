void setup() {
  size(1000, 700);
  background(181, 242, 241);
}

void draw() {
  fill(86, 180, 113);
  strokeWeight(2);
  stroke(61, 137, 47);
  rect(0, 500, 1000, 250);
  noStroke();
  fill(255, 255);
  ellipse(200, 100, 175, 85);
  ellipse(285, 100, 175, 85);
  ellipse(300, 225, 175, 85);
  ellipse(385, 225, 175, 85);
  stroke(255, 153, 57);
  strokeWeight(3);
  fill(255, 246, 57);
  ellipse(850, 120, 200, 200);
  strokeWeight(5);
  stroke(0);
  fill(93);
  quad(650, 500, 775, 500, 600, 700, 475, 700);
  strokeWeight(2);
  stroke(255);
}