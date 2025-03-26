#cookie clicker
import tkinter as tk
import time
import threading

root = tk.Tk(screenName="mmm")
label=tk.Label(text="0", font=("Arial",64))
root.geometry("440x900")

# all the prices, counters and multipliers are stored as global variables

inc=0
grandmaCost=100
autoClickManCost=1000
clickPower=1
ClPS=0
ClPS2=0
multiplierCost=100000
mult=1
upgrade4Cost=500000
upgrade5Cost=1000000
upgrade6Cost=1500000


#this handles the score going up whenever you click
def fun():
    global inc
    global clickPower
    inc = inc + clickPower
    label['text']=inc


#handles checking to see if you can afford grandma, changing the price of grandma after purchasing, and increasing clickpower when purchased
def BuyGrandma():
    global grandmaCost
    global inc
    global clickPower
    global mult
    if grandmaCost<=inc:
        inc=inc-grandmaCost
        grandmaCost=grandmaCost+900
        clickPower=clickPower+(10*mult)
        grandmaButton['text']=f"Buy a grandma for {grandmaCost} cookies"
        cookie_per_click['text']=f"Cookies per click: {clickPower}"


#this is handles incrementing the scorea AFTER buying an autoclick. increases score by 1 ever .05 seconds per autoclicker
def Autoclick():
    global inc
    global ClPS
    global mult
    while True:
        if ClPS>0:
            time.sleep(0.05)
            inc=int(inc+(ClPS*mult))
            label["text"]=inc
    



#handles checking to see if you can afford autoclicker, changing price after buying one, and increasing the amount you get per second

def buyAutoClick():
    global inc
    global autoClickManCost
    global ClPS
    if autoClickManCost<=inc:
        inc=inc-autoClickManCost
        autoClickManCost=autoClickManCost+1000
        buyClickMan['text']=f"Buy autoclicker for {autoClickManCost} cookies"
        ClPS+=1


#checks to see if you can afford multiplier, changes multiplier cost after buying one, and changes click power
def multiPlier():
    global inc 
    global multiplierCost
    global clickPower
    global mult
    if multiplierCost<=inc:
        inc=inc-multiplierCost
        multiplierCost=multiplierCost*5
        multiplierCost=int(multiplierCost)
        buyMultiplier['text']=f"Buy a multiplier for {multiplierCost} cookies"
        clickPower=clickPower*3
        clickPower=int(clickPower)
        cookie_per_click['text']=f"Cookies per click: {clickPower}"
        mult+=3

# all of the upgrade functions are basically the same. It checks to see if you can afford the upgrade, and if so, subtracts the cost from your total, changes the price,
#then increments your clicks per second or clicking power by an amount
def upgrade4():
    global inc
    global upgrade4Cost
    global ClPS
    if inc>=upgrade4Cost:
        ClPS+=100
        inc=inc-upgrade4Cost
        upgrade4Cost=int(upgrade4Cost*1.5)
        buyUpgrade4['text']=f"Buy an autoclicker TURBO for {upgrade4Cost} cookies"


def upgrade5():
    global inc 
    global ClPS
    global upgrade5Cost
    if inc>=upgrade5Cost:
        ClPS+=500
        inc=inc-upgrade5Cost
        upgrade5Cost=int(upgrade5Cost*1.5)
        buyUpgrade5['text']=f"Buy an autoclicker ULTRA for {upgrade5Cost} cookies"

def upgrade6():
    global inc
    global ClPS
    global upgrade6Cost
    if inc>=upgrade6Cost:
        ClPS+=5000
        inc=inc-upgrade6Cost
        upgrade6Cost=int(upgrade6Cost*1.5)
        buyUpgrade6['text']=f"Buy an autoclicker MAX for {upgrade6Cost} cookies"


# this is for testing so you can test all functionalities quickly
def cheat():
    global inc
    inc=10000000
    label['text']=inc


    


#thread to allow the score to go up without you clicking. for some reason a bunch of errors show up after you close the window, but they dont seem to actually effect anything.
#the thread is always running, but the ClPS variable starts at 0, so you gain 0 cookies

autoclick = threading.Thread(target=Autoclick)
autoclick.start()

# autoclick2=threading.Thread(target=upgrade4Auto)
# autoclick2.start()



cookie_per_click=tk.Label(text=f"Cookies per click: {clickPower}")


grandma=tk.PhotoImage(file="./assets/upgrade1.png").subsample(8)
img=tk.PhotoImage(file="./assets/cookie.png").subsample(4)
clickMan=tk.PhotoImage(file="./assets/upgrade2.png").subsample(8)
multiplier=tk.PhotoImage(file="./assets/upgrade3.png").subsample(8)
upgradefour=tk.PhotoImage(file="./assets/upgrade4.png").subsample(8)
upgradefive=tk.PhotoImage(file="./assets/upgrade5.png").subsample(8)
upgradesix=tk.PhotoImage(file="./assets/upgrade6.png").subsample(8)


buyClickMan=tk.Button(root, image=clickMan, text=f"Buy autoclicker for {autoClickManCost} cookies ", compound="left", command=buyAutoClick)
buyMultiplier=tk.Button(root,image=multiplier,text=f"Buy a multiplier for {multiplierCost} cookies", compound="left", command=multiPlier)
buyUpgrade4=tk.Button(root, image=upgradefour,text=f"Buy an autoclicker TURBO for {upgrade4Cost} cookies", compound="left", command=upgrade4)
buyUpgrade5=tk.Button(root, image=upgradefive,text=f"Buy an autoclicker ULTRA for {upgrade5Cost} cookies", compound="left", command=upgrade5)
buyUpgrade6=tk.Button(root, image=upgradesix, text=f"Buy an autoclicker MAX for {upgrade6Cost} cookies", compound="left", command=upgrade6)
cheatb=tk.Button(root, text="PRESS THIS BUTTON FOR TESTING PURPOSES. GIVES YOU A LOT OF COOKIES.", command=cheat)
label.grid()
cookie_per_click.grid()



btn=tk.Button(root,image=img, command=fun, text="click the cookie", compound="bottom")
grandmaButton=tk.Button(root,image=grandma, text=f"Buy a grandma for {grandmaCost} cookies", compound="left", command=BuyGrandma)

btn.grid(row=10)
grandmaButton.grid()
buyClickMan.grid()
buyMultiplier.grid()
buyUpgrade4.grid()
buyUpgrade5.grid()
buyUpgrade6.grid()
cheatb.grid()


root.mainloop()