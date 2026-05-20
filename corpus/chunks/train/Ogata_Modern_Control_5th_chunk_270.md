The next term in the first column is $c _ { 1 } .$ , which is equal to

$$
\begin{array}{l} \frac {b _ {1} a _ {3} - a _ {1} b _ {2}}{b _ {1}} = \frac {\left[ \frac {a _ {1} a _ {2} - a _ {3}}{a _ {1}} \right] a _ {3} - a _ {1} \left[ \frac {a _ {1} a _ {4} - a _ {5}}{a _ {1}} \right]}{\left[ \frac {a _ {1} a _ {2} - a _ {3}}{a _ {1}} \right]} \\ = \frac {a _ {1} a _ {2} a _ {3} - a _ {3} ^ {2} - a _ {1} ^ {2} a _ {4} + a _ {1} a _ {5}}{a _ {1} a _ {2} - a _ {3}} \\ = \frac {\Delta_ {3}}{\Delta_ {2}} \\ \end{array}
$$

In a similar manner the remaining terms in the first column of the Routh array can be found.

The Routh array has the property that the last nonzero terms of any columns are the same; that is, if the array is given by

$$
\begin{array}{l} \begin{array}{c c c c} a _ {0} & a _ {2} & a _ {4} & a _ {6} \end{array} \\ \begin{array}{c c c c} a _ {1} & a _ {3} & a _ {5} & a _ {7} \end{array} \\ \begin{array}{c c c} b _ {1} & b _ {2} & b _ {3} \end{array} \\ \begin{array}{c c c} c _ {1} & c _ {2} & c _ {3} \end{array} \\ \begin{array}{c c} d _ {1} & d _ {2} \end{array} \\ \begin{array}{c c} e _ {1} & e _ {2} \end{array} \\ f _ {1} \\ g _ {1} \\ \end{array}
$$

then

$$a _ {7} = c _ {3} = e _ {2} = g _ {1}$$

and if the array is given by

$$
\begin{array}{l} \begin{array}{c c c c} a _ {0} & a _ {2} & a _ {4} & a _ {6} \end{array} \\ \begin{array}{c c c c} a _ {1} & a _ {3} & a _ {5} & 0 \end{array} \\ \begin{array}{c c c} b _ {1} & b _ {2} & b _ {3} \end{array} \\ \begin{array}{c c c} c _ {1} & c _ {2} & 0 \end{array} \\ \begin{array}{c c} d _ {1} & d _ {2} \end{array} \\ e _ {1} 0 \\ f _ {1} \\ \end{array}
$$

then

$$a _ {6} = b _ {3} = d _ {2} = f _ {1}$$

In any case, the last term of the first column is equal to $a _ { n } , \mathrm { o r }$

$$a _ {n} = \frac {\Delta_ {n - 1} a _ {n}}{\Delta_ {n - 1}} = \frac {\Delta_ {n}}{\Delta_ {n - 1}}$$

For example, if n=4, then

$$
\Delta_ {4} = \left| \begin{array}{c c c c} a _ {1} & 1 & 0 & 0 \\ a _ {3} & a _ {2} & a _ {1} & 1 \\ a _ {5} & a _ {4} & a _ {3} & a _ {2} \\ a _ {7} & a _ {6} & a _ {5} & a _ {4} \end{array} \right| = \left| \begin{array}{c c c c} a _ {1} & 1 & 0 & 0 \\ a _ {3} & a _ {2} & a _ {1} & 1 \\ 0 & a _ {4} & a _ {3} & a _ {2} \\ 0 & 0 & 0 & a _ {4} \end{array} \right| = \Delta_ {3} a _ {4}
$$

Thus it has been shown that the first column of the Routh array is given by

$$1, \quad \Delta_ {1}, \quad \frac {\Delta_ {2}}{\Delta_ {1}}, \quad \frac {\Delta_ {3}}{\Delta_ {2}}, \quad \dots , \quad \frac {\Delta_ {n}}{\Delta_ {n - 1}}$$

A–5–20. Show that the Routh’s stability criterion and Hurwitz stability criterion are equivalent.

Solution. If we write Hurwitz determinants in the triangular form
