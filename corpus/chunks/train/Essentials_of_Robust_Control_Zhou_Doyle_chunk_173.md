$$
(T _ {2} ^ {*}) ^ {- 1} (T _ {1} ^ {*}) ^ {- 1} Q T _ {1} ^ {- 1} (T _ {2}) ^ {- 1} = \left[ \begin{array}{c c c} \Sigma_ {1} ^ {2} & 0 & \hat {Q} _ {1 2 1} \\ 0 & 0 & \hat {Q} _ {1 2 2} \\ \hat {Q} _ {1 2 1} ^ {*} & \hat {Q} _ {1 2 2} ^ {*} & Q _ {2 2} \end{array} \right]
$$

But $Q \geq 0$ implies $\hat { Q } _ { 1 2 2 } = 0$ . So now let

$$
(T _ {3} ^ {*}) ^ {- 1} = \left[ \begin{array}{c c c} I & 0 & 0 \\ 0 & I & 0 \\ - \hat {Q} _ {1 2 1} ^ {*} \Sigma_ {1} ^ {- 2} & 0 & I \end{array} \right]
$$

giving

$$
(T _ {3} ^ {*}) ^ {- 1} (T _ {2} ^ {*}) ^ {- 1} (T _ {1} ^ {*}) ^ {- 1} Q T _ {1} ^ {- 1} (T _ {2}) ^ {- 1} (T _ {3}) ^ {- 1} = \left[ \begin{array}{c c c} \Sigma_ {1} ^ {2} & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & Q _ {2 2} - \hat {Q} _ {1 2 1} ^ {*} \Sigma_ {1} ^ {- 2} \hat {Q} _ {1 2 1} \end{array} \right]
$$

Next find a unitary matrix $U _ { 2 }$ such that

$$
U _ {2} (Q _ {2 2} - \hat {Q} _ {1 2 1} ^ {*} \Sigma_ {1} ^ {- 2} \hat {Q} _ {1 2 1}) U _ {2} ^ {*} = \left[ \begin{array}{c c} \Sigma_ {3} & 0 \\ 0 & 0 \end{array} \right], \Sigma_ {3} > 0
$$

Define

$$
(T _ {4} ^ {*}) ^ {- 1} = \left[ \begin{array}{c c c} \Sigma_ {1} ^ {- 1 / 2} & 0 & 0 \\ 0 & I & 0 \\ 0 & 0 & U _ {2} \end{array} \right]
$$

and let

$$T = T _ {4} T _ {3} T _ {2} T _ {1}$$

Then

$$
T P T ^ {*} = \left[ \begin{array}{c c c c} \Sigma_ {1} & & & \\ & \Sigma_ {2} & & \\ & & 0 & \\ & & & 0 \end{array} \right], (T ^ {*}) ^ {- 1} Q T ^ {- 1} = \left[ \begin{array}{c c c c} \Sigma_ {1} & & & \\ & 0 & & \\ & & \Sigma_ {3} & \\ & & & 0 \end{array} \right]
$$

with $\Sigma _ { 2 } = I .$ .

![](image/49307a119d1b48e5917f4c12dc0ac53f72f11c823df8a8b2cb019cd4921200eb.jpg)

Corollary 7.6 The product of two positive semidefinite matrices is similar to a positive semidefinite matrix.

Proof. Let P and Q be any positive semidefinite matrices. Then it is easy to see that with the transformation given previously

$$
T P Q T ^ {- 1} = \left[ \begin{array}{c c} \Sigma_ {1} ^ {2} & 0 \\ 0 & 0 \end{array} \right]
$$

![](image/02665f88f74f84653fcff0b9b152d168d663e5789115645f4b23833a20dd220d.jpg)

Corollary 7.7 For any stable system $G = \left\lceil { \frac { A \mid B } { C \mid D } } \right\rceil$ , there exists a nonsingular transformation T such that $G = \left[ \frac { \left. T A T ^ { - 1 } \right| T \bar { B } } { \left. C T ^ { - 1 } \right| D } \right]$ has controllability Gramian P and observability Gramian Q given by

$$
P = \left[ \begin{array}{c c c c} {\Sigma_ {1}} & & & \\ & {\Sigma_ {2}} & & \\ & & 0 & \\ & & & 0 \end{array} \right], Q = \left[ \begin{array}{c c c c} {\Sigma_ {1}} & & & \\ & 0 & & \\ & & {\Sigma_ {3}} & \\ & & & 0 \end{array} \right]
$$
