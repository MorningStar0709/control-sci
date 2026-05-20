Theorem 14.4.1 — Drivetrain linear/angular velocity model.

$$
\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} \mathbf {u}
\mathbf {x} = \left[ \begin{array}{c} \text { linear   velocity } \\ \text { angular   velocity } \end{array} \right] \quad \mathbf {u} = \left[ \begin{array}{c} \text { left   voltage } \\ \text { right   voltage } \end{array} \right]

\dot {\mathbf {x}} = \left[ \begin{array}{c c} - \frac {K _ {v , l i n}}{K _ {a , l i n}} & 0 \\ 0 & - \frac {K _ {v , a n g}}{K _ {a , a n g}} \end{array} \right] \mathbf {x} + \left[ \begin{array}{c c} \frac {0 . 5}{K _ {a , l i n}} & \frac {0 . 5}{K _ {a , l i n}} \\ - \frac {0 . 5}{K _ {a , a n g}} & \frac {0 . 5}{K _ {a , a n g}} \end{array} \right] \mathbf {u}
$$

$K _ { v , a n g }$ and $K _ { a , a n g }$ have units of $\frac { V } { A / T }$ and $\frac { V } { A / T ^ { 2 } }$ respectively where V means voltage units, A means angle units, and $T$ means time units.
