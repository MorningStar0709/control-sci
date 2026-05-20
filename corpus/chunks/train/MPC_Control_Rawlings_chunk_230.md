# 2.4 Stability

Proof. From the DP recursion (2.10)

$$V _ {1} ^ {0} (x) = \min _ {u \in \mathbb {U}} \{\ell (x, u) + V _ {0} ^ {0} (f (x, u)) \mid f (x, u) \in \mathcal {X} _ {0} \}$$

But $V _ { 0 } ^ { 0 } ( \cdot ) : = V _ { f } ( \cdot )$ and $\mathcal { X } _ { 0 } : = \mathbb { X } _ { f }$ . Also, by Assumption 2.12,

$$\min _ {u \in \mathbb {U}} \{\ell (x, u) + V _ {f} (f (x, u)) \} \leq V _ {f} (x) \quad \forall x \in \mathbb {X} _ {f}$$

so that

$$V _ {1} ^ {0} (x) \leq V _ {0} ^ {0} (x) \quad \forall x \in \mathcal {X} _ {0}$$

Next, suppose that for some $j \geq 1$ ,

$$V _ {j} ^ {0} (x) \leq V _ {j - 1} ^ {0} (x) \quad \forall x \in \mathcal {X} _ {j - 1}$$

Then, using the DP equation (2.10)

$$
\begin{array}{l} V _ {j + 1} ^ {0} (x) - V _ {j} ^ {0} (x) = \ell (x, \kappa_ {j + 1} (x)) + V _ {j} ^ {0} (f (x, \kappa_ {j + 1} (x))) \\ - \ell (x, \kappa_ {j} (x)) - V _ {j - 1} ^ {0} (f (x, \kappa_ {j} (x))) \quad \forall x \in \mathcal {X} _ {j} \subseteq \mathcal {X} _ {j + 1} \\ \end{array}
$$

Since $\kappa _ { j } ( x )$ may not be optimal for $\mathbb { P } _ { j + 1 } ( x )$ for all $x \in \mathcal { X } _ { j } \subseteq \mathcal { X } _ { j + 1 }$ , we have

$$
\begin{array}{l} V _ {j + 1} ^ {0} (x) - V _ {j} ^ {0} (x) \leq \ell (x, \kappa_ {j} (x)) + V _ {j} ^ {0} (f (x, \kappa_ {j} (x))) \\ - \ell (x, \kappa_ {j} (x)) - V _ {j - 1} ^ {0} (f (x, \kappa_ {j} (x))) \quad \forall x \in \mathcal {X} _ {j} \\ \end{array}
$$

Also, from (2.12), $x \in \mathcal X _ { j }$ implies $f ( x , \kappa _ { j } ( x ) ) \in \mathcal { X } _ { j - 1 }$ so that, by assumption, $V _ { j } ^ { 0 } ( f ( x , \kappa _ { j } ( x ) \bar { ) } ) \leq V _ { j - 1 } ^ { 0 } ( f ( x , \bar { \kappa _ { j } } ( x ) ) )$ for all $x \in \mathcal { X } _ { j }$ . Hence

$$V _ {j + 1} ^ {0} (x) \leq V _ {j} ^ {0} (x) \quad \forall x \in \mathcal {X} _ {j}$$

By induction

$$V _ {j + 1} ^ {0} (x) \leq V _ {j} ^ {0} (x) \quad \forall x \in \mathcal {X} _ {j}, \forall j \in \{1, 2, \dots , N - 1 \}$$

It then follows that $V _ { N } ^ { 0 } ( x ) \le V _ { 0 } ^ { 0 } ( x ) : = V _ { f } ( x )$ for all $x \in \mathcal { X } _ { 0 } : = \mathbb { X } _ { f }$

Lemma 2.15 also holds if U is closed but not bounded. The monotonicity property can be used to establish the descent property of $V _ { N } ^ { 0 } ( \cdot )$ proved in Lemma 2.14 by noting that

$$
\begin{array}{l} V _ {N} ^ {0} (x) = \ell (x, \kappa_ {N} (x)) + V _ {N - 1} ^ {0} (f (x, \kappa_ {N} (x))) \\ = \ell (x, \kappa_ {N} (x)) + V _ {N} ^ {0} (f (x, \kappa_ {N} (x))) + \\ [ V _ {N - 1} ^ {0} (f (x, \kappa_ {N} (x))) - V _ {N} ^ {0} (f (x, \kappa_ {N} (x))) ] \\ \end{array}
$$

so that using the monotonicity property

$$
\begin{array}{l} V _ {N} ^ {0} (f (x, \kappa_ {N} (x))) = V _ {N} ^ {0} (x) - \ell (x, \kappa_ {N} (x)) + \\ [ V _ {N} ^ {0} (f (x, \kappa_ {N} (x))) - V _ {N - 1} ^ {0} (f (x, \kappa_ {N} (x))) ] \\ \leq V _ {N} ^ {0} (x) - \ell (x, \kappa_ {N} (x)) \quad \forall x \in \mathcal {X} _ {N} \\ \end{array}
$$

which is the desired descent property.
