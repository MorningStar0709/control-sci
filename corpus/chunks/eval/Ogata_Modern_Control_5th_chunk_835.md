$$
\begin{array}{l} \left[ \begin{array}{c c c c c c c c} \mathbf {A f} _ {1} & \mathbf {A f} _ {2} & \dots & \mathbf {A f} _ {q} & \mathbf {A v} _ {q + 1} & \dots & \mathbf {A v} _ {n} \end{array} \right] \\ = \left[ \begin{array}{c c c c c c c c} \mathbf {f} _ {1} & \mathbf {f} _ {2} & \dots & \mathbf {f} _ {q} & \mathbf {v} _ {q + 1} & \dots & \mathbf {v} _ {n} \end{array} \right] \left[ \begin{array}{c c} \mathbf {A} _ {1 1} & \mathbf {A} _ {1 2} \\ \hline \mathbf {0} & \mathbf {A} _ {2 2} \end{array} \right] \\ \end{array}
$$

Thus,

$$
\mathbf {A} \mathbf {P} = \mathbf {P} \left[ \begin{array}{c c} \mathbf {A} _ {1 1} & \mathbf {A} _ {1 2} \\ \hline \mathbf {0} & \mathbf {A} _ {2 2} \end{array} \right]
$$

Hence,

$$
\mathbf {P} ^ {- 1} \mathbf {A} \mathbf {P} = \hat {\mathbf {A}} = \left[ \begin{array}{c c} \mathbf {A} _ {1 1} & \mathbf {A} _ {1 2} \\ \hline \mathbf {0} & \mathbf {A} _ {2 2} \end{array} \right]
$$

Next, referring to Equation (10–138), we have

$$
\mathbf {B} = \left[ \begin{array}{c c c c c c c c} \mathbf {f} _ {1} & \mathbf {f} _ {2} & \dots & \mathbf {f} _ {q} & \mathbf {v} _ {q + 1} & \dots & \mathbf {v} _ {n} \end{array} \right] \hat {\mathbf {B}} \tag {10-139}
$$

Referring to Equation (10–136), notice that vector B can be written in terms of $q$ linearly independent column vectors $\mathbf { f } _ { 1 } , \mathbf { f } _ { 2 } , \ldots , \mathbf { f } _ { q } .$ . Thus, we have

$$\mathbf {B} = b _ {1 1} \mathbf {f} _ {1} + b _ {2 1} \mathbf {f} _ {2} + \dots + b _ {q 1} \mathbf {f} _ {q}$$

Consequently, Equation (10–139) may be written as follows:

$$
b _ {1 1} \mathbf {f} _ {1} + b _ {2 1} \mathbf {f} _ {2} + \dots + b _ {q 1} \mathbf {f} _ {q} = \left[ \begin{array}{c c c c c c c c c} \mathbf {f} _ {1} & \mathbf {f} _ {2} & \dots & \mathbf {f} _ {q} & \mathbf {v} _ {q + 1} & \dots & \mathbf {v} _ {n} \end{array} \right] \left[ \begin{array}{c} b _ {1 1} \\ b _ {2 1} \\ . \\ . \\ . \\ b _ {q 1} \\ 0 \\ . \\ . \\ . \\ 0 \end{array} \right]
$$

Thus,

$$
\hat {\mathbf {B}} = \left[ \begin{array}{c} \mathbf {B} _ {1 1} \\ \hline \mathbf {0} \end{array} \right]
$$

where

$$
\mathbf {B} _ {1 1} = \left[ \begin{array}{c} b _ {1 1} \\ b _ {2 1} \\ \cdot \\ \cdot \\ \cdot \\ b _ {q 1} \end{array} \right]
$$

A–10–2. Consider a completely state controllable system

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} u$$

Define the controllability matrix as M:

$$
\mathbf {M} = \left[ \begin{array}{c c c c} \mathbf {B} & \mathbf {A B} & \dots & \mathbf {A} ^ {n - 1} \mathbf {B} \end{array} \right]
$$

Show that
