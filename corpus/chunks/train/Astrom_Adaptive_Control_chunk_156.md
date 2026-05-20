# EXAMPLE 3.3 Continuous-time system

The process discussed in Examples 3.1 and 3.2 has the transfer function

$$G (s) = \frac {b}{s (s + a)}$$

with a = 1 and b = 1. The design procedure given by Algorithm 3.1 will now be used to find a continuous-time controller. Since the process is of second order, the closed-loop system will be of third order and the minimum-degree controller is of first order. Polynomial $A_{m}$ has degree two, $B_{m}$ is a constant, and $A_{n}$ has degree one. We choose

$$A _ {o} (s) = s + a _ {o}$$

and let the desired response be specified by the transfer function.

$$\frac {B _ {m} (s)}{A _ {m} (s)} = \frac {\omega^ {2}}{s ^ {2} + 2 \zeta \omega s + \omega^ {2}}$$

The Diophantine equation (3.4) becomes

$$s (s + a) \left(s + r _ {1}\right) + b \left(s _ {0} s + s _ {1}\right) = \left(s ^ {2} + 2 \zeta \omega s + \omega^ {2}\right) \left(s + a _ {o}\right)$$

Equating coefficients of equal powers of $s$ gives the equations

$$a + r _ {1} = 2 \zeta \omega + a _ {0}a r _ {1} + b s _ {0} = \omega^ {2} + 2 \zeta \omega a _ {o}b s _ {1} = \omega^ {2} a _ {o}$$

If $b \neq 0$ , these equations can be solved, and we get

$$r _ {1} = 2 \zeta \omega + a _ {o} - as _ {0} = \frac {a _ {o} 2 \zeta \omega + \omega^ {2} - a r _ {1}}{b}s _ {1} = \frac {\omega^ {2} a _ {0}}{b}$$

Furthermore, we have $B^{+} = 1$ , $B^{-} = b$ , and $B_{m}' = \omega^{2} / b$ . It then follows from Eq. (3.12) that

$$T (s) = B _ {m} ^ {\prime} (s) A _ {o} (s) = \frac {\omega^ {2}}{b} (s + a _ {o})$$
