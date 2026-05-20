MATLAB Is Case Sensitive. It is important to note that MATLAB is case sensitive.That is, MATLAB distinguishes between upper- and lowercase letters.Thus, x and X are not the same variable. All function names must be in lowercase, such as inv(A), $\mathrm { e i g } ( \mathsf { A } )$ , and poly(A).

Differentiation and Integration of Matrices. The derivative of an $n \times m$ matrix ${ \bf A } ( t )$ is defined to be the $n \times m$ matrix, each element of which is the derivative of the corresponding element of the original matrix, provided that all the elements $a _ { i j } ( t )$ have derivatives with respect to t. That is,

$$
\frac {d}{d t} \mathbf {A} (t) = \left(\frac {d}{d t} a _ {i j} (t)\right) = \left[ \begin{array}{c c c c} \frac {d}{d t} a _ {1 1} (t) & \frac {d}{d t} a _ {1 2} (t) & \dots & \frac {d}{d t} a _ {1 m} (t) \\ \frac {d}{d t} a _ {2 1} (t) & \frac {d}{d t} a _ {2 2} (t) & \dots & \frac {d}{d t} a _ {2 m} (t) \\ \vdots & \vdots & & \vdots \\ \frac {d}{d t} a _ {n 1} (t) & \frac {d}{d t} a _ {n 2} (t) & \dots & \frac {d}{d t} a _ {n m} (t) \end{array} \right]
$$

Similarly, the integral of an $n \times m$ matrix ${ \bf A } ( t )$ is defined to be

$$
\int \mathbf {A} (t) d t = \left(\int a _ {i j} (t) d t\right) = \left[ \begin{array}{c c c c} \int a _ {1 1} (t) d t & \int a _ {1 2} (t) d t & ... & \int a _ {1 m} (t) d t \\ \int a _ {2 1} (t) d t & \int a _ {2 2} (t) d t & ... & \int a _ {2 m} (t) d t \\ \vdots & \vdots & & \vdots \\ \int a _ {n 1} (t) d t & \int a _ {2 n} (t) d t & ... & \int a _ {n m} (t) d t \end{array} \right]
$$

Differentiation of the Product of Two Matrices. If the matrices ${ \bf A } ( t )$ and $\mathbf { B } ( t )$ can be differentiated with respect to t, then

$$\frac {d}{d t} [ \mathbf {A} (t) \mathbf {B} (t) ] = \frac {d \mathbf {A} (t)}{d t} \mathbf {B} (t) + \mathbf {A} (t) \frac {d \mathbf {B} (t)}{d t}$$

Here again the multiplication of ${ \bf A } ( t )$ and $d { \bf B } ( t ) / d t$ [or dA(t)/dt and $\mathbf { B } ( t ) ]$ is, in general, not commutative.

Differentiation of $\mathsf { A } ^ { - 1 } ( t )$ . If a matrix A(t) and its inverse $\mathbf { A } ^ { - 1 } ( t )$ are differentiable with respect to t, then the derivative of $\mathbf { A } ^ { - 1 } ( t )$ is given by

$$\frac {d \mathbf {A} ^ {- 1} (t)}{d t} = - \mathbf {A} ^ {- 1} (t) \frac {d \mathbf {A} (t)}{d t} \mathbf {A} ^ {- 1} (t)$$

The derivative may be obtained by differentiating $\mathbf { A } ( t ) \mathbf { A } ^ { - 1 } ( t )$ with respect to t. Since
