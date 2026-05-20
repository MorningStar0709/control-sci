# 6.9.2 Model augmentation

As per subsection 6.7.2, we will now augment the model so a $u _ { e r r o r } $ state is added to the control input.

The plant and observer augmentations should be performed before the model is discretized. After the controller gain is computed with the unaugmented discrete model, the controller may be augmented. Therefore, the plant and observer augmentations assume a continuous model and the controller augmentation assumes a discrete controller.

$$
\mathbf {x} _ {a u g} = \left[ \begin{array}{c} x \\ v \\ u _ {e r r o r} \end{array} \right] \quad \mathbf {y} = x \quad \mathbf {u} = V

\mathbf {A} _ {a u g} = \left[ \begin{array}{c c} \mathbf {A} & \mathbf {B} \\ \mathbf {0} _ {1 \times 2} & 0 \end{array} \right] \quad \mathbf {B} _ {a u g} = \left[ \begin{array}{c} \mathbf {B} \\ 0 \end{array} \right] \quad \mathbf {C} _ {a u g} = \left[ \begin{array}{c c} \mathbf {C} & 0 \end{array} \right] \quad \mathbf {D} _ {a u g} = \mathbf {D} \tag {6.11}

\mathbf {K} _ {a u g} = \left[ \begin{array}{l l} \mathbf {K} & 1 \end{array} \right] \quad \mathbf {r} _ {a u g} = \left[ \begin{array}{l} \mathbf {r} \\ 0 \end{array} \right] \tag {6.12}
$$

This will compensate for unmodeled dynamics such as gravity. However, using a constant voltage feedforward to counteract gravity is preferred over $u _ { e r r o r } $ estimation in this case because it results in a simpler controller with similar performance.
