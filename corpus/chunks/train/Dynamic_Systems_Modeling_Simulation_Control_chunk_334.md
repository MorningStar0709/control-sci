<details>
<summary>text_image</summary>

Nonlinear
inductor
L
+
e_in(t)
-
I_L
R
</details>

Figure P6.10

6.11 Figure P6.11 shows a mass m sliding on an oil film with viscous friction coefficient b (see Problem 2.6 in Chapter 2). The mass is moving toward the stiffness element k and at time $t = 0$ it has position $x ( 0 ) = 0$ , velocity $\dot { x } ( 0 ) = 0 . 4 \mathrm { m / s }$ , and it is 0.5 m from the stiffness element. The system parameters are $m = 1 . 8 \mathrm { k g } .$ , $b = 0 . 7 5 \mathrm { N - s / m } .$ , and $k = 2 \mathrm { N } / \mathrm { m }$ . Use Simulink to determine the system response and plot $x ( t ) , \dot { x } ( t )$ , and spring force. Does the mass return to its starting position $\mathrm { ( } x = 0 \mathrm { ) ? }$

![](image/62e6e078d0e10c447ccb5787429da83420576529eedbace3183e3414d1243cdc.jpg)

<details>
<summary>text_image</summary>

x(0) = 0
ẋ(0) = 0.4 m/s
Oil film,
friction b
m
k
0.5 m
</details>

Figure P6.11

6.12 Consider again the nonlinear system from Problem 5.5 in Chapter 5:

$$
\begin{array}{l} \dot {x} _ {1} - x _ {2} = 0 \\ \dot {x} _ {2} + 2 x _ {1} ^ {1 / 4} + 3 x _ {2} = u \\ \end{array}
$$

The initial conditions are $x _ { 1 } ( 0 ) = 0 . 0 8 , x _ { 2 } ( 0 ) = 0 . 0 2$ , and the input is $u = 1 . 0 1 \ : ( \mathrm { c o n s t a n t } )$ .

a. Simulate the nonlinear system using Simulink to obtain the state responses $\mathbf { x } ( t ) = \left[ x _ { 1 } ( t ) x _ { 2 } ( t ) \right] ^ { T }$ . Plot $x _ { 1 } ( t )$ and $x _ { 2 } ( t )$ on the same figure.   
b. Linearize the system about the static equilibrium state vector $\mathbf { x } ^ { * }$ that arises when the nominal input is $u ^ { * } = 1$ (see Problem 5.5). Use Simulink to simulate the linear model and obtain the approximate state response $\mathbf { x } ( t ) = \mathbf { x } ^ { * } + \delta \mathbf { x } ( t )$ ). Plot the nonlinear state solutions [from part (a)] and linearized state solutions on the same figure. Comment on the accuracy of the linear solution.
