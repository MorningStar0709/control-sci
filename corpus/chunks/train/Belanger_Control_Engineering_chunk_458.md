Show that $K_{x}$ in Equation 7.45 is the gain matrix obtained by solving the LQ problem without disturbance or reference inputs, with $J = \int_{0}^{\infty} [\Delta x^{T} Q_{xx} \Delta x + \Delta u^{T} R \Delta u] dt$ .

\* H i n t Partition the P matrix in the same way as Q, and write the Riccati equation in terms of the matrix blocks.

7.30 For the system

$$\dot {x} _ {1} = x _ {1} + uy = x _ {1}$$

a. Calculate the constant input $u^{*}$ corresponding to a dc steady-state output $y_{d}^{*}$ .

b. For $y_{d} = y_{d}^{*} + Ae^{-t}$ , derive the control law that minimizes

$$J = \int_ {0} ^ {\infty} [ (y - y _ {d}) ^ {2} + (u - u ^ {*}) ^ {2} ] d t.$$

7.31 Repeat Problem 7.30, but with the constant $y_{d}^{*}$ replaced by the sinusoid $y_{d}^{*}(t) = B\sin t$ .

![](image/dafbf6ef7adacbd42daeb287779b545e6a52586a010ec93f5fc0a172aa088b0d.jpg)

7.32 Servo, simplified model For the linear, second-order model of Problem 2.4 (Chapter 2):

a. Calculate the steady-state $v^*$ required to yield a constant angle $\theta_d$ in the face of a constant disturbance $T_L^*$ . Express $v^*$ as a linear combination of $\theta_d$ and $T_L^*$ .   
b. Use the control law derived in Problem 7.10 plus the feedforward term for $T_{L}^{*}$ . Show that this law cancels out $T_{L}$ ; i.e., show that the state does not change in response to changes in $T_{L}$ .   
c. Remove the feedforward term in $T_{L}^{*}$ , and compute the response $\Delta \theta / T_{L}$ .

![](image/3cb8cf407a80bb25ee6a3ee4adedd6d10730b643fd565443b9dfcf0b9d962cb5.jpg)

7.33 Drum speed control In Problem 7.23, an LQ control system was designed for the system of Problem 2.6 (Chapter 2). The design was tested for a step response in the desired speed $\omega_0$ . We wish to investigate the response for a larger, but more gradual, speed increase. Accordingly, let $\omega_d(t) = 25 - 25e^{-t / \tau}$ , where $\tau$ is a time constant to be determined.
