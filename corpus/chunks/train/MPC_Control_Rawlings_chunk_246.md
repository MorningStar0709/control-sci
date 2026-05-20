# 2.4 Stability

problem appropriately, however, stability can be ensured, as we now show. We replace the stability assumptions (2.12 and 2.13) by their time-varying extension.

Assumption 2.30 (Basic stability assumption; time-varying case). For all $\begin{array} { r } { i \in \mathbb { I } _ { \geq 0 } , \operatorname* { m i n } _ { u \in \mathbb { U } _ { i } } \{ V _ { f } ( f ( x , u , i ) , i + 1 ) + \ell ( x , u , i ) \mid f ( x , u , i ) \in \mathbb { X } _ { f } ( i + 1 , \ell ) \} , } \end{array}$ $1 ) \} \} \leq V _ { f } ( x , i ) , \ \forall x \in \mathbb { X } _ { f } ( i )$ .

This assumption implicitly requires that the sets $\{ \mathbb { X } _ { f } ( i ) \}$ are timevarying positive invariant in the following sense.

Assumption 2.31 (Implied invariance assumption; time-varying case). For each $i \in \mathbb { I } _ { \geq 0 }$ and each ${ \boldsymbol { x } } \in \mathbb { X } _ { f } ( i )$ , there exists a $u \in \mathbb { U } ( i )$ such that $f ( x , u , i ) \in \mathbb { X } _ { f } ( i + 1 )$ .

A direct consequence of Assumption 2.31 is the extension of Lemma 2.14, namely, that the time-varying value function $V _ { N } ^ { 0 } ( \cdot )$ has the descent property that its value at $( f ( x , \kappa _ { N } ( x , i ) , i ) , i + 1 )$ is less than its value at $( x , i )$ by an amount $\ell ( x , \kappa _ { N } ( x , i ) , i )$ .

Lemma 2.32 (Optimal cost decrease; time-varying case). Suppose Assumptions 2.25, 2.26, 2.30 and 2.31 hold. Then,

$$V _ {N} ^ {0} (f (x, \kappa_ {N} (x, i), i), i + 1) \leq V _ {N} ^ {0} (x, i) - \ell (x, \kappa_ {N} (x, i), i) \tag {2.29}$$

for all $x \in \mathcal { X } _ { N } ( i )$ , all $i \in \mathbb { I } _ { \geq 0 }$

Lemma 2.33 (MPC cost is less than terminal cost). Suppose Assumptions 2.25, 2.26, 2.30 and 2.31 hold. Then,

$$V _ {N} ^ {0} (x, i) \leq V _ {f} (x, i) \quad \forall x \in \mathbb {X} _ {f} (i), \quad \forall i \in \mathbb {I} _ {\geq 0}$$
