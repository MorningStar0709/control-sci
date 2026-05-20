$$\langle z, (A - j \omega I) x \rangle = \langle z, B B ^ {*} z \rangle = \| B ^ {*} z \| ^ {2}- \langle x, (A - j \omega I) ^ {*} z \rangle = \langle x, C ^ {*} C x \rangle = \| C x \| ^ {2}$$

so $\langle x , ( A - j \omega I ) ^ { * } z \rangle$ is real and

$$- \| C x \| ^ {2} = \langle (A - j \omega I) x, z \rangle = \overline {{\langle z , (A - j \omega I) x \rangle}} = \| B ^ {*} z \| ^ {2}.$$

Therefore, $B ^ { * } z = 0$ and $C x = 0$ . So from equations (12.11) and (12.12)

$$(A - j \omega I) x = 0(A - j \omega I) ^ {*} z = 0.$$

Combine the last four equations to get

$$
z ^ {*} [ A - j \omega I \quad B ] = 0
\left[ \begin{array}{c} A - j \omega I \\ C \end{array} \right] x = 0.
$$

The stabilizability of $( A , B )$ gives $z = 0 .$ . Now it is clear that $j \omega$ is an eigenvalue of H iff $j \omega$ is an unobservable mode of $( C , A )$ .

Next, set $X : = \operatorname { R i c } ( H )$ . We will show that $X \geq 0$ . The Riccati equation is

$$A ^ {*} X + X A - X B B ^ {*} X + C ^ {*} C = 0$$

or, equivalently,

$$(A - B B ^ {*} X) ^ {*} X + X (A - B B ^ {*} X) + X B B ^ {*} X + C ^ {*} C = 0. \tag {12.13}$$

Noting that $A - B B ^ { * } X$ is stable (Theorem 12.1), we have

$$X = \int_ {0} ^ {\infty} \mathrm{e} ^ {(A - B B ^ {*} X) ^ {*} t} (X B B ^ {*} X + C ^ {*} C) \mathrm{e} ^ {(A - B B ^ {*} X) t} d t. \tag {12.14}$$

Since X $B B ^ { * } X + C ^ { * } C$ is positive semidefinite, so is $X$ .

Finally, we will show that KerX is nontrivial if and only if $( C , A )$ has stable unobservable modes. Let $x \in \operatorname { K e r } X$ , then $X x = 0$ . Premultiply equation (12.13) by $x ^ { * }$ and postmultiply by x to get

$$C x = 0.$$

Now postmultiply equation (12.13) again by x to get

$$X A x = 0.$$

We conclude that $\mathrm { K e r } ( X )$ is an A-invariant subspace. Thus if $\operatorname { K e r } ( X ) \neq \{ 0 \}$ , then there is a $0 \neq x \in \operatorname { K e r } ( X )$ and a λ such that $\lambda x = A x = ( A - B B ^ { * } X ) x$ and $C x =$ 0. Since $( A - B B ^ { * } X )$ is stable, Reλ < 0; thus λ is a stable unobservable mode. Conversely, suppose $( C , A )$ has an unobservable stable mode λ (i.e., there is an x such that $A x \ = \ \lambda x , C x \ = \ 0 )$ . By premultiplying the Riccati equation by $x ^ { * }$ and postmultiplying by x, we $\mathrm { g e t }$

$$2 \mathrm{Re} \lambda x ^ {*} X x - x ^ {*} X B B ^ {*} X x = 0.$$

Hence $x ^ { * } X x = 0 \ { \mathrm { ( i . e . } }$ , X is singular) since $\mathrm { R e } \lambda < 0 .$

Example 12.2 This example shows that the observability of $( C , A )$ is not necessary for the existence of a positive definite stabilizing solution. Let
