# 6.7.2 Input error estimation

Models can predict system behavior, but unmodeled disturbances make the observed system behavior deviate from the model. We want to react to these disturbances quickly and improve the model’s predictive power in the face of these disturbances.

Input error estimation uses a state observer (covered in chapter 9) to estimate the difference between the provided model input and a hypothetical input that makes the model match the observed behavior. Subtracting this value from the provided input compensates for unmodeled disturbances, and adding it to the state observer’s input makes the model better predict the system’s future behavior.

First, we’ll consider the one-dimensional case. Let $u _ { e r r o r } $ be the difference between the hypothetical input with disturbances and the provided input. The $u _ { e r r o r } $ term is then added to the system as follows.

$$\dot {x} = A x + B \left(u + u _ {\text { error }}\right)$$

$u + u _ { e r r o r } $ is the hypothetical input actually applied to the system.

$$\dot {x} = A x + B u + B u _ {e r r o r}$$

The following equation generalizes this to a multiple-input system.

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} \mathbf {u} + \mathbf {B} _ {e r r o r} u _ {e r r o r}$$

where $\mathbf { B } _ { e r r o r }$ is a column vector that maps $u _ { e r r o r } $ to changes in the rest of the state the same way B does for u. $\mathbf { B } _ { e r r o r }$ is only a column of B if $u _ { e r r o r } $ corresponds to an existing input within u.

Given the above equation, we’ll augment the plant as

$$
\begin{array}{l} \left[ \begin{array}{c} \dot {\mathbf {x}} \\ u _ {e r r o r} \end{array} \right] = \left[ \begin{array}{c c} \mathbf {A} & \mathbf {B} _ {e r r o r} \\ \mathbf {0} & \mathbf {0} \end{array} \right] \left[ \begin{array}{c} \mathbf {x} \\ u _ {e r r o r} \end{array} \right] + \left[ \begin{array}{c} \mathbf {B} \\ \mathbf {0} \end{array} \right] \mathbf {u} \\ \mathbf {y} = \left[ \begin{array}{c c} \mathbf {C} & 0 \end{array} \right] \left[ \begin{array}{c} \mathbf {x} \\ u _ {e r r o r} \end{array} \right] + \mathbf {D u} \\ \end{array}
$$

Notice how the state is augmented with $u _ { e r r o r }$ . With this model, the observer will estimate both the state and the $u _ { e r r o r } $ term. The controller is augmented similarly. r is augmented with a zero for the goal $u _ { e r r o r } $ term.
