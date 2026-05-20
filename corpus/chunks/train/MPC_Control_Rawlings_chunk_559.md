# Exercise 4.2: Output to state stability and convergence

Assume the nonlinear system

$$x ^ {+} = f (x) \quad y = h (x)$$

is output to state stable (OSS) so that for all $x _ { 0 } \in \mathbb { R } ^ { n }$ and $k \geq 0$

$$\left| x (k; x _ {0}) \right| \leq \beta \left(\left| x _ {0} \right|, k\right) + \gamma \left(\left\| \mathbf {y} \right\| _ {0: k}\right)$$

in which $x ( k ; x _ { 0 } )$ is the solution to the system equation at time k starting at state $x _ { 0 }$ , and $\gamma \in \mathcal { K }$ and $\beta \in \mathcal { K L }$ .

Show that the OSS property implies the “converging-output converging-state” property (Sontag and Wang, 1997, p. 281) i.e., show that if the system is OSS, then $y ( k ) \to 0$ implies $x ( k ) \to 0$ .
