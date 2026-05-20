where $U(s)$ , $U_{c}(s)$ , and $Y(s)$ are the Laplace transforms of the input, reference, and output signals, respectively. The desired response of the closed-loop system is given by the transfer function

$$G _ {m} (s) = \frac {4 (s + 1)}{(s + 2) ^ {2}}$$

An MRAS has been designed, giving the parameter update law

$$\frac {d \theta}{d t} = - \gamma e (t) \left(\frac {1}{(p + 2) ^ {2}} u _ {c} (t)\right)$$

where $e = y - y_m$ .

(a) Find the equilibrium parameter set of the parameter update law, giving a parameter estimate that is constant for any reference input $u_{c}(t)$ . Give an expression for the averaged nonlinear differential equation of the parameter update law.

(b) Determine the local stability of the equilibrium parameter set for a sinusoidal reference signal $u_{c}(t) = \sin \omega t$ by examining the characteristic polynomial of the linear differential equation obtained by linearizing the averaged differential equation around the equilibrium parameter set. Determine for what frequencies the linearized equation is stable.

6.13 Formulate the averaging equation for a discrete-time algorithm corresponding to Eq. 6.49.

6.14 Consider discrete-time adaptive control of the system

$$y (t + 1) = a y (t) + b u t (t)$$

Derive an MRAS that gives a closed-loop system

$$y _ {m} (t + 1) = a _ {m} y _ {m} (t) + b _ {m} u _ {c} (t)$$

Use averaging methods to analyze the system when the command signal is a step and a sinusoid.

6.15 Consider Problem 6.14. Investigate the behavior of the system when the command signal is a step and when there is sinusoidal measurement noise.

6.16 Consider the MRAS given by Eqs. (6.57). Investigate the local behavior of the closed-loop system when the command signal is a sinusoid and the gradient method

$$\frac {d \hat {\theta}}{d t} = \gamma \varphi e$$

is replaced with a least-squares method of the form

$$\frac {d \hat {\theta}}{d t} = P \varphi e\frac {d P}{d t} = - P \varphi \varphi^ {T} P + \lambda P$$

6.17 Show that there is no constant-gain controller that can simultaneously stabilize the systems $G(s) = 1/(1 + s)$ and $G(s) = 1/(1 - s)$ .

6.18 Show that there is a fixed-gain controller that will simultaneously stabilize the systems $G(s) = 1 / (s + 1)$ and $G(s) = 1 / (s - 1)$ .
