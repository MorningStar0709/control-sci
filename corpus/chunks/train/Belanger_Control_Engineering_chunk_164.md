$$
\dot {\mathbf {x}} = \left[ \begin{array}{l l} 0 & 1 \\ 1 & 0 \end{array} \right] \mathbf {x}.
$$

M 3.9 For the system

$$
\dot {\mathbf {x}} = \left[ \begin{array}{c c} 0 & 1 \\ - 1 & 0 \end{array} \right] \mathbf {x}
$$

a. Calculate $e^{At}$ .   
b. Plot $x_{2}(t)$ vs. $x_{1}(t)$ for $\mathbf{x}(0) = [1]$ .

Interpret the result.

3.10 Calculate the transfer function of the system

$$
\dot {\mathbf {x}} = \left[ \begin{array}{l l} 0 & 1 \\ 1 & 0 \end{array} \right] \mathbf {x} + \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] u

y = \left[ \begin{array}{l l} 1 & 0 \end{array} \right] \mathbf {x}.
$$

![](image/09e8552034a8d247654d12f152b9b1baad952ff7d0b535242ed9c4573cfe9cea.jpg)

3.11 Repeat Problem 3.10 for the system

$$
\dot {\mathbf {x}} = \left[ \begin{array}{l l} 0 & 1 \\ - 3 & - 4 \end{array} \right] \mathbf {x} + \left[ \begin{array}{l l} 0 & 1 \\ - 1 & 1 \end{array} \right] \mathbf {u}

\mathbf {y} = \left[ \begin{array}{l l} 1 & 1 \\ 0 & 1 \end{array} \right] \mathbf {x}.
$$

a. Calculate the transmission zeros, using the equation $\operatorname{det} H(s_0) = 0$ .

b. Repeat part (a), using MATLAB.

3.12 Suppose $s_{0}$ is not a pole of the matrix transfer function $H(s)$ .

a. Show that, if the input is $e^{s_0 t} \mathbf{w} u_{-1}(t)$ , there is a component $H(s_0) \mathbf{w} e^{s_0 t}$ in the output.

\* H i n t Use partial-fraction ideas.

b. Use the results of part (a) to write an interpretation of the concept of a transmission zero.

3.13 Servo, simplified model Calculate the transfer function $\theta / v$ for the dc servo of Problem 2.4 (Chapter 2).

![](image/6632fd817271c7114d1777234ba48334fa6eb97cd53e00325bb66e1a406ce257.jpg)

3.14 Servo with flexible shaft Compute the transfer function $\theta_{2} / v$ and $\theta_{1} / v$ for the dc servo of Problem 2.5 (Chapter 2).

![](image/917f3ece695705c9aa9a7e81af540adc6c1adaa9f4f6332fce42fd6c1c7beab4.jpg)

3.15 Drum speed control For the drum speed control model of Problem 2.6 (Chapter 2), compute the transfer functions $\omega_0 / u_1$ , $\omega_0 / u_2$ , and $\omega_0 / T_0$ .

![](image/aa596e5ba74a5b88527254ad1b5ac415ec07cab136b293df21184e0031f20bd6.jpg)

3.16 High-wire artist For the linearized system of Problem 2.18 (Chapter 2), compute the transfer functions $\theta / \tau$ and $\phi / \tau$ .

![](image/02cb108a51503933594fd28cccaae464ac2a95d1d013d31f5094ddadb7af7554.jpg)
