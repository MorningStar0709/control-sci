# 8.4 Frequency-Response Design Methods

This chapter has so far shown how continuous-time controllers can be translated into discrete-time forms. This section discusses how continuous-time frequency-design methods can be used to design discrete-time controllers.

Frequency-design methods based on Bode and Nichols plots are useful for designing compensators for systems described by transfer functions. The usefulness of the methods depends on the simplicity of drawing the Bode plots and on rules of thumb for choosing the compensators. The Bode plots are easy to draw because the transfer functions are in general rational functions in $i\omega$ , except for pure time delays. Frequency curves for discrete-time systems are more difficult to draw because the pulse-transfer functions are not rational functions in $i\omega$ , but in $\exp(i\omega h)$ . The w-transform method is one way to circumvent this difficulty. The method can be summarized into the following steps:

1. Sample the continuous-time system that should be controlled using a zero-order-hold circuit. This gives $H(z)$ .

2. Introduce the variable

$$w = \frac {2}{h} \frac {z - 1}{z + 1}$$

[compare (8.6)]. Transform the pulse-transfer function of the process into the w-plane giving

$$H ^ {\prime} (w) = H (z) \Bigg | _ {z = \frac {1 + w h / 2}{1 - w h / 2}}$$

For $z = \exp (i\omega h)$ then

$$w = i \frac {2}{h} \tan (\omega h / 2) = i v$$

(compare frequency prewarping in Sec.8.2). The transformed transfer function $H'(iv)$ is a rational function in $iv$ .

3. Draw the Bode plot of $H'(iv)$ and use conventional methods to design a compensator $H_c'(iv)$ that gives desired frequency domain properties. The distortion of the frequency scale between $v$ and $\omega$ must be taken into account when deciding, for instance, crossover frequency and bandwidth.

4. Transform the compensator back into the z-plane and implement $H_{c}(z)$ as a discrete-time system.

The advantage with the w-transform method is that conventional Bode diagram techniques can be used to make the design. One difficulty is to handle the distortion of the frequency scale and to choose the sampling interval.
