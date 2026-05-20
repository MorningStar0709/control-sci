# PROBLEMS

6.1 Consider the indirect continuous-time self-tuning controller in Example 3.6. Collect all equations that describe the self-tuner, and show that

they can be written in the form

$$\frac {d \xi}{d t} = A (\vartheta) \xi + B (\vartheta) u _ {c}\binom{e}{\varphi} = C (\vartheta) \xi + D (\vartheta) u _ {c}\vartheta = \chi (\theta)\frac {d \theta}{d t} = P \varphi e\frac {d P}{d t} = \alpha P - P \varphi \varphi^ {T} P$$

Give explicit expressions for all components of the vectors $\xi, \varphi, \vartheta$ , and $\theta$ and the matrix $P$ .

6.2 Consider a system with unknown gain whose transfer function is SPR. Show that a closed-loop system that is insensitive to variations in the gain is easily obtained by applying proportional feedback. Carry out a detailed analysis for the case in which the transfer function is $G(s) = 1/(s + 1)$ .

6.3 Consider an MRAS for adjustment of a feedforward gain. Assume that the system is designed on the basis of the assumption that the process dynamics are

$$G (s) = \frac {a}{s + a}$$

(a) Investigate the behavior of the systems obtained with the SPR and MIT rules when the real system has the transfer function

$$G (s) = \frac {a b ^ {2}}{(s + a) (s + b) ^ {2}}$$

Determine in particular which frequency ranges give stable adaptation rules for sinusoidal command signals.

(b) Consider the MRAS based on the SPR rule when the reference signal is constant and when an additional constant load disturbance is acting on the input of the process. Investigate how the load disturbance influences the stationary point of the total system. Investigate the local stability properties through linearization.

6.4 Consider an MRAS for adjustment of a feedforward gain based on the MIT rule. Let the command signal be

$$u _ {c} = a _ {1} \sin \omega_ {1} t + a _ {2} \sin \omega_ {2} t$$

and assume that the process has the transfer function

$$G (s) = \frac {1}{(s + 1) ^ {3}}$$

Derive conditions for the closed-loop system to be stable.

6.5 Consider Theorem 6.7. Generalize the results to cover the case in which the polynomial $B^{*}$ has isolated zeros on the unit circle.

6.6 Consider the system described by

$$y (t) = u (t \quad d)$$

Assume that a direct adaptive control (e.g., with $A_{o}^{*} = A_{m}^{*} = 1$ ) is designed according to the assumption that d = 1. Investigate how this controller behaves when applied to a system with d = 2.

6.7 Construct a proof analogous to Theorem 6.7 for continuous-time systems.
