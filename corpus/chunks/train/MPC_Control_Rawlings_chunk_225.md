in which $x ^ { 0 } ( 1 ; x ) = x ^ { + } = f ( x , \kappa _ { N } ( x ) )$ ; since there are no state or terminal constraints, the state sequence $\tilde { \mathbf { x } }$ is clearly feasible if $u \in \mathbb { U }$ . Since $\mathbf { x } ^ { 0 }$ coincides with $\tilde { \mathbf { x } }$ and u(·) coincides with u for $i = 1 , 2 , \ldots , N - 1$ (but not for $i = N )$ , a simple calculation yields

$$
\begin{array}{l} V _ {N} ^ {0} (x) = V _ {N} (x, \mathbf {u} ^ {0} (x)) \\ = \ell (x, \kappa_ {N} (x)) + \sum_ {j = 1} ^ {N - 1} \ell (x ^ {0} (j; x), u ^ {0} (j; x)) + V _ {f} (x ^ {0} (N; x)) \\ \end{array}
$$

so that

$$
\begin{array}{l} V _ {N} (x ^ {+}, \tilde {\mathbf {u}}) = V _ {N} ^ {0} (x) - \ell (x, \kappa_ {N} (x)) - V _ {f} (x ^ {0} (N; x)) + \\ \ell (x ^ {0} (N; x), u) + V _ {f} (f (x ^ {0} (N; x), u)) \\ \end{array}
$$

in which $x ^ { + } = f ( x , \kappa _ { N } ( x ) )$ . Since $V _ { N } ^ { 0 } ( x ^ { + } ) \le V _ { N } ( x ^ { + } , \widetilde { \mathbf { u } } )$ , it follows that

$$V _ {N} ^ {0} (f (x, \kappa_ {N} (x))) - V _ {N} ^ {0} (x) \leq - \ell (x, \kappa_ {N} (x)) \tag {2.18}$$

for all $\boldsymbol { x } \in \mathbb { R } ^ { n }$ provided that for all $\boldsymbol { x } \in \mathbb { R } ^ { n }$ , there exists a $u \in \mathbb { U }$ such that

$$V _ {f} (f (x, u)) - V _ {f} (x) + \ell (x, u) \leq 0 \tag {2.19}$$

A continuous positive definite function $V _ { f } ( \cdot )$ satisfying inequality (2.19) for all $\boldsymbol { x } \in \mathbb { R } ^ { n }$ with a positive definite $\ell ( \cdot )$ is a global control-Lyapunov function (CLF). If $V _ { f } ( \cdot )$ is a global CLF, the value function $V _ { N } ^ { 0 } ( \cdot )$ has the desired descent property (2.18). Global asymptotic stability of the origin for the system $x ^ { + } = f ( x , \kappa _ { N } ( x ) )$ under MPC may be established. If $V _ { f } ( \cdot )$ is a global CLF satisfying (2.19), however, there exists a control law $\kappa _ { f } ( \cdot )$ satisfying $V _ { f } ( f ( x , \kappa _ { f } ( x ) ) ) ~ \le ~ V _ { f } ( x ) - \ell ( x , \kappa _ { f } ( x ) )$ for all $x \in \mathbb { R } ^ { n }$ . Global asymptotic stability of the origin for the system $x ^ { + } = f ( x , \kappa _ { f } ( x ) )$ may be established. In this case MPC is not required to stabilize the system, though it may provide superior performance.
