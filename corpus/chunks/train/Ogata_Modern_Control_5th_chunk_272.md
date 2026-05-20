$$
\Delta_ {4} = \left| \begin{array}{c c c c} a _ {1 1} & a _ {3} & a _ {5} & a _ {7} \\ 0 & a _ {2 2} & a _ {2 3} & a _ {2 4} \\ 0 & 0 & a _ {3 3} & a _ {3 4} \\ 0 & 0 & 0 & a _ {4 4} \end{array} \right|
$$

where

$$a _ {4 4} = \hat {a} _ {4 4} - \frac {\hat {a} _ {4 3}}{a _ {3 3}} a _ {3 4}$$

From this analysis, we see that

$$\Delta_ {4} = a _ {1 1} a _ {2 2} a _ {3 3} a _ {4 4}\Delta_ {3} = a _ {1 1} a _ {2 2} a _ {3 3}\Delta_ {2} = a _ {1 1} a _ {2 2}\Delta_ {1} = a _ {1 1}$$

The Hurwitz conditions for asymptotic stability

$$\Delta_ {1} > 0, \quad \Delta_ {2} > 0, \quad \Delta_ {3} > 0, \quad \Delta_ {4} > 0, \quad \dots$$

reduce to the conditions

$$a _ {1 1} > 0, \quad a _ {2 2} > 0, \quad a _ {3 3} > 0, \quad a _ {4 4} > 0, \quad \dots$$

The Routh array for the polynomial

$$a _ {0} s ^ {4} + a _ {1} s ^ {3} + a _ {2} s ^ {2} + a _ {3} s + a _ {4} = 0$$

where $a _ { 0 } > 0$ and n=4, is given by

$$
\begin{array}{c c c} a _ {0} & a _ {2} & a _ {4} \end{array}

\begin{array}{c c} a _ {1} & a _ {3} \end{array}

\begin{array}{c c} b _ {1} & b _ {2} \end{array}
c _ {1}d _ {1}
$$

From this Routh array, we see that

$$a _ {1 1} = a _ {1}a _ {2 2} = a _ {2} - \frac {a _ {0}}{a _ {1}} a _ {3} = b _ {1}a _ {3 3} = a _ {3} - \frac {a _ {1}}{a _ {2 2}} a _ {2 3} = \frac {a _ {3} b _ {1} - a _ {1} b _ {2}}{b _ {1}} = c _ {1}a _ {4 4} = \hat {a} _ {4 4} - \frac {\hat {a} _ {4 3}}{a _ {3 3}} a _ {3 4} = a _ {4} = d _ {1}$$

(The last equation is obtained using the fact that $a _ { 3 4 } = 0 , \hat { a } _ { 4 4 } = a _ { 4 }$ , and $a _ { 4 } = b _ { 2 } = d _ { 1 } . )$ Hence the Hurwitz conditions for asymptotic stability become

$$a _ {1} > 0, \quad b _ {1} > 0, \quad c _ {1} > 0, \quad d _ {1} > 0$$

Thus we have demonstrated that Hurwitz conditions for asymptotic stability can be reduced to Routh’s conditions for asymptotic stability. The same argument can be extended to Hurwitz determinants of any order, and the equivalence of Routh’s stability criterion and Hurwitz stability criterion can be established.

A–5–21. Consider the characteristic equation

$$s ^ {4} + 2 s ^ {3} + (4 + K) s ^ {2} + 9 s + 2 5 = 0$$

Using the Hurwitz stability criterion, determine the range of K for stability.

Solution. Comparing the given characteristic equation

$$s ^ {4} + 2 s ^ {3} + (4 + K) s ^ {2} + 9 s + 2 5 = 0$$

with the following standard fourth-order characteristic equation:

$$a _ {0} s ^ {4} + a _ {1} s ^ {3} + a _ {2} s ^ {2} + a _ {3} s + a _ {4} = 0$$

we find

$$a _ {0} = 1, \quad a _ {1} = 2, \quad a _ {2} = 4 + K, \quad a _ {3} = 9, \quad a _ {4} = 2 5$$

The Hurwitz stability criterion states that $\Delta _ { 4 }$ is given by
