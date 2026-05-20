# ■ Theorem 7.9

Suppose $(C, A)$ is detectable, $(A, \mathbf{w}_0)$ is stabilizable, and, $v_0 > 0$ . The gain $G$ that minimizes the performance index $J$ of Equation 7.69 is

$$G = P C ^ {T} V ^ {- 1} \tag {7.72}$$

where P is the positive definite solution of the Riccati equation,

$$A P + P A ^ {T} - P C ^ {T} V ^ {- 1} C P + W = 0. \tag {7.73}$$

Here, $V = v_{0}^{2}$ and $W = w_{0}w_{0}^{T}$ .

Proof: From Equations 7.69, 7.70, and 7.71,

$$J = \int_ {0} ^ {\infty} \left[ \mathbf {k} ^ {T} e ^ {(A - G C) t} \mathbf {w} _ {0} \mathbf {w} _ {0} ^ {T} e ^ {(A - G C) ^ {T} t} \mathbf {k} + \mathbf {k} ^ {T} e ^ {(A - G C) t} G v _ {0} ^ {2} G ^ {T} e ^ {(A - G C) ^ {T} t} \mathbf {k} \right] d t$$

where we have used the fact that $\widetilde{z}_w^T = \widetilde{z}_w$ , since $\widetilde{z}_w$ is a scalar. We write this as

$$J = \mathbf {k} ^ {T} \left[ \int_ {0} ^ {\infty} e ^ {(A ^ {T} - C ^ {T} G ^ {T}) ^ {T} t} (W + G V G ^ {T}) e ^ {(A ^ {T} - C ^ {T} G ^ {T}) t} d t \right] \mathbf {k}. \tag {7.74}$$

We can relate this to the LQ problem as follows. Define the system

$$\dot {\theta} = A ^ {T} \theta + C ^ {T} \psi . \tag {7.75}$$

A control law $\psi = -G^T\theta$ applied to this system results in

$$\dot {\theta} = (A ^ {T} - C ^ {T} G ^ {T}) \theta .$$

The response for an initial state $\theta(0) = \mathbf{k}$ is $\theta(t) = e^{(A^T - C^T G^T)_I}\mathbf{k}$ . Thus, $J$ in Equation 7.74 is written

$$J = \int_ {0} ^ {\infty} \theta^ {T} (t) [ W + (G ^ {T}) ^ {T} V (G ^ {T}) ] \theta (t) d t. \tag {7.76}$$

The minimization of $J$ , with $\theta(t)$ described by Equation 7.75, is an LQ problem. The matrix $W$ replaces $Q$ , $V$ replaces $R$ , and $G^T$ stands for $K$ . The detectability of $(W^{1/2}, A^T)$ is ensured by the stabilizability of $(A, \mathbf{w}_0)$ because of duality; the stabilizability of $(A^T, C^T)$ follows from the assumption that $(C, A)$ is detectable.

The solution of the LQ problem is

$$G ^ {T} = V ^ {- 1} \left(C ^ {T}\right) ^ {T} P \tag {7.77}$$

where $P$ satisfies the Riccati equation,

$$(A ^ {T}) ^ {T} P + P (A ^ {T}) - P (C ^ {T}) V ^ {- 1} \left(C ^ {T}\right) ^ {T} P + W = 0. \tag {7.78}$$

Transposition of Equation 7.74 yields

$$G = P C ^ {T} V ^ {- 1}$$

where the fact that $P$ and $V$ are symmetric is used. Equation 7.78 is written as

$$A P + P A ^ {T} - P C ^ {T} V ^ {- 1} C P + W = 0.$$

This completes the proof.
