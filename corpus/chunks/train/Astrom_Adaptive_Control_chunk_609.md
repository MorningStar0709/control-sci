# EXAMPLE 10.2 A basic SOAS

Assume that the linear parts are characterized by the transfer function

$$G (s) = \frac {K \alpha}{s (s + 1) (s + \alpha)}$$

![](image/526c4194a2efd33a0fd16bd038d24be2eb44c8b609b6e3de2907ddcf4d14635e.jpg)  
Figure 10.9 Simulation of an SOAS applied to the system in Example 10.2. The dashed line shows the desired response $y_{m}$ .

From Example 8.1 the period of the limit cycle is approximately given by

$$\omega_ {u} = \sqrt {\alpha}$$

The magnitude of the transfer function at this frequency is

$$\left| G (i \omega_ {u}) \right| = \frac {K}{\alpha + 1}$$

If the relay amplitude is d, it follows that the amplitude of the limit cycle oscillation at the relay input is approximately given by

$$e _ {0} = \frac {K d}{1 + \alpha}$$

The limit cycle amplitude is thus inversely proportional to $\alpha$ . A simulation of the system is shown in Fig. 10.9. The feedforward transfer function is a second-order system with the damping 0.7 and the natural frequency 1 rad/s. The nominal values of the parameters are K = 3, d = 0.35, and $\alpha = 20$ . The approximate analysis gives a limit cycle with period T = 1.4 and amplitude 0.05. The process gain is suddenly increased by a factor of 5 at t = 25. Notice the rapid adaptation. However, the amplitude of the oscillation will also increase by a factor of 5. If the value of d is chosen such that the error would be 0.05 for the higher value of K, then the system becomes too slow for small K.
