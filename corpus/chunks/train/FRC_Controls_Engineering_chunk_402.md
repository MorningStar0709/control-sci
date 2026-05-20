$$
\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} \mathbf {u} + \mathbf {c}
\mathbf {x} = \left[ \begin{array}{c} \text { position } \\ \text { velocity } \end{array} \right] \quad \mathbf {u} = \left[ \begin{array}{c} \text { voltage } \end{array} \right]

\dot {\mathbf {x}} = \left[ \begin{array}{c c} 0 & 1 \\ 0 & - \frac {K _ {v}}{K _ {a}} \end{array} \right] \mathbf {x} + \left[ \begin{array}{c} 0 \\ \frac {1}{K _ {a}} \end{array} \right] \mathbf {u} + \left[ \begin{array}{c} 0 \\ - \frac {K _ {s}}{K _ {a}} \operatorname{sgn} (\text { velocity }) \end{array} \right] \tag {14.3}
$$

The model in theorem 14.2.1 is undefined when $K _ { a } = 0$ . To design an LQR for such a system, use the model in theorem 14.2.2 instead. As $K _ { a }$ tends to zero, acceleration requires no effort and velocity becomes an input for position control.

Theorem 14.2.2 — 1-DOF mechanism position model $( K _ { a } = 0 )$ .

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} \mathbf {u}\mathbf {x} = [ \text { position } ] \quad \mathbf {u} = [ \text { velocity } ]\dot {\mathbf {x}} = [ 0 ] \mathbf {x} + [ 1 ] \mathbf {u} \tag {14.4}$$
