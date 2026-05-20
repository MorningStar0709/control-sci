where $u ( 0 )$ is the first element in u. Stability of the origin can be established using (2.42), (2.43) and the properties of $V _ { f } ( \cdot )$ as shown subsequently. Inequality (2.43) is achieved quite simply by using the control law $u = \kappa _ { f } ( x )$ to generate the control u when $\boldsymbol { x } \in \mathbb { X } _ { f }$ . Let $\mathbf { x } ( x ; \kappa _ { f } )$ and ${ \bf { u } } ( x ; \kappa _ { f } )$ denote the state and control sequences generated in this way when the initial state is x; these sequences satisfy

$$x ^ {+} = f (x, \kappa_ {f} (x)) \quad u = \kappa_ {f} (x)$$

with initial condition $x ( 0 ) = x$ , so that $x ( 0 ; x , \kappa _ { f } ) = x , x ( 1 ; x , \kappa _ { f } ) =$ $f ( x , \kappa _ { f } ( x ) ) , \ x ( 2 ; x , \kappa _ { f } ) \ = \ f ( x ( 1 ; x , \kappa _ { f } ) ) , \kappa _ { f } ( x ( 1 ; x , \kappa _ { f } ) )$ , etc. Since Assumption 2.12 is satisfied,

$$V _ {f} (x) \geq \ell (x, \kappa_ {f} (x)) + V _ {f} (f (x, \kappa_ {f} (x)))$$

which, when used iteratively, implies

$$V _ {f} (x) \geq \sum_ {i = 0} ^ {N - 1} \ell (x (i; x, \kappa_ {f}), \kappa_ {f} (x (i; x, \kappa_ {f}))) + V _ {f} (x (N; x, \kappa_ {f}))$$

Hence, for all $\boldsymbol { x } \in \mathbb { X } _ { f }$

$$
\begin{array}{l} V _ {N} (x, \mathbf {u} (x; \kappa_ {f})) = \sum_ {i = 0} ^ {N - 1} \ell (x (i; x, \kappa_ {f}), \kappa_ {f} (x (i; x, \kappa_ {f}))) + V _ {f} (x (N; x, \kappa_ {f})) \\ \leq V _ {f} (x) \\ \end{array}
$$

as required. Also, it follows from Assumption 2.12 and the definition of $\kappa _ { f } ( \cdot )$ that $x ^ { + } = f ( x , u ( 0 ) ) \in \mathbb { X } _ { f } \mathrm { i f } x \in \mathbb { X } _ { f }$ . Thus the two conditions in (2.43) are satisfied by ${ \bf { u } } ( x ; \kappa _ { f } )$ . If desired, $\mathbf { \Omega } _ { \mathbf { l } } ( x ; \kappa _ { f } )$ may be used for the current control sequence u or as a “warm start” for an optimization algorithm yielding an improved control sequence. In any case, if (2.43) is satisfied, stability of the origin may be established as follows.
