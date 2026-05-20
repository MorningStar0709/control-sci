# PROBLEMS

5.1 Consider the process

$$G (s) = \frac {1}{s (s + a)}$$

where a is an unknown parameter. Determine a controller that can give the closed-loop system

$$G _ {m} (s) = \frac {\omega^ {2}}{s ^ {2} + 2 \zeta \omega s + \omega^ {2}}$$

Determine model-reference adaptive controllers based on gradient and stability theory, respectively. (Compare Problem 3.2.)

5.2 Consider the simple MRAS in Fig. 5.4 with G = 1/s. Let the parameter adjustment law be Eq. (5.57) (i.e., of PI type). Determine the differential equation for $\theta$ , and discuss how $\gamma_{1}$ and $\gamma_{2}$ influence the convergence rate.

5.3 Consider a position servo described by

$$
\begin{array}{l} \frac {d v}{d t} = - a v + b u \\ \frac {d y}{d t} = v \\ \end{array}
$$

where parameters $a$ and $b$ are unknown. Assume that the control law

$$u = \theta_ {1} (u _ {c} - y) - \theta_ {2} v$$

is used and that it is desired to control the system in such a way that the transfer function from command signal to process output is given by

$$G _ {m} (s) = \frac {\omega^ {2}}{s ^ {2} + 2 \zeta \omega s + \omega^ {2}}$$

Determine an adaptive control law that adjusts parameter $\theta_{1}$ and $\theta_{2}$ so that the desired objective is obtained.

5.4 An integrator

$$G _ {p} (s) = \frac {b}{s}$$

is to be controlled by a zero-order continuous-time controller

$$u (t) = s _ {0} y (t) + t _ {0} u _ {c} (t)$$

The desired response model is given by

$$G _ {m} (s) = \frac {b _ {m}}{s + a _ {m}}$$

Derive, using the Lyapunov theory, a parameter update law of an MRAS guaranteeing that the error $e = y - y_{m}$ goes to zero. Try the Lyapunov function

$$V (x) = \frac {1}{2} \left(e ^ {2} + \frac {1}{b} \left(b s _ {0} - a _ {m}\right) ^ {2} + \frac {1}{b} \left(b t _ {0} - b _ {m}\right) ^ {2}\right)$$

where

$$e (t) = y (t) - y _ {m} (t)$$

5.5 Consider the problem of adaptation of a feedforward gain in Example 5.1 when

$$G (s) = \frac {1}{(s + 1) (s + 2)}$$

(a) Introduce the augmented error, and determine an MRAS based on stability theory.   
(b) Show that the derived adaptation law in part (a) gives a stable closed-loop system.

5.6 Determine conditions in which a second-order transfer function

$$G (s) = \frac {b _ {0} s ^ {2} + b _ {1} s + b _ {2}}{s ^ {2} + a _ {1} s + a _ {2}}$$

is strictly positive real.

5.7 Show that $B(s) / A(s)$ is SPR if $A(s)$ is a stable polynomial and the $B$ polynomial is the first row of the $P$ -matrix defined by the Lyapunov equation

$$\boldsymbol {A} ^ {T} \boldsymbol {P} + \boldsymbol {P A} = - \boldsymbol {Q}$$
