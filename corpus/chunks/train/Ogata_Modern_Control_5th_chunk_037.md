1. The transfer function of a system is a mathematical model in that it is an operational method of expressing the differential equation that relates the output variable to the input variable.   
2. The transfer function is a property of a system itself, independent of the magnitude and nature of the input or driving function.   
3. The transfer function includes the units necessary to relate the input to the output; however, it does not provide any information concerning the physical structure of the system. (The transfer functions of many physically different systems can be identical.)   
4. If the transfer function of a system is known, the output or response can be studied for various forms of inputs with a view toward understanding the nature of the system.   
5. If the transfer function of a system is unknown, it may be established experimentally by introducing known inputs and studying the output of the system. Once established, a transfer function gives a full description of the dynamic characteristics of the system, as distinct from its physical description.

Convolution Integral. For a linear, time-invariant system the transfer function $G ( s )$ is

$$G (s) = \frac {Y (s)}{X (s)}$$

where X(s) is the Laplace transform of the input to the system and Y(s) is the Laplace transform of the output of the system, where we assume that all initial conditions involved are zero. It follows that the output $Y ( s )$ can be written as the product of $G ( s )$ and X(s), or

$$Y (s) = G (s) X (s) \tag {2-1}$$

Note that multiplication in the complex domain is equivalent to convolution in the time domain (see Appendix A), so the inverse Laplace transform of Equation (2–1) is given by the following convolution integral:

$$
\begin{array}{l} y (t) = \int_ {0} ^ {t} x (\tau) g (t - \tau) d \tau \\ = \int_ {0} ^ {t} g (\tau) x (t - \tau) d \tau \\ \end{array}
$$

where both g(t) and x(t) are 0 for $t < 0$ .

Impulse-Response Function. Consider the output (response) of a linear timeinvariant system to a unit-impulse input when the initial conditions are zero. Since the Laplace transform of the unit-impulse function is unity, the Laplace transform of the output of the system is

$$Y (s) = G (s) \tag {2-2}$$

The inverse Laplace transform of the output given by Equation (2–2) gives the impulse response of the system. The inverse Laplace transform of G(s), or

$$\mathscr {L} ^ {- 1} [ G (s) ] = g (t)$$
