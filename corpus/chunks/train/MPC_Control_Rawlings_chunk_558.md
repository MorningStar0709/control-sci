# Exercise 4.1: Input to state stability and convergence

Assume the nonlinear system

$$x ^ {+} = f (x, u)$$

is input to state stable (ISS) so that for all $\boldsymbol { x } _ { 0 } \in \mathbb { R } ^ { n }$ , input sequences u, and $k \geq 0$

$$\left| x (k; x _ {0}, \mathbf {u}) \right| \leq \beta \left(\left| x _ {0} \right|, k\right) + \gamma (\left\| \mathbf {u} \right\|)$$

in which $x ( k ; x _ { 0 } , { \mathbf { u } } )$ is the solution to the system equation at time k starting at state $x _ { 0 }$ using input sequence u, and $\gamma \in { \mathcal { K } }$ and $\beta \in \mathcal { K L }$ .

(a) Show that the ISS property also implies

$$\left| x \left(k; x _ {0}, \mathbf {u}\right) \right| \leq \beta \left(\left| x _ {0} \right|, k\right) + \gamma \left(\left\| \mathbf {u} \right\| _ {0: k}\right)$$

in which $\begin{array} { r } { \| \mathbf { u } \| _ { 0 : k } = \operatorname* { m a x } _ { 0 \leq j \leq k } \left| u ( j ) \right| . } \end{array}$ .

(b) Show that the ISS property implies the “converging-input converging-state” property (Jiang and Wang, 2001), (Sontag, 1998a, p. 330), i.e., show that if the system is ISS, then u(k) → 0 implies x(k) → 0.
