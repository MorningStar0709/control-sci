# Example 2.10 (Sprung Beam)

Figure 2.15 shows a bar moving in a vertical plane, resting on a pair of linear spring-damper combinations. The mass of the bar is M, and its moment of inertia about its center of gravity is J. A force u is applied at the center, in the vertical direction.

Write a linear model for small variations from equilibrium of height y and angle $\theta$ .

Solution At equilibrium, the bar rests horizontally at some height $y_0$ . For small motion, Newton's second law states that

$$M \Delta \ddot {y} = \Delta FJ \Delta \ddot {\theta} = \Delta T$$

where $\Delta F$ and $\Delta T$ are the incremental force and torque, referred to equilibrium. Invoking linearity, $\Delta F$ is expressed as a linear function of the incremental state variables and input. Thus,

$$\Delta F = k _ {1} \Delta y + k _ {2} \Delta \dot {y} + k _ {3} \Delta \theta + k _ {4} \Delta \dot {\theta} + k _ {5} \Delta u.$$

We obtain the constants by calculating the force, with each term acting alone.

If $\Delta \dot{y} = \Delta \theta = \Delta \dot{\theta} = \Delta u = 0$ and $\Delta y \neq 0$ , the bar is at rest in the horizontal position, $\Delta y$ away from $y_0$ . The force on the bar is $-2K\Delta y$ , so $k_1 = -2K$ .

If $\Delta y = \Delta \theta = \Delta \dot{\theta} = \Delta u = 0$ and $\Delta \dot{y} \neq 0$ , the bar is at its equilibrium position but is moving vertically. The force is $-2D\Delta \dot{y}$ , so that $k_{2} = -2D$ .

If $\Delta y = \Delta \dot{y} = \Delta \dot{\theta} = \Delta u = 0$ and $\Delta \theta \neq 0$ , the center of gravity is at its equilibrium position and the bar is at rest, at an angle $\Delta \theta$ to the horizontal. There is no net force, because the incremental forces exerted by the springs are equal and in opposite directions. Thus, $k_{3} = 0$ . It can be seen that $k_{4}$ is also zero.

If $\Delta y = \Delta \dot{y} = \Delta \theta = \Delta \dot{\theta} = 0$ and $\Delta u \neq 0$ , the net force is $\Delta u$ , so $k_5 = 1$ . Thus,

$$\Delta F = - 2 K \Delta y - 2 D \Delta \dot {y} + \Delta u.$$

![](image/aa896183c8783d1eeeff7ead50095501c3ae4ac970987b5e0cc34b30d8a19cf4.jpg)

<details>
<summary>text_image</summary>

K
D
u
θ
K
D
y
</details>

Figure 2.15 Beam moving in a vertical plane
