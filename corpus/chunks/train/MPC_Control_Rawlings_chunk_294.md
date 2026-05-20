In these definitions, $x ( i ) = \phi ( i ; x , { \bf u } )$ , the solution at time i of $x ^ { + } =$ $f ( x , u )$ if the initial state is x and the control sequence is u. Let ${ \bf u } ^ { 0 } ( x , r , \hat { d } )$ denote the solution of $\mathbb { P } _ { N } ( x , r , \hat { d } )$ . The MPC control law is $\kappa _ { N } ( x , r , \hat { d } )$ , the first control in the sequence $\mathbf { u } ^ { 0 } ( x , r , \hat { d } )$ . The terminal cost function $V _ { f } ( \cdot , r , \hat { d } )$ and constraint set $\mathbb { X } _ { f } ( r , \hat { d } )$ must be chosen to satisfy suitably modified stabilizing conditions. Since both depend on $( r , { \hat { d } } )$ , the simplest option is to choose a terminal equality constraint so that

$$V _ {f} (\bar {x} (r, \hat {d}), r, \hat {d}) = 0 \qquad \mathbb {X} _ {f} (r, \hat {d}) = \{\bar {x} (r, \hat {d}) \} \subset \mathbb {X}$$

This constraint is equivalent to requiring that the terminal state is equal to $\bar { x } ( r , \hat { d } )$ in the optimal control problem $\mathbb { P } _ { N } ( x , r , \hat { d } )$ .

If $\hat { d }$ is constant, standard MPC theory shows, under suitable assumptions, that the constant target state $\bar { x } ( r , \hat { d } )$ is asymptotically stable for $x ^ { + } = f ( x , \kappa _ { N } ( x , r , \hat { d } ) )$ ) with a region of attraction $\mathcal { X } _ { N } ( r , \hat { d } ) : =$ $\{ x \mid \mathcal { U } _ { N } ( x , r , \hat { d } ) \neq \emptyset \}$ . In particular, the state x(i) of the controlled system at time i converges to $\bar { x } ( r , \hat { d } )$ as $i ~  ~ \infty$ . We now assume that the disturbance ν(i) → 0 and, consequently, that $\hat { d } ( i ) \ \to \ d _ { s }$ , $x ( i ) \to x _ { s } : = \bar { x } ( r , d _ { s } ) , \mathrm { a n d } u ( i ) \to u _ { s } : = \bar { u } ( r , d _ { s } )$ as $i  \infty$ . Hence $y ( i ) = h ( x ( i ) ) + \hat { d } ( i ) + \nu ( i )  h ( x _ { s } ) + d _ { s }$ as $i  \infty$ . It follows from the difference equations for x and dˆ that

$$x _ {s} = f (x _ {s}, u _ {s}) \quad L (y _ {s} - h (x _ {s}) - d _ {s}) = 0$$

If L is invertible (y and d have the same dimension), it follows that

$$x _ {s} = f (x _ {s}, u _ {s}) \quad y _ {s} = h (x _ {s}) + d _ {s}$$

But, since $x _ { s } : = \bar { x } ( r , d _ { s } )$ and $u _ { s } : = \bar { u } ( r , d _ { s } )$ , it follows, by definition, that

$$h (x _ {s}) + d _ {s} = r$$

Hence $\begin{array} { r } { y ( i )  y _ { s } = r } \end{array}$ as $i  \infty ;$ ; the offset is asymptotically zero.

If we do not assume that $\hat { d }$ converges to a constant value, however, uncertainty in the evolution of $\hat { d }$ may cause the value function $V _ { N } ^ { 0 } ( x , r , { \hat { d } } )$ to increase sufficiently often to destroy stability. Robust output MPC, discussed in Chapter 5, may have to be employed to ensure stability of a set rather than a point.
