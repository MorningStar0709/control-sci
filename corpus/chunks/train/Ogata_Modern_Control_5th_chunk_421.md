First rewrite the sinusoidal transfer function $G ( j \omega ) H ( j \omega )$ as a product of basic factors discussed above.Then identify the corner frequencies associated with these basic factors. Finally, draw the asymptotic log-magnitude curves with proper slopes between the corner frequencies. The exact curve, which lies close to the asymptotic curve, can be obtained by adding proper corrections.

The phase-angle curve of $G ( j \omega ) H ( j \omega )$ can be drawn by adding the phase-angle curves of individual factors.

The use of Bode diagrams employing asymptotic approximations requires much less time than other methods that may be used for computing the frequency response of a transfer function. The ease of plotting the frequency-response curves for a given transfer function and the ease of modification of the frequency-response curve as compensation is added are the main reasons why Bode diagrams are very frequently used in practice.

$$G (j \omega) = \frac {1 0 (j \omega + 3)}{(j \omega) (j \omega + 2) [ (j \omega) ^ {2} + j \omega + 2 ]}$$

Make corrections so that the log-magnitude curve is accurate.

To avoid any possible mistakes in drawing the log-magnitude curve, it is desirable to put $G ( j \omega )$ in the following normalized form, where the low-frequency asymptotes for the first-order factors and the second-order factor are the 0-dB line:

$$G (j \omega) = \frac {7 . 5 \left(\frac {j \omega}{3} + 1\right)}{(j \omega) \left(\frac {j \omega}{2} + 1\right) \left[ \frac {(j \omega) ^ {2}}{2} + \frac {j \omega}{2} + 1 \right]}$$

This function is composed of the following factors:

$$7. 5, \quad (j \omega) ^ {- 1}, \quad 1 + j \frac {\omega}{3}, \quad \left(1 + j \frac {\omega}{2}\right) ^ {- 1}, \quad \left[ 1 + j \frac {\omega}{2} + \frac {(j \omega) ^ {2}}{2} \right] ^ {- 1}$$

The corner frequencies of the third, fourth, and fifth terms are $\omega = 3 , \omega = 2$ , and $\omega = \sqrt { 2 }$ , respectively. Note that the last term has the damping ratio of 0.3536.
