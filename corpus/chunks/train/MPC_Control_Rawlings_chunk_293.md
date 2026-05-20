# 2.9 Tracking

in which $y - h ( x )$ may be regarded as a noisy measurement of $d ,$ , since $y - h ( x ) = d + \nu$ . The difference equation for the estimation error $\tilde { \boldsymbol { d } } : = \boldsymbol { d } - \boldsymbol { \hat { d } }$ is

$$\tilde {\boldsymbol {d}} ^ {+} = A _ {L} \tilde {\boldsymbol {d}} - L \nu$$

in which L is chosen to ensure that $A _ { L } : = I - L$ is stable. If there is zero measurement noise, $\check { d } ( i )  0$ exponentially as $i  \infty$ . Since $y - h ( x ) = d + \nu$ , the difference equation for dˆ may be written as

$$\hat {d} ^ {+} = \hat {d} + L (\tilde {\vec {d}} + \nu)$$

Since d is unknown, we have to use $\hat { d }$ for control. Hence, for the purpose of control we employ the difference equations

$$
\begin{array}{l} x ^ {+} = f (x, u) \\ \hat {d} ^ {+} = \hat {d} + L (\tilde {\vec {d}} + \nu) \\ \end{array}
$$

If $\hat { d }$ is the current estimate of $^ { d , }$ our best estimate of d at any time in the future is also $\hat { d } .$ Given the current state $( x , { \hat { d } } )$ of the composite system and the current reference r , we determine the target state and associated control by minimizing $| u | ^ { 2 }$ with respect to $( x , u )$ subject to the equality constraints

$$
\begin{array}{l} x = f (x, u) \\ r = h (x) + \hat {d} \\ \end{array}
$$

and the inequality constraints $x \in \mathbb { X }$ and $u \in \mathbb { U }$ . We assume that a solution to this problem exists and denote the solution by $( \bar { x } ( r , \hat { d } ) , \bar { u } ( r , \hat { d } ) )$ .

MPC may then be achieved by solving online the optimal control problem $\mathbb { P } _ { N } ( x , r , \hat { d } )$ defined by

$$V _ {N} ^ {0} (x, r, \hat {d}) = \min _ {\mathbf {u}} \{V _ {N} (x, r, \mathbf {u}) \mid \mathbf {u} \in \mathcal {U} _ {N} (x, r, \hat {d}) \}$$

in which the cost function $V _ { N } ( \cdot )$ and the constraint set are defined by

$$
\begin{array}{l} V _ {N} (x, r, \hat {d}, \mathbf {u}) := \sum_ {i = 0} ^ {N - 1} \ell (x (i) - \bar {x} (r, \hat {d}), u (i) - \bar {u} (r, \hat {d})) + V _ {f} (x, r, \hat {d}) \\ \mathcal {U} _ {N} (x, r, \hat {d}) := \{\mathbf {u} \mid x (i) \in \mathbb {X}, u (i) \in \mathbb {U}, \forall i \in \mathbb {I} _ {0: N - 1}; x (N) \in \mathbb {X} _ {f} (r, \hat {d}) \} \\ \end{array}
$$
