# Constrained One-Step Minimization

One class of suboptimal dual controllers is obtained by constrained one-step minimization. Suggested constraints are

- Limitation of the minimum value of the control signal and   
- Limitation of the variance.

One method is to choose the control as

$$
u (t) = \left\{ \begin{array}{l l} u _ {\text { lim }} \cdot \operatorname{sign} (u _ {\text { cautious }}) & \quad \text { if } | u _ {\text { cautious }} | <   | u _ {\text { lim }} | \\ u _ {\text { cautious }} & \quad \text { if } | u _ {\text { cautious }} | \geq | u _ {\text { lim }} | \end{array} \right.
$$

This will give an extra probing signal if the cautious controller gives too small an input signal.

Different ways to constrain the minimization by using the P-matrix have been suggested. For instance, the one-step loss of Eq. (7.14) can be minimized under the constraint that

$$\operatorname{tr} P ^ {- 1} (t + 2) \geq M$$

$P^{-1}$ is proportional to the information matrix. The constraint on the trace of $P^{-1}$ means that the information about the parameters is always larger than some chosen value M. A similar approach is to constrain only the variance of $\hat{b}_{0}$ to

$$
p _ {b _ {0}} (t + 2) \leq \left\{ \begin{array}{l l} \gamma \hat {b} _ {0} ^ {2} (t + 2) & \text { if } p _ {b _ {0}} (t + 1) \leq \hat {b} _ {0} ^ {2} (t + 1) \\ \alpha p _ {b _ {0}} (t + 1) & \text { otherwise } \end{array} \right.
$$

These modifications of the cautious controller have the advantage that the control signal can be easily computed, but the algorithms will contain application-dependent parameters that have to be chosen by the user. Finally, the approximations will not prevent the turn-off. The extra perturbation is not activated until the turn-off occurs.
