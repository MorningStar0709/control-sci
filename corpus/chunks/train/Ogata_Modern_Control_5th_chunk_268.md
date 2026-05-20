Thus, the three conditions cannot be fulfilled simultaneously.Therefore, there is no value of K that allows stability of the system.

A–5–18. Consider the characteristic equation given by

$$a _ {0} s ^ {n} + a _ {1} s ^ {n - 1} + a _ {2} s ^ {n - 2} + \dots + a _ {n - 1} s + a _ {n} = 0 \tag {5-67}$$

The Hurwitz stability criterion, given next, gives conditions for all the roots to have negative real parts in terms of the coefficients of the polynomial.As stated in the discussions of Routh’s stability criterion in Section 5–6, for all the roots to have negative real parts, all the coefficients $\boldsymbol { a } ^ { * } \boldsymbol { \mathbf { s } }$ must be positive. This is a necessary condition but not a sufficient condition. If this condition is not satisfied, it indicates that some of the roots have positive real parts or are imaginary or zero. A sufficient condition for all the roots to have negative real parts is given in the following Hurwitz stability criterion: If all the coefficients of the polynomial are positive, arrange these coefficients in the following determinant:

$$
\Delta_ {n} = \left| \begin{array}{c c c c c c c} a _ {1} & a _ {3} & a _ {5} & \dots & 0 & 0 & 0 \\ a _ {0} & a _ {2} & a _ {4} & \dots & \cdot & \cdot & \cdot \\ 0 & a _ {1} & a _ {3} & \dots & a _ {n} & 0 & 0 \\ 0 & a _ {0} & a _ {2} & \dots & a _ {n - 1} & 0 & 0 \\ \cdot & \cdot & \cdot & & a _ {n - 2} & a _ {n} & 0 \\ \cdot & \cdot & \cdot & & a _ {n - 3} & a _ {n - 1} & 0 \\ 0 & 0 & 0 & \dots & a _ {n - 4} & a _ {n - 2} & a _ {n} \end{array} \right|
$$

where we substituted zero for $a _ { s } \mathrm { i f } s > n .$ . For all the roots to have negative real parts, it is necessary and sufficient that successive principal minors of $\Delta _ { n }$ be positive. The successive principal minors are the following determinants:

$$
\Delta_ {i} = \left| \begin{array}{c c c c} a _ {1} & a _ {3} & \dots & a _ {2 i - 1} \\ a _ {0} & a _ {2} & \dots & a _ {2 i - 2} \\ 0 & a _ {1} & \dots & a _ {2 i - 3} \\ . & . & & . \\ 0 & 0 & \dots & a _ {i} \end{array} \right| \qquad (i = 1, 2, \ldots , n - 1)
$$

where $a _ { s } = 0 { \mathrm { i f } } s > n .$ . (It is noted that some of the conditions for the lower-order determinants are included in the conditions for the higher-order determinants.) If all these determinants are positive, and $a _ { 0 } > 0$ as already assumed, the equilibrium state of the system whose characteristic equation is given by Equation (5–67) is asymptotically stable. Note that exact values of determinants are not needed; instead, only signs of these determinants are needed for the stability criterion.
