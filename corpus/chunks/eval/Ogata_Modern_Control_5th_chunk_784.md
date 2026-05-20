The characteristic equation for the minimum-order observer is obtained from Equation (10–94) as follows:

$$
\begin{array}{l} \left| s \mathbf {I} - \mathbf {A} _ {b b} + \mathbf {K} _ {e} \mathbf {A} _ {a b} \right| = (s - \mu_ {1}) (s - \mu_ {2}) \dots (s - \mu_ {n - 1}) \\ = s ^ {n - 1} + \hat {\alpha} _ {1} s ^ {n - 2} + \dots + \hat {\alpha} _ {n - 2} s + \hat {\alpha} _ {n - 1} = 0 \tag {10-95} \\ \end{array}
$$

where $\mu _ { 1 } , \mu _ { 2 } , \ldots , \mu _ { n - 1 }$ are desired eigenvalues for the minimum-order observer. The observer gain matrix $\mathbf { K } _ { e }$ can be determined by first choosing the desired eigenvalues for the minimum-order observer [that is, by placing the roots of the characteristic equation, Equation (10–95), at the desired locations] and then using the procedure developed for the full-order observer with appropriate modifications. For example, if the formula for determining matrix $\mathbf { K } _ { e }$ given by Equation (10–61) is to be used, it should be modified to

$$
\mathbf {K} _ {e} = \hat {\mathbf {Q}} \left[ \begin{array}{c} \hat {\alpha} _ {n - 1} - \hat {a} _ {n - 1} \\ \hat {\alpha} _ {n - 2} - \hat {a} _ {n - 2} \\ \cdot \\ \cdot \\ \cdot \\ \hat {\alpha} _ {1} - \hat {a} _ {1} \end{array} \right] = (\hat {\mathbf {W}} \hat {\mathbf {N}} ^ {*}) ^ {- 1} \left[ \begin{array}{c} \hat {\alpha} _ {n - 1} - \hat {a} _ {n - 1} \\ \hat {\alpha} _ {n - 2} - \hat {a} _ {n - 2} \\ \cdot \\ \cdot \\ \cdot \\ \hat {\alpha} _ {1} - \hat {a} _ {1} \end{array} \right] \tag {10-96}
$$

where $\mathbf { K } _ { e }$ is an $( n - 1 ) \times 1$ matrix and

$$
\hat {\mathbf {N}} = \left[ \begin{array}{c c c c} \mathbf {A} _ {a b} ^ {*} & \mathbf {A} _ {b b} ^ {*} \mathbf {A} _ {a b} ^ {*} & \dots & \left(\mathbf {A} _ {b b} ^ {*}\right) ^ {n - 2} \mathbf {A} _ {a b} ^ {*} \end{array} \right] = (n - 1) \times (n - 1) \text {   matrix }

\hat {\mathbf {W}} = \left[ \begin{array}{c c c c c} \hat {a} _ {n - 2} & \hat {a} _ {n - 3} & \dots & \hat {a} _ {1} & 1 \\ \hat {a} _ {n - 3} & \hat {a} _ {n - 4} & \dots & 1 & 0 \\ \cdot & \cdot & & \cdot & \cdot \\ \cdot & \cdot & & \cdot & \cdot \\ \cdot & \cdot & & \cdot & \cdot \\ \hat {a} _ {1} & 1 & \dots & 0 & 0 \\ 1 & 0 & \dots & 0 & 0 \end{array} \right] = (n - 1) \times (n - 1) \text {   matrix }
$$

Note that $\hat { a } _ { 1 } , \hat { a } _ { 2 } , \dots , \hat { a } _ { n - 2 }$ are coefficients in the characteristic equation for the state equation

$$\left| s \mathbf {I} - \mathbf {A} _ {b b} \right| = s ^ {n - 1} + \hat {a} _ {1} s ^ {n - 2} + \dots + \hat {a} _ {n - 2} s + \hat {a} _ {n - 1} = 0$$
