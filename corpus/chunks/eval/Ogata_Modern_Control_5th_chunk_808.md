$$\mathbf {R} = \mathbf {T} ^ {*} \mathbf {T}$$

where T is a nonsingular matrix. Then Equation (10–115) can be written as

$$(\mathbf {A} ^ {*} - \mathbf {K} ^ {*} \mathbf {B} ^ {*}) \mathbf {P} + \mathbf {P} (\mathbf {A} - \mathbf {B K}) + \mathbf {Q} + \mathbf {K} ^ {*} \mathbf {T} ^ {*} \mathbf {T K} = \mathbf {0}$$

which can be rewritten as

$$\mathbf {A} ^ {*} \mathbf {P} + \mathbf {P A} + \left[ \mathbf {T K} - (\mathbf {T} ^ {*}) ^ {- 1} \mathbf {B} ^ {*} \mathbf {P} \right] * \left[ \mathbf {T K} - (\mathbf {T} ^ {*}) ^ {- 1} \mathbf {B} ^ {*} \mathbf {P} \right] - \mathbf {P B R} ^ {- 1} \mathbf {B} ^ {*} \mathbf {P} + \mathbf {Q} = \mathbf {0}$$

The minimization of J with respect to K requires the minimization of

$$\mathbf {x} ^ {*} \left[ \mathbf {T K} - (\mathbf {T} ^ {*}) ^ {- 1} \mathbf {B} ^ {*} \mathbf {P} \right] * \left[ \mathbf {T K} - (\mathbf {T} ^ {*}) ^ {- 1} \mathbf {B} ^ {*} \mathbf {P} \right] \mathbf {x}$$

with respect to K. (See Problem A–10–16.) Since this last expression is nonnegative, the minimum occurs when it is zero, or when

$$\mathbf {T K} = (\mathbf {T} ^ {*}) ^ {- 1} \mathbf {B} ^ {*} \mathbf {P}$$

Hence,

$$\mathbf {K} = \mathbf {T} ^ {- 1} (\mathbf {T} ^ {*}) ^ {- 1} \mathbf {B} ^ {*} \mathbf {P} = \mathbf {R} ^ {- 1} \mathbf {B} ^ {*} \mathbf {P} \tag {10-117}$$

Equation (10–117) gives the optimal matrix K.Thus, the optimal control law to the quadratic optimal control problem when the performance index is given by Equation (10–114) is linear and is given by

$$\mathbf {u} (t) = - \mathbf {K x} (t) = - \mathbf {R} ^ {- 1} \mathbf {B} ^ {*} \mathbf {P x} (t)$$

The matrix P in Equation (10–117) must satisfy Equation (10–115) or the following reduced equation:

$$\mathbf {A} ^ {*} \mathbf {P} + \mathbf {P A} - \mathbf {P B R} ^ {- 1} \mathbf {B} ^ {*} \mathbf {P} + \mathbf {Q} = \mathbf {0} \tag {10-118}$$

Equation (10–118) is called the reduced-matrix Riccati equation. The design steps may be stated as follows:

1. Solve Equation (10–118), the reduced-matrix Riccati equation, for the matrix P. [If a positive-definite matrix P exists (certain systems may not have a positivedefinite matrix P), the system is stable, or matrix A-BK is stable.]   
2. Substitute this matrix P into Equation (10–117). The resulting matrix K is the optimal matrix.

A design example based on this approach is given in Example 10–9. Note that if the matrix A-BK is stable, the present method always gives the correct result.
