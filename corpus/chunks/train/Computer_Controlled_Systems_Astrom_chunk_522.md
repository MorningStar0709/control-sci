# 6.7 Problems

8.1 Find how the left half-s-plane is transformed into the z-plane when using the mappings in (8.4) to (8.6).   
8.2 Use different methods to make an approximation of the transfer function

$$G (s) = \frac {a}{s + a}$$

(a) Euler's method   
(b) Tustin's approximation   
(c) Tustin's approximation with prewarping if the warping frequency is $\omega_{1} = \alpha$ rad/s

8.3 The lead network given in (8.9) gives about $20^{\circ}$ phase advance at $\omega_{c} = 1.6$ rad/s. Approximate the network for h = 0.25 using

(a) Euler's method   
(b) Backward differences   
(c) Tustin's approximation   
(e) Zero-order-hold sampling

(d) Tustin's approximation with prewarping using $\omega_{1} = \omega_{c}$ as the warping frequency

Compute the phase of the approximated networks at $z = \exp(i\omega_{c}h)$ .

8.4 Verify the calculations leading to the rule of thumb for the choice of the sampling interval given in Sec. 8.2.

8.5 Show that (8.24) is obtained from (8.22) by approximating the integral part using Euler's method and backward difference for the derivative part. Discuss advantages and disadvantages for each of the following cases.

(a) The integral part is approximated using backward difference.   
(b) The derivative part is approximated using Euler's method. (Hint: Consider the case when $T_{d}$ is small.)

8.6 A continuous-time PI-controller is given by the transfer function

$$K \left(1 + \frac {1}{T _ {i} s}\right)$$

Use the bilinear approximation to find a discrete-time controller. Find the relation between the continuous-time parameters K and $T_{t}$ and the corresponding discrete-time parameters in (8.24).

8.7 Consider the tank system in Problem 2.10. Assume the following specifications for the closed-loop system:

1. The steady-state error after a step in the reference value is zero.   
2. The crossover frequency of the compensated system is 0.025 rad/s.   
3. The phase margin is about $50^{\circ}$ .
