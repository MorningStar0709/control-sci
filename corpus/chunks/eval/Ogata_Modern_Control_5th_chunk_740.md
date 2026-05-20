$$
\begin{array}{l} \phi (\mathbf {A}) = \mathbf {B} \left(\alpha_ {2} \mathbf {K} + \alpha_ {1} \mathbf {K} \widetilde {\mathbf {A}} + \mathbf {K} \widetilde {\mathbf {A}} ^ {2}\right) + \mathbf {A B} \left(\alpha_ {1} \mathbf {K} + \mathbf {K} \widetilde {\mathbf {A}}\right) + \mathbf {A} ^ {2} \mathbf {B K} \\ = \left[ \begin{array}{c c c c} \mathbf {B} & \vdots & \mathbf {A B} & \vdots \\ \hline \end{array} \right] \left[ \begin{array}{c} \alpha_ {2} \mathbf {K} + \alpha_ {1} \mathbf {K} \widetilde {\mathbf {A}} + \mathbf {K} \widetilde {\mathbf {A}} ^ {2} \\ \alpha_ {1} \mathbf {K} + \mathbf {K} \widetilde {\mathbf {A}} \\ \mathbf {K} \end{array} \right] \tag {10-17} \\ \end{array}
$$

Since the system is completely state controllable, the inverse of the controllability matrix

$$
\left[ \begin{array}{c c c} \mathbf {B} & \mathbf {A B} & \mathbf {A} ^ {2} \mathbf {B} \end{array} \right]
$$

exists. Premultiplying both sides of Equation (10–17) by the inverse of the controllability matrix, we obtain

$$
\left[ \begin{array}{c c c c} \mathbf {B} & \mathbf {A B} & \mathbf {A ^ {2} B} \end{array} \right] ^ {- 1} \phi (\mathbf {A}) = \left[ \begin{array}{c} \alpha_ {2} \mathbf {K} + \alpha_ {1} \widetilde {\mathbf {K A}} + \mathbf {K} \widetilde {\mathbf {A}} ^ {2} \\ \alpha_ {1} \mathbf {K} + \mathbf {K} \widetilde {\mathbf {A}} \\ \mathbf {K} \end{array} \right]
$$

Premultiplying both sides of this last equation by $[ 0 \_ { 0 } \_ { 1 } ]$ , we obtain

$$
[ 0 \quad 0 \quad 1 ] [ \mathbf {B} \mid \mathbf {A B} \mid \mathbf {A} ^ {2} \mathbf {B} ] ^ {- 1} \phi (\mathbf {A}) = [ 0 \quad 0 \quad 1 ] \left[ \begin{array}{c} \alpha_ {2} \mathbf {K} + \alpha_ {1} \mathbf {K} \widetilde {\mathbf {A}} + \mathbf {K} \widetilde {\mathbf {A}} ^ {2} \\ \alpha_ {1} \mathbf {K} + \mathbf {K} \widetilde {\mathbf {A}} \\ \mathbf {K} \end{array} \right] = \mathbf {K}
$$

which can be rewritten as

$$
\mathbf {K} = \left[ \begin{array}{c c c} 0 & 0 & 1 \end{array} \right] \left[ \begin{array}{c c c} \mathbf {B} & \mathbf {A B} & \mathbf {A} ^ {2} \mathbf {B} \end{array} \right] ^ {- 1} \phi (\mathbf {A})
$$

This last equation gives the required state feedback gain matrix K.

For an arbitrary positive integer n, we have

$$
\mathbf {K} = \left[ \begin{array}{l l l l l} 0 & 0 & \dots & 0 & 1 \end{array} \right] \left[ \begin{array}{c c c c c} \mathbf {B} & \mathbf {A B} & \dots & \mathbf {A} ^ {n - 1} \mathbf {B} \end{array} \right] ^ {- 1} \phi (\mathbf {A}) \tag {10-18}
$$
