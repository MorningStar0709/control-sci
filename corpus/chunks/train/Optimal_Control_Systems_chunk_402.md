for the control sequence $u(t) = U = \pm1$ . The switching curve is the same as shown in Figure 7.9 (for time-optimal control of a double integral system) which is repeated here in Figure 7.20. For the control sequence $u(t) = U = 0$ , we have from (7.3.1)

![](image/6919e6d93c56248d51e30fdd0ffc8190ae77ccbf3ce21c83c979e76f713b4359.jpg)

<details>
<summary>text_image</summary>

x2
γ-
u* = -1
R-
γ = γ+ ∪ γ-
0
x1
u* = +1
R+
u* = +1
γ+
</details>

Figure 7.20 Switching Curve for a Double Integral Fuel-Optimal Control System

$$x _ {1} (t) = x _ {1 0} + x _ {2 0} t,x _ {2} (t) = x _ {2 0},t = (x _ {1} (t) - x _ {1 0}) / x _ {2 0}. \tag {7.3.19}$$

These trajectories for $u(t) = 0$ are shown in Figure 7.21. Here, we cannot drive the system from any initial state to the origin by means of the zero control. For example, if the system is on the $x_{1}$ axis at $(1,0)$ , it continues to stay there for ever. Or if the system is at $(0,1)$ or $(0,-1)$ , it travels along the trajectory with constant $x_{20}$ towards the right or left.

![](image/49eaedaf2a1b4d056e28afc62c961bc5062246a3f22a22830440757900fec67e.jpg)

<details>
<summary>text_image</summary>

x₂
+1
-1
+1
x₁
-1
</details>

Figure 7.21 Phase-Plane Trajectories for $u(t) = 0$

\- Step 6: Minimum Fuel: If there is a control $u(t)$ which drives the system from any initial condition $(x_{10}, x_{20})$ to the origin $(0, 0)$ , then the minimum fuel satisfies the relation

$$J ^ {*} (x _ {1 0}, x _ {2 0}) = J ^ {*} \geq | x _ {2 0} | \tag {7.3.20}$$

and hence

$$\boxed {J ^ {*} = | x _ {2 0} |.} \tag {7.3.21}$$

Proof: Solving the state equation (7.3.1), we have

$$x _ {2} (t) = x _ {2 0} + \int_ {0} ^ {t} u (\tau) d \tau . \tag {7.3.22}$$

Since we must reach the origin at $t_f$ , it follows from the previous equation

$$x _ {2} (t _ {f}) = 0 = x _ {2 0} + \int_ {0} ^ {t _ {f}} u (t) d t \tag {7.3.23}$$

which yields

$$x _ {2 0} = - \int_ {0} ^ {t _ {f}} u (t) d t. \tag {7.3.24}$$

Or using the well-known inequality,

$$\left| x _ {2 0} \right| = \left| \int_ {0} ^ {t _ {f}} u (t) d t \right| \leq \int_ {0} ^ {t _ {f}} | u (t) | d t = J. \tag {7.3.25}$$

Hence, $|x_{20}| = J^{*}$ . Note, if the initial state is $(x_{10}, 0)$ , the fuel consumed J = 0, which implies that $u(t) = 0$ for all $t \in [0, t_{f}]$ . In other words, a minimum-fuel solution does not exist for the initial state $(x_{10}, 0)$ .

\- Step 7: Switching Sequences: Now let us define the various regions in state space. (See Figure 7.22.)
