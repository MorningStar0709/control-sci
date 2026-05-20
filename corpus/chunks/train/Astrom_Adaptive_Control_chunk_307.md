# LEMMA 5.2 Kalman-Yakubovich lemma

Let the time-invariant linear system

$$
\begin{array}{l} \frac {d x}{d t} = A x + B u \\ \mathbf {y} = \mathbf {C x} \\ \end{array}
$$

be completely controllable and completely observable. The transfer function

$$G (s) = C (s I - A) ^ {- 1} B$$

is strictly positive real if and only if there exist positive definite matrices $P$ and $Q$ such that

$$A ^ {T} P + P A = - Q$$

and

$$\boldsymbol {B} ^ {T} \boldsymbol {P} = \boldsymbol {C}$$

A proof of this result is given in Section 5.6. There is a more general version of the theorem that applies to systems with a direct term from input to output. The simpler version is sufficient for our purposes.
