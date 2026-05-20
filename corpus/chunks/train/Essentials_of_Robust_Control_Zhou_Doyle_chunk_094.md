# 4.1 Hilbert Spaces

Recall the inner product of vectors defined on a Euclidean space $\mathbb { C } ^ { n }$ :

$$
\langle x, y \rangle := x ^ {*} y = \sum_ {i = 1} ^ {n} \bar {x} _ {i} y _ {i} \quad \forall x = \left[ \begin{array}{c} x _ {1} \\ \vdots \\ x _ {n} \end{array} \right], y = \left[ \begin{array}{c} y _ {1} \\ \vdots \\ y _ {n} \end{array} \right] \in \mathbb {C} ^ {n}.
$$

Note that many important metric notions and geometrical properties, such as length, distance, angle, and the energy of physical systems, can be deduced from this inner product. For instance, the length of a vector $x \in \mathbb { C } ^ { n }$ is defined as

$$\| x \| := \sqrt {\langle x , x \rangle}$$

and the angle between two vectors $x , y \in \mathbb { C } ^ { n }$ can be computed from

$$\cos \angle (x, y) = \frac {\langle x , y \rangle}{\| x \| \| y \|}, \angle (x, y) \in [ 0, \pi ].$$

The two vectors are said to be orthogonal if $\begin{array} { r } { \angle ( x , y ) = \frac { \pi } { 2 } } \end{array}$ .

We now consider a natural generalization of the inner product on $\mathbb { C } ^ { n }$ to more general (possibly infinite dimensional) vector spaces.

Definition 4.1 Let V be a vector space over C. An inner product1 on V is a complexvalued function,

$$\langle \cdot , \cdot \rangle : V \times V \longmapsto \mathbb {C}$$

such that for any $x , y , z \in V$ and $\alpha , \beta \in \mathbb { C }$

(i) $\langle x , \alpha y + \beta z \rangle = \alpha \langle x , y \rangle + \beta \langle x , z \rangle$

(ii) $\langle x , y \rangle = { \overline { { \langle y , x \rangle } } }$

(iii) $\langle x , x \rangle > 0 { \mathrm { ~ i f ~ } } x \neq 0 .$ .

A vector space V with an inner product is called an inner product space.

It is clear that the inner product defined above induces a norm $\| x \| : = { \sqrt { \langle x , x \rangle } }$ , so that the norm conditions in Chapter 2 are satisfied. In particular, the distance between vectors x and y is $d ( x , y ) = \| x - y \|$ .

Two vectors x and y in an inner product space V are said to be orthogonal if $\langle x , y \rangle = 0$ , denoted $x \perp y$ . More generally, a vector x is said to be orthogonal to a set $S \subset V$ , denoted by $x \perp S .$ , if $x \perp y$ for all $y \in S$ .

The inner product and the inner product induced norm have the following familiar properties.

Theorem 4.1 Let V be an inner product space and let $x , y \in V$ . Then

(i) $| \langle x , y \rangle | \leq \| x \| \| y \|$ (Cauchy-Schwarz inequality). Moreover, the equality holds if and only $i f x = \alpha y$ for some constant α or $y = 0$ .
