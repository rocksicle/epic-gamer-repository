#audio used for this can be found at https://www.youtube.com/watch?v=hg5behq8PlM

import time
import pygame
#counter is used in the "something in the way" lines, used for the weird timing after the first set of something in the ways
i = 0
file=open("./song.txt")
song=file.readlines()


#import the music and whatnot. file is in a folder within the code folder called assets and the file is called song
pygame.mixer.init()
pygame.mixer.music.load("./assets/song.mp3")
pygame.mixer.music.play()

print("\nSomething in the way\nBy Nirvana\n")

time.sleep(20)
for line in song:
    #loops through every line in the song and sees if it meets the conditions. if it does, it does the wait time specified. the if statement checks to see if i 
    #which is incremented by .17 for each something in the way. when it reaches one, it waits for an extra 2 seconds because the song has an extra few seconds after the chorus
    #the counter resets to -10 because the second set of something in the ways has 8 instead of 6 something in the ways.
    if(i>=1):
        time.sleep(2)
        i=-10
    print(line)
    if line[0] == 'S' and line[-10]!='h':
        time.sleep(9)
        i+=.17
    if line[0] == 'S' and line[-10]=='h':
        time.sleep(11.5)
        i+=.17
    if line[0]=='U':
        time.sleep(8)
    if line[-3]=='t':
        time.sleep(9.5)
    if line[-3]=='g' or line[-3]=='n':
        time.sleep(10)
#all this other stuff should be pretty self explanatory