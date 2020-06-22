let r1, r2, r3, b1, b2, b3, g1, g2, g3;

function setup() {
  createCanvas(900, 700);
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
  rect(0, 0, 300, 700);
  fill(r2, g2, b2);
  rect(300,0,300,700);
  fill(r3, g3, b3);
  rect(600,0,300,700);
}