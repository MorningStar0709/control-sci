Obtaining Steady-State Outputs to Sinusoidal Inputs. We shall show that the steady-state output of a transfer function system can be obtained directly from the sinusoidal transfer function—that is, the transfer function in which s is replaced by jv, where v is frequency.

Consider the stable,linear,time-invariant system shown in Figure 7–1.The input and output of the system, whose transfer function is $G ( s )$ ,are denoted by $x ( t )$ and $y ( t )$ , respectively. If the input $x ( t )$ is a sinusoidal signal, the steady-state output will also be a sinusoidal signal of the same frequency, but with possibly different magnitude and phase angle.

Let us assume that the input signal to the system is given by

$$x (t) = X \sin \omega t$$

[In this book $" \omega ^ { \ast }$ is always measured in rad/sec. When the frequency is measured in cycle/sec, we use notation $^ { 6 6 } f ^ { , 9 }$ . That is, $\omega = 2 \pi f . ]$

Suppose that the transfer function $G ( s )$ of the system can be written as a ratio of two polynomials in $s ;$ that is,

$$G (s) = \frac {p (s)}{q (s)} = \frac {p (s)}{(s + s _ {1}) (s + s _ {2}) \cdots (s + s _ {n})}$$

The Laplace-transformed output $Y ( s )$ of the system is then

$$Y (s) = G (s) X (s) = \frac {p (s)}{q (s)} X (s) \tag {7-1}$$

where $X ( s )$ is the Laplace transform of the input $x ( t )$ .

It will be shown that, after waiting until steady-state conditions are reached, the frequency response can be calculated by replacing s in the transfer function by $j \omega .$ It will also be shown that the steady-state response can be given by

$$G (j \omega) = M e ^ {j \phi} = M \underline {{\phi}}$$

where M is the amplitude ratio of the output and input sinusoids and $\phi$ is the phase shift between the input sinusoid and the output sinusoid. In the frequency-response test, the input frequency v is varied until the entire frequency range of interest is covered.

The steady-state response of a stable, linear, time-invariant system to a sinusoidal input does not depend on the initial conditions. (Thus, we can assume the zero initial condition.) If Y(s) has only distinct poles, then the partial fraction expansion of Equation (7–1) when $x ( t ) = X$ yieldssin vt

$$
\begin{array}{l} Y (s) = G (s) X (s) = G (s) \frac {\omega X}{s ^ {2} + \omega^ {2}} \\ = \frac {a}{s + j \omega} + \frac {\bar {a}}{s - j \omega} + \frac {b _ {1}}{s + s _ {1}} + \frac {b _ {2}}{s + s _ {2}} + \dots + \frac {b _ {n}}{s + s _ {n}} \tag {7-2} \\ \end{array}
$$
