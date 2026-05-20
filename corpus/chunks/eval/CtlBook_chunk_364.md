# 11.2 Overview

Tustin's method (aka the Bilinear Transform) lets us convert a controller designed in the continuous time LaPlace domain to an equivalent (over a certain bandwidth) discrete time controller. In order to implement a controller in a digital platform such as a microcontroller or FPGA, we must have it expressed in discrete time.

In this chapter, we will describe a procedure to convert a continuous time transfer function (such as a controller you might design on the computer) into a line of code you could build into a software application.

In the following, it will help if you have been exposed to some discrete time signals and systems theory (the Z-Transform), but full knowledge of Z-transforms is not required to calculate this conversion. Our procedure will boil down to the following process for converting your continous time controller into computer code.

1. Model your system   
2. Design your controller as in previous chapters.   
3. Convert controller from continuous time to discrete time   
4. Convert your discrete time controller to a digital lter which can be easily coded.   
5. Code and test your lter in the computer.

![](image/7d70e108b1ba2f4cbf214ec45491ad7004263674a3ecaa999e990131e7745cfa.jpg)  
Figure 11.1: Continuous time (top) and discrete time (bottom) signals. The time between samples is T .
