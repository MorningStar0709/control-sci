$$
\begin{array}{l} J = \int_ {0} ^ {\infty} \left(\mathbf {x} ^ {*} \mathbf {Q x} + \mathbf {x} ^ {*} \mathbf {K} ^ {*} \mathbf {R K x}\right) d t \\ = \int_ {0} ^ {\infty} \mathbf {x} ^ {*} (\mathbf {Q} + \mathbf {K} ^ {*} \mathbf {R K}) \mathbf {x} d t \\ \end{array}
$$

Let us set

$$\mathbf {x} ^ {*} (\mathbf {Q} + \mathbf {K} ^ {*} \mathbf {R K}) \mathbf {x} = - \frac {d}{d t} \left(\mathbf {x} ^ {*} \mathbf {P x}\right)$$

where P is a positive-definite Hermitian or real symmetric matrix. Then we obtain

$$\mathbf {x} ^ {*} (\mathbf {Q} + \mathbf {K} ^ {*} \mathbf {R K}) \mathbf {x} = - \dot {\mathbf {x}} ^ {*} \mathbf {P x} - \mathbf {x} ^ {*} \mathbf {P} \dot {\mathbf {x}} = - \mathbf {x} ^ {*} [ (\mathbf {A} - \mathbf {B K}) ^ {*} \mathbf {P} + \mathbf {P} (\mathbf {A} - \mathbf {B K}) ] \mathbf {x}$$

Comparing both sides of this last equation and noting that this equation must hold true for any x, we require that

$$(\mathbf {A} - \mathbf {B K}) ^ {*} \mathbf {P} + \mathbf {P} (\mathbf {A} - \mathbf {B K}) = - (\mathbf {Q} + \mathbf {K} ^ {*} \mathbf {R K}) \tag {10-115}$$

It can be proved that if A-BK is a stable matrix, there exists a positive-definite matrix P that satisfies Equation (10–115). (See Problem A–10–15.)

Hence our procedure is to determine the elements of P from Equation (10–115) and see if it is positive definite. (Note that more than one matrix P may satisfy this equation. If the system is stable, there always exists one positive-definite matrix P to satisfy this equation. This means that, if we solve this equation and find one positive-definite matrix P, the system is stable. Other P matrices that satisfy this equation are not positive definite and must be discarded.)

The performance index J can be evaluated as

$$J = \int_ {0} ^ {\infty} \mathbf {x} ^ {*} (\mathbf {Q} + \mathbf {K} ^ {*} \mathbf {R K}) \mathbf {x} d t = - \mathbf {x} ^ {*} \mathbf {P x} \bigg | _ {0} ^ {\infty} = - \mathbf {x} ^ {*} (\infty) \mathbf {P x} (\infty) + \mathbf {x} ^ {*} (0) \mathbf {P x} (0)$$

Since all eigenvalues of A-BK are assumed to have negative real parts, we have Therefore, we obtainx(q) S 0.

$$J = \mathbf {x} ^ {*} (0) \mathbf {P x} (0) \tag {10-116}$$

Thus, the performance index J can be obtained in terms of the initial condition x(0) and P.

To obtain the solution to the quadratic optimal control problem, we proceed as follows: Since R has been assumed to be a positive-definite Hermitian or real symmetric matrix, we can write
