# EXAMPLE 6.3 Adaptation of a feedforward gain

In Example 5.1 we derived an adaptation law for adjusting the feedforward gain by using the MIT rule. The behavior of the system was illustrated in Fig. 5.3. The system is described by

$$\frac {d y}{d t} = k \hat {\theta} (t) u _ {c} (t) - y (t)$$

and the parameter adjustment rule is

$$\frac {d \hat {\theta}}{d t} = - \gamma y _ {m} (t) e (t) = - \gamma y _ {m} (t) (y (t) - y _ {m} (t))$$

Since the signal $y_{m}$ can be computed from the command signal $u_{c}$ , both $u_{c}$ and $y_{m}$ can thus be regarded as known time-varying signals. The adaptive system is described by the equation

$$
\frac {d}{d t} \binom {\hat {\theta}} {y} = \left( \begin{array}{c c} 0 & - \gamma y _ {m} (t) \\ k u _ {c} (t) & - 1 \end{array} \right) \binom {\hat {\theta}} {y} + \binom {\gamma y _ {m} ^ {2} (t)} {0} \tag {6.16}
$$

The system can thus be described by a time-varying linear differential equation of second order. In Fig. 6.5 we show three simulations for the case in which $G(s) = 1 / (s + 1)$ , $k = k_0 = 1$ , and $\gamma = 11$ . The reference signal is sinusoidal in all cases. The frequency is $\omega = 1$ in the first case, $\omega = 2$ in the second, and $\omega = 3$ in the third. The controller parameter converges to the correct value for $\omega = 1$ and $\omega = 3$ , but it diverges for $\omega = 2$ . We thus have a situation in which the system is stable for one input but unstable for another. The system is stable for low frequencies of the input signal. As the frequency increases, it becomes unstable. It becomes stable again as the frequency is increased further. This pattern repeats itself as the frequency is increased further.

Example 6.3 shows that the system has quite a complex behavior that cannot be explained by the intuitive argument of the previous section. To understand what is happening, we analyze the equations describing the system. Equation (6.16) can be written as

$$\frac {d x}{d t} = A (t) x + B (t) \tag {6.17}$$

This is a linear system with time-varying parameters. In the particular case in which the input $u_{c}$ is periodic and we connect the adaptation when model output $y_{m}$ has also become periodic, the system is also periodic. For such systems there is a well-developed theory that can be used to understand the behavior of the system.

![](image/b5e460f32d0c1c08e93d68eec6a59993c6da907edf3b0efb1f7dd2448881856d.jpg)  
Figure 6.5 Behavior of the controller gain for an MRAS using the MIT rule. The input signal is a unit amplitude sinusoidal with frequency (a) 1; (b) 2; and (c) 3 rad/s. The system has the transfer function $G(s) = 1/(s + 1)$ , the parameters are $k = k_{0} = 1$ , and the adaptation gain is $\gamma = 11$ . The dashed lines indicate the correct values of the gain.
