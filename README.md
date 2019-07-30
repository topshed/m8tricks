# M8tricks

Current release: 0.7 Beta

Please raise an issue on guthub if you encounter any problems.

This Python [GuiZero](https://lawsie.github.io/guizero/) application is for creating 8x8 pixel images and animations for a Raspberry Pi [Sense HAT](https://www.raspberrypi.org/blog/buy-the-sense-hat-as-seen-in-space/) LED Matrix.

![alt tag](https://raw.githubusercontent.com/topshed/m8tricks/master/readme_images/m8tricks1.png)


### Installation

This software is written for Python3.5 and later.

1. Open a terminal window.
2. Type:

```Python

 sudo pip3 install m8tricks

 ```

### Getting started on Desktop Raspbian

1. Open a terminal window.
2. Run `m8tricxks`. This will check whether if you have a SenseHAT attached to your Raspberry Pi. If not, it will ask if you want to run the emulator instead.

### Getting started on other platforms.

M8tricks is intended for use on Raspbian, but should work on other platforms. Obviously you can only attach a SenseHAT to a Raspberry Pi but you'll still be able to create and save Python files that can be transferred onto Raspberry Pi and run there later.


### Basic features

On the left is a 8x8 grid representing the SenseHAT LED matrix.

On the right hand side are a set of square buttons to select the desired LED colour. Black means the LED will not be illuminated at all (i.e. it's off).

The currently selected colour is shown in the square below the matrix and labelled as "Selected Colour".

To set an LED's colour, click on its position in the big 8x8 grid. If the LED is already set to a colour then clicking again will turn it to off, even if you have selected a new colour as the current one in use. Clicking a second time will set the LED to the new colour.

The '**LED Rotation**' drop-down allows you to rotate the image displayed on the SenseHAT LEDs by 90 degrees clockwise for SenseHAT. It will not alter the orientation of the image within the m8tricks editor.

The '**Clear**' button will set all the LEDs on the screen to the selected colour.

![alt tag](https://raw.githubusercontent.com/topshed/m8tricks/master/readme_images/m8tricks3.png)

To turn all the LEDs off, select the Black colour first.

### Animations

You can create animations by sequentially loading frames.

To add a new frame, click on the **New** button. This will create a new blank frame and increment the frame number displayed to the left of the button. If you want a copy of the preceding frame rather than a blank one, just click the **Duplicate**  button.

The **Delete** button will remove the current frame and set the displayed frame to be the previous one in the series (e.g. if you're editing frame 6 and press the '**Delete**' button, you will set the current frame to number 5).

The top of the editor has a familiar set of 6 buttons for stepping through the frames and playing the animation. the outer two blue buttons will take you to the first or last frames in the sequence.  The two regular arrows will step forward or backward one frame.

At the bottom of the editor window you can see the previous frame on the left and the next frame on the right.

![alt tag](https://raw.githubusercontent.com/topshed/m8tricks/master/readme_images/m8tricks2.png)

The green Play button will step through the animation starting from the currently shown frame. So if you want to run your entire sequence from the start, first click on the leftmost blue arrow and then press play. The red pause button will stop the animation at the current frame.

To increase or decrease the speed at which the animation is played, use the framerate slider. The maximum is 25 fps. If you want the animation to loop repeatedly, check the **Repeat** checkbox.

### Saving your masterpiece

The File menu allows you to export your frame or animation in a python file.

![alt tag](https://raw.githubusercontent.com/topshed/m8tricks/master/readme_images/m8tricks4.png)

This can be run outside of the m8tricks editor through a Python editor like Mu or Thonny. or from the command line:

```python
python3 myanimation.py
```

You can also load back in previously saved animations to edit or extend them. Use the Import option.


### Colour Definitions:

RED: [255,0,0]

BLUE: [0,0,255]

GREEN: [0,255,0]

PURPLE: [102,0,204]

PINK: [255,0,255]

ORANGE:[255,128,0]

YELLOW:[255,255,0]

WHITE:[255,255,255]

CYAN: [0,255,255]
