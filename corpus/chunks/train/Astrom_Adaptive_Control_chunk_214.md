# EXAMPLE 4.3 Moving-average controller

Consider the system (4.1) with

$$
\begin{array}{l} A (q) = q ^ {2} + a _ {1} q + a _ {2} \\ B (q) = b _ {0} q + b _ {1} \\ C (q) = q ^ {2} + c _ {1} q + c _ {2} \\ \end{array}
$$

In this case, $d_{0} = 1$ . The minimum-variance controller is obtained from Eq. (4.9), giving the controller

$$u (t) = - \frac {\left(c _ {1} - a _ {1}\right) + \left(c _ {2} - a _ {2}\right) q ^ {- 1}}{b _ {0} + b _ {1} q ^ {- 1}} y (t)$$

and the closed-loop system is

$$y (t) = e (t)$$

The minimum-variance controller can be used only if $|b_{1}/b_{0}| < 1$ , that is, for the minimum-phase case.

The moving-average controller is obtained by solving Eq. (4.18). In this case, d = 2 and $B^{+}(q) = 1$ . This gives the Diophantine equation

$$q \left(q ^ {2} + c _ {1} q + c _ {2}\right) = \left(q ^ {2} + a _ {1} q + a _ {2}\right) \left(q + r _ {1}\right) + \left(b _ {0} q + b _ {1}\right) \left(s _ {0} q + s _ {1}\right)$$

Notice that this is the same as Eq. (3.19) with $A_{o}(q) = q$ and $A_{m}(q) = C(q)$ . The solution is thus given by Eqs. (3.20) and (3.21):

$$
\begin{array}{l} r _ {1} = \frac {(a _ {2} - c _ {2}) b _ {0} b _ {1} + (c _ {1} - a _ {1}) b _ {1} ^ {2}}{b _ {1} ^ {2} + a _ {1} b _ {0} b _ {1} + a _ {2} b _ {0} ^ {2}} \\ s _ {0} = \frac {b _ {1} \left(a _ {1} ^ {2} - a _ {2} - c _ {1} a _ {1} + c _ {2}\right) + b _ {0} \left(c _ {1} a _ {2} - a _ {1} a _ {2}\right)}{b _ {1} ^ {2} + a _ {1} b _ {0} b _ {1} + a _ {2} b _ {0} ^ {2}} \\ s _ {1} = \frac {b _ {1} \left(a _ {1} a _ {2} - c _ {1} a _ {2}\right) + b _ {0} \left(a _ {2} c _ {2} - a _ {2} ^ {2}\right)}{b _ {1} ^ {2} + a _ {1} b _ {0} b _ {1} + a _ {2} b _ {0} ^ {2}} \\ \end{array}
$$

The closed-loop system is

$$y (t) = \left(1 + r _ {1} q ^ {- 1}\right) e (t)$$
