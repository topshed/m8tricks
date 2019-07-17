# M8tricks

This Python GuiZero application is for creating 8x8 pixel images and animations for loading onto a Raspberry Pi [Sense HAT] (https://www.raspberrypi.org/blog/buy-the-sense-hat-as-seen-in-space/) (as used on the Astro Pi) LED Matrix.

![alt tag](https://raw.githubusercontent.com/topshed/m8tricks/master/readme_images/m8tricks1.png)

It offers a choice of several colours for the LEDs:

Red, Blue, Green, Yellow, White, Orange, Pink, Purple, Cyan


See my [blog] (http://richardhayler.blogspot.com/2015/06/creating-images-for-astro-pi-hat.html) for more details, screenshots, updates and other Raspberry Pi projects.

###Installation

This software is written for Python3.5 and later.

```Python

 sudo pip3 install m8tricks

 ```

### Getting started on Desktop Raspbian

1. Open a terminal window.
2. Run `m8tricxks`. This will check whether if you have a SenseHAT attached to your Raspberry Pi. If not, it will ask if you want to run the emulator instead.


###Basic features

On the left is a 8x8 grid representing the SenseHAT LED matrix.

On the right hand side are a set of square buttons to select the desired LED colour.

The currently selected colour is shown in the square below the matrix.

To set an LED's colour, click on its position in the editing window. If the LED is already set to a colour then clicking again will turn it to off, even if you have selected a new colour as the current one in use. Clicking a second time will set the LED to the new colour.

To add a new frame, click on the **New** button. This will create a new blank frame and increment the frame number displayed to the left of the button. If you want a copy of the preceding frame rather than a blank one, just click the **Duplicate**  button.

The arrow buttons at the top are used to navigate through the frames.


The '**Play on LEDs**' button will load the image you have created onto the LED matrix and – if there is more than one frame - run through the frames of the00 animation.

To increase or decrease the speed at which the animation is played on the LED matrix, use the **+** and **–** buttons. You should the Frames per Second (FPS) value change accordingly. Note that this will also alter the frame-rate set in the exported .py file (default is 1 fps).

The '**Rotate LEDs**' button will rotate the image displayed on the LEDs by 90 degrees clockwise for SenseHAT and UnicornHAT and 180 degrees for UnicornPHAT. It will not alter the orientation of the image within the editor.

![alt tag](https://raw.githubusercontent.com/topshed/RPi_8x8GridDraw/master/GUI-phat.png)

As mentioned earlier, the '**Clear**' button will set all the LEDs on the screen to off (this will not affect any image loaded on to the LED matrix).

The '**Delete**' button will remove the current frame and set the displayed frame to be the previous on in the series (e.g. if you're editing frame 6 and press the '**Delete**' button, you will set the current frame to number 5).

The '**Quit**' button will exit the program.

####Animation

**Export to py**: generates a .py file which when run, will display the animation on the LED matrix. The file contains a few lines of Python and the raw list containing each frame (itself a list) as elements. If you want to use the list in another Python program, simply copy-n-paste the FRAMES list from the file. The output file is always called animation8x8.py and will be overwritten without warning you if it already exists.

When you've saved an animation, I recommend you copy anaimation8x8.py to another filename to avoid accidental overwriting.  

If your animation is just a single frame, this method will work fine too and is the recommended way of saving your work.

###Import

The '**Import from file**' loads the contents of animation8x8.py into the editor.  

###Colour Definitions:

RED: [255,0,0]

BLUE: [0,0,255]

GREEN: [0,255,0]

PURPLE: [102,0,204]

PINK: [255,0,255]

ORANGE:[255,128,0]

YELLOW:[255,255,0]

WHITE:[255,255,255]

CYAN: [0,255,255]
