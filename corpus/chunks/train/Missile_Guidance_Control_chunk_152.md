Glint: Glint, or angle noise, is the phenomenon in which interference by two or more sources causes a distortion in the shape of the propagating wavefront. The effect of this distortion is to change the apparent angle of arrival of the wavefront. This appears to the tracking system as a wander of the apparent target location from its true location. Thus, glint is a target-induced error term that introduces an angular error in the target tracker. The apparent center of the target moves along the length of the target and can occasionally exceed the target dimension. Furthermore, the apparent location of the target may lie outside of the target a significant amount of time. (Note that the phenomenon of glint is also known as the radar bright spot wander.) Since glint is a distance error along the target, the equivalent angular error varies as $1 / R _ { m t }$ , where $R _ { m t }$ is the total missile-to-target range. Glint is usually described as a Gaussian random variable whose main value is at the center of the target and whose standard deviation (σ ) depends on the target span, perpendicular to the LOS angle. A typical value for the standard deviation of correlated glint for an aircraft is

$$\sigma = 0. 2 5 S / R _ {m t}, \tag {3.87a}$$

where S is a characteristic length (or effective target length). The correlation coefficient is computed by

$$\rho = \exp (- \omega_ {g} \cdot \Delta T), \tag {3.87b}$$

where

$$\omega_ {g} = \text { the glint half - power frequency },\Delta T = \text { magnitude of time since last call. }$$

The standard deviation of the correlated glint error is then computed by the following relation:

$$\sigma_ {c} = \sigma \cdot (1 - \rho^ {2}) ^ {1 / 2}. \tag {3.87c}$$

The spectral density of glint error is maximum at zero hertz and decreases with upward concavity as frequency increases. The glint spectral density is commonly approximated with a Lorentzian lineshape as follows:

$$\Phi_ {g} (\omega) = \Phi_ {0} [ \omega_ {g} ^ {2} / (\omega^ {2} + \omega_ {g} ^ {2}) ], - \infty < \omega < \infty , \tag {3.87d}$$

where

$$\Phi_ {g} (\omega) = \text { spectral density },\Phi_ {0} = \text { zero - frequency value of the spectral density },\omega_ {g} = \text { glint half - power frequency }.$$

The glint half-power frequency is given by

$$\omega_ {g} = 4 \pi \Omega S / \lambda ,$$

where
