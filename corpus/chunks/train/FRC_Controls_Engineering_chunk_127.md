# 5.12.3 Useful identities

Here’s some useful matrix calculus identities pulled from Wikipedia’s table.[1]

Theorem 5.12.1 $\begin{array} { r } { \frac { \partial \mathbf { x } ^ { \top } \mathbf { A } \mathbf { x } } { \partial \mathbf { x } } = 2 \mathbf { A } \mathbf { x } } \end{array}$ where A is symmetric.

Theorem 5.12.2 ∂(Ax+b)TC(Dx+e) = ATC(Dx + e) + DTCT(Ax + b) ∂x

Corollary 5.12.3 $\begin{array} { r } { \frac { \partial ( \mathbf { A } \mathbf { x } + \mathbf { b } ) ^ { \mathsf { T } } \mathbf { C } ( \mathbf { A } \mathbf { x } + \mathbf { b } ) } { \partial \mathbf { x } } = 2 \mathbf { A } ^ { \mathsf { T } } \mathbf { C } ( \mathbf { A } \mathbf { x } + \mathbf { b } ) } \end{array}$ where C is symmetric.

Proof:

$$\frac {\partial (\mathbf {A x} + \mathbf {b}) ^ {\top} \mathbf {C} (\mathbf {A x} + \mathbf {b})}{\partial \mathbf {x}} = \mathbf {A} ^ {\top} \mathbf {C} (\mathbf {A x} + \mathbf {b}) + \mathbf {A} ^ {\top} \mathbf {C} ^ {\top} (\mathbf {A x} + \mathbf {b})\frac {\partial (\mathbf {A x} + \mathbf {b}) ^ {\top} \mathbf {C} (\mathbf {A x} + \mathbf {b})}{\partial \mathbf {x}} = (\mathbf {A} ^ {\top} \mathbf {C} + \mathbf {A} ^ {\top} \mathbf {C} ^ {\top}) (\mathbf {A x} + \mathbf {b})$$

C is symmetric, so

$$\frac {\partial (\mathbf {A x} + \mathbf {b}) ^ {\top} \mathbf {C} (\mathbf {A x} + \mathbf {b})}{\partial \mathbf {x}} = (\mathbf {A} ^ {\top} \mathbf {C} + \mathbf {A} ^ {\top} \mathbf {C}) (\mathbf {A x} + \mathbf {b})\frac {\partial (\mathbf {A x} + \mathbf {b}) ^ {\top} \mathbf {C} (\mathbf {A x} + \mathbf {b})}{\partial \mathbf {x}} = 2 \mathbf {A} ^ {\top} \mathbf {C} (\mathbf {A x} + \mathbf {b})$$

This page intentionally left blank
