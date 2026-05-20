# Solution:

If the above expression satisfies the following conditions, then it is an inner product:

• Conjugate symmetry:

$$\langle x, y \rangle = \int_ {a} ^ {b} x (t) y (t) d t = \int_ {a} ^ {b} y (t) x (t) d t = \overline {{\langle y , x \rangle}} \tag {55}$$

The expression hold because of the commutative property of the R space. The conjugate symmetry is just symmetry in R.

• Linearity:

$$\langle \alpha x, y \rangle = \int_ {a} ^ {b} \alpha x (t) y (t) d t = \alpha \int_ {a} ^ {b} y (t) x (t) d t = \alpha \langle x, y \rangle \tag {56}$$

holds because of the properties of the integral, where $\alpha \in \mathbb { R }$ . Also, we can see that the following holds

$$\langle x + y, z \rangle = \int_ {a} ^ {b} \alpha [ x (t) + y (t) ] z (t) d t = \int_ {a} ^ {b} x (t) z (t) d t + \int_ {a} ^ {b} y (t) z (t) d t = \langle x, z \rangle + \langle y, z \rangle \tag {57}$$

thus satisfying the linearity conditions.

• Positive definiteness:

$$\langle x, x \rangle = \int_ {a} ^ {b} x (t) x (t) d t = \int_ {a} ^ {b} x (t) ^ {2} d t > 0 \tag {58}$$

where $x ( t ) ^ { 2 } > 0$ . Thus, since the integral of a positive function is positive, by our definition the expression will be positive unless for $x ( t ) = 0$ .

Therefore, we can conclude the expression is indeed an inner product on the vector space $\mathbb { C } ^ { 0 }$ . 
