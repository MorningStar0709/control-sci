# Damping Ratio and Undamped Natural Frequency

We have seen from the previous section and Example 7.7 that the form of the free (or transient) response of a second-order system is completely determined by the two characteristic roots. When the two roots are complex with a negative real part, the transient response is a damped sinusoid. Another way to categorize the second-order transient response is to use the damping ratio. Consider again the general LTI second-order I/O equation

$$\ddot {y} + a _ {1} \dot {y} + a _ {0} y = b _ {0} u (t) \tag {7.62}$$

Its characteristic roots are determined by Eq. (7.51), which is repeated here

$$\text { Characteristic roots: } \quad r = \frac {- a _ {1} \pm \sqrt {a _ {1} ^ {2} - 4 a _ {0}}}{2} \tag {7.63}$$

Let’s assume that coefficients $a _ { 1 }$ and $a _ { 0 }$ are positive. Note that if coefficient $a _ { 1 }$ is too small so that $a _ { 1 } ^ { 2 } < 4 a _ { 0 }$ , the roots will be complex conjugates because the radicand is negative. In this case, the transient response will be a damped sinusoid, and the system is said to be underdamped. Furthermore, if coefficient $a _ { 1 }$ is large enough so that $a _ { 1 } ^ { 2 } > 4 a _ { 0 }$ , the two roots will be real, distinct, and negative. In this case, the transient response will consist of two decaying exponential functions, and the system is said to be overdamped. The transitional condition is when $a _ { 1 } = 2 \sqrt { a _ { 0 } }$ and the two roots are real, negative, and equal. In this transitional case, the system is said to be critically damped. We can characterize these three cases by defining the damping ratio $\zeta$ as the ratio of coefficient $a _ { 1 }$ to its critical value $( 2 \sqrt { a _ { 0 } } )$ when both roots become real and equal

$$\text { Damping ratio: } \quad \zeta = \frac {a _ {1}}{2 \sqrt {a _ {0}}} \tag {7.64}$$

Therefore, we can classify the three cases in terms of the damping ratio $\zeta \colon$ :

1. ?? > 1: Overdamped system (see Fig. 7.13a)   
2. ?? = 1: Critically damped system (see Fig. 7.14a)   
3. $0 < \zeta < 1$ : Underdamped system (see Fig. 7.15a)

Another way to think of the damping ratio is to observe the mathematical model of a mechanical valve in a hydraulic fluid with a return spring, which might be modeled by the mass–spring–damper system:

$$m \ddot {x} + b \dot {x} + k x = f (t)$$

where x is the valve position from static equilibrium and f (t) is the applied force. The roots of the massspring-damper system are

$$r = \frac {- b \pm \sqrt {b ^ {2} - 4 m k}}{2 m}$$
