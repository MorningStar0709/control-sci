respectively, with $\Sigma _ { 1 } , \ \Sigma _ { 2 } , \ \Sigma _ { 3 }$ diagonal and positive definite.

In the special case where $\left\lceil { \frac { A \left\lfloor B \right\rceil } { C \left\lceil D \right\rceil } } \right\rceil$ is a minimal realization, a balanced realization can be obtained through the following simplified procedure:

1. Compute the controllability and observability Gramians $P > 0 , Q > 0$ .   
2. Find a matrix R such that $P = R ^ { * } R$ .   
3. Diagonalize $R Q R ^ { * }$ to get $R Q R ^ { * } = U \Sigma ^ { 2 } U ^ { * }$ .   
4. Let $T ^ { - 1 } = R ^ { * } U \Sigma ^ { - 1 / 2 }$ . Then $T P T ^ { * } = ( T ^ { * } ) ^ { - 1 } Q T ^ { - 1 } = \Sigma \ \mathrm { a n d } \ \left[ \frac { T A T ^ { - 1 } \ \big | \ T B } { \ C T ^ { - 1 } \ \big | \ D } \right]$

is balanced.

Assume that the Hankel singular values of the system are decreasingly ordered so that $\Sigma = \operatorname { d i a g } ( \sigma _ { 1 } I _ { s _ { 1 } } , \sigma _ { 2 } I _ { s _ { 2 } } , \dots , \sigma _ { N } I _ { s _ { N } } )$ with $\sigma _ { 1 } > \sigma _ { 2 } > . . . > \sigma _ { N }$ and suppose $\sigma _ { r } \gg$ $\sigma _ { r + 1 }$ for some r. Then the balanced realization implies that those states corresponding to the singular values of $\sigma _ { r + 1 } , \ldots , \sigma _ { N }$ are less controllable and less observable than those states corresponding to $\sigma _ { 1 } , \ldots , \sigma _ { r }$ . Therefore, truncating those less controllable and less observable states will not lose much information about the system.

Two other closely related realizations are called input normal realization with $P = I$ and $Q = \Sigma ^ { 2 }$ , and output normal realization with $P = \Sigma ^ { 2 }$ and $Q = I$ . Both realizations can be obtained easily from the balanced realization by a suitable scaling on the states.

Next we shall derive some simple and useful bounds for the $\mathcal { H } _ { \infty }$ norm and the $\mathcal { L } _ { 1 }$ norm of a stable system.

Theorem 7.8 Suppose

$$
G (s) = \left[ \begin{array}{c c} A & B \\ \hline C & 0 \end{array} \right] \in \mathcal {R H} _ {\infty}
$$

is a balanced realization; that is, there exists

$$\Sigma = d i a g (\sigma_ {1} I _ {s _ {1}}, \sigma_ {2} I _ {s _ {2}}, \dots , \sigma_ {N} I _ {s _ {N}}) \geq 0$$

with $\sigma _ { 1 } > \sigma _ { 2 } > . . . > \sigma _ { N } \geq 0$ , such that

$$A \Sigma + \Sigma A ^ {*} + B B ^ {*} = 0 \quad A ^ {*} \Sigma + \Sigma A + C ^ {*} C = 0$$

Then

$$\sigma_ {1} \leq \| G \| _ {\infty} \leq \int_ {0} ^ {\infty} \| g (t) \| d t \leq 2 \sum_ {i = 1} ^ {N} \sigma_ {i}$$

where $g ( t ) = C e ^ { A t } B$ .
