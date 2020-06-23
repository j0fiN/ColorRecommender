var r1; var g1; var b1;
var r2; var g2; var b2;
var r3; var g3; var b3;
var w1 = 200; var h1 = 400;
var w2 = 200; var h2 = 400;
var w3 = 200; var h3 = 400;
var Width = 600; var Height = 400;
var ratings;
function setup() {
  let cnv = createCanvas(Width, 600);
  cnv.position(50, 100);
  r1 = floor(random(0,255));
  r2 = floor(random(0,255));
  r3 = floor(random(0,255));
  g1 = floor(random(0,255));
  g2 = floor(random(0,255));
  g3 = floor(random(0,255));
  b1 = floor(random(0,255));
  b2 = floor(random(0,255));
  b3 = floor(random(0,255));
  ratings = floor(random(1,4));

}

function draw() {
    background(255, 255, 255);
    noStroke();
    fill(r1, g1, b1);
    rect(0, 200, Width/3, Height);
    fill(r2, g2, b2);
    rect(Width/3, 200, Width/3, Height);
    fill(r3, g3, b3);
    rect(2*Width/3, 200, Width/3, Height);
    textSize(15);
    if (mouseX > 0 && mouseX < 200 && mouseY > 0 && mouseY < Height) {
      fill(0, 0, 0);
      text("RGB: " + (r1) + ", " + (g1) + ", " + (b1), mouseX, mouseY);
    }
    if (mouseX > 200 && mouseX < 400 && mouseY > 0 && mouseY < Height) {
      fill(0, 0, 0);
      text("RGB: " + (r2) + ", " + (g2) + ", " + (b2), mouseX, mouseY);
    }
    if (mouseX > 400 && mouseX < 600 && mouseY > 0 && mouseY < Height) {
      fill(0, 0, 0);
      text("RGB: " + (r3) + ", " + (g3) + ", " + (b3), mouseX, mouseY);
    }
    fill(0,0,0);
    textSize(30);
    text(ratings, 300, 0);

}

function mouseClicked() {
  let values;
    if (mouseX > 0 && mouseX < 200 && mouseY > 0 && mouseY < Height) {
      values = {r: r1, g: g1, b: b1, rate:ratings};
      r1 = floor(random(0, 255));
      g1 = floor(random(0, 255));
      b1 = floor(random(0, 255));
      ratings = floor(random(1, 4));
    }
    if (mouseX > 200 && mouseX < 400 && mouseY > 0 && mouseY < Height) {
      values = {r: r2, g: g2, b: b2, rate:ratings};
      r2 = floor(random(0, 255));
      g2 = floor(random(0, 255));
      b2 = floor(random(0, 255));
      ratings = floor(random(1, 4));
    }
    if (mouseX > 400 && mouseX < 600 && mouseY > 0 && mouseY < Height) {
      values = {r: r3, g: g3, b: b3, rate:ratings};
      r3 = floor(random(0, 255));
      g3 = floor(random(0, 255));
      b3 = floor(random(0, 255));
      ratings = floor(random(1, 4));
    }
    fetch('http://127.0.0.1:5000/api', {
      method: 'POST',
      body: JSON.stringify(values),
    })
        .then(response => response.text())
        .then(data => {
          console.log('Success:', data);
        })
        .catch((error) => {
          console.error('Error:', error);
        });

}
