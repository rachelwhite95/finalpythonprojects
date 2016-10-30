from graphics import *
import time

marks = open("marks.txt") 
marksContent = marks.read()
marksList = marksContent.split('\n')
marks.close() #opens marks lists, splits and reads it line by line

thirdMarks = []
twoTwoMarks = []
twoOneMarks = []
firstMarks = [] #lists to have the different classifications of marks in

rectangleXposition = 0
rectangleYposition = 0
rectangleXposition2 = 40
rectangleYposition2 = 40 #sets the initial position of the first square

for theMark in marksList:
    if (theMark >= "40") and (theMark < "50"):
        thirdMarks.append(theMark)
    elif (theMark >= "50") and (theMark < "60"):
        twoTwoMarks.append(theMark)
    elif (theMark >= "60") and (theMark < "70"):
        twoOneMarks.append(theMark)
    elif (theMark >= "70"):
        firstMarks.append(theMark) #places the marks from the text file into the correct lists 

window = GraphWin("My Visualisation", 1800, 600)
window.setBackground('black') #opens new window with a black background

Title = Text(Point(window.getWidth()/2, 25),"Visualisation of marks for DAT505") #places a title in the middle of the screen
Title.setTextColor("white")
Title.setStyle('bold')
Title.setSize(20)
Title.draw(window)

#this for loop goes through the list of marks and draws a different coloured square depending on which list it has been sorted into to

for theMark in marksList:
    rectangleXposition = rectangleXposition + 60 #puts a space inbetween the next square
    rectangleXposition2 = rectangleXposition2 + 60
    if (theMark in thirdMarks):
        box = Rectangle(Point(rectangleXposition, 400),Point(rectangleXposition2, 440))
        box.setOutline(color_rgb(255,153,153)) #pastel red
        box.setFill(color_rgb(255,153,153))
        box.draw(window)   
        time.sleep(0.5)
    elif (theMark in twoTwoMarks):
        box = Rectangle(Point(rectangleXposition, 300),Point(rectangleXposition2, 340))
        box.setOutline(color_rgb(255,204,153)) #pastel orange
        box.setFill(color_rgb(255,204,153))
        box.draw(window)  
        time.sleep(0.5)
    elif (theMark in twoOneMarks):
        box = Rectangle(Point(rectangleXposition, 200),Point(rectangleXposition2, 240))
        box.setOutline(color_rgb(255,255,204)) #pastel yellow
        box.setFill(color_rgb(255,255,204))
        box.draw(window)  
        time.sleep(0.5)
    elif (theMark in firstMarks):
        box = Rectangle(Point(rectangleXposition, 100),Point(rectangleXposition2, 140))
        box.setOutline(color_rgb(204,255,204)) #pastel green
        box.setFill(color_rgb(204,255,204))
        box.draw(window)  
        time.sleep(0.5)
        
window.getMouse() 

