$$
\left[ \begin{array}{c c} A - j \omega I & B \\ C & D \end{array} \right] \left[ \begin{array}{c c} I & 0 \\ - R ^ {- 1} D ^ {*} C & I \end{array} \right] \left[ \begin{array}{c} x \\ 0 \end{array} \right] = 0.
$$

But this implies that

$$
\left[ \begin{array}{c c} A - j \omega I & B \\ C & D \end{array} \right] \tag {12.16}
$$

does not have full-column rank. Conversely, suppose equation (12.16) does not have full-column rank for some $\omega ;$ then there exists $\left[ \begin{array} { l } { u } \\ { v } \end{array} \right] \neq 0$ such that

$$
\left[ \begin{array}{c c} A - j \omega I & B \\ C & D \end{array} \right] \left[ \begin{array}{c} u \\ v \end{array} \right] = 0.
$$

Now let

$$
\left[ \begin{array}{c} u \\ v \end{array} \right] = \left[ \begin{array}{c c} I & 0 \\ - R ^ {- 1} D ^ {*} C & I \end{array} \right] \left[ \begin{array}{c} x \\ y \end{array} \right].
$$

Then

$$
\left[ \begin{array}{c} x \\ y \end{array} \right] = \left[ \begin{array}{c c} I & 0 \\ R ^ {- 1} D ^ {*} C & I \end{array} \right] \left[ \begin{array}{c} u \\ v \end{array} \right] \neq 0
$$

and

$$(A - B R ^ {- 1} D ^ {*} C - j \omega I) x + B y = 0 \tag {12.17}(I - D R ^ {- 1} D ^ {*}) C x + D y = 0. \tag {12.18}$$

Premultiply equation (12.18) by $D ^ { * }$ to get $y = 0$ . Then we have

$$(A - B R ^ {- 1} D ^ {*} C) x = j \omega x, \quad (I - D R ^ {- 1} D ^ {*}) C x = 0;$$

that is, jω is an unobservable mode of $\big ( ( I - D R ^ { - 1 } D ^ { * } ) C , A - B R ^ { - 1 } D ^ { * } C \big )$ .

Remark 12.2 If D is not square, then there is a $D _ { \perp }$ such that $\left\lceil \begin{array} { l l } { D _ { \perp } } & { D R ^ { - 1 / 2 } } \end{array} \right\rceil$ i is unitary and that $D _ { \perp } D _ { | } ^ { * } = I  – D R ^ { - 1 } D ^ { * }$ . Hence, in some cases we will write the condition (ii) in the preceding lemma as $( D _ { \textrm { l } } ^ { * } C , A - B R ^ { - 1 } D ^ { * } C )$ having no imaginary unobservable modes. Of course, if D is square, the condition is simplified to $A - B R ^ { - 1 } D ^ { * } C$ having no imaginary eigenvalues. Note also that if $D ^ { * } C = 0 .$ , condition (ii) becomes $( C , A )$ having no imaginary unobservable modes. ✸

Corollary 12.7 Suppose D has $f u l l$ column rank and denote $R = D ^ { * } D > 0$ . Let H have the form
