# Example 7.1

Consider the first-order linear differential equation with initial condition $y ( 0 ) = 3$ .

$$4 \dot {y} + 8 y = 6$$

Determine the complete solution $y ( t )$ .

First, we determine the characteristic equation by equating the terms between Eqs. (7.6) and (7.2). For this first-order system, we get a first-order characteristic equation

$$4 r + 8 = 0$$

and the single characteristic root is $r = - 8 / 4 = - 2$ . Therefore, the homogeneous solution has the form $y _ { H } ( t ) =$ $c e ^ { - 2 t }$ . Next, we determine the particular solution. Because the forcing function (right-hand side) is $f ( t ) = 6$ , we assume that the particular solution is also a constant, $y _ { P } ( t ) = a$ . Substituting $y _ { P } ( t ) = a$ and $\dot { y } _ { P } ( t ) = 0$ into the original differential equation yields $8 a = 6$ , and therefore the particular solution is $y _ { P } ( t ) = a = 6 / 8 = 0 . 7 5$ . Finally, the complete solution is the sum of the homogeneous and particular solutions, or

$$y (t) = y _ {H} (t) + y _ {P} (t) = c e ^ {- 2 t} + 0. 7 5$$

The final step is to determine the coefficient c from the known initial condition, $y ( 0 ) = 3$ :

$$y (0) = c e ^ {0} + 0. 7 5 = 3$$

which yields $c = 3 - 0 . 7 5 = 2 . 2 5$ . Therefore, the complete solution of the differential equation is

$$y (t) = 2. 2 5 e ^ {- 2 t} + 0. 7 5$$
