$$
\begin{array}{l} \mathbf {u} = \mathbf {K} (\mathbf {r} - \mathbf {x}) - \mathbf {k} _ {\text {error}} u _ {\text {error}} \\ \mathbf {u} = \left[ \begin{array}{c c} \mathbf {K} & \mathbf {k} _ {e r r o r} \end{array} \right] \left(\left[ \begin{array}{c} \mathbf {r} \\ 0 \end{array} \right] - \left[ \begin{array}{c} \mathbf {x} \\ u _ {e r r o r} \end{array} \right]\right) \\ \end{array}
$$

where $\mathbf { k } _ { e r r o r }$ is a column vector with a 1 in a given row if $u _ { e r r o r } $ should be applied to that input or a 0 otherwise.

This process can be repeated for an arbitrary error which can be corrected via some linear combination of the inputs.
