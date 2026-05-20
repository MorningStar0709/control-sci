It is a function only of the damping ratio $\zeta .$ Thus, the damping ratio $\zeta$ can be determined by use of the logarithmic. decrement.

In the experimental determination of the damping ratio z from the rate of decay of the oscillation, we measure the amplitude $x _ { 1 }$ at $t = t _ { p }$ and amplitude $x _ { n }$ at $t = t _ { p } + ( n - 1 ) T$ . Note that it is necessary to choose n large enough so that the ratio $x _ { 1 } / x _ { n }$ is not near unity. Then

$$\frac {x _ {1}}{x _ {n}} = e ^ {(n - 1) 2 \zeta \pi / \sqrt {1 - \zeta^ {2}}}$$

or

$$\ln {\frac {x _ {1}}{x _ {n}}} = (n - 1) \frac {2 \zeta \pi}{\sqrt {1 - \zeta^ {2}}}$$

Hence

$$\zeta = \frac {\frac {1}{n - 1} \left(\ln \frac {x _ {1}}{x _ {n}}\right)}{\sqrt {4 \pi^ {2} + \left[ \frac {1}{n - 1} \left(\ln \frac {x _ {1}}{x _ {n}}\right) \right] ^ {2}}}$$

A–5–7.

In the system shown in Figure 5–55, the numerical values of $m , b ,$ and k are given as $m = 1$ kg, $b = 2 \mathrm { N - s e c / m }$ , and $k = 1 0 0 \mathrm { N } / \mathrm { m }$ . The mass is displaced 0.05 m and released without initial velocity. Find the frequency observed in the vibration. In addition, find the amplitude four cycles later. The displacement x is measured from the equilibrium position.

![](image/a2eada2ec6a7e116ff031a69fd65b94ebf7d33c42642ccf6a7f02b95e38a6e24.jpg)

<details>
<summary>text_image</summary>

k
b
m
x
</details>

Solution. The equation of motion for the system is

$$m \ddot {x} + b \dot {x} + k x = 0$$

Substituting the numerical values for $m , b ,$ and k into this equation gives

$$\ddot {x} + 2 \dot {x} + 1 0 0 x = 0$$

where the initial conditions are $\mathbf { x } ( 0 ) = 0 . 0 5$ and $\dot { x } ( 0 ) = 0 .$ From this last equation the undamped. natural frequency $\omega _ { n }$ and the damping ratio $\zeta$ are found to be

$$\omega_ {n} = 1 0, \quad \zeta = 0. 1$$

The frequency actually observed in the vibration is the damped natural frequency $\omega _ { d } .$

$$\omega_ {d} = \omega_ {n} \sqrt {1 - \zeta^ {2}} = 1 0 \sqrt {1 - 0 . 0 1} = 9. 9 5 \mathrm{rad/sec}$$

In the present analysis, is given as zero. Thus, solutionx  (0) $x ( t )$ can be written as

$$x (t) = x (0) e ^ {- \zeta \omega_ {n} t} \left(\cos \omega_ {d} t + \frac {\zeta}{\sqrt {1 - \zeta^ {2}}} \sin \omega_ {d} t\right)$$

It follows that at $t = n T$ , where $T = 2 \pi / \omega _ { d }$ ,

$$x (n T) = x (0) e ^ {- \zeta \omega_ {n} n T}$$

Consequently, the amplitude four cycles later becomes
