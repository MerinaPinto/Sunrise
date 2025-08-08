from p5 import *

def setup():
  global y, g
  createCanvas(windowWidth,windowHeight)

  y= 250

  g = 0
  
def draw():
  global y,g
  background(0,g,225)
  drawTickAxes()

  #map / linmap
  
  
  fill("yellow")
  circle(300,constrain(y,250,500),200 )

  y = y+1

  g = g+1
  
  #if y<500:
  #  y = y+1
  #else:
  #  y=500

  
  fill(150, 75, 0)
  rect(0,0,windowWidth,150)

  fill("grey")
  triangle(250,150,450,300,600,150)
  #triangle(x1,y1,x2,y2,x3,y3)

  fill("grey")
  triangle(400,150,150,300,0,150)

 
