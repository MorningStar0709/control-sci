# 6.6.4 Output augmentation

Output augmentation is the process of adding rows to the C matrix. This is done to help the controls designer visualize the behavior of internal states or other aspects of the system in MATLAB or Python Control. C matrix augmentation doesn’t affect state feedback, so the designer has a lot of freedom here. Noting that the output is defined as y = Cx + Du, the following row augmentations of C may prove useful. Of course, D needs to be augmented with zeroes as well in these cases to maintain the correct matrix dimensionality.

Since u = −Kx, augmenting C with −K makes the observer estimate the control input u applied.

$$
\begin{array}{l} \mathbf {y} = \mathbf {C x} + \mathbf {D u} \\ \left[ \begin{array}{c} \mathbf {y} \\ \mathbf {u} \end{array} \right] = \left[ \begin{array}{c} \mathbf {C} \\ - \mathbf {K} \end{array} \right] \mathbf {x} + \left[ \begin{array}{c} \mathbf {D} \\ \mathbf {0} \end{array} \right] \mathbf {u} \\ \end{array}
$$

This works because K has the same number of columns as states.

Various states can also be produced in the output with I matrix augmentation.
