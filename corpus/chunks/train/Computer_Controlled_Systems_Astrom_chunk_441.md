# Predictive First-Order-Hold Sampling: An Input-Output Approach

The pulse-transfer function obtained by predictive first-order-hold sampling of a system with a transfer function $G(s)$ can also be obtained by a direct calculation. Figure 7.14 shows the inputs and the outputs of a system with predictive first-order-hold sampling. Let u be the input of the system and let y denote the output. The piecewise affine input u can be generated as the output of an integrator whose input is the piecewise constant signal

$$v (t) = \frac {u (k h + h) - u (k h)}{h} \tag {7.18}$$

Because this signal is constant over the sampling intervals, the results of Chapter 2 can be applied and we find that the z-transform of the output is given by

$$Y (z) = S _ {\mathrm{zoh}} \left(\frac {G (s)}{\mathrm{s}}\right) V (z) \tag {7.19}$$

where $S_{20h}$ denotes the map of transfer functions to pulse-transfer functions through zero-order-hold sampling. This operator is given by Eq. (2.30). Combining Eqs. (7.18) and (7.19) we get

$$Y (z) = S _ {\mathrm{zoh}} \left(\frac {G (s)}{s}\right) \frac {z - 1}{h} U (z)$$

We have thus obtained the input-output relation for sampling with a predictive first-order-hold that can be expressed as follows.

$$S _ {\mathrm{pfoh}} (G (s)) = \frac {z - 1}{h} S _ {\mathrm{zoh}} \left(\frac {G (s)}{s}\right) \tag {7.20}$$

By using Eq. (2.30) it follows that the pulse-transfer function obtained by the predictive first-order-hold sampling of a continuous system with the transfer function $G(s)$ can be expressed by

$$H (z) = \frac {(z - 1) ^ {2}}{z h} \frac {1}{2 \pi i} \int_ {\gamma - i \infty} ^ {\gamma + i \infty} \frac {e ^ {s h}}{z - e ^ {s h}} \frac {G (s)}{s ^ {2}} d s \tag {7.21}$$

We illustrate the results with an example.
