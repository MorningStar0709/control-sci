# Example 8.2 cont.

![](image/b5c5b7b3ad6905b731f3bcb7d34312ee6257a40402ac8b74407c99f097e197b1.jpg)

<details>
<summary>line</summary>

| Position | Velocity |
| --- | --- |
| 0.0 | 0.0 |
| 0.1 | 2.9 |
| 0.2 | 1.8 |
| 0.3 | 2.3 |
| 0.4 | 2.1 |
| 0.5 | 2.2 |
| 0.6 | 2.1 |
| 0.7 | 2.0 |
| 0.8 | 1.9 |
| 0.9 | 1.7 |
| 1.0 | 1.5 |
| 1.1 | 1.2 |
| 1.2 | 0.8 |
| 1.3 | 0.3 |
| 1.4 | -0.5 |
</details>

Step response of the car suspension system in state space. Horizontal axis is $x _ { 3 } ,$ the position of the car body, and vertical axis is ${ \dot { x } } _ { 3 } ,$ the velocity of the body's vertical travel.

The result plots the body position, $( x _ { 3 } ,$ horizontal $\mathrm { a x i s } )$ vs. body vertical velocity $( { \dot { x } } _ { 3 } ,$ vertical axis). The system trajectory starts at $( x _ { 3 } = 0 , \quad \dot { x } _ { 3 } = 0 )$ followed by a sharp initial transient to high positive (upward) velocity followed by an interesting spiral to the nal point $( x _ { 3 } \stackrel { - } { = } 1 , \quad \dot { x } _ { 3 } = 0 )$ . The $x _ { 3 } \overline { { ( t ) } }$ data is the same as our initial step response of this example, and the x˙ data is its time derivative. Time is not explicitly shown but the spiral indicates the roughly 40% overshoot in the step response and most of its convergence to the steady state position value (1.0).

Using the state space representation we can really put the dynamic response under the microscope because the $\breve { C }$ matrix let's us look at all 4 state variables after a step input. For

$$
C = \left[ \begin{array}{l} 1, 0, 0, 0 \\ 0, 1, 0, 0 \\ 0, 0, 1, 0 \\ 0, 0, 0, 1 \end{array} \right]
$$

We see the 4 step responses of all the state variables.
