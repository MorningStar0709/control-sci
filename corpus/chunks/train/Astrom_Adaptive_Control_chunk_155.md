# EXAMPLE 3.2 Model-following without zero cancellation

Consider the same process as in Example 3.1, but use a control design in which there is no cancellation of the process zero. Since the process is of second order, the minimum-degree solution has polynomials R, S, and T of first order and the closed-loop system will be of third order. Since no zero is canceled, it follows from the compatibility condition in Algorithm 3.1 that $\deg A_{0} = 1$ . Since no process zeros are canceled, we have

$$\boldsymbol {B} ^ {+} = 1B ^ {-} = B = b _ {0} q + b _ {1}$$

It also follows from the compatibility conditions that the model must have the same zero as the process. The desired closed-loop transfer operator is thus

$$H _ {m} (q) = \beta \frac {b _ {0} q + b _ {1}}{q ^ {2} + a _ {m 1} q + a _ {m 2}} = \frac {b _ {m 0} q + b _ {m 1}}{q ^ {2} + a _ {m 1} q + a _ {m 2}}$$

where $b_{m0} = \beta b_0$ and

$$\beta = \frac {1 + a _ {m 1} + a _ {m 2}}{b _ {0} + b _ {1}}$$

which gives unit steady state gain. The Diophantine equation (3.4) becomes

$$(q ^ {2} + a _ {1} q + a _ {2}) (q + r _ {1}) + (b _ {0} q + b _ {1}) (s _ {0} q + s _ {1}) = (q ^ {2} + a _ {m 1} q + a _ {m 2}) (q + a _ {v}) \tag {3.19}$$

Putting $q = -b_{1} / b_{0}$ and solving for $r_{1}$ , we get

$$
\begin{array}{l} r _ {1} = \frac {b _ {1}}{b _ {0}} + \frac {\left(b _ {1} ^ {2} - a _ {m 1} b _ {0} b _ {1} + a _ {m 2} b _ {0} ^ {2}\right) \left(- b _ {1} + a _ {o} b _ {0}\right)}{b _ {0} \left(b _ {1} ^ {2} - a _ {1} b _ {0} b _ {1} + a _ {2} b _ {0} ^ {2}\right)} \\ = \frac {a _ {o} a _ {m 2} b _ {0} ^ {2} + (a _ {2} - a _ {m 2} - a _ {o} a _ {m 1}) b _ {0} b _ {1} + (a _ {o} + a _ {m 1} - a _ {1}) b _ {1} ^ {2}}{b _ {1} ^ {2} - a _ {1} b _ {0} b _ {1} + a _ {2} b _ {0} ^ {2}} \tag {3.20} \\ \end{array}
$$

Notice that the denominator is zero if polynomials $A(q)$ and $B(q)$ have a common factor. Equating coefficients of terms $q^{2}$ and $q^{0}$ in Eq. (3.19) gives

$$
\begin{array}{l} s _ {0} = \frac {b _ {1} \left(a _ {o} a _ {m 1} - a _ {2} - a _ {m 1} a _ {1} + a _ {1} ^ {2} + a _ {m 2} - a _ {1} a _ {o}\right)}{b _ {1} ^ {2} - a _ {1} b _ {0} b _ {1} + a _ {2} b _ {0} ^ {2}} \\ + \frac {b _ {0} \left(a _ {m 1} a _ {2} - a _ {1} a _ {2} - a _ {o} a _ {m 2} + a _ {o} a _ {2}\right)}{b _ {1} ^ {2} - a _ {1} b _ {0} b _ {1} + a _ {2} b _ {0} ^ {2}} \tag {3.21} \\ \end{array}
s _ {1} = \frac {b _ {1} \left(a _ {1} a _ {2} - a _ {m 1} a _ {2} + a _ {o} a _ {m 2} - a _ {o} a _ {2}\right)}{b _ {1} ^ {2} - a _ {1} b _ {0} b _ {1} + a _ {2} b _ {0} ^ {2}}+ \frac {b _ {0} \left(a _ {2} a _ {m 2} - a _ {2} ^ {2} - a _ {o} a _ {m 2} a _ {1} + a _ {o} a _ {2} a _ {m 1}\right)}{b _ {1} ^ {2} - a _ {1} b _ {0} b _ {1} + a _ {2} b _ {0} ^ {2}}
$$

Furthermore, it follows from Eq. (3.12) that

$$T (q) = \beta A _ {o} (q) = \beta (q + a _ {o})$$

Since the design method is purely algebraic, there is no difference between discrete-time systems and continuous-time systems. We illustrate this by an example.
