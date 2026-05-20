then the steady-state error for following a ramp input can be made equal to zero. Note that, if there are any variations in the values of $\zeta$ and/or $\omega _ { n }$ due to environmental changes or aging, then a nonzero steady-state error for a ramp response may result.

A–5–26. Consider the stable unity-feedback control system with feedforward transfer function $G ( s )$ . Suppose that the closed-loop transfer function can be written

$$\frac {C (s)}{R (s)} = \frac {G (s)}{1 + G (s)} = \frac {\left(T _ {a} s + 1\right) \left(T _ {b} s + 1\right) \cdots \left(T _ {m} s + 1\right)}{\left(T _ {1} s + 1\right) \left(T _ {2} s + 1\right) \cdots \left(T _ {n} s + 1\right)} \quad (m \leq n)$$

Show that

$$\int_ {0} ^ {\infty} e (t) d t = \left(T _ {1} + T _ {2} + \dots + T _ {n}\right) - \left(T _ {a} + T _ {b} + \dots + T _ {m}\right)$$

where $e ( t ) = r ( t ) - c ( t )$ is the error in the unit-step response. Show also that

$$\frac {1}{K _ {v}} = \frac {1}{\lim _ {s \rightarrow 0} s G (s)} = \left(T _ {1} + T _ {2} + \dots + T _ {n}\right) - \left(T _ {a} + T _ {b} + \dots + T _ {m}\right)$$

Solution. Let us define

$$\left(T _ {a} s + 1\right) \left(T _ {b} s + 1\right) \dots \left(T _ {m} s + 1\right) = P (s)$$

and

$$(T _ {1} s + 1) (T _ {2} s + 1) \dots (T _ {n} s + 1) = Q (s)$$

Then

$$\frac {C (s)}{R (s)} = \frac {P (s)}{Q (s)}$$

and

$$E (s) = \frac {Q (s) - P (s)}{Q (s)} R (s)$$

For a unit-step input, R(s)=1/s and

$$E (s) = \frac {Q (s) - P (s)}{s Q (s)}$$

Since the system is stable, $\textstyle \int _ { 0 } ^ { \infty } e ( t )$ converges to a constant value. Noting thatdt

$$\int_ {0} ^ {\infty} e (t) d t = \lim _ {s \rightarrow 0} s \frac {E (s)}{s} = \lim _ {s \rightarrow 0} E (s)$$

we have

$$
\begin{array}{l} \int_ {0} ^ {\infty} e (t) d t = \lim _ {s \rightarrow 0} \frac {Q (s) - P (s)}{s Q (s)} \\ = \lim _ {s \rightarrow 0} \frac {Q ^ {\prime} (s) - P ^ {\prime} (s)}{Q (s) + s Q ^ {\prime} (s)} \\ = \lim _ {s \rightarrow 0} \left[ Q ^ {\prime} (s) - P ^ {\prime} (s) \right] \\ \end{array}
$$

Since

$$
\begin{array}{l} \lim _ {s \rightarrow 0} P ^ {\prime} (s) = T _ {a} + T _ {b} + \dots + T _ {m} \\ \lim _ {s \rightarrow 0} Q ^ {\prime} (s) = T _ {1} + T _ {2} + \dots + T _ {n} \\ \end{array}
$$

we have

$$\int_ {0} ^ {\infty} e (t) d t = \left(T _ {1} + T _ {2} + \dots + T _ {n}\right) - \left(T _ {a} + T _ {b} + \dots + T _ {m}\right)$$

For a unit-step input r(t), since

$$\int_ {0} ^ {\infty} e (t) d t = \lim _ {s \rightarrow 0} E (s) = \lim _ {s \rightarrow 0} \frac {1}{1 + G (s)} R (s) = \lim _ {s \rightarrow 0} \frac {1}{1 + G (s)} \frac {1}{s} = \frac {1}{\lim _ {s \rightarrow 0} s G (s)} = \frac {1}{K _ {v}}$$

we have

$$\frac {1}{K _ {v}} = \frac {1}{\lim _ {s \rightarrow 0} s G (s)} = \left(T _ {1} + T _ {2} + \dots + T _ {n}\right) - \left(T _ {a} + T _ {b} + \dots + T _ {m}\right)$$

Note that zeros in the left half-plane (that is, positive $T _ { a } , T _ { b } , \dots , T _ { m } )$ will improve $K _ { v }$ . Poles close to the origin cause low velocity-error constants unless there are zeros nearby.
