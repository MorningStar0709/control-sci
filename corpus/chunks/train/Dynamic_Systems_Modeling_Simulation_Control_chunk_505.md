(b)   
Figure 9.30 Vibration isolation system: (a) instrument with vibration mounts and (b) representative mechanical system.

$$x _ {\mathrm{ss}} (t) = | G (j \omega) | U _ {0} \sin (\omega t + \phi) \mathrm{m} \tag {9.55}$$

where $\boldsymbol { G } ( s ) = \boldsymbol { X } ( s ) / X _ { b } ( s )$ is the transfer function relating the output (mass displacement x) to the input (base displacement $x _ { b } )$ . Because the amplitude of the mass displacement in Eq. (9.55) is $| G ( j \omega ) | U _ { 0 }$ and the amplitude of the base input is $U _ { 0 } .$ , the output-to-input amplitude ratio (or transmissibility) is $| G ( j \omega ) |$ . Hence, the magnitude plot of a Bode diagram essentially tells us the transmissibility of a system.

For example, let us plot the transmissibility of the simple vibration isolation system shown in Fig. 9.30b. Applying Newton’s laws to a free-body diagram of the mass–spring–damper system, we can derive the following mathematical model

$$m \ddot {x} + b (\dot {x} - \dot {x} _ {b}) + k (x - x _ {b}) = 0 \tag {9.56}$$

which can be rewritten with the input terms (base motion) on the right-hand-side

$$m \ddot {x} + b \dot {x} + k x = b \dot {x} _ {b} + k x _ {b} \tag {9.57}$$

Using either the D-operator or Laplace-transform methods we obtain the transfer function of the vibration isolation system:

$$G (s) = \frac {X (s)}{X _ {b} (s)} = \frac {b s + k}{m s ^ {2} + b s + k} = \frac {(b / m) s + (k / m)}{s ^ {2} + (b / m) s + (k / m)} \tag {9.58}$$

The sinusoidal transfer function is obtained by substituting $s = j \omega$ into Eq. (9.58)

$$G (j \omega) = \frac {(b / m) j \omega + (k / m)}{- \omega^ {2} + (b / m) j \omega + (k / m)} \tag {9.59}$$

Because the vibration isolator is a mass–spring–damper system, we can substitute the standard second-order system parameters $\omega _ { n } ^ { 2 } = k / m$ and $2 \zeta \omega _ { n } = b / m$ into Eq. (9.59)

$$G (j \omega) = \frac {\omega_ {n} ^ {2} + j 2 \zeta \omega_ {n} \omega}{\omega_ {n} ^ {2} - \omega^ {2} + j 2 \zeta \omega_ {n} \omega} \tag {9.60}$$

Dividing all terms in Eq. (9.60) by $\omega _ { n } ^ { 2 }$ we obtain

$$G (j \omega) = \frac {1 + j (2 \zeta \omega / \omega_ {n})}{1 - (\omega^ {2} / \omega_ {n} ^ {2}) + j (2 \zeta \omega / \omega_ {n})} \tag {9.61}$$

We can simplify Eq. (9.61) by substituting the nondimensional parameter $\beta = \omega / \omega _ { n }$

$$G (j \omega) = \frac {1 + j 2 \zeta \beta}{1 - \beta^ {2} + j 2 \zeta \beta} \tag {9.62}$$
