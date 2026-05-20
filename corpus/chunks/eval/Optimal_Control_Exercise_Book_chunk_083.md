# Exercise 5.19 (Linear quadratic regulator (LQR) problem)

Consider a cart with an inverted pendulum hinged on top of it as shown in the Figure 1. For simplicity, the cart and the pendulum are assumed to move in only one plane, and the friction, the mass of the stick, and the gust of wind are disregarded. The problem is to maintain the pendulum at the vertical position. For example, if the inverted pendulum is falling in the direction shown, the cart moves to the right and exerts a force, through the hinge, to push the pendulum back to the vertical position. Let’s consider the linearized inverted pendulum system (assuming θ(t) and ˙θ(t) are very small)

![](image/f6fd5bf53a769d559fe58b2c0a1e2512fb081edb7dd57d99807dab0a2d30e55f.jpg)

<details>
<summary>text_image</summary>

m
θ
l
y
x
M
F
</details>

Figure 1: The inverted pendulum model

$$
\left[ \begin{array}{l} \dot {x} _ {1} (t) \\ \dot {x} _ {3} (t) \\ \dot {x} _ {3} (t) \\ \dot {x} _ {4} (t) \end{array} \right] = \left[ \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ 0 & 0 & - \frac {m g}{M} & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & \frac {(M + m) g}{M l} & 0 \end{array} \right] \left[ \begin{array}{l} x _ {1} (t) \\ x _ {2} (t) \\ x _ {3} (t) \\ x _ {4} (t) \end{array} \right] + \left[ \begin{array}{c} 0 \\ \frac {1}{M} \\ 0 \\ - \frac {1}{M l} \end{array} \right] u (t) \tag {383}
$$

where $x _ { 1 } ( t ) = x ( t )$ , $x _ { 2 } ( t ) = \dot { x } ( t )$ , $x _ { 3 } ( t ) = \theta ( t )$ , and x4(t) = ˙θ(t).

Consider the LQR problem

$$u ^ {*} := \underset {u: [ 0, \infty) \rightarrow \mathbb {R} ^ {m}} {\operatorname{argmin}} J (u) := \int_ {0} ^ {\infty} \left(x (t) ^ {T} Q x (t) + u (t) ^ {T} R u (t)\right) d t \tag {384}$$

subject to (385)

$$\dot {x} (t) = A x (t) + B u (t), \quad x (0) = x _ {0} \tag {386}$$

where A and B are appropriate system matrices with $m { = } 1$ , $M { = } 2 ,$ , $l { = } \beta$ and $g { = } 9 . 8 .$ . Tasks:

1. Appropriately choose the weighting $Q \geq 0$ and $R > 0$ to maintain the pendulum at the vertical position, i.e., $\theta ( t ) = 0$ and $\dot { { \theta } } ( t ) = 0$ as much as possible.   
2. Find an optimal policy for the LQR problem using Python or Matlab functions.

3. Plot trajectories of the system x(t) and the control input u(t) over certain time interval to demonstrate the performance of your optimal control policy.   
4. In the answer, please include your Python or Matlab codes.   
5. Change the weight and see how the performance changes and discuss about the results.
