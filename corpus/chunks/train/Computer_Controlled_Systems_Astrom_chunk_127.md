# The Pulse-Transfer Operator

Use of operator calculus allows the input-output relationship to be conveniently expressed as a rational function in either the forward- or the backward-shift operator. This function is called the pulse-transfer operator and is easily obtained from any system description by eliminating internal variables using purely algebraic manipulations.

Consider, for example, the state-space model of (2.16). To obtain the input-output relationship, the state vector must be eliminated. It follows from (2.16) that

$$x (k + 1) = q x (k) = \Phi x (k) + \Gamma u (k)$$

Hence

$$(q I - \Phi) x (k) = \Gamma u (k)$$

This gives

$$y (k) = C x (k) + D u (k) = \left(C (q I - \Phi) ^ {- 1} \Gamma + D\right) u (k)$$

The pulse-transfer operator for the system (2.16) is thus given by

$$H (q) = C (q I - \Phi) ^ {- 1} \Gamma + D$$

The pulse-transfer operator can be also expressed in terms of the backward-shift operator.

$$H ^ {*} (q ^ {- 1}) = C (I - q ^ {- 1} \Phi) ^ {- 1} q ^ {- 1} \Gamma + D = H (q)$$

The pulse-transfer operator for the system of (2.16) is thus a matrix whose elements are rational functions in q. For a system with one input and one output,

$$H (q) = C (q I - \Phi) ^ {- 1} \Gamma + D = \frac {B (q)}{A (q)} \tag {2.26}$$

If the state vector is of dimension n and if the polynomials $A(q)$ and $B(q)$ do not have common factors, then the polynomial A is of degree n. It follows from (2.26) that the polynomial A is also the characteristic polynomial of the matrix $\Phi$ , which means that the input-output model can be written as

$$y (k) + a _ {1} y (k - 1) + \dots + a _ {n} y (k - n) = b _ {0} u (k) + \dots + b _ {n} u (k - n)$$

where $a_{i}$ are the coefficients of the characteristic polynomial of $\Phi$ . The most common case in computer-control systems is that $b_{0}=0$ , that is, there is no direct term in the discrete-time model. Usually $y(k)$ is measured first, and then $u(k)$ is determined. Then $y(k)$ cannot be influenced by $u(k)$ even if the continuous-time system has a direct term.
