$$y _ {\mathrm{ss}} (t) = | G (j \omega) | e ^ {j \phi} U (j \omega) e ^ {j \omega t} = | G (j \omega) | U (j \omega) e ^ {j (\omega t + \phi)} \tag {9.15}$$

Expanding the exponential function using Euler’s formula yields

$$y _ {\mathrm{ss}} (t) = | G (j \omega) | U (j \omega) \left[ \cos (\omega t + \phi) + j \sin (\omega t + \phi) \right] \tag {9.16}$$

Recall that $U ( j \omega )$ is a complex function of ?? and that the frequency response $y _ { \mathrm { s s } } ( t )$ is a real-valued function of time. If the input is a sine function, $u ( t ) = U _ { 0 }$ sin ??t, then we use the imaginary part of the bracketed term in Eq. (9.16) and the steady-state output is also a sine function:

$$y _ {\mathrm{ss}} (t) = | G (j \omega) | U _ {0} \sin (\omega t + \phi) \tag {9.17}$$

If the input is a cosine function, $u ( t ) = U _ { 0 }$ cos ??t, then we use the real part in Eq. (9.16)

$$y _ {\mathrm{ss}} (t) = | G (j \omega) | U _ {0} \cos (\omega t + \phi) \tag {9.18}$$

Let us summarize the key points of the frequency response:

1. Equation (9.17) is the frequency response of the LTI system shown in Fig. 9.1 when the input is a sine function, or $u ( t ) = U _ { 0 }$ sin ??t. Equation (9.18) is the frequency response of the same LTI system when the input is a cosine function $u ( t ) = U _ { 0 }$ cos ??t. The frequency response $y _ { \mathrm { s s } } ( t )$ is a sinusoidal function with the same frequency ?? (or, period) as the input u(t).   
2. In either case (sine or cosine input) the frequency response is completely determined by the magnitude and phase of the sinusoidal transfer function G( j??).   
3. The frequency-response equation (9.17) or (9.18) is valid only if the transient response “dies out” at steady state. In other words, the poles of the transfer function G(s) must lie in the left-half of the complex plane.

We demonstrate the frequency response with the following examples.
