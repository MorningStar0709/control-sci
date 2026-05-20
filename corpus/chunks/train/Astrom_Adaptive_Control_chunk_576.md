# Ship Steering

Autopilots for ships are normally based on feedback from a heading measurement, using a gyrocompass, to a steering engine, which drives the rudder. It is common practice to use a control law of the PID type with fixed parameters. Although such a controller can be made to work reasonably well, its performance is poor in heavy weather and when the speed of the ship is changed. The reason is that the ship dynamics change with the speed of the ship and that the disturbances change with the weather. There is a growing awareness that autopilots can be improved considerably by taking these changes into account. This is illustrated by analysis of some simple models.

The ship dynamics are obtained by applying Newton's equations to the motion of the ship. For large ships the motion in the vertical plane can be separated from the other motions. It is customary to describe the horizontal motion by using a coordinate system fixed to the ship (see Fig. 9.8). Let V be the total velocity, let u and v be the x and y components of the velocity, and let r be the angular velocity of the ship.

![](image/67eb2b1bcaec7acd90440dc434adfd90c0eb7345538dd74f276b59b167f3a968.jpg)

<details>
<summary>text_image</summary>

ψ
δ
v
y
u
x
V
</details>

Figure 9.8 Coordinates and notations used to describe the equations of motion of ships.

In normal steering, the ship makes small deviations from a straight-line course. It is thus natural to linearize the equations of motion around the solution $u = u_{0}$ , v = 0, r = 0, and $\delta = 0$ . The natural state variables are the sway velocity v, the turning rate r, and the heading $\psi$ . The following equations are obtained:

$$\frac {d v}{d t} = (u / l) a _ {1 1} v + u a _ {1 2} r + \left(u ^ {2} / l\right) b _ {1} \delta\frac {d r}{d t} = (u / l ^ {2}) a _ {2 1} v + (u / l) a _ {2 2} r + (u ^ {2} / l ^ {2}) b _ {2} \delta \tag {9.9}\frac {d \psi}{d t} = r$$

where u is the constant forward velocity and l is the length of the ship.

The parameters in the state equation (Eqs. 9.9) are surprisingly constant for different ships and different operating conditions (see Table 9.1). The transfer function from rudder angle $\delta$ to heading $\psi$ is easily determined from Eqs. (9.9). The following result is obtained:

$$G (s) = \frac {K (1 + s T _ {3})}{s (1 + s T _ {1}) (1 + s T _ {2})} \tag {9.10}$$

where

$$K = K _ {0} u / l \tag {9.11}T _ {i} = T _ {i 0} l / u \quad i = 1, 2, 3$$
