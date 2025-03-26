'''
interstate.py
Mr.Price

Given a highway number, determine if it is a major or auxillary highway, as well as it runs north/south or east/west
error check that the number is not 0, negative, divisible by 100 or over 100
'''

# takes a string as input and assigns it to interstate_number
interstate_number=int(input("Input Highway Number: "))

#error checking

while(interstate_number>1000 or interstate_number%100==0 or interstate_number<1):
    print("Invalid Highway Number.")
    interstate_number=int(input("Input Highway Number: "))


#for auxillary highways. Main highways should be perfectly divisible by 5

if(interstate_number%5>=1):
    if(interstate_number%2==0):
        print(f"Highway {interstate_number} is an auxillary highway that runs east/west.")
    else:
        print(f"Highway {interstate_number} is an auxillary highway that runs north/south.")


# for major highways. Major highways should be perfectly divisible by 5, and perfectly divisible by 10 if they run east/west

if(interstate_number%5==0):
    if(interstate_number%10==0):
        print(f"Highway {interstate_number} is a major highway that runs east/west.")
    else:
        print(f"Highway {interstate_number} is a major highway that runs north/south.")


