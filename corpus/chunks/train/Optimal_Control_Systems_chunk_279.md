Let us note from the optimal feedback control law (5.3.24) that the Kalman gains are dependent on the solution of the matrix DRE (5.3.20) involving the system matrices and performance index matrices. Finally, the closed-loop, optimal control (5.3.24) with the state (5.2.1) gives us the optimal system

$$\mathbf {x} ^ {*} (k + 1) = [ \mathbf {A} (k) - \mathbf {B} (k) \mathbf {L} _ {a} (k) ] \mathbf {x} ^ {*} (k). \tag {5.3.26}$$

Using the gain relation (5.3.25), an alternate form for the matrix DRE (5.3.20) becomes

$$\boxed {\mathbf {P} (k) = \mathbf {A} ^ {\prime} (k) \mathbf {P} (k + 1) [ \mathbf {A} (k) - \mathbf {B} (k) \mathbf {L} _ {a} (k) ] + \mathbf {Q} (k).} \tag {5.3.27}$$

Let us now make some notes:

1. There is essentially more than one form of the matrix DRE given by (5.3.11) or (5.3.12), (5.3.20), and (5.3.27).   
2. However, the Kalman feedback gain matrix has only two forms given by the first form (5.3.17) which goes with the DRE (5.3.11) or (5.3.12) and the second form (5.3.25) which corresponds to the DRE (5.3.20) or (5.3.27).   
3. It is a simple matter to see that the matrix DRE (5.3.11) and the associated Kalman feedback gain matrix (5.3.17) involve the inversion of the matrix $\mathbf{I} + \mathbf{E}(k)\mathbf{P}(k+1)$ once only, whereas the
