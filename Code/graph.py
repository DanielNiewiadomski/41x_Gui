import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
from colorama import Fore, Back, Style

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

temp = False;
sound = False;

#overlay a picture over the plot
im = plt.imread("floorplanfinal.png")
#implot = plt.imshow(im)

def animate(i):
    xar = []
    yar = []
    #populating thr arrays with get_data func
    get_data(xar,yar)
    #clearing previous line
    #ax1.clear()
    #drawing line again wiht new data
    # if (temp == True):
    #     ax1.scatter(xar,yar, color = 'red')
    #
    # ax1.scatter(xar, yar, color = 'blue')

    #making the overlay visible
    implot = plt.imshow(im)

def get_data(xar,yar):
    #figure out what pins the data is going to be coming form. Going to write to a file with [x,y] format, then update the xar array
    x = random.randrange(1200)
    y = random.randrange(500)
    xar.append(x)
    yar.append(y)
    ax1.scatter(xar, yar,s=30 , color='blue',alpha=0.5)

    #condition if temp is too high, then prints the location and warning
    if(x%2 == 0):
        temp = True;
        if(temp == True):
            ax1.scatter(xar, yar,s=40 , color='red')
            print('Too high of a Temperature at location [',x ,y ,"]")
            temp = False;

    # # condition if fall detected, then prints the location and warning
    # if (x % 2 == 0):
    #     temp = True;
    #     if (temp == True):
    #         print("FALL DETECTED [", x, y, "]" )
    #         temp = False;
    #
    #     # condition if high sound level detected, then prints the location and warning
    #     if (x % 2 == 0):
    #         temp = True;
    #         if (temp == True):
    #             print("FALL DETECTED [", x, y, "]")
    #             temp = False;
