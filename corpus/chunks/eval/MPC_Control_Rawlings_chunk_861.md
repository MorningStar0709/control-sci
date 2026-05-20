To see how the singular normal arises, let the scalar random variable $\xi$ be distributed normally with zero mean and positive definite covariance, $\xi \sim N ( 0 , P _ { x } )$ , and consider the simple linear transformation

$$
\eta = A \xi \qquad A = \left[ \begin{array}{c} 1 \\ 1 \end{array} \right]
$$

in which we have created two identical copies of $\xi$ for the two components $\eta _ { 1 }$ and $\eta _ { 2 }$ of $\eta .$ . Now consider the density of $\eta .$ . If we try to use the standard formulas for transformation of a normal, we would have

$$
\eta \sim N (0, P _ {y}) \qquad P _ {y} = A P _ {x} A ^ {\prime} = \left[ \begin{array}{c c} P _ {x} & P _ {x} \\ P _ {x} & P _ {x} \end{array} \right]
$$

and $P _ { y }$ is singular since its rows are linearly dependent. Therefore one of the eigenvalues of $P _ { y }$ is zero and $P _ { y }$ is positive semidefinite and not positive definite. Obviously we cannot use (A.22) for the density in this case because the inverse of $P _ { y }$ does not exist. To handle these cases, we first provide an interpretation that remains valid when the covariance matrix is singular and semidefinite.

Definition A.37 (Density of a singular normal). A singular joint normal density of random variables $( \xi _ { 1 } , \xi _ { 2 } ) , \xi _ { 1 } \in \mathbb { R } ^ { n _ { 1 } } , \xi _ { 2 } \in \mathbb { R } ^ { n _ { 2 } }$ , is denoted

$$
\left[ \begin{array}{c} \xi_ {1} \\ \xi_ {2} \end{array} \right] \sim N \Big [ \left[ \begin{array}{c} m _ {1} \\ m _ {2} \end{array} \right], \left[ \begin{array}{c c} \Lambda_ {1} & 0 \\ 0 & 0 \end{array} \right] \Big ]
$$

with $\Lambda _ { 1 } > 0$ . The density is defined by

$$p _ {\xi} \left(x _ {1}, x _ {2}\right) = \frac {1}{(2 \pi) ^ {\frac {n _ {1}}{2}} (\det \Lambda_ {1}) ^ {\frac {1}{2}}} \exp \left[ - \frac {1}{2} \left| x _ {1} - m _ {1}\right) \mid_ {\Lambda_ {1} ^ {- 1}} ^ {2} \right] \delta \left(x _ {2} - m _ {2}\right) \tag {A.23}$$
