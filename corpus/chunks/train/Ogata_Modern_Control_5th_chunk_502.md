Once the corner frequencies are noted on the log-magnitude curve, the corresponding phaseangle curve for each component factor of the transfer function can easily be drawn. The sum of these component phase-angle curves is that of the assumed transfer function. The phase-angle curve for $G ( j \omega )$ is denoted by in Figure 7–88. From Figure 7–88, we clearly notice a dis-/G crepancy between the computed phase-angle curve and the experimentally obtained phaseangle curve. The difference between the two curves at very high frequencies appears to be a constant rate of change. Thus, the discrepancy in the phase-angle curves must be caused by transport lag.

Hence, we assume the complete transfer function to be $G ( s ) e ^ { - T s }$ . Since the discrepancy between the computed and experimental phase angles is –0.2v rad for very high frequencies, we can determine the value of T as follows:

$$\lim _ {\omega \rightarrow \infty} \frac {d}{d \omega} \underline {{{\left\lfloor G (j \omega) e ^ {- j \omega T} \right.}}} = - T = - 0. 2$$

or

$$T = 0. 2 \mathrm{sec}.$$

The presence of transport lag can thus be determined, and the complete transfer function determined from the experimental curves is

$$G (s) e ^ {- T s} = \frac {3 2 0 (s + 2) e ^ {- 0 . 2 s}}{s (s + 1) \left(s ^ {2} + 8 s + 6 4\right)}$$
