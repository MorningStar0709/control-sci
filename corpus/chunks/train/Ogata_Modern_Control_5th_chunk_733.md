This means that there are q linearly independent column vectors in the controllability matrix. Let us define such q linearly independent column vectors as $\mathbf { f } _ { 1 } , \mathbf { f } _ { 2 } , \ldots , \mathbf { f } _ { q }$ . Also, let us choose $n - q$ additional n-vectors $\mathbf { v } _ { q { \mathrm { ~ + ~ } } 1 } , \mathbf { v } _ { q { \mathrm { ~ + ~ } } 2 } , \ldots , \mathbf { v } _ { n }$ such that

$$
\mathbf {P} = \left[ \begin{array}{c c c c c c c c c} \mathbf {f} _ {1} & \mathbf {f} _ {2} & \dots & \mathbf {f} _ {q} & \mathbf {v} _ {q + 1} & \mathbf {v} _ {q + 2} & \dots & \mathbf {v} _ {n} \end{array} \right]
$$

is of rank n. Then it can be shown that

$$
\hat {\mathbf {A}} = \mathbf {P} ^ {- 1} \mathbf {A} \mathbf {P} = \left[ \begin{array}{c c} \mathbf {A} _ {1 1} & \mathbf {A} _ {1 2} \\ \hline \mathbf {0} & \mathbf {A} _ {2 2} \end{array} \right], \qquad \hat {\mathbf {B}} = \mathbf {P} ^ {- 1} \mathbf {B} = \left[ \begin{array}{c} \mathbf {B} _ {1 1} \\ \hline \mathbf {0} \end{array} \right]
$$

(See Problem A–10–1 for the derivation of these equations.) Now define

$$
\hat {\mathbf {K}} = \mathbf {K P} = \left[ \begin{array}{c c} \mathbf {k} _ {1} & \mathbf {k} _ {2} \end{array} \right]
$$

Then we have

$$
\begin{array}{l} \left| s \mathbf {I} - \mathbf {A} + \mathbf {B K} \right| = \left| \mathbf {P} ^ {- 1} (s \mathbf {I} - \mathbf {A} + \mathbf {B K}) \mathbf {P} \right| \\ = \left| s \mathbf {I} - \mathbf {P} ^ {- 1} \mathbf {A P} + \mathbf {P} ^ {- 1} \mathbf {B K P} \right| \\ = \left| s \mathbf {I} - \hat {\mathbf {A}} + \hat {\mathbf {B}} \hat {\mathbf {K}} \right| \\ = \left| s \mathbf {I} - \left[ \begin{array}{c c} \mathbf {A} _ {1 1} & \mathbf {A} _ {1 2} \\ \hline \mathbf {0} & \mathbf {A} _ {2 2} \end{array} \right] + \left[ \begin{array}{c} \mathbf {B} _ {1 1} \\ \hline \mathbf {0} \end{array} \right] \left[ \begin{array}{c c} \mathbf {k} _ {1} & \mathbf {k} _ {2} \end{array} \right] \right| \\ = \left| \begin{array}{c c} s \mathbf {I} _ {q} - \mathbf {A} _ {1 1} + \mathbf {B} _ {1 1} \mathbf {k} _ {1} & - \mathbf {A} _ {1 2} + \mathbf {B} _ {1 1} \mathbf {k} _ {2} \\ \mathbf {0} & s \mathbf {I} _ {n - q} - \mathbf {A} _ {2 2} \end{array} \right| \\ = \left| s \mathbf {I} _ {q} - \mathbf {A} _ {1 1} + \mathbf {B} _ {1 1} \mathbf {k} _ {1} \right| \cdot \left| s \mathbf {I} _ {n - q} - \mathbf {A} _ {2 2} \right| = 0 \\ \end{array}
$$

where $\mathbf { I } _ { q }$ is a q-dimensional identity matrix and $\mathbf { I } _ { n \mathrm { ~ - ~ } q }$ is an $( n - q )$ -dimensional identity matrix.
