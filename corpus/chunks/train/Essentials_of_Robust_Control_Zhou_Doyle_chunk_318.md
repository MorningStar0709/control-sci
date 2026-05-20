$$
A = \left[ \begin{array}{l l} 1 & 0 \\ 0 & 2 \end{array} \right], B = \left[ \begin{array}{l} 1 \\ 1 \end{array} \right], C = \left[ \begin{array}{l l} 0 & 0 \end{array} \right].
$$

Then (A, B) is stabilizable, but (C, A) is not detectable. However,

$$
X = \left[ \begin{array}{c c} {1 8} & {- 2 4} \\ {- 2 4} & {3 6} \end{array} \right] > 0
$$

is the stabilizing solution.

Corollary 12.5 Suppose that (A, B) is stabilizable and $( C , A )$ is detectable. Then the Riccati equation

$$A ^ {*} X + X A - X B B ^ {*} X + C ^ {*} C = 0$$

has a unique positive semidefinite solution. Moreover, the solution is stabilizing.

Proof. It is obvious from the preceding theorem that the Riccati equation has a unique stabilizing solution and that the solution is positive semidefinite. Hence we only need to show that any positive semidefinite solution $X \geq 0$ must also be stabilizing. Then by the uniqueness of the stabilizing solution, we can conclude that there is only one positive semidefinite solution. To achieve that goal, let us assume that $X \geq 0$ satisfies the Riccati equation but that it is not stabilizing. First rewrite the Riccati equation as

$$(A - B B ^ {*} X) ^ {*} X + X (A - B B ^ {*} X) + X B B ^ {*} X + C ^ {*} C = 0 \tag {12.15}$$

and let λ and $x$ be an unstable eigenvalue and the corresponding eigenvector of $A - B B ^ { * } X$ , respectively; that is,

$$(A - B B ^ {*} X) x = \lambda x.$$

Now premultiply and postmultiply equation (12.15) by $x ^ { * }$ and x, respectively, and we have

$$(\bar {\lambda} + \lambda) x ^ {*} X x + x ^ {*} (X B B ^ {*} X + C ^ {*} C) x = 0.$$

This implies

$$B ^ {*} X x = 0, \quad C x = 0$$

since $\mathrm { R e } ( \lambda ) \geq 0$ and $X \geq 0$ . Finally, we arrive at

$$A x = \lambda x, \quad C x = 0.$$

That is, $( C , A )$ is not detectable, which is a contradiction. Hence $\operatorname { R e } ( \lambda ) < 0 ( \mathrm { i . e . , } X \geq 0$ is the stabilizing solution). ✷

Lemma 12.6 Suppose D has full column rank and let $R = D ^ { * } D > 0 .$ then the following statements are equivalent:

$\left( i \right) \left[ \begin{array} { c c } { { A - j \omega I } } & { { B } } \\ { { C } } & { { D } } \end{array} \right] h a s f u l l c o l u m n r a n k f o r a l l \omega .$   
(ii) $\big ( ( I - D R ^ { - 1 } D ^ { * } ) C , A - B R ^ { - 1 } D ^ { * } C \big )$ has no unobservable modes on the jω axis.

Proof. Suppose $j \omega$ is an unobservable mode of $\big ( ( I - D R ^ { - 1 } D ^ { * } ) C , A - B R ^ { - 1 } D ^ { * } C \big )$ ; then there is an $x \neq 0$ such that

$$(A - B R ^ {- 1} D ^ {*} C) x = j \omega x, (I - D R ^ {- 1} D ^ {*}) C x = 0;$$

that is,
