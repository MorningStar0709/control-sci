Jordan Canonical Form. Next we shall consider the case where the denominator polynomial of Equation (9–2) involves multiple roots. For this case, the preceding diagonal canonical form must be modified into the Jordan canonical form. Suppose, for example, that the $\boldsymbol { p } _ { i } { } ^ { \prime } { \bf s }$ are different from one another, except that the first three $p _ { i }$ ’s are equal, or $p _ { 1 } = p _ { 2 } = p _ { 3 }$ . Then the factored form of $Y ( s ) / U ( s )$ becomes

$$\frac {Y (s)}{U (s)} = \frac {b _ {0} s ^ {n} + b _ {1} s ^ {n - 1} + \cdots + b _ {n - 1} s + b _ {n}}{(s + p _ {1}) ^ {3} (s + p _ {4}) (s + p _ {5}) \cdots (s + p _ {n})}$$

The partial-fraction expansion of this last equation becomes

$$\frac {Y (s)}{U (s)} = b _ {0} + \frac {c _ {1}}{(s + p _ {1}) ^ {3}} + \frac {c _ {2}}{(s + p _ {1}) ^ {2}} + \frac {c _ {3}}{s + p _ {1}} + \frac {c _ {4}}{s + p _ {4}} + \dots + \frac {c _ {n}}{s + p _ {n}}$$

A state-space representation of this system in the Jordan canonical form is given by

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \\ \dot {x} _ {4} \\ . \\ . \\ . \\ \dot {x} _ {n} \end{array} \right] = \left[ \begin{array}{c c c c c c c} - p _ {1} & 1 & 0 & 0 & \dots & 0 \\ 0 & - p _ {1} & 1 & : & & : \\ 0 & 0 & - p _ {1} & 0 & \dots & 0 \\ \hline 0 & \dots & 0 & - p _ {4} & & 0 \\ . & & . & & . & \\ . & & . & & . & \\ . & & . & & & . \\ 0 & \dots & 0 & 0 & & - p _ {n} \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \\ x _ {4} \\ . \\ . \\ . \\ x _ {n} \end{array} \right] + \left[ \begin{array}{c} 0 \\ 0 \\ 1 \\ 1 \\ . \\ . \\ . \\ 1 \end{array} \right] u \tag {9-10}

y = \left[ \begin{array}{l l l l} c _ {1} & c _ {2} & \dots & c _ {n} \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ \cdot \\ \cdot \\ \cdot \\ x _ {n} \end{array} \right] + b _ {0} u \tag {9-11}
$$

EXAMPLE 9–1 Consider the system given by

$$\frac {Y (s)}{U (s)} = \frac {s + 3}{s ^ {2} + 3 s + 2}$$

Obtain state-space representations in the controllable canonical form, observable canonical form, and diagonal canonical form.

Controllable Canonical Form:

$$
\begin{array}{l} \left[ \begin{array}{c} \dot {x} _ {1} (t) \\ \dot {x} _ {2} (t) \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ - 2 & - 3 \end{array} \right] \left[ \begin{array}{c} x _ {1} (t) \\ x _ {2} (t) \end{array} \right] + \left[ \begin{array}{c} 0 \\ 1 \end{array} \right] u (t) \\ y (t) = \left[ \begin{array}{c c} 3 & 1 \end{array} \right] \left[ \begin{array}{c} x _ {1} (t) \\ x _ {2} (t) \end{array} \right] \\ \end{array}
$$

Observable Canonical Form:
