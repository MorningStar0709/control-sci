b. With reference to Figure 7.26, compute the loop gain $L(j\omega) = K(j\omega I - A)^{-1}B$ and the corresponding complementary sensitivity $T(j\omega) = L(j\omega) / [1 + L(j\omega)]$ . Plot $|T(j\omega)|$ versus $\omega$ .

c. Repeat parts (a) and (b) to place poles at $-12 \pm j12$ and $-96$ and at $-24 \pm j24$ and $-192$ . In view of the results of Chapter 5, Section 5.6.5, what, in each case, is the frequency range over which the multiplicative modeling uncertainty $|\Delta(j\omega)| = \ell(j\omega)$ must be less than 1 to guarantee stability, according to the results of Section 5.6.5?

7.10 Servo, simplified model For the dc servo of Problem 2.4 (Chapter 2):

a. Design a state feedback gain such that the closed-loop poles are complex, with damping factor $\zeta = \sqrt{2}/2$ and arbitrary distance $\omega_{0}$ from the origin.   
b. Design the control law for regulation to a set point $\theta = \theta_{d}$ , and calculate the transfer function $\theta / \theta_{d}$ .   
c. Obtain the transfer function $v/\theta_{d}$ , and discuss its variation as a function of $\omega_{0}$ .

M 7.11 Servo with flexible shaft For the servo with flexible shaft of Problem 2.5 (Chapter 2):

a. Design a state feedback such that the closed-loop poles are located at -4, -5, -21.52, and $-150 \pm j150$ .   
b. The pole placement called for in part (a) represents modest displacement of the open-loop real poles at 0, -2.47, and -21.52 and considerable movement of the open-loop imaginary poles at ±j171.3. [See Problem 3.14 (Chapter 3) for the open-loop transfer functions.] To ascertain how much control effort is required to displace the high-frequency imaginary poles, repeat part (a) for the closed-loop location 0, -2.47, -21.52, -150 ± j150. Compare the two gains.   
c. Using the gain of part (a), design the control law for regulation to a set point $\theta_{2}=\theta_{d}$ , and calculate the transfer function $\theta_{2}/\theta_{d}$ .   
d. Compute the unit-step response for the transfer functions of part (c).
