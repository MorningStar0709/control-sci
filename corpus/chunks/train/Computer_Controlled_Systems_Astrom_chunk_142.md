# Example 2.16 Complex poles

Consider the continuous-time system

$$\frac {\omega_ {0} ^ {2}}{s ^ {2} + 2 \zeta \omega_ {0} s + \omega_ {0} ^ {2}} \tag {2.37}$$

The poles of the corresponding discrete-time system are given by the characteristic equation

$$z ^ {2} + a _ {1} z + a _ {2} = 0$$

where

$$a _ {1} = - 2 e ^ {- \zeta \omega_ {0} h} \cos \left(\sqrt {1 - \zeta^ {2}} \omega_ {0} h\right)a _ {2} = e ^ {- 2 \zeta \omega_ {0} h}$$

(Compare with Table 2.1.) Figure 2.7 shows the step responses of the discrete-time system for different values of the sampling interval when $\omega_0 = 1.83$ and $\zeta = 0.5$ . Figure 2.8 gives a more detailed picture of how the continuous-time poles of (2.37) are mapped into the unit circle for different values of $\zeta$ and $\omega_0h$ when the system is sampled.
