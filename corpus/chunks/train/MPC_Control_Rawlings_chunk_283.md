The basic idea behind the suboptimal model predictive controller is simple. Suppose that the current state is x and that ${ \bf u } = \{ u ( 0 ) , u ( 1 ) , \ldots \}$ , $u ( N - 1 ) \} \in { \mathcal { U } } _ { N } ( x )$ is a feasible control sequence for $\mathbb { P } _ { N } ( x )$ . The first element u(0) of u is applied to the system $x ^ { + } = f ( x , u )$ . In the absence of uncertainty, the next state is equal to the predicted state $x ^ { + } = f ( x , u ( 0 ) )$ . Consider the control sequence ${ \bf u } ^ { + }$ defined by

$$\mathbf {u} ^ {+} = \{u (1), u (2), \dots , u (N - 1), \kappa_ {f} (x (N)) \} \tag {2.40}$$

in which $x ( N ) = \phi ( N ; x , { \bf u } )$ and $\kappa _ { f } ( \cdot )$ is a local control law with the property that $u = \kappa _ { f } ( x )$ satisfies Assumption 2.12 for all $x \in \mathbb { X } _ { f }$ . The existence of such a $\kappa _ { f } ( \cdot )$ , which is usually of the form $K _ { f } ( x ) = K x$ , is implied by Assumption 2.12. Then, as shown in Section 2.4.3, the control sequence ${ \mathbf { u } } ^ { + } \in \mathcal { U } _ { N } ( x )$ satisfies

$$V _ {N} \left(x ^ {+}, \mathbf {u} ^ {+}\right) + \ell (x, u (0)) \leq V _ {N} (x, \mathbf {u}) \tag {2.41}$$

and, hence

$$V _ {N} \left(x ^ {+}, \mathbf {u} ^ {+}\right) \leq V _ {N} (x, \mathbf {u}) - \alpha_ {1} (| x |) \tag {2.42}$$
