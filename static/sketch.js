var r1; var g1; var b1;
var r2; var g2; var b2;
var r3; var g3; var b3;
var w1 = 200; var h1 = 400;
var w2 = 200; var h2 = 400;
var w3 = 200; var h3 = 400;
function setup() {
  createCanvas(600, 400);
  r1 = floor(random(0,255));
  r2 = floor(random(0,255));
  r3 = floor(random(0,255));
  g1 = floor(random(0,255));
  g2 = floor(random(0,255));
  g3 = floor(random(0,255));
  b1 = floor(random(0,255));
  b2 = floor(random(0,255));
  b3 = floor(random(0,255));

}

function draw() {
  background(255, 255, 255);
  noStroke();
  fill(r1, g1, b1);
  rect(0, 0, w1, h1);
  fill(r2, g2, b2);
  rect(200, 0, w2, h2);
  fill(r3, g3, b3);
  rect(400, 0, w3, h3);
  textSize(15);
  if(mouseX > 0 && mouseX < 200 && mouseY > 0 && mouseY < height){
    fill(0, 0, 0);
    text("RGB: "+(r1)+", "+(g1) +", "+(b1),mouseX, mouseY);
  }
  if(mouseX > 200 && mouseX < 400 && mouseY > 0 && mouseY < height){
    fill(0, 0, 0);
    text("RGB: "+(r2)+", "+(g2) +", "+(b2),mouseX, mouseY);
  }
  if(mouseX > 400 && mouseX < 600 && mouseY > 0 && mouseY < height){
    fill(0, 0, 0);
    text("RGB: "+(r3)+", "+(g3) +", "+(b3), mouseX, mouseY);
  }
}

function mouseClicked() {
  if (mouseX > 0 && mouseX < 200 && mouseY > 0 && mouseY < height) {
    r1 = floor(random(0, 255));
    g1 = floor(random(0, 255));
    b1 = floor(random(0, 255));
  }
  if(mouseX > 200 && mouseX < 400 && mouseY > 0 && mouseY < height){
    r2 = floor(random(0, 255));
    g2 = floor(random(0, 255));
    b2 = floor(random(0, 255));
  }
  if(mouseX > 400 && mouseX < 600 && mouseY > 0 && mouseY < height){
    r3 = floor(random(0, 255));
    g3 = floor(random(0, 255));
    b3 = floor(random(0, 255));
  }
}