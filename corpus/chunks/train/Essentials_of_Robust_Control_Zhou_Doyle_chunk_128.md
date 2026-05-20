Now suppose that the system is internally stable; then $( I - P \hat { K } ) ^ { - 1 } \in \mathcal { R } \mathcal { H } _ { \infty }$ . So we only need to show that given condition (ii), condition (i) is necessary and sufficient for the internal stability. This follows by noting that $( { \bar { A } } , { \bar { B } } )$ is stabilizable iff

$$
\left(\left[ \begin{array}{c c} A & B \hat {C} \\ 0 & \hat {A} \end{array} \right], \left[ \begin{array}{c} B \hat {D} \\ \hat {B} \end{array} \right]\right) \tag {5.5}
$$

is stabilizable; and $( { \bar { C } } , { \bar { A } } )$ is detectable iff

$$
\left(\left[ \begin{array}{l l} C & D \hat {C} \end{array} \right], \left[ \begin{array}{c c} A & B \hat {C} \\ 0 & \hat {A} \end{array} \right]\right) \tag {5.6}
$$

is detectable. But conditions (5.5) and (5.6) are equivalent to condition (i).

Condition (i) in the preceding theorem implies that there is no unstable pole/zero cancellation in forming the product $P \hat { K }$ .

The preceding theorem is, in fact, the basis for the classical control theory, where the stability is checked only for one closed-loop transfer function with the implicit assumption that the controller itself is stable (and most probably also minimum phase; or at least marginally stable and minimum phase with the condition that any imaginary axis pole of the controller is not in the same location as any zero of the plant).

Example 5.1 Let P and $\hat { K }$ be two-by-two transfer matrices

$$
P = \left[ \begin{array}{c c} {\frac {1}{s - 1}} & 0 \\ {0} & {\frac {1}{s + 1}} \end{array} \right], \quad \hat {K} = \left[ \begin{array}{c c} {\frac {1 - s}{s + 1}} & {- 1} \\ {0} & {- 1} \end{array} \right].
$$

Then

$$
P \hat {K} = \left[ \begin{array}{c c} \frac {- 1}{s + 1} & \frac {- 1}{s - 1} \\ 0 & \frac {- 1}{s + 1} \end{array} \right], (I - P \hat {K}) ^ {- 1} = \left[ \begin{array}{c c} \frac {s + 1}{s + 2} & - \frac {(s + 1) ^ {2}}{(s + 2) ^ {2} (s - 1)} \\ 0 & \frac {s + 1}{s + 2} \end{array} \right].
$$

So the closed-loop system is not stable even though

$$\det (I - P \hat {K}) = \frac {(s + 2) ^ {2}}{(s + 1) ^ {2}}$$

has no zero in the closed right-half plane and the number of unstable poles of $P \hat { K } =$ $n _ { k } + n _ { p } = 1$ . Hence, in general, det $( I - P { \hat { K } } )$ having no zeros in the closed right-half plane does not necessarily imply $( I - P \hat { K } ) ^ { - 1 } \in \mathcal { R } \mathcal { H } _ { \infty }$ .
