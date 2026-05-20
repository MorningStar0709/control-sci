# 9.4.1 State vector expectation evolution

First, we will compute how the expectation of the system state evolves.

$$
\begin{array}{l} E [ \mathbf {x} _ {k + 1} ] = E [ \mathbf {A x} _ {k} + \mathbf {B u} _ {k} + \mathbf {w} _ {k} ] \\ E \left[ \mathbf {x} _ {k + 1} \right] = E \left[ \mathbf {A x} _ {k} \right] + E \left[ \mathbf {B u} _ {k} \right] + E \left[ \mathbf {w} _ {k} \right] \\ E [ \mathbf {x} _ {k + 1} ] = \mathbf {A} E [ \mathbf {x} _ {k} ] + \mathbf {B} E [ \mathbf {u} _ {k} ] + E [ \mathbf {w} _ {k} ] \\ E \left[ \mathbf {x} _ {k + 1} \right] = \mathbf {A} E \left[ \mathbf {x} _ {k} \right] + \mathbf {B} \mathbf {u} _ {k} + 0 \\ \overline {{{\mathbf {x}}}} _ {k + 1} = \mathbf {A} \overline {{{\mathbf {x}}}} _ {k} + \mathbf {B} \mathbf {u} _ {k} \\ \end{array}
$$
