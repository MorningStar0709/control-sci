# 4.7 A Design Example

To illustrate the design method we will consider control of an elastic joint in a robot. Consider a motor with current constant $k_{I}$ that drives a load consisting of two masses coupled with a spring with spring constant k (see Fig. 4.17). It is assumed that friction and and damping can be neglected. The input signal is the motor current I. The angular velocities and the angles of the masses are $\omega_{1}$ , $\omega_{2}$ , $\varphi_{1}$ , and $\varphi_{2}$ ; the moments of inertia are $J_{1}$ and $J_{2}$ . It is assumed that there is a relative damping, d, in the spring and that the first mass may be disturbed by a torque v. Finally the output of the process is the angular velocity $\omega_{2}$ .

![](image/e41292faaf0af6824f962238e8a6226e8feee08a7cfd09d6c4f224a4119803ac.jpg)

<details>
<summary>text_image</summary>

I
Motor
φ₁
ω₁
J₁
φ₂
J₂
ω₂
</details>

Figure 4.17 A flexible robot arm.

We now introduce the states

$$
\begin{array}{l} x _ {1} = \varphi_ {1} - \varphi_ {2} \\ x _ {2} = \omega_ {1} / \omega_ {0} \\ x _ {3} = \omega_ {2} / \omega_ {0} \\ \end{array}
$$

where

$$\omega_ {0} = \sqrt {k (J _ {1} + J _ {2}) / (J _ {1} J _ {2})}$$

The process is then described by

$$
\frac {d x}{d t} = \omega_ {0} \left( \begin{array}{c c c} 0 & 1 & - 1 \\ \alpha - 1 & - \beta_ {1} & \beta_ {1} \\ \alpha & \beta_ {2} & - \beta_ {2} \end{array} \right) x + \left( \begin{array}{l} 0 \\ \gamma \\ 0 \end{array} \right) u + \left( \begin{array}{l} 0 \\ \delta \\ 0 \end{array} \right) v \tag {4.65}

y = \left( \begin{array}{c c c} 0 & 0 & \omega_ {0} \end{array} \right) x
$$

where

$$\alpha = J _ {1} / \left(J _ {1} + J _ {2}\right)\beta_ {1} = d / J _ {1} \omega_ {0}\beta_ {2} = d / J _ {2} \omega_ {0}\gamma = k _ {I} / J _ {1} \omega_ {0}\delta = 1 / J _ {1} \omega_ {0}$$

The following values have been used in the example: $J_{1} = 10/9$ , $J_{2} = 10$ , k = 1, d = 0.1, and $k_{I} = 1$ , which gives $\omega_{0} = 1$ . With these values the process (4.65) has three poles, $p_{1} = 0$ and $p_{23} = -0.05 \pm 0.999i$ , and one zero, $z_{1} = -10$ . Notice that the system contains a pure integrator. The complex poles have a damping of $\zeta_{p} = 0.05$ and a natural frequency $\omega_{p} = 1$ rad/s. The Bode plot of the process is shown in Fig. 4.18 and the impulse response in Fig. 4.19.
