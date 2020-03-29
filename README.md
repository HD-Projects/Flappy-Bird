# Flappy Bird
 All of the flappy bird exaples for our robotics programs 2d programming challenges

<html><body><pre>
<span style="color: #33997E;">import</span> <span style="color: #006699;">random</span>,time
<span style="color: #669900;">try</span>:
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #33997E;">from</span> data <span style="color: #33997E;">import</span> *
<span style="color: #669900;">except</span>:
&nbsp;&nbsp;&nbsp;&nbsp;file&nbsp;=&nbsp;<span style="color: #006699;">open</span>(<span style="color: #7D4793;">&quot;data.py&quot;</span>, <span style="color: #7D4793;">&quot;w&quot;</span>)
&nbsp;&nbsp;&nbsp;&nbsp;file.write(<span style="color: #7D4793;">&quot;highScore = 0&quot;</span>)
&nbsp;&nbsp;&nbsp;&nbsp;file.<span style="color: #006699;">close</span>()
&nbsp;&nbsp;&nbsp;
pos&nbsp;=&nbsp;0
pillarDistance&nbsp;=&nbsp;200
pillarDistanceTwo&nbsp;=&nbsp;350
pillarDistanceThree&nbsp;=&nbsp;500
pillarMid&nbsp;=&nbsp;<span style="color: #006699;">random</span>.randint(30, 130)
pillarMidTwo&nbsp;=&nbsp;<span style="color: #006699;">random</span>.randint(30, 130)
pillarMidThree&nbsp;=&nbsp;<span style="color: #006699;">random</span>.randint(30, 130)
birdH&nbsp;=&nbsp;100
startTime&nbsp;=&nbsp;time.time()-30
play&nbsp;=&nbsp;0
score&nbsp;=&nbsp;0
gameOver&nbsp;=&nbsp;0
gameScreen&nbsp;=&nbsp;2
frameNums&nbsp;=&nbsp;0
<span style="color: #006699;">print</span>(highScore)


<span style="color: #33997E;">def</span> <span style="color: #006699;"><b>setup</b></span>():
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">frameRate</span>(100)
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">background</span>(255)
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">size</span>(300, 400)
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">background</span>(0, 163, 255)
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #33997E;">global</span> pillarDistance,pillarDistanceTwo,pillarDistanceThree,pillarMidTwo,pillarMidThree, pillarMid,birdH,startTime,score,highScore,gameScreen
&nbsp;&nbsp;&nbsp;&nbsp;pillarDistance&nbsp;+=&nbsp;-1
&nbsp;&nbsp;&nbsp;&nbsp;pillarDistanceTwo&nbsp;+=&nbsp;-1
&nbsp;&nbsp;&nbsp;&nbsp;pillarDistanceThree&nbsp;+=&nbsp;-1
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">fill</span>(0, 189, 0)
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">rect</span>(pillarDistanceThree, pillarMidThree+50, 30, 300,3, 3, 3, 3)
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">fill</span>(0, 189, 0)
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">rect</span>(pillarDistanceThree, pillarMidThree-210, 30, 200,3, 3, 3, 3)
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">fill</span>(0, 189, 0)
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">rect</span>(pillarDistanceTwo, pillarMidTwo+50, 30, 300,3, 3, 3, 3)
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">fill</span>(0, 189, 0)
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">rect</span>(pillarDistanceTwo, pillarMidTwo-210, 30, 200,3, 3, 3, 3)
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">fill</span>(0, 189, 0)
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">rect</span>(pillarDistance, pillarMid+50, 30, 300,3, 3, 3, 3)
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">fill</span>(0, 189, 0)
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">rect</span>(pillarDistance, pillarMid-210, 30, 200,3, 3, 3, 3)
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">fill</span>(0, 189, 0)
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">fill</span>(0, 170, 0)
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">rect</span>(pillarDistanceThree-10, pillarMidThree+50, 50,20, 2)
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">rect</span>(pillarDistanceThree-10, pillarMidThree-20, 50,20, 2)
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">rect</span>(pillarDistanceTwo-10, pillarMidTwo+50, 50, 20,2)
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">rect</span>(pillarDistanceTwo-10, pillarMidTwo-20, 50, 20,2)
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">rect</span>(pillarDistance-10, pillarMid+50, 50, 20,2)
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">rect</span>(pillarDistance-10, pillarMid-20, 50, 20,2)
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">rect</span>(0,250,500,400)
&nbsp;&nbsp;&nbsp;&nbsp;img&nbsp;=&nbsp;<span style="color: #006699;">loadImage</span>(<span style="color: #7D4793;">&quot;bird.png&quot;</span>)
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">image</span>(img, 0, birdH, 50,45)
&nbsp;&nbsp;&nbsp;&nbsp;startTime&nbsp;=&nbsp;time.time()
&nbsp;&nbsp;&nbsp;&nbsp;time.sleep(2)
&nbsp;&nbsp;&nbsp;&nbsp;gameScreen&nbsp;=&nbsp;1
&nbsp;&nbsp;&nbsp;&nbsp;

