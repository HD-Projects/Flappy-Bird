import random,time
try:
    from data import *
except:
    file = open("data.py", "w")
    file.write("highScore = 0")
    file.close()
   
pos = 0
pillarDistance = 200
pillarDistanceTwo = 350
pillarDistanceThree = 500
pillarMid = random.randint(30, 130)
pillarMidTwo = random.randint(30, 130)
pillarMidThree = random.randint(30, 130)
birdH = 100
startTime = time.time()-30
play = 0
score = 0
gameOver = 0
gameScreen = 2
frameNums = 0
print(highScore)


def setup():
    frameRate(100)
    background(255)
    size(300, 400)
    background(0, 163, 255)
    global pillarDistance,pillarDistanceTwo,pillarDistanceThree,pillarMidTwo,pillarMidThree, pillarMid,birdH,startTime,score,highScore,gameScreen
    pillarDistance += -1
    pillarDistanceTwo += -1
    pillarDistanceThree += -1
    fill(0, 189, 0)
    rect(pillarDistanceThree, pillarMidThree+50, 30, 300,3, 3, 3, 3)
    fill(0, 189, 0)
    rect(pillarDistanceThree, pillarMidThree-210, 30, 200,3, 3, 3, 3)
    fill(0, 189, 0)
    rect(pillarDistanceTwo, pillarMidTwo+50, 30, 300,3, 3, 3, 3)
    fill(0, 189, 0)
    rect(pillarDistanceTwo, pillarMidTwo-210, 30, 200,3, 3, 3, 3)
    fill(0, 189, 0)
    rect(pillarDistance, pillarMid+50, 30, 300,3, 3, 3, 3)
    fill(0, 189, 0)
    rect(pillarDistance, pillarMid-210, 30, 200,3, 3, 3, 3)
    fill(0, 189, 0)
    fill(0, 170, 0)
    rect(pillarDistanceThree-10, pillarMidThree+50, 50,20, 2)
    rect(pillarDistanceThree-10, pillarMidThree-20, 50,20, 2)
    rect(pillarDistanceTwo-10, pillarMidTwo+50, 50, 20,2)
    rect(pillarDistanceTwo-10, pillarMidTwo-20, 50, 20,2)
    rect(pillarDistance-10, pillarMid+50, 50, 20,2)
    rect(pillarDistance-10, pillarMid-20, 50, 20,2)
    rect(0,250,500,400)
    img = loadImage("bird.png")
    image(img, 0, birdH, 50,45)
    startTime = time.time()
    time.sleep(2)
    gameScreen = 1
    

