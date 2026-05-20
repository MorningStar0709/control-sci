Let us suppose that $d ( \lambda )$ , a polynomial in l, is the greatest common divisor of all the elements of $\operatorname { a d j } ( \lambda \mathbf { I } - \mathbf { A } )$ . Show that, if the coefficient of the highest-degree term in l of $d ( \lambda )$ is chosen as 1, then the minimal polynomial $\phi ( \lambda )$ is given by

$$\phi (\lambda) = \left| \frac {\lambda \mathbf {I} - \mathbf {A}}{d (\lambda)} \right|$$

Solution. By assumption, the greatest common divisor of the matrix adj(lI-A) is d(l).Therefore,

$$\operatorname{adj} (\lambda \mathbf {I} - \mathbf {A}) = d (\lambda) \mathbf {B} (\lambda)$$

where the greatest common divisor of the $n ^ { 2 }$ elements (which are functions of l) of B(l) is unity. Since

$$(\lambda \mathbf {I} - \mathbf {A}) \operatorname{adj} (\lambda \mathbf {I} - \mathbf {A}) = | \lambda \mathbf {I} - \mathbf {A} | \mathbf {I}$$

we obtain

$$d (\lambda) (\lambda \mathbf {I} - \mathbf {A}) \mathbf {B} (\lambda) = | \lambda \mathbf {I} - \mathbf {A} | \mathbf {I} \tag {9-98}$$

from which we find that $| \lambda \mathbf { I } - \mathbf { A } |$ is divisible by d(l). Let us put

$$\left| \lambda \mathbf {I} - \mathbf {A} \right| = d (\lambda) \psi (\lambda) \tag {9-99}$$

Because the coefficient of the highest-degree term in l of $d ( \lambda )$ has been chosen to be 1, the coefficient of the highest-degree term in l of $\psi ( \lambda )$ is also 1. From Equations (9–98) and (9–99), we have

$$(\lambda \mathbf {I} - \mathbf {A}) \mathbf {B} (\lambda) = \psi (\lambda) \mathbf {I}$$

Hence,

$$\psi (\mathbf {A}) = \mathbf {0}$$

Note that c(l) can be written as

$$\psi (\lambda) = g (\lambda) \phi (\lambda) + \alpha (\lambda)$$

where $\alpha ( \lambda )$ is of lower degree than $\phi ( \lambda )$ . Since c(A)=0 and f(A)=0, we must have $\alpha ( \mathbf { A } ) = \mathbf { 0 }$ . Also, since f(l) is the minimal polynomial, $\alpha ( \lambda )$ must be identically zero, or

$$\psi (\lambda) = g (\lambda) \phi (\lambda)$$

Note that because $\phi ( \mathbf { A } ) = \mathbf { 0 } { \mathrm { : } }$ , we can write

$$\phi (\lambda) \mathbf {I} = (\lambda \mathbf {I} - \mathbf {A}) \mathbf {C} (\lambda)$$

Hence,

$$\psi (\lambda) \mathbf {I} = g (\lambda) \phi (\lambda) \mathbf {I} = g (\lambda) (\lambda \mathbf {I} - \mathbf {A}) \mathbf {C} (\lambda)$$

Noting that , we obtain(lI - A)B(l) = c(l)I

$$\mathbf {B} (\lambda) = g (\lambda) \mathbf {C} (\lambda)$$
