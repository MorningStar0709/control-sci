# Alternate Forms for the DRE

Alternate forms which do not require the inversion of the matrix $\mathbf{A}(k)$ for the matrix DRE (5.3.11) and the optimal control (5.3.16) are obtained as follows. Using the well-known matrix inversion lemma

$$\left[ \mathbf {A} _ {1} ^ {- 1} + \mathbf {A} _ {2} \mathbf {A} _ {4} \mathbf {A} _ {3} \right] ^ {- 1} = \mathbf {A} _ {1} - \mathbf {A} _ {1} \mathbf {A} _ {2} \left[ \mathbf {A} _ {3} \mathbf {A} _ {1} \mathbf {A} _ {2} + \mathbf {A} _ {4} ^ {- 1} \right] ^ {- 1} \mathbf {A} _ {3} \mathbf {A} _ {1} \tag {5.3.19}$$

in (5.3.12), and manipulating, we have the matrix DRE as

$$
\begin{array}{l} \mathbf {P} (k) = \mathbf {A} ^ {\prime} (k) \left\{\mathbf {P} (k + 1) - \mathbf {P} (k + 1) \mathbf {B} (k). \right. \\ \left. \left[ \mathbf {B} ^ {\prime} (k) \mathbf {P} (k + 1) \mathbf {B} (k) + \mathbf {R} (k) \right] ^ {- 1} \mathbf {B} ^ {\prime} (k) \mathbf {P} (k + 1) \right\} \mathbf {A} (k) \\ + \mathbf {Q} (k). \tag {5.3.20} \\ \end{array}
$$

Next, consider the optimal control (5.3.2) and the transformation (5.3.6), to get

$$\mathbf {u} ^ {*} (k) = - \mathbf {R} ^ {- 1} (k) \mathbf {B} ^ {\prime} (k) \mathbf {P} (k + 1) \mathbf {x} ^ {*} (k + 1) \tag {5.3.21}$$

which upon using the state equation (5.2.1) becomes

$$\mathbf {u} ^ {*} (k) = - \mathbf {R} ^ {- 1} (k) \mathbf {B} ^ {\prime} (k) \mathbf {P} (k + 1) [ \mathbf {A} (k) \mathbf {x} ^ {*} (k) + \mathbf {B} (k) \mathbf {u} ^ {*} (k) ]. \tag {5.3.22}$$

Rearranging, we have

$$
\begin{array}{l} \left[ \mathbf {I} + \mathbf {R} ^ {- 1} (k) \mathbf {B} ^ {\prime} (k) \mathbf {P} (k + 1) \mathbf {B} (k) \right] \mathbf {u} ^ {*} (k) = \\ - \mathbf {R} ^ {- 1} (k) \mathbf {B} ^ {\prime} (k) \mathbf {P} (k + 1) \mathbf {A} (k) \mathbf {x} ^ {*} (k). \tag {5.3.23} \\ \end{array}
$$

Premultiplying by $\mathbf{R}(k)$ and solving for $\mathbf{u}^*(k)$ ,

$$\boxed {\mathbf {u} ^ {*} (k) = - \mathbf {L} _ {a} (k) \mathbf {x} ^ {*} (k)} \tag {5.3.24}$$

where, $\mathbf{L}_a(k)$ , called the Kalman gain matrix is

$$\boxed {\mathbf {L} _ {a} (k) = \left[ \mathbf {B} ^ {\prime} (k) \mathbf {P} (k + 1) \mathbf {B} (k) + \mathbf {R} (k) \right] ^ {- 1} \mathbf {B} ^ {\prime} (k) \mathbf {P} (k + 1) \mathbf {A} (k).} \tag {5.3.25}$$
