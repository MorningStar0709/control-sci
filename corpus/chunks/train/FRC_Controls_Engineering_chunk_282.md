# 9.3.15 Relations for independent random vectors

First, independent vectors imply linearity from $p ( \mathbf { x } , \mathbf { y } ) = p ( \mathbf { x } ) p ( \mathbf { y } )$ .

$$E [ \mathbf {A x} + \mathbf {B y} ] = \mathbf {A} E [ \mathbf {x} ] + \mathbf {B} E [ \mathbf {y} ]E [ \mathbf {A x} + \mathbf {B y} ] = \mathbf {A} \overline {{\mathbf {x}}} + \mathbf {B} \overline {{\mathbf {y}}}$$

Second, independent vectors being uncorrelated means their covariance is zero.

$$\pmb {\Sigma} _ {\mathbf {x y}} = \operatorname{cov} (\mathbf {x}, \mathbf {y})\boldsymbol {\Sigma} _ {\mathbf {x y}} = E \left[ (\mathbf {x} - \overline {{\mathbf {x}}}) (\mathbf {y} - \overline {{\mathbf {y}}}) ^ {\top} \right]\boldsymbol {\Sigma} _ {\mathbf {x y}} = E [ \mathbf {x y} ^ {\mathsf {T}} ] - E [ \mathbf {x} \overline {{\mathbf {y}}} ^ {\mathsf {T}} ] - E [ \overline {{\mathbf {x}}} \mathbf {y} ^ {\mathsf {T}} ] + E [ \overline {{\mathbf {x y}}} ^ {\mathsf {T}} ]\boldsymbol {\Sigma} _ {\mathbf {x y}} = E [ \mathbf {x y} ^ {\top} ] - E [ \mathbf {x} ] \overline {{\mathbf {y}}} ^ {\top} - \overline {{\mathbf {x}}} E [ \mathbf {y} ^ {\top} ] + \overline {{\mathbf {x y}}} ^ {\top}\boldsymbol {\Sigma} _ {\mathbf {x y}} = E \left[ \mathbf {x y} ^ {\top} \right] - \overline {{\mathbf {x y}}} ^ {\top} - \overline {{\mathbf {x y}}} ^ {\top} + \overline {{\mathbf {x y}}} ^ {\top}\boldsymbol {\Sigma} _ {\mathbf {x y}} = E [ \mathbf {x y} ^ {\top} ] - \overline {{{{\mathbf {x y}}}}} ^ {\top} \tag {9.9}$$

Now, compute $E [ \mathbf { x y } ^ { \mathsf { T } } ]$ .

$$E [ \mathbf {x y} ^ {\top} ] = \int_ {X} \int_ {Y} \mathbf {x y} ^ {\top} p (\mathbf {x}) p (\mathbf {y}) d \mathbf {x} d \mathbf {y} ^ {\top}$$

Factor out constants from the inner integral. This includes variables which are held constant for each inner integral evaluation.

$$E [ \mathbf {x} \mathbf {y} ^ {\mathsf {T}} ] = \int_ {X} p (\mathbf {x}) \mathbf {x} d \mathbf {x} \int_ {Y} p (\mathbf {y}) \mathbf {y} ^ {\mathsf {T}} d \mathbf {y} ^ {\mathsf {T}}$$

Each of these integrals is just the expected value of their respective integration variable.

$$E [ \mathbf {x y} ^ {\top} ] = \overline {{{\mathbf {x y}}}} ^ {\top} \tag {9.10}$$

Substitute equation (9.10) into equation (9.9).

$$\pmb {\Sigma} _ {\mathbf {x y}} = (\overline {{\mathbf {x y}}} ^ {\mathsf {T}}) - \overline {{\mathbf {x y}}} ^ {\mathsf {T}}\pmb {\Sigma} _ {\mathbf {x y}} = 0$$
