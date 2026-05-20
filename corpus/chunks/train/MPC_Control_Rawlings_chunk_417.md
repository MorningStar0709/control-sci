The set $\mathcal { M } _ { N }$ is bounded. For any $( x , z ) \in \mathcal { M } _ { N }$ , the minimizing control sequence is $\mathbf { u } ^ { 0 } ( x , z ) = \{ u ^ { 0 } ( 0 ; x , z ) , u ^ { 0 } ( 1 ; x , z ) , \ldots , u ^ { 0 } ( N - 1 ; x , z ) \}$ , and the control applied to the system is $u ^ { 0 } ( 0 ; x , z )$ , the first element in this sequence. The corresponding optimal state sequence is $\mathbf { x } ^ { 0 } ( x , z ) =$ $\{ x , x ^ { 0 } ( 1 ; x , z ) , \ldots , x ^ { 0 } ( N ; x , z ) \}$ . The implicit ancillary control law is, therefore, $\kappa _ { N } ( \cdot )$ defined by

$$\kappa_ {N} (x, z) := u ^ {0} (0; x, z)$$

The composite uncertain system then satisfies

$$x ^ {+} = f (x, \kappa_ {N} (x, z)) + w \tag {3.52}z ^ {+} = f (x, \bar {\kappa} _ {N} (z)) \tag {3.53}$$

If $x = z$ , then, as is easily verified, $V _ { N } ^ { 0 } ( x , z ) = 0$ and

$$u ^ {0} (i; x, z) = v ^ {*} (i; z), i = 0, 1, \dots , N - 1$$

so that the control and state trajectories of the two systems (3.49) and (3.50) are identical. In particular

$$\kappa_ {N} (z, z) = \bar {\kappa} _ {N} (z)$$

If some controllability assumptions are satisfied, the value function $V _ { N } ^ { 0 } ( \cdot )$ has properties analogous to those of $\bar { V } _ { N } ^ { 0 } ( \cdot )$ , except that the bounds are $\mathcal { K } _ { \infty }$ functions of $x - z$ rather than of $_ x$

$$V _ {N} ^ {0} (x, z) \geq c _ {1} | x - z | ^ {2} \tag {3.54}V _ {N} ^ {0} (x, z) \leq c _ {2} | x - z | ^ {2} \tag {3.55}\Delta V _ {N} ^ {0} (x, z) \leq - c _ {1} | x - z | ^ {2} \tag {3.56}$$

for all $( x , z ) \in \mathcal { M } _ { N }$ in which, now

$$\Delta V _ {N} ^ {0} (x, z) := V _ {N} ^ {0} (f (z, \kappa_ {N} (x, z)), f (x, \bar {\kappa} _ {N} (z))) - V _ {N} ^ {0} (x, z)$$

Note that $\Delta V _ { N } ^ { 0 } ( x , z )$ is the change in the value as x changes to $x ^ { + } =$ $f ( x , \kappa _ { N } ( x , z ) )$ and z changes to $z ^ { + } ~ = ~ f ( x , \bar { \kappa } _ { N } ( z ) )$ ; the effect of the disturbance w is ignored in this expression. It follows from (3.54)- (3.56) that

$$V _ {N} ^ {0} (f (x, \kappa_ {N} (x, z)), f (z, \bar {\kappa} _ {N} (z))) \leq \gamma V _ {N} ^ {0} (x, z)$$
