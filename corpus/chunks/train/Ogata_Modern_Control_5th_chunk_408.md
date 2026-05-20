# EXAMPLE 7–2 Consider the network given by

$$G (s) = \frac {s + \frac {1}{T _ {1}}}{s + \frac {1}{T _ {2}}}$$

Determine whether this network is a lead network or lag network.

For the sinusoidal input $x ( t ) = X$ sin vt, the steady-state output $y _ { \mathrm { s s } } ( t )$ can be found as follows: Since

$$G (j \omega) = \frac {j \omega + \frac {1}{T _ {1}}}{j \omega + \frac {1}{T _ {2}}} = \frac {T _ {2} (1 + T _ {1} j \omega)}{T _ {1} (1 + T _ {2} j \omega)}$$

we have

$$\left| G (j \omega) \right| = \frac {T _ {2} \sqrt {1 + T _ {1} ^ {2} \omega^ {2}}}{T _ {1} \sqrt {1 + T _ {2} ^ {2} \omega^ {2}}}$$

and

$$\phi = \underline {{{/ G (j \omega)}}} = \tan^ {- 1} T _ {1} \omega - \tan^ {- 1} T _ {2} \omega$$

Thus the steady-state output is

$$y _ {\mathrm{ss}} (t) = \frac {X T _ {2} \sqrt {1 + T _ {1} ^ {2} \omega^ {2}}}{T _ {1} \sqrt {1 + T _ {2} ^ {2} \omega^ {2}}} \sin (\omega t + \tan^ {- 1} T _ {1} \omega - \tan^ {- 1} T _ {2} \omega)$$

From this expression, we find that if $T _ { 1 } > T _ { 2 }$ then tan , $^ { - 1 } T _ { 1 } \omega - \tan ^ { - 1 } T _ { 2 } \omega > 0 .$ Thus, if. $T _ { 1 } > T _ { 2 }$ then the network is a lead network. If $T _ { 1 } < T _ { 2 }$ then the network is a lag network.,

Presenting Frequency-Response Characteristics in Graphical Forms. The sinusoidal transfer function, a complex function of the frequency v, is characterized by its magnitude and phase angle, with frequency as the parameter. There are three commonly used representations of sinusoidal transfer functions:

1. Bode diagram or logarithmic plot   
2. Nyquist plot or polar plot   
3. Log-magnitude-versus-phase plot (Nichols plots)

We shall discuss these representations in detail in this chapter. We shall include the MATLAB approach to obtain Bode diagrams, Nyquist plots, and Nichols plots.