<span style="color: #33997E;">def</span> <span style="color: #006699;"><b>draw</b></span>():
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #33997E;">global</span> pillarDistance,pillarDistanceTwo,pillarDistanceThree,pillarMidTwo,pillarMidThree, pillarMid,birdH,startTime,score,gameOver,gameScreen, frameNums,highScore
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #669900;">if</span> gameScreen == 0 <span style="color: #33997E;">and</span> gameOver  == 0:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">background</span>(0, 163, 255)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pillarDistance&nbsp;+=&nbsp;-1
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pillarDistanceTwo&nbsp;+=&nbsp;-1
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pillarDistanceThree&nbsp;+=&nbsp;-1
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">fill</span>(0, 189, 0)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">rect</span>(pillarDistanceThree, pillarMidThree+50, 30, 300,3, 3, 3, 3)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">fill</span>(0, 189, 0)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">rect</span>(pillarDistanceThree, pillarMidThree-210, 30, 200,3, 3, 3, 3)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">fill</span>(0, 189, 0)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">rect</span>(pillarDistanceTwo, pillarMidTwo+50, 30, 300,3, 3, 3, 3)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">fill</span>(0, 189, 0)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">rect</span>(pillarDistanceTwo, pillarMidTwo-210, 30, 200,3, 3, 3, 3)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">fill</span>(0, 189, 0)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">rect</span>(pillarDistance, pillarMid+50, 30, 300,3, 3, 3, 3)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">fill</span>(0, 189, 0)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">rect</span>(pillarDistance, pillarMid-210, 30, 200,3, 3, 3, 3)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">fill</span>(0, 189, 0)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">fill</span>(0, 170, 0)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">rect</span>(pillarDistanceThree-10, pillarMidThree+50, 50,20, 2)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">rect</span>(pillarDistanceThree-10, pillarMidThree-20, 50,20, 2)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">rect</span>(pillarDistanceTwo-10, pillarMidTwo+50, 50, 20,2)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">rect</span>(pillarDistanceTwo-10, pillarMidTwo-20, 50, 20,2)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">rect</span>(pillarDistance-10, pillarMid+50, 50, 20,2)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">rect</span>(pillarDistance-10, pillarMid-20, 50, 20,2)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">rect</span>(0,275,500,400)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">fill</span>(0)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">textSize</span>(15)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">text</span>(<span style="color: #006699;">str</span>(score), 10, 15)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">fill</span>(0)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">textSize</span>(15)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">text</span>(<span style="color: #006699;">str</span>(highScore), 270, 15)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;img&nbsp;=&nbsp;<span style="color: #006699;">loadImage</span>(<span style="color: #7D4793;">&quot;bird.png&quot;</span>)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">image</span>(img, 0, birdH, 50,45)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;birdH&nbsp;+=&nbsp;-((startTime-time.time()+0.4))*6
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #669900;">if</span> birdH &gt; 250:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gameOver&nbsp;=&nbsp;1
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #669900;">if</span> pillarDistance == -50:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pillarDistance&nbsp;=&nbsp;400
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">print</span>(pillarDistance)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pillarMid&nbsp;=&nbsp;<span style="color: #006699;">random</span>.randint(30, 160)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;score&nbsp;+=&nbsp;1
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">print</span>(score)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #669900;">if</span> pillarDistanceTwo == -50:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pillarDistanceTwo&nbsp;=&nbsp;400
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">print</span>(pillarDistanceTwo)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pillarMidTwo&nbsp;=&nbsp;<span style="color: #006699;">random</span>.randint(30, 160)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;score&nbsp;+=1
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">print</span>(score)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #669900;">if</span> pillarDistanceThree == -50:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pillarDistanceThree&nbsp;=&nbsp;400
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">print</span>(pillarDistanceThree)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pillarMidThree&nbsp;=&nbsp;<span style="color: #006699;">random</span>.randint(30, 160)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;score&nbsp;+=1
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">print</span>(score)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #669900;">if</span> pillarDistance &lt; 30 <span style="color: #33997E;">and</span> (pillarMid+24&lt;birdH <span style="color: #33997E;">or</span> pillarMid-10&gt;birdH) <span style="color: #33997E;">and</span> pillarDistance &gt; -15:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gameOver&nbsp;=&nbsp;1
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time.sleep(1)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #669900;">if</span> pillarDistanceTwo &lt; 30 <span style="color: #33997E;">and</span> (pillarMidTwo+24&lt;birdH <span style="color: #33997E;">or</span> pillarMidTwo-10&gt;birdH)<span style="color: #33997E;">and</span> pillarDistanceTwo &gt; -15:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gameOver&nbsp;=&nbsp;1
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time.sleep(1)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #669900;">if</span> pillarDistanceThree &lt; 30 <span style="color: #33997E;">and</span> (pillarMidThree+24&lt;birdH <span style="color: #33997E;">or</span> pillarMidThree-10&gt;birdH)<span style="color: #33997E;">and</span> pillarDistanceThree &gt; -15:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gameOver&nbsp;&nbsp;=&nbsp;1&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time.sleep(1)&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #669900;">elif</span> gameScreen == 2:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">background</span>(0, 163, 255)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">fill</span>(0)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">circle</span>(90, 200, 100)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">fill</span>(255)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">textSize</span>(15)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">text</span>(<span style="color: #7D4793;">&quot;  Press\nTo Start&quot;</span>, 60, 190)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;img&nbsp;=&nbsp;<span style="color: #006699;">loadImage</span>(<span style="color: #7D4793;">&quot;bird.png&quot;</span>)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">image</span>(img, 125, 10, 100,90)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">textSize</span>(15)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">text</span>(<span style="color: #7D4793;">&quot;    Game By:\nAlex Dickhans&quot;</span>, 100, 90)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">fill</span>(0)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">circle</span>(210, 200, 100)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">fill</span>(255)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">textSize</span>(15)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">text</span>(<span style="color: #7D4793;">&quot;  Press\nTo Close&quot;</span>, 180, 190)
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #669900;">elif</span> gameScreen == 1:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">background</span>(0, 163, 255)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">fill</span>(0)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">circle</span>(90, 200, 100)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">fill</span>(255)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">textSize</span>(15)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">text</span>(<span style="color: #7D4793;">&quot;  Press\nTo Start&quot;</span>, 60, 190)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;img&nbsp;=&nbsp;<span style="color: #006699;">loadImage</span>(<span style="color: #7D4793;">&quot;bird.png&quot;</span>)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">image</span>(img, 125, 50, 100,90)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">fill</span>(0)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">circle</span>(210, 200, 100)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">fill</span>(255)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">textSize</span>(13)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">text</span>(<span style="color: #7D4793;">&quot;    Press\nTo See Credits&quot;</span>, 170, 190)
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #669900;">elif</span> gameOver == 1:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">background</span>(0, 163, 255)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">textSize</span>(30)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">text</span>(<span style="color: #7D4793;">&quot;Gameover\n  Score:&quot;</span>+<span style="color: #006699;">str</span>(score), 70, 50)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #006699;">fill</span>(0)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pillarDistance&nbsp;=&nbsp;200
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pillarDistanceTwo&nbsp;=&nbsp;350
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pillarDistanceThree&nbsp;=&nbsp;500
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;birdH&nbsp;=&nbsp;100
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;frameNums&nbsp;+=&nbsp;1
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #669900;">if</span> score &gt; highScore:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;highScore&nbsp;=&nbsp;score&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gameFile&nbsp;=&nbsp;<span style="color: #006699;">open</span>(<span style="color: #7D4793;">&quot;data.py&quot;</span>, <span style="color: #7D4793;">&quot;w&quot;</span>)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;stringToSave&nbsp;=&nbsp;<span style="color: #7D4793;">&quot;highScore = &quot;</span>+<span style="color: #006699;">str</span>(score)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gameFile.write(stringToSave)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gameFile.<span style="color: #006699;">close</span>()
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #669900;">if</span> frameNums == 120:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;frameNums&nbsp;=&nbsp;0
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gameOver&nbsp;=&nbsp;0
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;score&nbsp;=&nbsp;0
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;startTime&nbsp;=&nbsp;time.time()&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

