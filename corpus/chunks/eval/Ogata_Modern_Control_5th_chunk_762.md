$$\dot {\mathbf {x}} - \dot {\widetilde {\mathbf {x}}} = \mathbf {A} \mathbf {x} - \mathbf {A} \widetilde {\mathbf {x}} - \mathbf {K} _ {e} (\mathbf {C x} - \mathbf {C} \widetilde {\mathbf {x}})= \left(\mathbf {A} - \mathbf {K} _ {e} \mathbf {C}\right) (\mathbf {x} - \widetilde {\mathbf {x}}) \tag {10-58}$$

Define the difference between x and $\widetilde { \mathbf { x } }$ as the error vector e, or

$$\mathbf {e} = \mathbf {x} - \widetilde {\mathbf {x}}$$

Then Equation (10–58) becomes

$$\dot {\mathbf {e}} = \left(\mathbf {A} - \mathbf {K} _ {e} \mathbf {C}\right) \mathbf {e} \tag {10-59}$$

From Equation (10–59), we see that the dynamic behavior of the error vector is determined by the eigenvalues of matrix $\mathbf { A } - \mathbf { K } _ { e } \mathbf { C }$ . If matrix $\mathbf { A } - \mathbf { K } _ { e } \mathbf { C }$ is a stable matrix, the error vector will converge to zero for any initial error vector ${ \bf e } ( 0 )$ . That is, $\widetilde { \mathbf { x } } \left( t \right)$ will converge to ${ \bf x } ( t )$ regardless of the values of $\mathbf { x } ( 0 )$ and $\widetilde { \mathbf { x } } \left( 0 \right)$ If the eigenvalues of matrix. $\mathbf { A } - \mathbf { K } _ { e } \mathbf { C }$ are chosen in such a way that the dynamic behavior of the error vector is asymptotically stable and is adequately fast, then any error vector will tend to zero (the origin) with an adequate speed.

If the plant is completely observable, then it can be proved that it is possible to choose matrix $\mathbf { K } _ { e }$ such that $\mathbf { A } - \mathbf { K } _ { e } \mathbf { C }$ has arbitrarily desired eigenvalues. That is, the observer gain matrix $\mathbf { K } _ { e }$ can be determined to yield the desired matrix $\mathbf { A } - \mathbf { K } _ { e } \mathbf { C } .$ . We shall discuss this matter in what follows.
