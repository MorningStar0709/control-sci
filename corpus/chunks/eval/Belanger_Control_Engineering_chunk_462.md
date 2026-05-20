d. Simulate the linear system response with $\Delta Q(t) = 10,000\mathrm{J / min}$ , $\Delta c_{A0}(t) = 0.01\mathrm{kgmoles / m^3}$ , $\Delta c_A(0) = 0.5\mathrm{kgmoles / m^3}$ , and $\Delta T(0) = -10^{\circ}\mathrm{C}$ . Drive the observer of part (c) with $\Delta T(t)$ , $\Delta Q(t)$ , and $\Delta c_{A0}(t)$ with the observer initially in the zero state. Compare the estimates with the true values of the state variables.

![](image/3bf874e885b792bf1f9347c384afa28b04e9ee1ac02f327382dd51ac0082f5ba.jpg)

7.42 Chemical reactor With reference to Problem 7.41, it is noted that the inlet concentration $\Delta c_{A0}(t)$ may often be unavailable. We wish to modify the observer to observe $\Delta c_{A0}$ of the form $Ae^{-0.3t}$ . Design a modified (third-order) observer, adding a pole to the error system at $-1$ . Repeat the simulation of Problem 7.41(d), but with $\Delta c_{A0}(t) = 0.01e^{-0.3t}$ , and estimate $\Delta c_{A0}$ as well as the system state.

7.43 Design an optimal observer for the system

$$
\begin{array}{l} \dot {x} = a x + u + w \\ y = x + v. \\ \end{array}
$$

Express the observer gain in terms of $a$ and the design parameters $W$ and $V$ , and discuss its variation as a function of those parameters. (Note that $W \geq 0, V > 0$ , and $a$ may be positive or negative.) Calculate the transfer function $\widehat{x} / y$ .

7.44 The design of a differentiator may be approached from the observer point of view. A signal $x(t)$ is modeled as

$$
\begin{array}{l} \dot {x} = z \\ \dot {z} = w \\ \end{array}
$$

with a noisy observation

$$y = x + v.$$

Here, $z(t)$ is the derivative of $x(t)$ .

Use the design parameters $W = \left[\begin{matrix} 0 & 0 \\ 0 & w_{0}^{2} \end{matrix}\right]$ and V > 0 to obtain an optimal observer. Calculate the transfer function $\widehat{z}/y$ of the differentiator, and discuss its variations with $w_{0}^{2}$ and V.

7.45 An observer can be designed to recover a sinusoid of known frequency from a noisy observation.

a. Show that the model

$$
\begin{array}{l} \dot {\mathbf {x}} = \left[ \begin{array}{c c} 0 & \omega \\ - \omega & 0 \end{array} \right] \mathbf {x} \\ y = x _ {1} \\ \end{array}
$$

is such that $y(t)$ is a sinusoid of frequency $\omega$ whose phase depends on $\mathbf{x}(0)$ .
