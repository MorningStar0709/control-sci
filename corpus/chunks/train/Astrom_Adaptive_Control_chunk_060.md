# Industrial Products

The industrial products can, broadly speaking, be divided into three different categories: standard controllers, distributed control systems, and dedicated special-purpose systems.

Standard controllers form the largest category. They are typically based on some version of the PID algorithm. Currently, there is very vigorous development of these systems, which are manufactured in large quantities. Practically all new single-loop controllers introduced use some form of adaptation. Many different schemes are used. The single-loop controller is in fact becoming a proving ground for adaptive control. One example is shown in Fig. 1.23. This system has automatic tuning of the PID controller. The controller also has feedforward and gain scheduling. The automatic tuning is implemented in such a way that the user only has to push a button to execute the tuning.

![](image/9e8934184f605cb1edadea45b3a6c8fcbc8bf6e7667fad1df7907cf2f78e9d61.jpg)

<details>
<summary>text_image</summary>

52.8
100
90
80
70
60
50
40
30
20
10
0
PV % SP
R L
STORE
C L
M
TUNE
SET
PROG
0
SaltControl
</details>

Figure 1.23 A commercial PID controller with automatic tuning, gain scheduling, and feedforward (SattControl Instruments ECA50). Tuning is performed on operator demand when the tune button is pushed. (By courtesy of SattControl Instrument.)

A standard controller may be regarded as automation of the actions of a process operator. The controller shown in Fig. 1.23 may be viewed as the next level of automation, in which the actions of an instrument engineer are automated.

Distributed control systems are general-purpose systems primarily for process control applications. These systems may be viewed as a toolbox for implementing a wide variety of control systems. Typically, in addition to tools for PID control, alarm, and startup, more advanced control schemes are also incorporated. Adaptive techniques are now being introduced in the distributed systems, although the rate of development is not as rapid as for single-loop controllers.

There are many special-purpose systems for adaptive control. The applications range from space vehicles to automobiles and consumer electronics. The spacecraft Gemini, for example, has an adaptive notch filter and adaptive friction compensation. The following is another example of an adaptive controller.
