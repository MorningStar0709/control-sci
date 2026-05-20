# 6–3 PLOTTING ROOT LOCI WITH MATLAB

In this section we present the MATLAB approach to the generation of root-locus plots and finding relevant information from the root-locus plots.

Plotting Root Loci with MATLAB. In plotting root loci with MATLAB we deal with the system equation given in the form of Equation (6–11), which may be written as

$$1 + K \frac {\mathrm{num}}{\mathrm{den}} = 0$$

where num is the numerator polynomial and den is the denominator polynomial. That is,

$$
\begin{array}{l} \mathrm{num} = (s + z _ {1}) (s + z _ {2}) \dots (s + z _ {m}) \\ = s ^ {m} + \left(z _ {1} + z _ {2} + \dots + z _ {m}\right) s ^ {m - 1} + \dots + z _ {1} z _ {2} \dots z _ {m} \\ \mathrm{den} = (s + p _ {1}) (s + p _ {2}) \dots (s + p _ {n}) \\ = s ^ {n} + \left(p _ {1} + p _ {2} + \dots + p _ {n}\right) s ^ {n - 1} + \dots + p _ {1} p _ {2} \dots p _ {n} \\ \end{array}
$$

Note that both vectors num and den must be written in descending powers of s.

A MATLAB command commonly used for plotting root loci is

$$r l o c u s (n u m, d e n)$$

Using this command, the root-locus plot is drawn on the screen.The gain vector K is automatically determined. (The vector K contains all the gain values for which the closedloop poles are to be computed.)

For the systems defined in state space, rlocus(A,B,C,D) plots the root locus of the system with the gain vector automatically determined.

Note that commands

$$\text { rlocus(num,den,K) } \quad \text { and } \quad \text { rlocus(A,B,C,D,K) }$$

use the user-supplied gain vector K.

If it is desired to plot the root loci with marks $" _ { 0 } \cdot$ or $^ { 1 } \mathrm { x } ^ { 1 }$ , it is necessary to use the following command:

$$r = r \text { locus } (\text { num }, \text { den })\text { plot } (r, ^ {\prime} o ^ {\prime}) \quad \text { or } \quad \text { plot } (r, ^ {\prime} x ^ {\prime})$$

Plotting root loci using marks o or x is instructive, since each calculated closed-loop pole is graphically shown; in some portion of the root loci those marks are densely placed and in another portion of the root loci they are sparsely placed. MATLAB supplies its own set of gain values used to calculate a root-locus plot. It does so by an internal adaptive stepsize routine.Also, MATLAB uses the automatic axis-scaling feature of the plot command.
