We now define what we mean by the derivative of $f ( \cdot )$ . Let $f : \mathbb { R } ^ { n } \to$ $\mathbb { R } ^ { m }$ be a continuous function with domain Rn. We say that $f ( \cdot )$ is differentiable at xˆ if there exists a matrix $D f ( \hat { x } ) \in \mathbb { R } ^ { m \times n }$ (the Jacobian) such that

$$\lim _ {h \rightarrow 0} \frac {\left| f (\hat {x} + h) - f (\hat {x}) - D f (\hat {x}) h \right|}{| h |} = 0$$

in which case $D f ( \cdot )$ is called the derivative of $f ( \cdot )$ at $\hat { x } .$ . When $f ( \cdot )$ is differentiable at all $\boldsymbol { x } \in \mathbb { R } ^ { n }$ , we say that f is differentiable.

We note that the affine function $h \mapsto f ( { \hat { x } } ) + D f ( { \hat { x } } ) h$ is a first order approximation of $f ( { \hat { x } } + h )$ . The Jacobian can be expressed in terms of the partial derivatives of $f ( \cdot )$ .

Proposition A.8 (Derivative and partial derivative). Suppose that the function $f : \mathbb { R } ^ { n }  \mathbb { R } ^ { m }$ is differentiable at xˆ. Then its derivative $D f ( { \hat { x } } )$ satisfies

$$D f (\hat {x}) = f _ {x} (\hat {x}) := \partial f (\hat {x}) / \partial x$$

Proof. From the definition of $D f ( { \hat { x } } )$ we deduce that for each $i \in \left\{ { 1 , 2 , \dots , m } \right\}$

$$\lim _ {h \rightarrow 0} \frac {\left| f _ {i} (\hat {x} + h) - f _ {i} (\hat {x}) - D f _ {i} (\hat {x}) h \right|}{| h |} = 0$$

where $f _ { i }$ is the ith element of $f$ and $( D f ) _ { i }$ the ith row of $D f$ . Set $h = t e _ { j }$ , where $e _ { j }$ is the j-th unit vector in $\mathbb { R } ^ { n }$ so that $| h | = t$ . Then $( D f ) _ { i } ( \hat { x } ) h = t ( D f ) _ { i } ( \hat { x } ) e _ { j } = ( D f ) _ { i j } ( \hat { x } )$ , the ijth element of the matrix $D f ( { \hat { x } } )$ . It then follows that

$$\lim _ {t \searrow 0} \frac {\left| f ^ {i} (\hat {x} + t e _ {j}) - f (\hat {x}) - t (D f) _ {i j} (\hat {x}) \right|}{t} = 0$$

which shows that $( D f ) _ { i j } ( \hat { x } ) = \partial f _ { i } ( \hat { x } ) / \partial x _ { j }$ .

A function $f : \mathbb { R } ^ { n }  \mathbb { R } ^ { m }$ is locally Lipschitz continuous at $\hat { x }$ if there exist $L \in [ 0 , \infty ) , \hat { \rho } > 0$ such that

$$\left| f (x) - f \left(x ^ {\prime}\right) \right| \leq L \left| x - x ^ {\prime} \right|, \text { for all } x, x ^ {\prime} \in B (\hat {x}, \hat {\rho})$$
