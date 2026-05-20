# U error estimation

As per subsection 6.7.2, we will now augment the model so $u _ { e r r o r } $ states are added to the control inputs.

The plant and observer augmentations should be performed before the model is discretized. After the controller gain is computed with the unaugmented discrete model, the controller may be augmented. Therefore, the plant and observer augmentations assume a continuous model and the controller augmentation assumes a discrete controller.

The three $u _ { e r r o r } $ states we’ll be adding are $u _ { e r r o r , l } , u _ { e r r o r , r } ,$ , and $u _ { e r r o r , h e a d i n g }$ for left voltage error, right voltage error, and heading error respectively. The left and right wheel positions are filtered encoder positions and are not adjusted for heading error. The turning angle computed from the left and right wheel positions is adjusted by the gyroscope heading. The heading $u _ { e r r o r } $ state is the heading error between what the wheel positions imply and the gyroscope measurement.

The full state is thus

$$
\mathbf {x} = \left[ \begin{array}{c} x \\ y \\ \theta \\ v _ {l} \\ v _ {r} \\ x _ {l} \\ x _ {r} \\ u _ {e r r o r, l} \\ u _ {e r r o r, r} \\ u _ {e r r o r, h e a d i n g} \end{array} \right]
$$

The complete nonlinear model is as follows. Let $\begin{array} { r } { v = \frac { v _ { l } + v _ { r } } { 2 } } \end{array}$ . The three $u _ { e r r o r }$ states augment the linear subspace, so the nonlinear pose dynamics are the same.

$$
\left[ \begin{array}{l} \dot {x} \\ y \\ \theta \end{array} \right] = \left[ \begin{array}{c} v \cos \theta \\ v \sin \theta \\ \frac {v _ {r}}{2 r _ {b}} - \frac {v _ {l}}{2 r _ {b}} \end{array} \right] \tag {8.20}
$$

The left and right voltage error states should be mapped to the corresponding velocity states, so the system matrix should be augmented with B.

The heading $u _ { e r r o r } $ is measuring counterclockwise encoder understeer relative to the gyroscope heading, so it should add to the left position and subtract from the right position for clockwise correction of encoder positions. That corresponds to the following input mapping vector.

$$
\mathbf {B} _ {\theta} = \left[ \begin{array}{l} 0 \\ 0 \\ 1 \\ - 1 \end{array} \right]
$$

Now we’ll augment the linear system matrix horizontally to accommodate the $u _ { e r r o r } $ states.