<span style="color: #33997E;">def</span> <span style="color: #D94A7A;">mousePressed</span>():
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #33997E;">global</span> birdH,startTime,play,gameScreen
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #669900;">if</span> gameScreen == 1:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #669900;">if</span> (<span style="color: #006699;">dist</span>(<span style="color: #D94A7A;">mouseX</span>,<span style="color: #D94A7A;">mouseY</span>,90, 200)&lt;50):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gameScreen&nbsp;=&nbsp;0
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;startTime&nbsp;=&nbsp;time.time()-0.1
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #669900;">elif</span>(<span style="color: #006699;">dist</span>(<span style="color: #D94A7A;">mouseX</span>,<span style="color: #D94A7A;">mouseY</span>,210, 200)&lt;50):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gameScreen&nbsp;=&nbsp;2
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time.sleep(0.1)
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #669900;">elif</span> gameScreen == 2:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #669900;">if</span> (<span style="color: #006699;">dist</span>(<span style="color: #D94A7A;">mouseX</span>,<span style="color: #D94A7A;">mouseY</span>,90, 200)&lt;50):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gameScreen&nbsp;=&nbsp;0
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;startTime&nbsp;=&nbsp;time.time()-0.1
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #669900;">elif</span>(<span style="color: #006699;">dist</span>(<span style="color: #D94A7A;">mouseX</span>,<span style="color: #D94A7A;">mouseY</span>,210, 200)&lt;50):
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gameScreen&nbsp;=&nbsp;1
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #669900;">elif</span> gameScreen == 0:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;startTime&nbsp;=&nbsp;time.time()-0.1

<span style="color: #33997E;">def</span> <span style="color: #D94A7A;">keyPressed</span>():
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #33997E;">global</span> birdH,startTime,play,gameScreen
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #669900;">if</span> <span style="color: #D94A7A;">key</span> == <span style="color: #718A62;">CODED</span>:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #669900;">if</span> <span style="color: #D94A7A;">keyCode</span> == <span style="color: #718A62;">UP</span>:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;startTime&nbsp;=&nbsp;time.time()-0.1
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #669900;">if</span> <span style="color: #D94A7A;">key</span> == <span style="color: #7D4793;">&quot; &quot;</span>:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;startTime&nbsp;=&nbsp;time.time()-0.1

</pre></body></html>
