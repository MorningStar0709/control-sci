# ■ Theorem 3.5

A realization is minimal if, and only if, it is controllable and observable.

Proof: To show necessity (“only if”), we show that minimality is precluded if the realization is either uncontrollable or unobservable. This follows directly from observation of the canonical decomposition: the uncontrollable or unobservable blocks can be removed without affecting the transfer function. If a realization is uncontrollable or unobservable, it can be transformed into its canonical decomposition and the uncontrollable and unobservable blocks removed, to generate a realization of lower order with the same transfer function.

We show sufficiency for the special case where the $A$ matrix has distinct eigenvalues. In such a case, transformation into diagonal form is possible, leading to equations of the form of Equation 3.65. From that equation,

$$z _ {i} (s) = \frac {1}{s - s _ {i}} \mathbf {w _ {i}} ^ {\mathrm{T}} B \mathbf {u} (s)$$

and

$$\mathbf {y} (s) = \left[ \sum_ {i} = 1 ^ {n} \frac {1}{s - s _ {i}} (C \mathbf {v} _ {i}) (\mathbf {w} _ {i} ^ {T} B) + D \right] \mathbf {u} (s).$$

If the system is controllable and observable, $C\mathbf{v}_i \neq \mathbf{0}$ and $\mathbf{w}_i^T B \neq \mathbf{0}$ for $i = 1, 2, \ldots, n$ ; hence, the coefficient of each term $\frac{1}{s - s_i}$ is nonzero and the transfer function has $n$ poles, $s_1, s_2, \ldots, s_n$ . Since all transfer function poles must be eigenvalues of $A$ , then $A$ must have at least $n$ eigenvalues, so a realization with fewer than $n$ states is not possible.
