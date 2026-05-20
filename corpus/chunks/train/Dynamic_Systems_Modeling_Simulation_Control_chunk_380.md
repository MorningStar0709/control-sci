Equation (7.66) is our “standard form” for an LTI second-order I/O equation. Recall that we are able to put any LTI first-order I/O equation into the standard form of Eq. (7.25) and consequently identify the time constant ??, which is the important parameter for a first-order system response. Likewise, we can put any LTI secondorder I/O equation into the standard form of Eq. (7.66) and identify the damping ratio $\zeta$ and the undamped natural frequency $\omega _ { n } .$ , which are the two important parameters for an underdamped second-order system response.

When the system is undamped $( \zeta = 0 )$ or underdamped $( 0 < \zeta < 1 )$ , we can write the characteristic roots in terms of $\zeta$ and $\omega _ { n }$ by using Eq. (7.63) with $a _ { 1 } = 2 \zeta \omega _ { n }$ and $a _ { 0 } = \omega _ { n } ^ { 2 } .$ , and the resulting complex roots are

$$r = - \zeta \omega_ {n} \pm j \omega_ {n} \sqrt {1 - \zeta^ {2}} \tag {7.67}$$

Hence the product $- \zeta \omega _ { n }$ is the real part of the two complex roots, and $\omega _ { n } \sqrt { 1 - \zeta ^ { 2 } }$ is the imaginary part of the two complex roots. Recall that Eq. (7.58) describes the free response of an underdamped system (Case 3), where the real part of the roots determines the “exponential envelope” while the imaginary part determines the frequency of oscillation. Therefore, the free response of an underdamped system is

$$y _ {H} (t) = K e ^ {- \zeta \omega_ {n} t} \cos (\omega_ {d} t + \phi) \tag {7.68}$$

where $\omega _ { d } = \omega _ { n } \sqrt { 1 - \zeta ^ { 2 } }$ is called the damped frequency (rad/s). It is important to note that an underdamped system oscillates at frequency $\omega _ { d }$ when damping is present $( \mathrm { i . e . , 0 < \zeta < 1 } )$ , and that a second-order response oscillates at frequency $\omega _ { n }$ only when there is no damping $( \mathrm { i . e . , } \zeta = 0 )$ .

Figure 7.17 shows two complex conjugate roots in the complex plane. Note the right triangle formed by leg $A = \zeta \omega _ { n }$ (magnitude of real part) and leg $B = \omega _ { d } = \omega _ { n } \sqrt { 1 - \zeta ^ { 2 } }$ (magnitude of imaginary part). The distance from either root to the origin is the undamped natural frequency, as demonstrated by the length of the hypotenuse C

![](image/54468f7239b39ee3256bb73e80f1e6e360367b4f34e533626689f3f5f84cdc9b.jpg)

<details>
<summary>text_image</summary>

Roots: r = -ζωₙ ± jωₙ√(1 - ζ²)
Imaginary
jωₐ
B
C
θ
-ζωₙ
A
0
Real
-jωₐ
</details>
