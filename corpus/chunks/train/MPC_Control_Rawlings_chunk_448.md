Definition 4.1 (i-IOSS). The system $x ^ { + } = f ( x , w ) , y = h ( x )$ is incrementally input/output-to-state stable (i-IOSS) if there exists some $\beta ( \cdot ) \in$ $\mathcal { K L }$ and $\gamma _ { 1 } ( \cdot ) , \gamma _ { 2 } ( \cdot ) \in \mathcal { K }$ such that for every two initial states $z _ { 1 }$ and $z _ { 2 }$ , and any two disturbance sequences $\mathbf { w } _ { 1 }$ and $\mathbf { w } _ { 2 }$

$$
\begin{array}{l} \left| x \left(k; z _ {1}, \mathbf {w} _ {1}\right) - x \left(k; z _ {2}, \mathbf {w} _ {2}\right) \right| \leq \beta \left(\left| z _ {1} - z _ {2} \right|, k\right) + \\ \gamma_ {1} \left(\| \mathbf {w} _ {1} - \mathbf {w} _ {2} \| _ {0: k - 1}\right) + \gamma_ {2} \left(\left\| \mathbf {y} _ {z _ {1}, \mathbf {w} _ {1}} - \mathbf {y} _ {z _ {2}, \mathbf {w} _ {2}} \right\| _ {0: k}\right) \\ \end{array}
$$

The notation $x ( k ; x _ { 0 } , \mathbf { w } )$ denotes the solution to $x ^ { + } = f ( x , w )$ satisfying initial condition $x ( 0 ) ~ = ~ x _ { 0 }$ with disturbance sequence $\begin{array} { r l } { \mathbf { w } } & { { } = } \end{array}$ $\{ w ( 0 ) , w ( 1 ) , \ldots \}$ . We also require the system with an “initial” condition at a time $k _ { 1 }$ other than $k _ { 1 } = 0$ , and use the notation $x ( k ; x _ { 1 } , k _ { 1 } , \mathbf { w } )$ to denote the solution to $x ^ { + } = f ( x , w )$ satisfying the condition $x ( k _ { 1 } ) = x _ { 1 }$ with disturbance sequence $\mathbf { w } = \{ w ( 0 ) , w ( 1 ) , \ldots \}$ .

One of the most important and useful implications of the i-IOSS property is the following proposition.

Proposition 4.2 (Convergence of state under i-IOSS). If system $\begin{array} { r l } { x ^ { + } } & { { } = } \end{array}$ $f ( x , w ) , y \ = \ h ( x )$ is i-IOSS, $w _ { 1 } ( k ) \to w _ { 2 } ( k )$ and $y _ { 1 } ( k ) \to y _ { 2 } ( k )$ as $k  \infty .$ , then

$$x (k; z _ {1}, \mathbf {w} _ {1}) \rightarrow x (k; z _ {2}, \mathbf {w} _ {2}) \quad a s k \rightarrow \infty \quad f o r a l l z _ {1}, z _ {2}$$

The proof of this proposition is discussed in Exercise 4.3.

The class of disturbances (w, v) affecting the system is defined next. Often we assume these are random variables with stationary probability densities, and often zero-mean normal densities. When we wish to establish estimator stability, however, we wish to show that if the disturbances affecting the measurement converge to zero, then the estimate error also converges to zero. So here we restrict attention to convergent disturbances.
