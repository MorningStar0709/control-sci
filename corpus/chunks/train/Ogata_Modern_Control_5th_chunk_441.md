Drawing Nyquist Plots with MATLAB. Nyquist plots, just like Bode diagrams, are commonly used in the frequency-response representation of linear, time-invariant, feedback control systems. Nyquist plots are polar plots, while Bode diagrams are rectangular plots. One plot or the other may be more convenient for a particular operation, but a given operation can always be carried out in either plot.

The MATLAB command nyquist computes the frequency response for continuoustime, linear, time-invariant systems.When invoked without left-hand arguments, nyquist produces a Nyquist plot on the screen.

The command

$$\text { nyquist(num,den) }$$

draws the Nyquist plot of the transfer function

$$G (s) = \frac {\operatorname{num} (s)}{\operatorname{den} (s)}$$

where num and den contain the polynomial coefficients in descending powers of s. Other commonly used nyquist commands are

$$
\begin{array}{l} \text { nyquist(num,den,w) } \\ \text { nyquist } (A, B, C, D) \\ \text { nyquist } (A, B, C, D, w) \\ \text { nyquist } (A, B, C, D, i u, w) \\ \text { nyquist(sys) } \\ \end{array}
$$

The command involving the user-specified frequency vector w, such as

$$\text { nyquist(num,den,w) }$$

calculates the frequency response at the specified frequency points in radians per second.

When invoked with left-hand arguments such as

$$
\begin{array}{l} [ \mathrm{re}, \mathrm{im}, \mathrm{w} ] = \text { nyquist } (\mathrm{num}, \mathrm{den}) \\ [ \mathrm{re}, \mathrm{im}, \mathrm{w} ] = \text { nyquist } (\mathrm{num}, \mathrm{den}, \mathrm{w}) \\ [ \mathrm{re}, \mathrm{im}, \mathrm{w} ] = \text { nyquist } (\mathrm{A}, \mathrm{B}, \mathrm{C}, \mathrm{D}) \\ [ \mathrm{re}, \mathrm{im}, \mathrm{w} ] = \text { nyquist } (\mathrm{A}, \mathrm{B}, \mathrm{C}, \mathrm{D}, \mathrm{w}) \\ [ \mathrm{re}, \mathrm{im}, \mathrm{w} ] = \text { nyquist } (\mathrm{A}, \mathrm{B}, \mathrm{C}, \mathrm{D}, \mathrm{iu}, \mathrm{w}) \\ [ \mathrm{re}, \mathrm{im}, \mathrm{w} ] = \text { nyquist(sys) } \\ \end{array}
$$

MATLAB returns the frequency response of the system in the matrices re, im, and w. No plot is drawn on the screen. The matrices re and im contain the real and imaginary parts of the frequency response of the system, evaluated at the frequency points specified in the vector w. Note that re and im have as many columns as outputs and one row for each element in w.
