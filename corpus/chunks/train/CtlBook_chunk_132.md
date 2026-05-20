# 5.4 Frequency Response

Another important way to analyze systems is in the frequency domain. In particular, we are interested in the steady state response when the system is driven by sinusoids of diering frequencies.

Drawing frequency response plots by hand is still an important skill for control engineers. Hand drawing skill enables much deeper engineering insight into the behavior of systems and enables design work in a meeting or at the white-board. A hand sketch done prior to a computer plot gives you condence that you entered everything correctly to generate the plot. Of course, our emphasis in hand drawing is a balance favoring quick results which accurately plot the major qualitative features of the system. When detailed accuracy is required (later in the engineering cycle) we rely on the computer.

When a system is driven by a sinusoidal input, the output is derived by multiplying the Laplace transform of the sinusoid with the transfer function. For example:

$$x (t) = \sin (\omega t) \Leftrightarrow X (s) = \frac {\omega}{s ^ {2} + \omega^ {2}}Y (s) = \frac {\omega}{s ^ {2} + \omega^ {2}} G (s)$$

The pole corresponding to the sinusoidal input is the root of $s ^ { 2 } + \omega ^ { 2 }$ which is $s = j \omega$ . Since the magnitude of sin(ωt) is always 1 (i.e. does not vary with frequency, ω), the key quantity of interest is the magnitude of the transfer function, $| G ( j \omega )$ |(which does vary with frequency). If the amplitude of the input sinusoid changes from

$$\sin (\omega t) \rightarrow A \sin (\omega t)$$

The frequency response can simply be scaled by A due to the linearity property.

$$| Y (j \omega) | = | G (j \omega) | \rightarrow | Y (j \omega) | = | A G (j \omega) | = A | G (j \omega) |$$

Thus we can focus on $| G ( j \omega ) |$ and get the response for any amplitude or frequency sinusoid.

We can show that the steady state output is also a sinusoid using the partial fraction expansion as we did above with the step response. Suppose

$$Y (s) = \frac {\omega}{s ^ {2} + \omega^ {2}} \frac {M}{(s + p _ {1}) (s + p _ {2}) (s + p _ {3})}$$

Then the partial fraction expansion would be

$$Y (s) = \frac {A _ {0}}{s ^ {2} + \omega^ {2}} + \frac {A _ {1}}{(s + p _ {1})} + \frac {A _ {2}}{(s + p _ {2})} + \frac {A _ {3}}{(s + p _ {3})}$$

The last three terms each transform into exponentials like Equation 5.1. We assume that the real part of each pole is negative so that the exponentials decay with time. We can thus neglect those terms since we are focused only on the steady state solution:

$$Y (s) = \frac {A _ {0}}{s ^ {2} + \omega^ {2}}y (t) = \frac {A}{\omega} \sin (\omega t + \phi)$$

Where A and ϕ are quantities to be determined. This section is about ecient ways to determine how A and ϕ change as a function of ω.
