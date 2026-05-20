It is noted that thus far we have assumed the matrices A, B, and C in the observer to be exactly the same as those of the physical plant. If there are discrepancies in A, B, and C in the observer and in the physical plant, the dynamics of the observer error are no longer governed by Equation (10–59). This means that the error may not approach zero as expected.Therefore, we need to choose $\mathbf { K } _ { e }$ so that the observer is stable and the error remains acceptably small in the presence of small modeling errors.

Transformation Approach to Obtain State Observer Gain Matrix Ke. By following the same approach as we used in deriving the equation for the state feedback gain matrix K, we can obtain the following equation:

$$
\mathbf {K} _ {e} = \mathbf {Q} \left[ \begin{array}{c} \alpha_ {n} - a _ {n} \\ \alpha_ {n - 1} - a _ {n - 1} \\ \cdot \\ \cdot \\ \cdot \\ \alpha_ {1} - a _ {1} \end{array} \right] = (\mathbf {W N} ^ {*}) ^ {- 1} \left[ \begin{array}{c} \alpha_ {n} - a _ {n} \\ \alpha_ {n - 1} - a _ {n - 1} \\ \cdot \\ \cdot \\ \cdot \\ \alpha_ {1} - a _ {1} \end{array} \right] \tag {10-61}
$$

where $\mathbf { K } _ { e }$ is an $n \times 1$ matrix,

$$\mathbf {Q} = (\mathbf {W N} ^ {*}) ^ {- 1}$$

and

$$
\begin{array}{l} \mathbf {N} = \left[ \begin{array}{c c c c c} \mathbf {C} ^ {*} & \mathbf {A} ^ {*} \mathbf {C} ^ {*} & \dots & (\mathbf {A} ^ {*}) ^ {n - 1} \mathbf {C} ^ {*} \end{array} \right] \\ \mathbf {W} = \left[ \begin{array}{c c c c c} a _ {n - 1} & a _ {n - 2} & \dots & a _ {1} & 1 \\ a _ {n - 2} & a _ {n - 3} & \dots & 1 & 0 \\ \cdot & \cdot & & \cdot & \cdot \\ \cdot & \cdot & & \cdot & \cdot \\ \cdot & \cdot & & \cdot & \cdot \\ a _ {1} & 1 & \dots & 0 & 0 \\ 1 & 0 & \dots & 0 & 0 \end{array} \right] \\ \end{array}
$$

[Refer to Problem A–10–10 for the derivation of Equation (10–61).]

Direct-Substitution Approach to Obtain State Observer Gain Matrix ${ \bf K } _ { e } .$ . Similar to the case of pole placement, if the system is of low order, then direct substitution of matrix $\mathbf { K } _ { e }$ into the desired characteristic polynomial may be simpler. For example, if x is a 3-vector, then write the observer gain matrix $\mathbf { K } _ { e }$ as

$$
\mathbf {K} _ {e} = \left[ \begin{array}{c} k _ {e 1} \\ k _ {e 2} \\ k _ {e 3} \end{array} \right]
$$

Substitute this $\mathbf { K } _ { e }$ matrix into the desired characteristic polynomial:

$$\left| s \mathbf {I} - \left(\mathbf {A} - \mathbf {K} _ {e} \mathbf {C}\right) \right| = (s - \mu_ {1}) (s - \mu_ {2}) (s - \mu_ {3})$$
