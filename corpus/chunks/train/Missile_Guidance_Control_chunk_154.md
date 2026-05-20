Scintillation Noise: Scintillation is a phenomenon similar to glint, in that reflections from various parts of the aircraft (e.g., target) interfere. In the case of scintillation, this affects the amplitude of the received signal. Typically, an aircraft is composed of many individual conducting surfaces, or scatterers, each with different scattering properties that vary as the viewing or striking angle changes. In addition, multiple or sequential reflections of the radiated signal may occur between the various scatterers. These features can strongly affect the resultant value of the target aircraft’s radar cross section $( R C S ) ^ { * }$ signature. The large-amplitude fluctuation of an RCS signature with respect to small changes in the viewing angle is referred to as scintillation. In general, the amount of scintillation decreases as the wavelength increases. The presence of interference in the returned signal causes a modulation of the returned signal amplitude. In conical scan systems, any component of amplitude scintillation at or near the system scan frequency will be interpreted by the system as a signal resulting from an off-axis target. For this reason, frequency components of amplitude scintillation near the scan frequency will drive the radar off target. Note, however, that this effect is absent from monopulse radar systems, which do not extract information from modulation frequencies. Scintillation errors can be modeled in the same manner as glint errors, with the exception of the form of the standard deviation. For scintillation, the standard deviation is given by

$$\sigma_ {s} = \frac {B \sqrt {W (\omega_ {g}) B _ {n}}}{E}, \tag {3.87g}$$

where

$$B = \text { beamwidth },B _ {n} = \text { equivalent bandwidth for the noise of the tracking loop },E = \text { error slope },W (\omega_ {g}) = \frac {1}{2 \pi} \frac {\omega_ {g}}{\omega_ {g} ^ {2} + \omega_ {s} ^ {2}}.$$

In the above equation, $\omega _ { g }$ is the glint half-power frequency, and $\omega _ { s }$ is the scan frequency. As for the glint error, the correlation coefficient is given by

$$\rho = \exp (- \omega_ {g} \cdot \Delta T),$$

and the standard deviation of the correlated output by the relation

$$\sigma_ {c} = \sigma (1 - \rho^ {2}) ^ {1 / 2}.$$
