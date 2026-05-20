# 3.3.3 Stability of Min-Max Receding Horizon Control

We consider in this subsection the stability properties of min-max RHC for the system $x ^ { + } ~ = ~ f ( x , u , w )$ with $\mathbb { P } _ { N } ( x )$ defined in (3.19) with $\ell ( x , u , w ) : = ( 1 / 2 ) ( | x | _ { O } ^ { 2 } + | u | _ { R } ^ { 2 } ) - ( \rho ^ { 2 } / 2 ) | w | ^ { 2 }$ and $V _ { f } ( x ) : = ( 1 / 2 ) | x | _ { P _ { f } } ^ { 2 }$ where Q, R and $P _ { f }$ are positive definite. In Section 3.3.2, we showed that max $\mathbf { \dot { \sigma } } _ { w \in \mathbb { W } } [ \Delta V _ { N } ^ { 0 } + \ell ] ( x , \kappa _ { N } ( x ) , w ) \leq 0$ for all $x \in \mathcal { X } _ { N }$ provided that Assumption 3.8 holds. We used the condition $[ \Delta V _ { N } ^ { 0 } + \ell ] ( x , \kappa _ { N } ( x ) , w ) \leq 0$ to establish asymptotic stability of the origin for a deterministic system in Chapter 2. Can we do so for the problem considered here? The answer is no; the disturbance w prevents convergence of state trajectories to the origin.

The obstacle appears in theoretical analysis as follows. Our usual conditions for establishing asymptotic stability of the origin for this problem are the existence of a Lyapunov function $V ( \cdot )$ satisfying for all $\boldsymbol { x } \in \mathcal { X } _ { N }$

(a) $V ( x ) \geq \alpha _ { 1 } ( | x | )$   
(b) $V ( x ) \leq \alpha _ { 2 } ( | x | )$   
$\begin{array} { r } { \mathrm { ( c ) } \operatorname* { m a x } _ { w \in \mathbb { W } } \Delta V ( x , \kappa _ { N } ( x ) , w ) \leq - \alpha _ { 3 } ( | x | ) } \end{array}$

in which $\alpha _ { 1 } ( \cdot )$ and $\alpha _ { 2 } ( \cdot )$ are $\mathcal { K } _ { \infty }$ functions and $\alpha _ { 3 } ( \cdot )$ is a positive definite, continuous function.
