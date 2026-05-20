# Theorem 14.3.1 — Drivetrain left/right velocity model.

$$
\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} \mathbf {u}
\mathbf {x} = \left[ \begin{array}{c} \text { left   velocity } \\ \text { right   velocity } \end{array} \right] \quad \mathbf {u} = \left[ \begin{array}{c} \text { left   voltage } \\ \text { right   voltage } \end{array} \right]

\dot {\mathbf {x}} = \left[ \begin{array}{c c} A _ {1} & A _ {2} \\ A _ {2} & A _ {1} \end{array} \right] \mathbf {x} + \left[ \begin{array}{c c} B _ {1} & B _ {2} \\ B _ {2} & B _ {1} \end{array} \right] \mathbf {u}

\left[ \begin{array}{l} A _ {1} \\ A _ {2} \\ B _ {1} \\ B _ {2} \end{array} \right] = \frac {1}{2} \left[ \begin{array}{c} - \left(\frac {K _ {v , l i n}}{K _ {a , l i n}} + \frac {K _ {v , a n g}}{K _ {a , a n g}}\right) \\ - \left(\frac {K _ {v , l i n}}{K _ {a , l i n}} - \frac {K _ {v , a n g}}{K _ {a , a n g}}\right) \\ \frac {1}{K _ {a , l i n}} + \frac {1}{K _ {a , a n g}} \\ \frac {1}{K _ {a , l i n}} - \frac {1}{K _ {a , a n g}} \end{array} \right] \tag {14.5}
$$

$K _ { v , a n g }$ and $K _ { a , a n g }$ have units of $\frac { V } { L / T }$ and $\frac { V } { L / T ^ { 2 } }$ respectively where V means voltage units, L means length units, and $T$ means time units.

If $K _ { v }$ and $K _ { a }$ are the same for both the linear and angular cases, it devolves to the one-dimensional case. This means the left and right sides are decoupled.

$$
\left[ \begin{array}{c} A _ {1} \\ A _ {2} \\ B _ {1} \\ B _ {2} \end{array} \right] = \frac {1}{2} \left[ \begin{array}{c} - \left(\frac {K _ {v}}{K _ {a}} + \frac {K _ {v}}{K _ {a}}\right) \\ - \left(\frac {K _ {v}}{K _ {a}} - \frac {K _ {v}}{K _ {a}}\right) \\ \frac {1}{K _ {a}} + \frac {1}{K _ {a}} \\ \frac {1}{K _ {a}} - \frac {1}{K _ {a}} \end{array} \right]

\left[ \begin{array}{c} A _ {1} \\ A _ {2} \\ B _ {1} \\ B _ {2} \end{array} \right] = \frac {1}{2} \left[ \begin{array}{c} - 2 \frac {K _ {v}}{K _ {a}} \\ 0 \\ \frac {2}{K _ {a}} \\ 0 \end{array} \right]

{\left[ \begin{array}{l} A _ {1} \\ A _ {2} \\ B _ {1} \\ B _ {2} \end{array} \right]} = {\left[ \begin{array}{l} - \frac {K _ {v}}{K _ {a}} \\ 0 \\ \frac {1}{K _ {a}} \\ 0 \end{array} \right]}
$$
