# Sliding Modes

One way to change the structure of the system is to use different controllers in different parts of the state space of the system. Consider the case in which the control law switches on the surface

$$\sigma (x) = 0$$

Assume that the closed-loop system is described by

$$
\frac {d x}{d t} = \left\{ \begin{array}{l l} f ^ {+} (x) & \sigma (x) > 0 \\ f ^ {-} (x) & \sigma (x) <   0 \end{array} \right. \tag {10.5}
$$

Two situations may occur, which for the two-dimensional case are shown in Fig. 10.13. In Case (a) the trajectories will pass the switching curve and continue into the other region. However, the dynamics are different in the two regions. In Case (b) the vector fields will drive the state toward the surface $\sigma(x) = 0$ . The control will change rapidly from one value to another on the switching surface. This is called chattering. The net effect is that the state will move toward the surface $\sigma(x) = 0$ and then slide along the surface. This is called sliding mode. This sliding motion can be described as follows: Let $f_n$ denote the projection of $f$ on the normal of the surface $\sigma(x) = 0$ . Introduce a number $\alpha$ such that

$$\alpha f _ {n} ^ {+} + (1 - \alpha) f _ {n} ^ {-} = 0$$

The sliding motion is then given by

$$\frac {d x}{d t} = \alpha f ^ {\dagger} + (1 - \alpha) f ^ {-}$$

![](image/333e50b7ffbceb093536924a421d8f2e076887ff4799494af56f69147b13b3b3.jpg)

<details>
<summary>text_image</summary>

(a)
σ(x) > 0
σ(x) < 0
f⁺
f⁻
</details>

![](image/6e43a20094f1fde291526acb66b3fd99bbb4adb51f00b1328ce11d6ff79375e4.jpg)

<details>
<summary>text_image</summary>

(b)
σ(x) > 0
σ(x) < 0
f'
f⁻
</details>

Figure 10.13 The trajectories of Eqs. (10.5) at the switching surface. (a) No sliding mode; (b) sliding mode.

This was formally shown by A. F. Filippov in the early 1960s. The control law giving the sliding motion is sometimes called the equivalent control law. If the switching is not ideal, then the trajectory will move back and forth over the switching surface. This is the case, for instance, when there is hysteresis in the switching. However, on average the motion will be along the switching surface.
