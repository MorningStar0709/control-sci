Then the columns of $T ^ { - 1 }$ are eigenvectors of $P Q$ corresponding to the eigenvalues $\{ \lambda _ { i } \}$ . Later, it will be shown that $P Q$ has a real diagonal Jordan form and that $\Lambda \geq 0$ , which are consequences of $P \geq 0$ and $Q \geq 0$ .

Although the eigenvectors are not unique, in the case of a minimal realization they can always be chosen such that

$$\hat {P} = T P T ^ {*} = \Sigma ,\hat {Q} = (T ^ {- 1}) ^ {*} Q T ^ {- 1} = \Sigma ,$$

where $\Sigma = \operatorname { d i a g } ( \sigma _ { 1 } I _ { s _ { 1 } } , \sigma _ { 2 } I _ { s _ { 2 } } , \dots , \sigma _ { N } I _ { s _ { N } } )$ and $\Sigma ^ { 2 } = \Lambda$ . This new realization with controllability and observability Gramians $\hat { P } = \hat { Q } = \Sigma$ will be referred to as a balanced realization (also called internally balanced realization). The decreasingly ordered numbers, $\sigma _ { 1 } > \sigma _ { 2 } > . . . > \sigma _ { N } \geq 0$ , are called the Hankel singular values of the system.

More generally, if a realization of a stable system is not minimal, then there is a transformation such that the controllability and observability Gramians for the transformed realization are diagonal and the controllable and observable subsystem is balanced. This is a consequence of the following matrix fact.

Theorem 7.5 Let P and Q be two positive semidefinite matrices. Then there exists a nonsingular matrix T such that

$$
T P T ^ {*} = \left[ \begin{array}{c c c c} \Sigma_ {1} & & & \\ & \Sigma_ {2} & & \\ & & 0 & \\ & & & 0 \end{array} \right], (T ^ {- 1}) ^ {*} Q T ^ {- 1} = \left[ \begin{array}{c c c c} \Sigma_ {1} & & & \\ & 0 & & \\ & & \Sigma_ {3} & \\ & & & 0 \end{array} \right]
$$

respectively, with $\Sigma _ { 1 } , \ \Sigma _ { 2 } , \ \Sigma _ { 3 }$ diagonal and positive definite.

Proof. Since $P$ is a positive semidefinite matrix, there exists a transformation $T _ { 1 }$ such that

$$
T _ {1} P T _ {1} ^ {*} = \left[ \begin{array}{c c} I & 0 \\ 0 & 0 \end{array} \right]
$$

Now let

$$
(T _ {1} ^ {*}) ^ {- 1} Q T _ {1} ^ {- 1} = \left[ \begin{array}{l l} Q _ {1 1} & Q _ {1 2} \\ Q _ {1 2} ^ {*} & Q _ {2 2} \end{array} \right]
$$

and there exists a unitary matrix $U _ { 1 }$ such that

$$
U _ {1} Q _ {1 1} U _ {1} ^ {*} = \left[ \begin{array}{c c} \Sigma_ {1} ^ {2} & 0 \\ 0 & 0 \end{array} \right], \Sigma_ {1} > 0
$$

Let

$$
(T _ {2} ^ {*}) ^ {- 1} = \left[ \begin{array}{c c} U _ {1} & 0 \\ 0 & I \end{array} \right]
$$

and then
