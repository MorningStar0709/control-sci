Theorem 12.2 Suppose H has no imaginary eigenvalues and R is either positive semidefinite or negative semidefinite. Then $H \in \operatorname { d o m } ( \operatorname { R i c } )$ if and only $i f \left( A , R \right)$ is stabilizable.

Proof. (⇐) To prove that $H \in \operatorname { d o m } ( \operatorname { R i c } )$ , we must show that

$$
\mathcal {X} _ {-} (H), \quad \mathrm{Im} \left[ \begin{array}{l} 0 \\ I \end{array} \right]
$$

are complementary. This requires a preliminary step. As in the proof of Theorem 12.1 define $X _ { 1 } , X _ { 2 } , H _ { - }$ so that

$$
\mathcal {X} _ {-} (H) = \mathrm{Im} \left[ \begin{array}{l} X _ {1} \\ X _ {2} \end{array} \right]

H \left[ \begin{array}{l} X _ {1} \\ X _ {2} \end{array} \right] = \left[ \begin{array}{l} X _ {1} \\ X _ {2} \end{array} \right] H _ {-}. \tag {12.7}
$$

We want to show that $X _ { 1 }$ is nonsingular $( \mathrm { i . e . }$ , Ker $X _ { 1 } = 0 )$ . First, it is claimed that Ker $X _ { 1 }$ is $H _ { - }$ invariant. To prove this, let $x \in$ Ker $X _ { 1 }$ . Premultiply equation (12.7) by $\left[ I \right] \quad 0 ]$ to get

$$A X _ {1} + R X _ {2} = X _ {1} H _ {-}. \tag {12.8}$$

Premultiply by $x ^ { * } X _ { 2 } ^ { * }$ , postmultiply by $x ,$ and use the fact that $X _ { 2 } ^ { * } X _ { 1 }$ is symmetric [see equation (12.4)] to get

$$x ^ {*} X _ {2} ^ {*} R X _ {2} x = 0.$$

Since R is semidefinite, this implies that $R X _ { 2 } x = 0$ . Now postmultiply equation (12.8) by x to get $X _ { 1 } H _ { - } x = 0 \ ( { \mathrm { i . e . , } } \ H _ { - } x \in \operatorname { K e r } X _ { 1 } )$ . This proves the claim.

Now to prove that $X _ { 1 }$ is nonsingular, suppose, on the contrary, that Ker $X _ { 1 } \neq 0$ . Then $H _ { - } | _ { \mathrm { K e r } X _ { 1 } }$ has an eigenvalue, λ, and a corresponding eigenvector, x:

$$H _ {-} x = \lambda x \tag {12.9}$$

$\mathrm { R e } \lambda < 0 , 0 \ne x \in \mathrm { K e r } X _ { 1 } .$

Premultiply equation (12.7) by [0 I]:

$$- Q X _ {1} - A ^ {*} X _ {2} = X _ {2} H _ {-}. \tag {12.10}$$

Postmultiply the above equation by x and use equation (12.9):

$$(A ^ {*} + \lambda I) X _ {2} x = 0.$$

Recall that $R X _ { 2 } x = 0 ;$ ; we have

$$x ^ {*} X _ {2} ^ {*} [ A + \overline {{\lambda}} I R ] = 0.$$

Then the stabilizability of $( A , R )$ implies $X _ { 2 } x = 0$ . But if both $X _ { 1 } x = 0$ and $X _ { 2 } x = 0$ then x = 0 since $\left[ \begin{array} { l } { X _ { 1 } } \\ { X _ { 2 } } \end{array} \right]$ has full column rank, which is a contradiction.
