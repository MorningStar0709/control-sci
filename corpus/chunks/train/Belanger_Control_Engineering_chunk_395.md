We now argue that $\delta P_{1}$ must be zero. If $K^{*}$ is indeed optimal, the minimum value of $J$ is $\mathbf{x}^T(0)P^*\mathbf{x}(0)$ , and therefore

$$\epsilon \mathbf {x} ^ {T} (0) \delta P _ {1} \mathbf {x} (0) + \epsilon^ {2} \mathbf {x} ^ {T} (0) \delta P _ {2} \mathbf {x} (0) + \dots \geq 0 \tag {7.33}$$

for all $\mathbf{x}(0)$ .

Suppose $\delta P_{1} \neq 0$ . Then, for some $\mathbf{x}(0)$ , $\mathbf{x}^{T}(0) \delta P_{1}\mathbf{x}(0) \neq 0$ . Choose $\epsilon$ small enough that the first term on the LHS of Equation 7.33 dominates and the sign of the LHS is that of the term in $\epsilon$ . By choosing the sign of $\epsilon$ , we can make $\epsilon\mathbf{x}^{T}(0) \delta P_{1}\mathbf{x}(0)$ negative, thus violating Equation 7.33. Hence, it is necessary that $\delta P_{1} = 0$ .

If that is so, then, from Equation 7.32,

$$\delta K ^ {T} (B ^ {T} P ^ {*} - R K ^ {*}) + (P ^ {*} B - K ^ {* T} R) \delta K = 0$$

or

$$\delta K ^ {T} (B ^ {T} P ^ {*} - R K ^ {*}) + [ \delta K ^ {T} (B ^ {T} P ^ {*} - R K ^ {*} ] ^ {T} = 0.$$

Since this must hold for all perturbations $\delta K$ , it is necessary that

$$B ^ {T} P ^ {*} - R K ^ {*} = 0$$

or

$$K ^ {*} = R ^ {- 1} B ^ {T} P ^ {*}.$$

Inserting this in Equation 7.30 yields

$$A ^ {T} P ^ {*} - P ^ {*} B R ^ {- 1} B ^ {T} P ^ {*} + P ^ {*} A - P ^ {*} B R ^ {- 1} B ^ {T} P ^ {*} = - Q - P ^ {*} B R ^ {- 1} R R ^ {- 1} B ^ {T} P ^ {*}$$

or

$$A ^ {T} P ^ {*} + P A ^ {*} - P ^ {*} B R ^ {- 1} B ^ {T} P ^ {*} + Q = 0$$

where the fact that $P^{*}$ is symmetric ( $= P^{*^T}$ ) has been used. This completes the proof.

As things stand, we need to solve the matrix Riccati equation, Equation 7.28, for P; calculate K from Equation 7.27; and check A - BK for stability. Since the Riccati equation is nonlinear, it generally has many solutions, so we must pick out the stabilizing ones and compare values of J. Fortunately, we can avoid most of that process.

First, we impose the requirement that $(A, Q^{1/2})$ be detectable. Suppose it is not. Then there exists an unstable, unobservable mode with eigenvalue $s_{i}$ and eigenvector $v_{i}$ . Then, for $\mathbf{x}(0) = \mathbf{v}_{i}$ , $\mathbf{x}(t) = \mathbf{v}_{i} e^{s_{i} t}$ and $\mathbf{x}^{T} Q \mathbf{x} = \mathbf{v}_{i}^{T} (Q^{1/2})^{T} Q^{1/2} \mathbf{v}_{i} e^{2s_{i} t} = 0$ . The performance index does not penalize this mode, so the mathematics of the optimization leave it unchanged, and the closed-loop system is not internally stable.
