# B.8 Input/Output-to-State Stability

Consider now a system with both inputs and outputs

$$x ^ {+} = f (x, u) \quad y = h (x) \tag {B.14}$$

Input/output-to-state stability corresponds, roughly, to the statement that, no matter what the initial state is, if the input and the output converge to zero, so does the state. We assume $f ( \cdot )$ is continuous and locally Lipschitz in x on bounded u and that $h ( \cdot )$ is continuously differentiable. We also assume $f ( 0 , 0 ) = 0$ and $h ( 0 ) = 0$ . Let $x ( \cdot , x _ { 0 } , { \bf u } )$ denote the solution of (B.14) which results from initial state $x _ { 0 }$ and control $\mathbf { u } = \{ u ( j ) \}$ and let $\begin{array} { r } { y _ { x _ { 0 } , \mathbf { u } } ( k ) = y ( k ; x _ { 0 } , \mathbf { u } ) } \end{array}$ denote $h ( x ( k ; x _ { 0 } , { \mathbf { u } } ) )$ .

Definition B.42 (Input/output-to-state stable (IOSS)). The system (B.14) is input/output-to-state stable (IOSS) if there exist functions $\beta ( \cdot ) \in \mathcal { K L }$ and $\gamma _ { 1 } ( \cdot ) , \gamma _ { 2 } ( \cdot ) \in \mathcal { K }$ such that

$$\left| x (k; x _ {0}) \right| \leq \max \left\{\beta \left(\left| x _ {0} \right|, k\right), \gamma_ {1} \left(\left\| \mathbf {u} \right\| _ {0: k - 1}\right), \gamma_ {2} \left(\left\| \mathbf {y} \right\| _ {0: k}\right) \right\}$$

for every initial state $\boldsymbol { x } _ { 0 } \in \mathbb { R } ^ { n }$ , every control sequence $\mathbf { u } = \{ u ( j ) \}$ , and all $k \geq 0$ .

Definition B.43 (IOSS-Lyapunov function). An IOSS-Lyapunov function for system (B.14) is any function V (·) with the following properties:

(a) There exist ${ \mathcal K } _ { \infty }$ -functions $\alpha _ { 1 } ( \cdot )$ and $\alpha _ { 2 } ( \cdot )$ such that

$$\alpha_ {1} (x) \leq V (x) \leq \alpha_ {2} (x)$$

for all x in $\mathbb { R } ^ { n }$ .

(b) There exist K∞-functions α(·) and $\sigma ( \cdot )$ such that for every trajectory $\{ x ( k ) \} , x ( k ) = x ( k ; x _ { 0 } , { \bf u } )$ , and all $k \geq 0$ either

$$
\begin{array}{l} V (x (k + 1; x _ {0}, \mathbf {u})) - V (x (k; x _ {0}, \mathbf {u})) \leq - \alpha (| x (k; x _ {0}, \mathbf {u}) |) + \sigma_ {1} (| u (k) |) \\ + \sigma_ {2} (\left| y (k; x _ {0}, \mathbf {u}) \right|) \\ \end{array}
$$

or

$$V (x (k + 1; x _ {0}, \mathbf {u})) \leq \rho V (x (k; x _ {0}, \mathbf {u})) \leq + \sigma_ {1} (| u (k) |) + \sigma_ {2} (| y (k; x _ {0}, \mathbf {u}) |)$$

Conjecture B.44 (IOSS and IOSS-Lyapunov function). The following properties are equivalent for system (B.14):

(a) The system is IOSS.   
(b) The system admits a smooth IOSS-Lyapunov function.   
(c) The system admits an exponential-decay IOSS-Lyapunov function.
