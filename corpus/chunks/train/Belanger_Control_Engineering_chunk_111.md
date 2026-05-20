We now show that an unobservable state cannot exist if $C\mathbf{v}_i \neq \mathbf{0}$ for all $i$ . If one does exist, then $\mathbf{y}(t) = \mathbf{0}$ for all $t$ , for some $\mathbf{x}(0) \neq \mathbf{0}$ . Because of the linear independence of the exponentials, this could happen only if the coefficient of each exponential vanishes, i.e., if

$$a _ {1} C \mathbf {v} _ {1} = a _ {2} C \mathbf {v} _ {2} = \dots = a _ {n} C \mathbf {v} _ {n} = \mathbf {0}. \tag {3.44}$$

For $\mathbf{x}(0)$ to be nonzero, at least one of the $a_{i}$ must be nonzero; let that be $a_{k}$ . To satisfy Equation 3.44, we must have $C\mathbf{v}_k = \mathbf{0}$ , which is contrary to the assumption. Therefore, there are no unobservable states and the system is observable.

If an eigenvector $\mathbf{v}_i$ satisfies $C\mathbf{v}_i = \mathbf{0}$ , mode $s_i$ is called an unobservable mode. What the theorem says is that there is always at least one such mode when the system is unobservable. The first part of the theorem demonstrates that such an eigenvector is itself an unobservable state (there may be others).

To implement the eigenvector test, we compute the eigenvectors $\mathbf{v}_i$ of the $A$ matrix and calculate $C\mathbf{v}_i$ . Because of finite arithmetic, the result will never be exactly zero, even if the system is in fact unobservable: it is usually necessary to give a certain tolerance, i.e., to decide how small a number has to be before we call it zero.

If to each eigenvalue there corresponds but a single linearly independent eigenvector, the eigenvector test is applied by computing a full set of eigenvectors of A and calculating $Cv_{i}$ .

If there are repeated eigenvalues, it is possible to have several independent eigenvectors associated with one eigenvalue—say $v_{i1}^{0}$ , $v_{i2}^{0}$ , $\ldots$ , $v_{iK}^{0}$ corresponding to $s_{i}$ . Since a linear combination of eigenvectors is also an eigenvector, the test consists of ascertaining whether constants $a_{1}, a_{2}, \ldots, a_{k}$ , not all zero, can be found such that $C(a_{1}\mathbf{v}_{i1}^{0} + a_{2}\mathbf{v}_{i2}^{0} + \cdots + a_{k}\mathbf{v}_{iK}^{0}) = 0$ or $a_{1}C\mathbf{v}_{i1}^{0} + a_{2}C\mathbf{v}_{i2} + \cdots + a_{k}C\mathbf{v}_{iK}^{0} = 0$ . Such a set of constants will exist if

$$\operatorname{rank} \left[ C \mathbf {v} _ {i ^ {1}} ^ {0} C \mathbf {v} _ {i ^ {2}} ^ {0} \dots C \mathbf {v} _ {i ^ {K}} ^ {0} \right] < K. \tag {3.45}$$
