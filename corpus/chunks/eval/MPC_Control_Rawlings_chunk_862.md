In this limit, the “random” variable $\xi _ { 2 }$ becomes deterministic and equal to its mean $m _ { 2 }$ . For the case $n _ { 1 } = 0$ , we have the completely degenerate case in which $p _ { \xi _ { 2 } } ( x _ { 2 } ) = \delta ( x _ { 2 } - m _ { 2 } )$ , which describes the completely deterministic case $\xi _ { 2 } \ = \ m _ { 2 }$ and there is no random component $\xi _ { 1 }$ . This expanded definition enables us to generalize the important result that the linear transformation of a normal is normal, so that it holds for any linear transformation, including rank deficient transformations such as the A matrix given above in which the rows are not independent (see Exercise 1.40). Starting with the definition of a singular normal, we can obtain the density for $\xi \sim N ( m _ { x } , P _ { x } )$ for any positive semidefinite $P _ { x } \geq 0$ . The result is

$$p _ {\xi} (x) = \frac {1}{(2 \pi) ^ {\frac {r}{2}} (\det \Lambda_ {1}) ^ {\frac {1}{2}}} \exp \left[ - \frac {1}{2} | (x - m _ {x}) | _ {Q _ {1}} ^ {2} \right] \delta \left(Q _ {2} ^ {\prime} (x - m _ {x})\right) \tag {A.24}$$

in which matrices $\boldsymbol { \Lambda } \in \mathbb { R } ^ { r \times r }$ and orthonormal $Q \in \mathbb { R } ^ { n \times n }$ are obtained from the eigenvalue decomposition of $P _ { x }$

$$
P _ {x} = Q \Lambda Q ^ {\prime} = \left[ \begin{array}{c c} Q _ {1} & Q _ {2} \end{array} \right] \left[ \begin{array}{c c} \Lambda_ {1} & 0 \\ 0 & 0 \end{array} \right] \left[ \begin{array}{c} Q _ {1} ^ {\prime} \\ Q _ {2} ^ {\prime} \end{array} \right]
$$

and $\Lambda _ { 1 } > 0 \in \mathbb { R } ^ { r \times r } , Q _ { 1 } \in \mathbb { R } ^ { n \times r } , Q _ { 2 } \in \mathbb { R } ^ { n \times ( n - r ) }$ . This density is nonzero for x satisfying $Q _ { 2 } ^ { \prime } ( x - m _ { x } ) ~ = ~ 0$ . If we let $N ( Q _ { 2 } ^ { \prime } )$ denote the $r$ dimensional nullspace of $Q _ { 2 } ^ { \prime }$ , we have that the density is nonzero for $x \in N ( Q _ { 2 } ^ { \prime } ) \oplus \{ m _ { x } \}$ in which ⊕ denotes set addition.
