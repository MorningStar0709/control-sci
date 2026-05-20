$$\ell (y, u) \geq \alpha_ {1} (| y |) + \alpha_ {1} (| u |) \quad V _ {f} (x) \leq \alpha_ {2} (| x |)$$

for all $( y , u )$ and all x. We also assume that the system $x ^ { + } = f ( x , u )$ , $y = h ( x )$ is IOSS and that $\mathbb { X } _ { f }$ has an interior. Under these assumptions, the value function $V _ { N } ^ { 0 } ( \cdot )$ has the following properties

$$
\begin{array}{l} V _ {N} ^ {0} (x) \geq \alpha_ {1} | h (x) | \quad \forall x \in \mathcal {X} _ {N} \\ V _ {N} ^ {0} (f (x, \kappa_ {N} (x))) \leq V _ {N} ^ {0} (x) - \alpha_ {1} (| h (x) |) \forall x \in \mathcal {X} _ {N} \\ V _ {N} ^ {0} (x) \leq \alpha_ {2} (| x |) \quad \forall x \in \mathbb {X} _ {f} \\ \end{array}
$$

That $V _ { N } ^ { 0 } ( f ( x , \kappa _ { N } ( x ) ) ) \leq V _ { N } ^ { 0 } ( x ) - \ell ( h ( x ) , \kappa _ { N } ( x ) )$ follows from the basic stability assumption. The fact that $h ( x )$ appears in the first and second inequalities instead of x complicates analysis and makes it necessary to assume the IOSS property. We require the following result:

Proposition 2.41 (Convergence of state under IOSS). Assume that the system $x ^ { + } = f ( x , u ) , y = h ( x )$ is IOSS and that $u ( i ) \to 0$ and $y ( i )  0$ as $i  \infty . \ T h e n x ( i ) = \phi ( i ; x , \mathbf { u } )  0 \ a s i  \infty$ for any initial state x.

This proof of this result is discussed in Exercise 2.16.

Given the IOSS property, one can establish that the origin is attractive for closed-loop system with a region of attraction $x _ { N }$ . For all $x \in \mathcal { X } _ { N }$ , all $i \in \mathbb { I } _ { \geq 0 }$ , let $x ( i ; x ) : = \phi ( i ; x , \kappa _ { N } ( . ) )$ , the solution at time i of $x ^ { + } = f ( x , \kappa _ { N } ( x ) )$ if the initial state is $x , y ( i ; x ) : = h ( x ( i ; x ) )$ and $u ( i ; x ) : = \kappa _ { N } ( x ( i ; x ) )$ . It follows from the properties of the value function that, for any initial state $x \in \mathcal { X } _ { N }$ , the sequence $\{ V _ { N } ^ { 0 } ( x ( i ; x ) ) \}$ is nonincreasing and bounded below by zero, so that $V _ { N } ^ { 0 } ( x ( i ; x ) ) \to c \geq 0$ as $i  \infty$ . Since $V _ { N } ^ { 0 } ( x ( i + 1 ) ) \le V _ { N } ^ { 0 } ( x ( i ) ) - \ell ( x ( i ; x ) , \mathcal { y } ( i ; x ) )$ , it follows that $\ell ( y ( i ; x ) , u ( i ; x ) ) \to 0$ and, hence, that $y ( i ; x )  0$ and $u ( i ; x ) \to 0$ as $i  \infty$ . From Proposition 2.41, $x ( i ; x ) \to 0 { \mathrm { ~ a s ~ } } i \to \infty$ for any initial state $\boldsymbol { x } \in \mathcal { X } _ { N }$ .
