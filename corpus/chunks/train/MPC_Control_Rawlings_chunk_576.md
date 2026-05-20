# Exercise 4.17: Pruning while resampling

Sometimes it is convenient in a simulation to reduce the number of samples when resampling a density. In many discrete processes, for example, the number of possible states that may be reached in the simulation increases with time. To keep the number of samples constant, we may wish to remove samples at each time through the resampling process. Consider a modification of Theorem 4.35 in which the number of resamples is ${ \widetilde { s } } ,$ which does not have to be equal to s.

Theorem 4.41 (Resampling and pruning). Consider a sampled density $p ( x )$ with s samples at $x = x _ { i }$ and associated weights $\boldsymbol { \psi } _ { i }$

$$p (x) = \sum_ {i = 1} ^ {s} w _ {i} \delta (x - x _ {i}) \quad w _ {i} \geq 0 \quad \sum_ {i = 1} ^ {s} w _ {i} = 1$$

Consider the resampling procedure that gives a resampled density with $\tilde { s } > 0$ samples

$$\tilde {p} (x) = \sum_ {i = 1} ^ {\tilde {s}} \tilde {w} _ {i} \delta (x - \tilde {x} _ {i})$$

in which the $\tilde { x } _ { i }$ are chosen according to resample probability $p _ { r }$

$$
p _ {r} (\tilde {x} _ {i}) = \left\{ \begin{array}{l l} w _ {j}, & \tilde {x} _ {i} = x _ {j} \\ 0, & \tilde {x} _ {i} \neq x _ {j} \end{array} \right.
$$

and with uniform weights $\widetilde { \boldsymbol { w } } _ { i } = 1 / \widetilde { \boldsymbol { s } } .$ Consider a function $f ( \cdot )$ defined on a set X containing the points $x _ { i }$ .

Under this resampling procedure, the expectation over resampling of any integral of the resampled density is equal to that same integral of the original density

$$\mathcal {E} _ {r} \left(\int f (x) \tilde {p} (x) d x\right) = \int f (x) p (x) d x \quad a l l f$$

(a) Is the proposed theorem correct? If so, prove it. If not, provide a counterexample.

(b) What do you suppose happens in a simulation if we perform aggressive pruning by always choosing $\tilde { s } = 1 2$
