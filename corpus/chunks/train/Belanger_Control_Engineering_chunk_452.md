a. Using the linearized model, design a pole-placement control law for closed-loop poles at $-11$ , $-12$ , $-0.5 \pm j0.5$ .   
b. Using the nonlinear model of Problem 2.12, simulate the closed-loop response for the conditions $\theta(0) = \theta_0$ , $\omega_{\theta}(0) = \phi(0) = \omega_{\phi}(0) = 0$ , for $\theta_0 = 0.5$ , 1 and 1.5 rad. Discuss the results.

![](image/d1eac9899a6f6f301174735ca9d483a5fdf2898784cf28a6dcd2bc1b99b52c93.jpg)

7.15 Crane The crane model of Problem 2.11 (Chapter 2) was linearized in Problem 2.17.

a. Using the linearized model of Problem 2.17, design a pole-placement-based control law to regulate x to a set point $x_{d}$ , and to place the closed-loop poles at -1, -2, and $-2 \pm j2$ . Compute the response x to a unit step in $x_{d}$ .   
i. Repeat part (a), but “speed up” the response by placing poles at -4, -8, and $-8 \pm j8$ .   
ii. Modify the nonlinear model of Problem 2.11 by including the control law of part (a). Simulate the response for steps in $x_{d}$ of 1 m and 10 m.   
iii. Repeat part (c) for the control law of part (b). Discuss differences between the results of parts (c) and (d).

![](image/cc4664df358d06d17ff2daa21eec6d97cb718d40008de3812b82ecf435ffffa7.jpg)

7.16 Maglev In Problem 3.22 (Chapter 3), the Maglev equations were rewritten in terms of three redefined inputs. It makes physical sense to say that heave (i.e., $\Delta z$ ) should be controlled through $\Delta u_{LC}$ , roll (i.e., $\theta$ ) should be controlled through $\Delta u_{LD}$ , and sway (i.e., $\Delta y$ ) should be controlled through $\Delta u_{GD}$ .
