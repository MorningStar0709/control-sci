# THEOREM 2.1 Least-squares estimation

The function of Eq. (2.2) is minimal for parameters $\hat{\theta}$ such that

$$\Phi^ {T} \Phi \hat {\theta} = \Phi^ {T} Y \tag {2.5}$$

If the matrix $\Phi^{T}\Phi$ is nonsingular, the minimum is unique and given by

$$\hat {\theta} = \left(\Phi^ {T} \Phi\right) ^ {- 1} \Phi^ {T} Y \tag {2.6}$$

Proof: The loss function of Eq. (2.2) can be written as

$$
\begin{array}{l} 2 V (\theta , t) = \mathcal {E} ^ {T} \mathcal {L} = (Y - \Phi \theta) ^ {T} (Y - \Phi \theta) \\ = Y ^ {T} Y - Y ^ {T} \Phi \theta - \theta^ {T} \Phi^ {T} Y + \theta^ {T} \Phi^ {T} \Phi \theta \tag {2.7} \\ \end{array}
$$

Since the matrix $\Phi^{T}\Phi$ is always nonnegative definite, the function V has a minimum. The loss function is quadratic in $\theta$ . The minimum can be found in many ways. One way is to determine the gradient of Eq. (2.7) with respect to $\theta$ . (See Problem 2.1 at the end of the chapter). The gradient is zero when Eq. (2.5) is satisfied. Another way to find the minimum is by completing the square. We get

$$
\begin{array}{l} 2 V (\theta , t) = Y ^ {T} Y - Y ^ {T} \Phi \theta - \theta^ {T} \Phi^ {T} Y + \theta^ {T} \Phi^ {T} \Phi \theta \\ + Y ^ {T} \Phi (\Phi^ {T} \Phi) ^ {- 1} \Phi^ {T} Y - Y ^ {T} \Phi (\Phi^ {T} \Phi) ^ {- 1} \Phi^ {T} Y \\ = Y ^ {T} \left(I - \Phi \left(\Phi^ {T} \Phi\right) ^ {- 1} \Phi^ {T}\right) Y \\ + \left(\theta - \left(\Phi^ {T} \Phi\right) ^ {- 1} \Phi^ {T} Y\right) ^ {T} \Phi^ {T} \Phi \left(\theta - \left(\Phi^ {T} \Phi\right) ^ {- 1} \Phi^ {T} Y\right) \tag {2.8} \\ \end{array}
$$

The first term on the right-hand side is independent of $\theta$ . The second term is always positive. The minimum is obtained for

$$\theta = \hat {\theta} = (\Phi^ {T} \Phi) ^ {- 1} \Phi^ {T} Y$$

and the theorem is proven.

Remark 1. Equation (2.5) is called the normal equation. Equation (2.6) can be written as

$$\hat {\theta} (t) = \left(\sum_ {i = 1} ^ {t} \varphi (i) \varphi^ {T} (i)\right) ^ {- 1} \left(\sum_ {i = 1} ^ {t} \varphi (i) y (i)\right) = P (t) \left(\sum_ {i = 1} ^ {t} \varphi (i) y (i)\right) \tag {2.9}$$

Remark 2. The condition that the matrix $\Phi^T\Phi$ is invertible is called an excitation condition.

Remark 3. The least-squares criterion weights all errors $\varepsilon(i)$ equally, and this corresponds to the assumption that all measurements have the same precision.

Different weighting of the errors can be accounted for by changing the loss function (2.2) to

$$V = \frac {1}{2} \mathcal {E} ^ {T} W \mathcal {E} \tag {2.10}$$

where W is a diagonal matrix with the weights in the diagonal. The least-squares estimate is then given by

$$\hat {\theta} = \left(\boldsymbol {\Phi} ^ {T} \boldsymbol {W} \boldsymbol {\Phi}\right) ^ {- 1} \boldsymbol {\Phi} ^ {T} \boldsymbol {W} \boldsymbol {Y} \tag {2.11}$$
