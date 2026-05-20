Theorem 12 (Lyapunov function and $\mathrm { G A S } )$ . Suppose $V ( \cdot )$ is a Lyapunov function for $x ^ { + } = f ( x )$ and set A with $\alpha _ { 3 } ( \cdot )$ a $\mathcal { K } _ { \infty }$ function. Then A is globally asymptotically stable under Definition 9.

Proof. From (B.4) of Definition B.10, we have that

$$V (\phi (i + 1; x)) \leq V (\phi (i; x)) - \alpha_ {3} (\left| \phi (i; x) \right| _ {\mathcal {A}}) \quad \forall x \in \mathbb {R} ^ {n} \quad i \in \mathbb {I} _ {\geq 0}$$

Using (B.3) we have that

$$\alpha_ {3} (| x | _ {\mathcal {A}}) \geq \alpha_ {3} \circ \alpha_ {2} ^ {- 1} (V (x)) \quad \forall x \in \mathbb {R} ^ {n}$$

Combining these we have that

$$V (\phi (i + 1; x)) \leq \sigma_ {1} (V (\phi (i; x))) \quad \forall x \in \mathbb {R} ^ {n} \quad i \in \mathbb {I} _ {\geq 0}$$

in which

$$\sigma_ {1} (\cdot) := (\cdot) - \alpha_ {3} \circ \alpha_ {2} ^ {- 1} (\cdot)$$

We have that $\sigma _ { 1 } ( \cdot )$ is continuous on $\mathbb { R } _ { \ge 0 } , \sigma _ { 1 } ( 0 ) = 0$ , and $0 < \sigma _ { 1 } ( s ) < s$ for $s > 0$ . But $\sigma _ { 1 } ( \cdot )$ may not be increasing. We modify $\sigma _ { 1 }$ to achieve this property in two steps. First define

$$\sigma_ {2} (s) := \max _ {s ^ {\prime} \in [ 0, s ]} \sigma_ {1} \left(s ^ {\prime}\right) \quad s \in \mathbb {R} _ {\geq 0}$$

in which the maximum exists for each $s \in \mathbb { R } _ { \geq 0 }$ because $\sigma _ { 1 } ( \cdot )$ is continuous. By its definition, $\sigma _ { 2 } ( \cdot )$ is nondecreasing, and we next show that $\sigma _ { 2 } ( \cdot )$ is continuous on $\mathbb { R } _ { \geq 0 }$ . Assume that $\sigma _ { 2 } ( \cdot )$ is discontinuous at a point $c \in \mathbb { R } _ { \geq 0 }$ . Because it is a nondecreasing function, there is a positive jump in the function $\sigma _ { 2 } ( \cdot )$ at c (Bartle and Sherbert, 2000, p. 150). Define 5

$$a _ {1} := \lim _ {s \nearrow c} \sigma_ {2} (s) \quad a _ {2} := \lim _ {s \searrow c} \sigma_ {2} (s)$$

We have that $\sigma _ { 1 } ( c ) \ : \le \ : a _ { 1 } \ : < \ : a _ { 2 }$ or we violate the limit of $\sigma _ { 2 }$ from below. Since $\sigma _ { 1 } ( c ) < a _ { 2 } , \sigma _ { 1 } ( s )$ must achieve value $\boldsymbol { a } _ { 2 }$ for some $s < c$ or we violate the limit from above. But $\sigma _ { 1 } ( s ) = a _ { 2 }$ for $s < c$ also violates the limit from below, and we have a contradiction and $\sigma _ { 2 } ( \cdot )$ is continuous. Finally, define

$$\sigma (s) := (1 / 2) \left(s + \sigma_ {2} (s)\right) \quad s \in \mathbb {R} _ {\geq 0}$$
