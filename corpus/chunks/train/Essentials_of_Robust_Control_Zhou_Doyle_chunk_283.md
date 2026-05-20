$$\mu_ {\Delta} (G (j \omega)) \leq \sqrt {\kappa (W _ {d} ^ {- 1} P W _ {1})} (\| W _ {2} T _ {i} W _ {1} \| + \| W _ {e} S _ {o} W _ {d} \|).$$

In particular, this suggests that the robust performance margin is inversely proportional to the square root of the plant condition number if $W _ { d } = I$ and $W _ { 1 } = I$ . This can be further illustrated by considering a plant-inverting control system.

To simplify the exposition, we shall make the following assumptions:

$$W _ {e} = w _ {s} I, W _ {d} = I, W _ {1} = I, W _ {2} = w _ {t} I,$$

and $P$ is stable and has a stable inverse $( { \mathrm { i . e . } }$ , minimum phase) $( P$ can be strictly proper). Furthermore, we shall assume that the controller has the form

$$K (s) = P ^ {- 1} (s) l (s)$$

where $l ( s )$ is a scalar loop transfer function that makes $K ( s )$ proper and stabilizes the closed loop. This compensator produces diagonal sensitivity and complementary sensitivity functions with identical diagonal elements; namely,

$$S _ {o} = S _ {i} = \frac {1}{1 + l (s)} I, T _ {o} = T _ {i} = \frac {l (s)}{1 + l (s)} I.$$

Denote

$$\varepsilon (s) = \frac {1}{1 + l (s)}, \tau (s) = \frac {l (s)}{1 + l (s)}$$

and substitute these expressions into $G ;$ we $\mathrm { g e t }$

$$
G = \left[ \begin{array}{c c} - w _ {t} \tau I & - w _ {t} \tau P ^ {- 1} \\ w _ {s} \varepsilon P & w _ {s} \varepsilon I \end{array} \right].
$$

The structured singular value for G at frequency ω can be computed by

$$
\mu_ {\boldsymbol {\Delta}} (G (j \omega)) = \inf _ {d \in \mathbb {R} _ {+}} \overline {{\sigma}} \left(\left[ \begin{array}{c c} - w _ {t} \tau I & - w _ {t} \tau (d P) ^ {- 1} \\ w _ {s} \varepsilon d P & w _ {s} \varepsilon I \end{array} \right]\right).
$$

Let the singular value decomposition of $P ( j \omega )$ at frequency ω be

$$P (j \omega) = U \Sigma V ^ {*}, \Sigma = \mathrm{diag} (\sigma_ {1}, \sigma_ {2}, \ldots , \sigma_ {m})$$

with $\sigma _ { 1 } = \overline { { \sigma } }$ and $\sigma _ { m } = \underline { { \sigma } } .$ , where m is the dimension of $P .$ . Then

$$
\mu_ {\boldsymbol {\Delta}} (G (j \omega)) = \inf _ {d \in \mathbb {R} _ {+}} \overline {{\sigma}} \left(\left[ \begin{array}{c c} - w _ {t} \tau I & - w _ {t} \tau (d \Sigma) ^ {- 1} \\ w _ {s} \varepsilon d \Sigma & w _ {s} \varepsilon I \end{array} \right]\right)
$$

since unitary operations do not change the singular values of a matrix. Note that
