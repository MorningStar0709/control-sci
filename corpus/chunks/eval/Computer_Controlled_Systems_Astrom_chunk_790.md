$$\boldsymbol {\Phi} ^ {T} \boldsymbol {\Phi} \hat {\boldsymbol {\theta}} = \boldsymbol {\Phi} ^ {T} y \tag {13.4}$$

If the matrix $\Phi^{T}\Phi$ is nonsingular, the minimum is unique and given by

$$\hat {\theta} = \left(\Phi^ {T} \Phi\right) ^ {- 1} \Phi^ {T} y = \Phi^ {\dagger} y \tag {13.5}$$

Proof. The loss function of (13.3) can be written as

$$2 J (\theta) = \varepsilon^ {T} \varepsilon = (y - \Phi \theta) ^ {T} (y - \Phi \theta)= y ^ {T} y - y ^ {T} \Phi \theta - \theta^ {T} \Phi^ {T} y + \theta^ {T} \Phi^ {T} \Phi \theta$$

Because the matrix $\Phi^T\Phi$ is always nonnegative definite, the function $J$ has a minimum. Assuming that $\Phi^T\Phi$ is nonsingular and using (11.12) the minimum is obtained for

$$\theta = \hat {\theta} = (\Phi^ {T} \Phi) ^ {- 1} \Phi^ {T} y$$

and the theorem is proved.

Remark 1. Equation (13.4) is called the normal equation.

Remark 2. The matrix $\Phi^{\dagger} = (\Phi^{T}\Phi)^{-1}\Phi^{T}$ is called the pseudo-inverse of $\Phi$ if the matrix $\Phi^{T}\Phi$ is nonsingular.
