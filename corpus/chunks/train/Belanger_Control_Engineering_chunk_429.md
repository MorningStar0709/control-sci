$$\widetilde {\mathbf {x}} = (A - G C) \widetilde {\mathbf {x}} + \mathbf {w} - G \mathbf {v}. \tag {7.66}$$

We consider the estimate of a scalar function

$$z = \mathbf {k} ^ {T} \mathbf {x} \tag {7.67}$$

where $\mathbf{k}^T$ is a row vector. For example, Equation 7.67 could represent a state feedback law for a system with one input. The estimation error is

$$\widetilde {z} = z - \widehat {z} = \mathbf {k} ^ {T} \mathbf {x} - \mathbf {k} ^ {T} \widehat {\mathbf {x}} = \mathbf {k} ^ {T} \widetilde {\mathbf {x}}. \tag {7.68}$$

The zero-state response $\widetilde{z}_{w}(t)$ to an input $\mathbf{w}(t)=\mathbf{w}_{0}u_{0}(t)$ is, from Equations 7.66 and 7.67,

$$\widetilde {z} _ {w} (t) = \mathbf {k} ^ {T} e ^ {(A - G C) t} \mathbf {w} _ {0}, \quad t > 0. \tag {7.69}$$

Similarly, the zero-state response $\widetilde{z}_v(t)$ to $\mathbf{v}(t) = \mathbf{v}_0u_0(t)$ is

$$\widetilde {z} _ {v} (t) = - \mathbf {k} ^ {T} e ^ {(A - G C) t} G \mathbf {v} _ {0}, \quad t > 0. \tag {7.70}$$

The use of an impulse to model $\mathbf{w}(t)$ is not as restrictive as it may appear. Any signal that can be modeled as the impulse response of a lumped-parameter LTI system can be included in this formulation; all we need do is derive the state-space model that generates the signal, and append it to the plant description. The impulse model used to describe the measurement noise represents a spike error in measurement. The impulses are actually the deterministic counterparts of the so-called white-noise processes in the stochastic framework that underlies this theory.

Examination of Equation 7.69 reveals that $\widetilde{z}_w(t)$ will be driven rapidly to zero if the eigenvalues of $A - GC$ are large and stable; this calls for a $G$ with large elements. On the other hand, we conclude from Equation 7.70 that a large $G$ will give a large value of $\widetilde{z}_v(t)$ for small $t$ , which is undesirable. A compromise between speed of response and initial value is sought, by minimization of

$$J = \int_ {0} ^ {\infty} [ \widetilde {z} _ {w} ^ {2} (t) + \widetilde {z} _ {v} ^ {2} (t) ] d t. \tag {7.71}$$

This performance index penalizes both slow convergence and large initial values. The solution is drawn directly from LQ theory. For technical reasons, we prove the result for scalar output.
