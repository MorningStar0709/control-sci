# B.6 Input-to-State Stability

We consider, as in the previous section, the system

$$x ^ {+} = f (x, w)$$

where the disturbance w takes values in $\mathbb { R } ^ { p }$ . In input-to-state stability (Sontag and Wang, 1995; Jiang and Wang, 2001) we seek a bound on the state in terms of a uniform bound on the disturbance sequence w := $\{ w ( 0 ) , w ( 1 ) , \ldots \}$ . Let k·k denote the usual $\ell _ { \infty }$ norm for sequences, i.e., $\left\| \mathbf { w } \right\| : = \operatorname* { s u p } _ { k \geq 0 } \left| w ( k ) \right|$ .

Definition B.33 (Input-to-state stable (ISS)). The system $x ^ { + } = f ( x , w )$ is (globally) input-to-state stable (ISS) if there exists a $\mathcal { K L }$ function $\beta ( \cdot )$ and a K function $\sigma ( \cdot )$ such that, for each $\boldsymbol { x } \in \mathbb { R } ^ { n }$ , and each disturbance sequence $\mathbf { w } = \{ w ( 0 ) , w ( 1 ) , \ldots \}$ in $\ell _ { \infty }$

$$| \phi (i; x, \mathbf {w} _ {i}) | \leq \beta (| x |, i) + \sigma (\| \mathbf {w} _ {i} \|)$$

for all $i \in \mathbb { I } _ { \geq 0 }$ , where $\phi ( i ; x , \mathbf { w } _ { i } )$ is the solution, at time i, if the initial state is x at time 0 and the input sequence is $\mathbf { w } _ { i } : = \{ w ( 0 ) , w ( 1 ) , \ldots , w ( i -$ 1)}.

We note that this definition implies the origin is globally asymptotically stable if the input sequence is identically zero. Also, the norm of the state is asymptotically bounded by $\sigma ( { \| \mathbf { w } \| } )$ where $\mathbf { w } : = \{ w ( 0 )$ , $w ( 1 ) , \ldots \}$ . As before, we seek a Lyapunov function that ensures inputto-state stability.

Definition B.34 (ISS-Lyapunov function). A function $V : \mathbb { R } ^ { n }  \mathbb { R } _ { \geq 0 }$ is an ISS-Lyapunov function for system $x ^ { + } = f ( x , w )$ if there exist $\mathcal { K } _ { \infty }$ functions $\alpha _ { 1 } ( \cdot ) , \alpha _ { 2 } ( \cdot ) , \alpha _ { 3 } ( \cdot )$ and a K function $\sigma ( \cdot )$ such that for all $\boldsymbol { x } \in \mathbb { R } ^ { n }$

$$V (| x |) \geq \alpha_ {1} (| x |)V (| x |) \leq \alpha_ {2} (| x |)V (f (x, w)) - V (x) \leq - \alpha_ {3} (| x |) + \sigma (| w |) \forall w \in \mathbb {R} ^ {p}$$

The following result appears in Jiang and Wang (2001), Lemma 3.5:

Lemma B.35 (ISS-Lyapunov function implies ISS). Suppose $f ( \cdot )$ is continuous and that there exists a continuous ISS-Lyapunov function for $x ^ { + } = f ( x , w )$ . Then the system $x ^ { + } = f ( x , w )$ is ISS.
