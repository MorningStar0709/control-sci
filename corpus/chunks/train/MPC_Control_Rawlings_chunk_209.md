# Example 2.6: Closer inspection of linear quadratic MPC

We revisit the MPC problem discussed in Example 2.5. The objective function is

$$V _ {N} (x, \mathbf {u}) = (1 / 2) \mathbf {u} ^ {\prime} H \mathbf {u} + c (x) ^ {\prime} \mathbf {u} + d (x)$$

where $c ( x ) ^ { \prime } = [ 2 \mathit { 1 } ] x$ and $d ( x ) = ( 3 / 2 ) x ^ { 2 }$ . The objective function may be written in the form

$$V _ {N} (x, \mathbf {u}) = (1 / 2) (\mathbf {u} - a (x)) ^ {\prime} H (\mathbf {u} - a (x)) + e (x)$$

Expanding the second form shows the two forms are equal if

$$
a (x) = - H ^ {- 1} c (x) = K _ {1} x \qquad K _ {1} = - (1 / 5) \left[ \begin{array}{c} 3 \\ 1 \end{array} \right]
$$

and

$$e (x) + (1 / 2) a (x) ^ {\prime} H a (x) = d (x)$$

Since H is positive definite, $\alpha ( x )$ is the unconstrained minimizer of the objective function; indeed $\nabla _ { \mathbf { u } } V _ { N } ( x , a ( x ) ) = 0$ since

$$\nabla_ {\mathbf {u}} V _ {N} (x, \mathbf {u}) = H \mathbf {u} + c (x)$$

The locus of $\alpha ( x )$ for $x \ge 0$ is shown in Figure 2.2. Clearly the unconstrained minimizer $a ( x ) \ = \ K _ { 1 } x$ is equal to the constrained minimizer $\mathbf { u } ^ { 0 } ( x )$ for all x such that $a ( x ) ~ \in ~ \mathcal { U } _ { 2 }$ where $\mathcal { U } _ { 2 }$ is the unit square illustrated in Figure 2.2; since $a ( x ) = K _ { 1 } x , a ( x ) \in \mathcal { U } _ { 2 }$ for all $x \in \mathbb { X } _ { 1 } = [ 0 , x _ { c 1 } ]$ where $x _ { c 1 } = 5 / 3$ . For $x \ > \ x _ { c 1 }$ , the unconstrained minimizer lies outside $\mathcal { U } _ { 2 }$ as shown in Figure 2.2 for $x = 2 . 2 5 , x = 3$ and $x = 5$ . For such $x ,$ , the constrained minimizer $\mathbf { u } ^ { 0 } ( x )$ is a point that lies on the intersection of a level set of the objective function (which is an ellipse) and the boundary of $\mathcal { U } _ { 2 }$ . For $x \in [ x _ { c 1 } , x _ { c 2 } ) , \mathbf { u } ^ { 0 } ( x )$ lies on the left face of the box $\mathcal { U } _ { 2 }$ and for $x \ge x _ { c 2 } = 3 , { \bf u } ^ { 0 } ( x )$ remains at $( - 1 , - 1 )$ , the bottom left vertex of $\mathcal { U } _ { 2 }$ .

When $u ^ { 0 } ( x )$ lies on the left face of $\mathcal { U } _ { 2 }$ , the gradient $\nabla _ { \mathbf { u } } V _ { N } ( x , { \mathbf { u } } ^ { 0 } ( x ) )$ of the objective function is normal to the left face of $\textstyle u _ { 2 } , \mathbf { i . e . }$ , the level set of $V _ { N } ^ { 0 } ( \cdot )$ passing through $\mathbf { u } ^ { 0 } ( x )$ is tangential to the left face of $\mathcal { U } _ { 2 }$ . The outward normal to $\mathcal { U } _ { 2 }$ at a point on the left face is $- e _ { 1 } = ( - 1 , 0 )$ so that at $ { \mathbf { u } } =  { \mathbf { u } } ^ { 0 } ( x )$

$$\nabla_ {\mathbf {u}} V (x, \mathbf {u} ^ {0} (x)) + \lambda (- e _ {1}) = 0$$
