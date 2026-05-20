$$
\left[ \begin{array}{c c} X & I _ {n} \\ I _ {n} & Y \end{array} \right] \geq 0 \qquad \text { and } \qquad \text { rank } \left[ \begin{array}{c c} X & I _ {n} \\ I _ {n} & Y \end{array} \right] \leq n + r.
$$

Proof. (⇐) By the assumption, there is a matrix $X _ { 1 2 } \in \mathbb { R } ^ { n \times r }$ such that $X - Y ^ { - 1 } =$ $X _ { 1 2 } X _ { 1 2 } ^ { * }$ . Defining $X _ { 2 } : = I _ { r }$ completes the construction.

(⇒) Using Schur complements,

$$Y = X ^ {- 1} + X ^ {- 1} X _ {1 2} (X _ {2} - X _ {1 2} ^ {*} X ^ {- 1} X _ {1 2}) ^ {- 1} X _ {1 2} ^ {*} X ^ {- 1}.$$

Inverting, using the matrix inversion lemma, gives

$$Y ^ {- 1} = X - X _ {1 2} X _ {2} ^ {- 1} X _ {1 2} ^ {*}.$$

Hence, r. $X - Y ^ { - 1 } = X _ { 1 2 } X _ { 2 } ^ { - 1 } X _ { 1 2 } ^ { * } \geq 0$ , and, indeed, rank $\left( X - Y ^ { - 1 } \right) = \operatorname { r a n k } ( X _ { 1 2 } X _ { 2 } ^ { - 1 } X _ { 1 2 } ^ { * } ) \leq$

Lemma 14.3 There exists an rth-order admissible controller such that $\| T _ { z w } \| _ { \infty } < \gamma$ only if the following three conditions hold:

(i) There exists a $Y _ { 1 } > 0$ such that

$$A Y _ {1} + Y _ {1} A ^ {*} + Y _ {1} C _ {1} ^ {*} C _ {1} Y _ {1} / \gamma^ {2} + B _ {1} B _ {1} ^ {*} - \gamma^ {2} B _ {2} B _ {2} ^ {*} < 0. \tag {14.1}$$

(ii) There exists an $X _ { 1 } > 0$ such that

$$X _ {1} A + A ^ {*} X _ {1} + X _ {1} B _ {1} B _ {1} ^ {*} X _ {1} / \gamma^ {2} + C _ {1} ^ {*} C _ {1} - \gamma^ {2} C _ {2} ^ {*} C _ {2} < 0. \tag {14.2}$$

$( i i i ) \left[ \begin{array} { c c } { X _ { 1 } / \gamma } & { I _ { n } } \\ { I _ { n } } & { Y _ { 1 } / \gamma } \end{array} \right] \geq 0 \qquad \mathrm { r a n k } \left[ \begin{array} { c c } { X _ { 1 } / \gamma } & { I _ { n } } \\ { I _ { n } } & { Y _ { 1 } / \gamma } \end{array} \right] \leq n + r .$

Proof. Suppose that there exists an rth-order controller $K ( s )$ such that $\| T _ { z w } \| _ { \infty } < \gamma$ Let K(s) have a state-space realization

$$
K (s) = \left[ \begin{array}{c c} \hat {A} & \hat {B} \\ \hline \hat {C} & \hat {D} \end{array} \right].
$$

Then

$$
T _ {z w} = \mathcal {F} _ {\ell} (G, K) = \left[ \begin{array}{c c c} A + B _ {2} \hat {D} C _ {2} & B _ {2} \hat {C} & B _ {1} + B _ {2} \hat {D} D _ {2 1} \\ \hat {B} C _ {2} & \hat {A} & \hat {B} D _ {2 1} \\ \hline C _ {1} + D _ {1 2} \hat {D} C _ {2} & D _ {1 2} \hat {C} & D _ {1 2} \hat {D} D _ {2 1} \end{array} \right] =: \left[ \begin{array}{c c} A _ {c c c} & B _ {c c c} \\ \hline C _ {c c c} & D _ {c c c} \end{array} \right].
$$

Denote

$$R = \gamma^ {2} I - D _ {c} ^ {*} D _ {c}, \qquad \tilde {R} = \gamma^ {2} I - D _ {c} D _ {c} ^ {*}.$$
