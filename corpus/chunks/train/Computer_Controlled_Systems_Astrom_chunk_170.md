# Example 3.3 Frequency responses

Consider the continuous-time system

$$G (s) = \frac {1}{s ^ {2} + 1 . 4 s + 1} \tag {3.6}$$

Zero-order-hold sampling of the system with h = 0.4 gives the discrete-time system

$$H (z) = \frac {0 . 0 6 6 z + 0 . 0 5 5}{z ^ {2} - 1 . 4 5 0 z + 0 . 5 7 1}$$

The frequency curve is given by $H(e^{i\omega h})$ . Figure 3.3 shows the Nyquist diagram and Fig 3.4 shows the Bode diagram for the continuous-time system and for the discrete-time system. The difference between the continuous-time and discrete-time frequency curves will decrease when the sampling period is decreased. The connection between the frequency curves of the discrete-time and continuous-time systems is further discussed in Sec. 7.7.
