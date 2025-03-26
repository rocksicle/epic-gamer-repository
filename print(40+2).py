import tkinter as tk

def interstate():
    interstate_number=ent.get()
    if interstate_number.isdigit()==False:
        label2["text"]="Invalid Highway Number."
    else:

        interstate_number=int(ent.get())

        if(interstate_number>1000 or interstate_number%100==0 or interstate_number<1):
            label2["text"]="Invalid Highway Number."
        else:
    #for auxillary highways. Main highways should be perfectly divisible by 5

            if(interstate_number%5>=1):
                if(interstate_number%2==0):
                    label2["text"]=f"Highway {interstate_number} is an auxillary highway that runs east/west."
                else:
                    label2['text']=f"Highway {interstate_number} is an auxillary highway that runs north/south."


        # for major highways. Major highways should be perfectly divisible by 5, and perfectly divisible by 10 if they run east/west

            if(interstate_number%5==0):
                if(interstate_number%10==0):
                    label2['text']=f"Highway {interstate_number} is a major highway that runs east/west."
                else:
                    label2['text']=f"Highway {interstate_number} is a major highway that runs north/south."



root = tk.Tk(screenName="mmm")
root.geometry("600x400")
label=tk.Label(text="Enter a highway number to see if it main, auxillary and if it runs north/south or east/west", font=20)
label2=tk.Label(text='',font=30,)

label.grid()
label2.grid(row=30)
ent=tk.Entry(root)

btn=tk.Button(root,text="Enter",command=interstate)
btn.grid(row=10)

ent.grid(row=2)
root.mainloop()
