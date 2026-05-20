# B.10 Observability

Definition B.46 (Observability). The system (B.14) is (uniformly) observable if there exists a positive integer N and an $\alpha ( \cdot ) \in \mathcal K$ such that

$$\sum_ {j = 0} ^ {k - 1} \left| h (x (j; x, u)) - h (x (j; z, u)) \right| \geq \alpha (| x - z |) \tag {B.15}$$

for all $x , z ,$ , all $k \geq N$ and all control sequences u; here $x ( j ; z , u ) ~ =$ $\phi ( j ; z , u )$ , the solution of (B.14) when the initial state is z at time 0 and the control sequence is u.

When the system is linear, i.e., $f ( x , u ) = A x + B u$ and $h ( x ) = C x$ , this assumption is equivalent to assuming the observability Gramian $\textstyle \sum _ { j = 0 } ^ { n - 1 } C A ^ { j } ( A ^ { j } ) ^ { \prime } C ^ { \prime }$ is positive definite. Consider the system described by

$$z ^ {+} = f (z, u) + w \quad y + v = h (z) \tag {B.16}$$

with output $y _ { w } = y + \nu$ . Let $z ( k ; z , u , w )$ denote the solution, at time k of (B.16) if the state at time 0 is z, the control sequence is u and the disturbance sequence is w. We assume, in the sequel, that

Assumption B.47 (Lipschitz continuity of model).

(a) The function $f ( \cdot )$ is globally Lipschitz continuous in $\mathbb { R } ^ { n } \times \mathbf { U }$ with Lipschitz constant c.

(b) The function h(·) is globally Lipschitz continuous in $\mathbb { R } ^ { n }$ with Lipschitz constant c.

Lemma B.48 (Lipschitz continuity and state difference bound). Suppose Assumption $B . 4 7$ is satisfied (with Lipschitz constant c). Then,

$$\left| x (k; x, u) - z (k; z, u, w) \right| \leq c ^ {k} | x - z | + \sum_ {i = 0} ^ {k - 1} c ^ {k - i - 1} | w (i) |$$

Proof. Let $\delta ( k ) : = | x ( k ; x , u ) - z ( k ; z , u , w )$ |. Then

$$
\begin{array}{l} \delta (k + 1) = \left| f (x (k; x, u), u (k)) - f (z (k; z, u, w), u (k)) - w (k) \right| \\ \leq c | \delta (k) | + | w (k) | \\ \end{array}
$$

Iterating this equation yields the desired result.

Theorem B.49 (Observability and convergence of state). Suppose (B.14) is (uniformly) observable and that Assumption $B . 4 7$ is satisfied. Then, $w ( k ) \to 0$ and v(k) → 0 as k → ∞ imply $| x ( k ; x , u ) - z ( k ; z , u , w ) | \to 0$ as $k  \infty$ .

Proof. Let $x ( k )$ and $z ( k )$ denote $x ( k ; x , u )$ and $z ( k ; z , u , w )$ , respectively, in the sequel. Since (B.14) is observable, there exists an integer

N satisfying (B.15). Consider the sum

$$
\begin{array}{l} S (k) = \sum_ {j = k} ^ {k + N} v (k) = \sum_ {j = k} ^ {k + N} | h (x (j; x, u)) - h (z (j; z, u, w)) | \\ \geq \sum_ {j = k} ^ {k + N} | h (x (j; x (k), u)) - h (x (j; z (k), u)) | \\ - \sum_ {j = k} ^ {k + N} | h (x (j; z (k), u)) - h (z (j; z (k), u, w)) | \tag {B.17} \\ \end{array}
$$
