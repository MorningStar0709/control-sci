$$
\begin{array}{l} y _ {\mathrm{ss}} (t) = X \left| G (j \omega) \right| \frac {e ^ {j (\omega t + \phi)} - e ^ {- j (\omega t + \phi)}}{2 j} \\ = X \left| G (j \omega) \right| \sin (\omega t + \phi) \\ = Y \sin (\omega t + \phi) \tag {7-5} \\ \end{array}
$$

Figure 7–2 Input and output sinusoidal signals.   
![](image/ddf9cde984f0cc852695ef6eda78aa5a52396987ffca61b253f0baf4135a8471.jpg)

<details>
<summary>text_image</summary>

Input x(t) = X sin ωt
X
Y
Output y(t) = Y sin (ωt + φ)
</details>

where $Y = X { \big | } G ( j \omega ) { \big | }$ @. We see that a stable, linear, time-invariant system subjected to a sinusoidal input will, at steady state, have a sinusoidal output of the same frequency as the input. But the amplitude and phase of the output will, in general, be different from those of the input. In fact, the amplitude of the output is given by the product of that of the input and $\left| G ( j \omega ) \right.$ @, while the phase angle differs from that of the input by the amount $\phi = \mathit { \Pi } / G ( j \omega )$ An example of input and output sinusoidal signals is shown in Figure 7–2..

On the basis of this, we obtain this important result: For sinusoidal inputs,

$$
\left| G (j \omega) \right| = \left| \frac {Y (j \omega)}{X (j \omega)} \right| = \begin{array}{l} \text { amplitude   ratio   of   the   output   sinusoid   to   the } \\ \text { input   sinusoid } \end{array}

\underline {{G (j \omega)}} = \left\lfloor \frac {Y (j \omega)}{X (j \omega)} = \begin{array}{l} \text { phase   shift   of   the   output   sinusoid   with   respect } \\ \text { to   the   input   sinusoid } \end{array} \right.
$$

Hence, the steady-state response characteristics of a system to a sinusoidal input can be obtained directly from

$$\frac {Y (j \omega)}{X (j \omega)} = G (j \omega)$$

The function $G ( j \omega )$ is called the sinusoidal transfer function. It is the ratio of $Y ( j \omega )$ to $X ( j \omega )$ , is a complex quantity, and can be represented by the magnitude and phase angle with frequency as a parameter.The sinusoidal transfer function of any linear system is obtained by substituting jv for s in the transfer function of the system.

As already mentioned in Chapter 6,a positive phase angle is called phase lead,and a negative phase angle is called phase lag.A network that has phase-lead characteristics is called a lead network, while a network that has phase-lag characteristics is called a lag network.
