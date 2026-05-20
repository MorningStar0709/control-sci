# 11.6 SQUARE ROOT ALGORITHMS

It is well known in numerical analysis that considerable accuracy may be lost when a least-squares problem is solved by forming and solving the normal equations. The reason is that the measured values are squared unnecessarily. The following procedure for solving the least-squares problem is much better conditioned numerically. Start with Eq. (2.4):

$$\mathcal {E} = Y - \Phi \theta$$

An orthogonal transformation $Q$ , that is, $Q^{T}Q = QQ^{T} = I$ , does not change the Euclidean norm of the error

$$\tilde {\mathcal {E}} = Q \mathcal {E} = Q Y - Q \Phi \theta$$

Choose the transformation $Q$ so that $Q\Phi$ is upper triangular. The above equation then becomes

$$\binom{\tilde {e} ^ {1}}{\tilde {e} ^ {2}} = \binom{\tilde {y} ^ {1}}{\tilde {y} ^ {2}} - \binom{\tilde {\Phi} _ {1}}{0} \theta$$

where $\tilde{\Phi}_1$ is upper triangular. It then follows that the least-squares estimate is given by

$$\tilde {\Phi} _ {1} \theta = \tilde {y} ^ {1}$$

and the error is $(\tilde{e}^{2})^{T}\tilde{e}^{2}$ . This way of computing the estimate is much more accurate than solving the normal equation, particularly if $\|E\|\ll\|Y\|$ . The method based on orthogonal transformation is called a square root method because it works with $\Phi$ or the square root of $\Phi^{T}\Phi$ . There are several numerical methods that can be used to find an orthogonal transformation Q, for example, Householder transformations or the QR method. We will not discuss these methods further, because we are primarily interested in recursive methods.
