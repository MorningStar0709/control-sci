# 7.5 HIGHER-ORDER SYSTEMS

Once we understand the nature of first- and second-order system responses, we can develop a qualitative feel for the response of third- and higher-order systems. Determining the characteristic roots (or, equivalently, the poles of the transfer function) should always be our first step in analyzing a linear system, whether it is a first-, second-, or higher-order system. The roots will tell us whether or not the system is stable, and if the free response is composed of exponential, sinusoidal, or damped sinusoidal functions. For example, consider the third-order linear I/O equation

$$\ddot {y} + 2. 5 \ddot {y} + 3 8 \dot {y} + 1 8. 5 y = u (t) \tag {7.89}$$

The characteristic equation is

$$r ^ {3} + 2. 5 r ^ {2} + 3 8 r + 1 8. 5 = 0 \tag {7.90}$$

which has three roots at $r _ { 1 } = - 0 . 5$ and $r _ { 2 , 3 } = - 1 \pm j 6$ . Hence, the homogeneous or free response will be the sum of an exponential function (the real root at $r _ { 1 } = - 0 . 5 )$ ) and a damped sinusoidal function (the complex conjugate roots at $r _ { 2 , 3 } = - 1 \pm j 6 )$

$$y _ {H} (t) = c _ {1} e ^ {- 0. 5 t} + c _ {2} e ^ {- t} \cos (6 t + \phi) \tag {7.91}$$

Note that the first term in Eq. (7.91) is due to the real root $r _ { 1 }$ and the second term is due to the complex conjugate roots $r _ { 2 }$ and $r _ { 3 }$ . Part of the free response $y _ { H } ( t )$ is an exponential function $e ^ { - 0 . 5 t }$ t that “dies out” in about 8 s (note that its time constant is $\tau = 2 \mathrm { ~ s ) }$ , while the other component of $y _ { H } ( t )$ is a damped sinusoid that “dies $\mathrm { o u t } ^ { \dag }$ in about 4 s and oscillates with a frequency of 6 rad/s. The three unknown constants $c _ { 1 } , c _ { 2 } .$ , and $\phi$ are determined from the three initial conditions y(0), ẏ (0), and ÿ(0), and the input u(t) (the input also determines the particular or forced solution $y _ { P } )$ ).

This simple example demonstrates that the free response of third- or higher-order systems is simply composed of a sum of first- and second-order response functions. Our knowledge of the free response for firstand second-order systems thus allows us to obtain a qualitative feel for the free response of a higher-order system.