def draw():
    global pillarDistance,pillarDistanceTwo,pillarDistanceThree,pillarMidTwo,pillarMidThree, pillarMid,birdH,startTime,score,gameOver,gameScreen, frameNums,highScore
    if gameScreen == 0 and gameOver  == 0:
        background(0, 163, 255)
        pillarDistance += -1
        pillarDistanceTwo += -1
        pillarDistanceThree += -1
        fill(0, 189, 0)
        rect(pillarDistanceThree, pillarMidThree+50, 30, 300,3, 3, 3, 3)
        fill(0, 189, 0)
        rect(pillarDistanceThree, pillarMidThree-210, 30, 200,3, 3, 3, 3)
        fill(0, 189, 0)
        rect(pillarDistanceTwo, pillarMidTwo+50, 30, 300,3, 3, 3, 3)
        fill(0, 189, 0)
        rect(pillarDistanceTwo, pillarMidTwo-210, 30, 200,3, 3, 3, 3)
        fill(0, 189, 0)
        rect(pillarDistance, pillarMid+50, 30, 300,3, 3, 3, 3)
        fill(0, 189, 0)
        rect(pillarDistance, pillarMid-210, 30, 200,3, 3, 3, 3)
        fill(0, 189, 0)
        fill(0, 170, 0)
        rect(pillarDistanceThree-10, pillarMidThree+50, 50,20, 2)
        rect(pillarDistanceThree-10, pillarMidThree-20, 50,20, 2)
        rect(pillarDistanceTwo-10, pillarMidTwo+50, 50, 20,2)
        rect(pillarDistanceTwo-10, pillarMidTwo-20, 50, 20,2)
        rect(pillarDistance-10, pillarMid+50, 50, 20,2)
        rect(pillarDistance-10, pillarMid-20, 50, 20,2)
        rect(0,275,500,400)
        fill(0)
        textSize(15)
        text(str(score), 10, 15)
        fill(0)
        textSize(15)
        text(str(highScore), 270, 15)
        img = loadImage("bird.png")
        image(img, 0, birdH, 50,45)
        birdH += -((startTime-time.time()+0.4))*6
        if birdH > 250:
            gameOver = 1
        if pillarDistance == -50:
            pillarDistance = 400
            print(pillarDistance)
            pillarMid = random.randint(30, 160)
            score += 1
            print(score)
        if pillarDistanceTwo == -50:
            pillarDistanceTwo = 400
            print(pillarDistanceTwo)
            pillarMidTwo = random.randint(30, 160)
            score +=1
            print(score)
        if pillarDistanceThree == -50:
            pillarDistanceThree = 400
            print(pillarDistanceThree)
            pillarMidThree = random.randint(30, 160)
            score +=1
            print(score)
        if pillarDistance < 30 and (pillarMid+24<birdH or pillarMid-10>birdH) and pillarDistance > -15:
            gameOver = 1
            time.sleep(1)
        if pillarDistanceTwo < 30 and (pillarMidTwo+24<birdH or pillarMidTwo-10>birdH)and pillarDistanceTwo > -15:
            gameOver = 1
            time.sleep(1)
        if pillarDistanceThree < 30 and (pillarMidThree+24<birdH or pillarMidThree-10>birdH)and pillarDistanceThree > -15:
            gameOver  = 1   
            time.sleep(1) 
    elif gameScreen == 2:
        background(0, 163, 255)
        fill(0)
        circle(90, 200, 100)
        fill(255)
        textSize(15)
        text("  Press\nTo Start", 60, 190)
        img = loadImage("bird.png")
        image(img, 125, 10, 100,90)
        textSize(15)
        text("    Game By:\nAlex Dickhans", 100, 90)
        fill(0)
        circle(210, 200, 100)
        fill(255)
        textSize(15)
        text("  Press\nTo Close", 180, 190)
    elif gameScreen == 1:
        background(0, 163, 255)
        fill(0)
        circle(90, 200, 100)
        fill(255)
        textSize(15)
        text("  Press\nTo Start", 60, 190)
        img = loadImage("bird.png")
        image(img, 125, 50, 100,90)
        fill(0)
        circle(210, 200, 100)
        fill(255)
        textSize(13)
        text("    Press\nTo See Credits", 170, 190)
    elif gameOver == 1:
        background(0, 163, 255)
        textSize(30)
        text("Gameover\n  Score:"+str(score), 70, 50)
        fill(0)
        pillarDistance = 200
        pillarDistanceTwo = 350
        pillarDistanceThree = 500
        birdH = 100
        frameNums += 1
        if score > highScore:
            highScore = score    
            gameFile = open("data.py", "w")
            stringToSave = "highScore = "+str(score)
            gameFile.write(stringToSave)
            gameFile.close()
        if frameNums == 120:
            frameNums = 0
            gameOver = 0
            score = 0
        startTime = time.time()  
    
        
        
        

def mousePressed():
    global birdH,startTime,play,gameScreen
    if gameScreen == 1:
        if (dist(mouseX,mouseY,90, 200)<50):
            gameScreen = 0
            startTime = time.time()-0.1
        elif(dist(mouseX,mouseY,210, 200)<50):
            gameScreen = 2
            time.sleep(0.1)
    elif gameScreen == 2:
        if (dist(mouseX,mouseY,90, 200)<50):
            gameScreen = 0
            startTime = time.time()-0.1
        elif(dist(mouseX,mouseY,210, 200)<50):
            gameScreen = 1
    elif gameScreen == 0:
        startTime = time.time()-0.1

def keyPressed():
    global birdH,startTime,play,gameScreen
    if key == CODED:
        if keyCode == UP:
            startTime = time.time()-0.1
    if key == " ":
        startTime = time.time()-0.1
