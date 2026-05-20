![](image/a8ba7cb4e3939d03e14320a2c512bea7f0bcb73278a412cc4ce61575e5d5f19d.jpg)  
Figure 6.6: Performance weight $W _ { e }$ and desired S

${ \mathrm { O r } } ,$ equivalently, $| W _ { e } S | \le 1$ with

$$W _ {e} = \frac {s / M _ {s} + \omega_ {b}}{s} \tag {6.5}$$

The preceding discussion applies in principle to most control design and hence the preceding weighting function can, in principle, be used as a candidate weighting function in an initial design. Since the steady-state error with respect to a step input is given by $| S ( 0 ) |$ , it is clear that $| S ( 0 ) | = 0$ if the closed-loop system is stable and $\| W _ { e } S \| _ { \infty } < \infty .$ .

Unfortunately, the optimal control techniques described in this book cannot be used directly for problems with such weighting functions since these techniques assume that all unstable poles of the system (including plant and all performance and control weighting functions) are stabilizable by the control and detectable from the measurement outputs, which is clearly not satisfied if $W _ { e }$ has an imaginary axis pole since $W _ { e }$ is not detectable from the measurement. We shall discuss in Chapter 14 how such problems can be reformulated so that the techniques described in this book can be applied. A theory dealing directly with such problems is available but is much more complicated both theoretically and computationally and does not seem to offer much advantage.

![](image/ee6f53e71551a50a15ffc3db2895df9c235806e9e20366adb502c5457cf7cf14.jpg)  
Figure 6.7: Practical performance weight $W _ { e }$ and desired S

Now instead of perfect tracking for step input, suppose we only need the steadystate error with respect to a step input to be no greater than $\epsilon \ ( \mathrm { i . e . , } \ | S ( 0 ) | \ \leq \ \epsilon )$ ; then it is sufficient to choose a weighting function $W _ { e }$ satisfying $| W _ { e } ( 0 ) | \ge 1 / \varepsilon$ so that $\| W _ { e } S \| _ { \infty } \leq 1$ can be achieved. $\mathrm { A }$ possible choice of $W _ { e }$ can be obtained by modifying the weighting function in equation (6.5):

$$W _ {e} = \frac {s / M _ {s} + \omega_ {b}}{s + \omega_ {b} \varepsilon} \tag {6.6}$$

Hence, for practical purpose, one can usually choose a suitable ε, as shown in Figure 6.7, to satisfy the performance specifications. If a steeper transition between low-frequency and high-frequency is desired, the weight $W _ { e }$ can be modified as follows:
