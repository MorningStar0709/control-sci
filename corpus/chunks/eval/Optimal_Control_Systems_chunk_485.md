# B.4 Controllability and Observability

Let us first consider the LTI, continuous-time system (B.1.1). Similar results are available for discrete-time systems [35]. The system (B.1.1) with the pair $(\mathbf{A}:nxn,\mathbf{B}:nxr)$ is called completely state controllable if any of the following conditions is satisfied:

1. rank of the controllability matrix

$$
\mathbf {Q} _ {c} = \left[ \begin{array}{l l l l} \mathbf {B} & \mathbf {A B} & \mathbf {A} ^ {2} \mathbf {B} \dots \mathbf {A} ^ {n - 1} \mathbf {B} \end{array} \right] \tag {B.4.1}
$$

is $n$ (full row rank), or

2. the controllability Grammian

$$
\begin{array}{l} \mathbf {W} _ {c} (t) = \int_ {0} ^ {t} e ^ {\mathbf {A} \tau} \mathbf {B} \mathbf {B} ^ {\prime} e ^ {\mathbf {A} ^ {\prime} \tau} d \tau \\ = \int_ {0} ^ {t} e ^ {\mathbf {A} (t - \tau)} \mathbf {B} \mathbf {B} ^ {\prime} e ^ {\mathbf {A} ^ {\prime} (t - \tau)} d \tau \tag {B.4.2} \\ \end{array}
$$

is nonsingular for any $t > 0$ .

The system (B.1.1) with the pair $(\mathbf{A}:nxn,\mathbf{C}:pxn)$ is completely observable if any of the following conditions is satisfied:

1. rank of the observability matrix

$$
\mathbf {Q} _ {o} = \left[ \begin{array}{l l l l} \mathbf {C} & \mathbf {C A} & \mathbf {C A} ^ {2} \dots \mathbf {C A} ^ {n - 1} \end{array} \right] ^ {\prime} \tag {B.4.3}
$$

has rank $n$ (full column rank).

2. the observability Grammian

$$\mathbf {W} _ {o} (t) = \int_ {0} ^ {t} e ^ {\mathbf {A} ^ {\prime} \tau} \mathbf {C} ^ {\prime} \mathbf {C} e ^ {\mathbf {A} \tau} d \tau \tag {B.4.4}$$

is nonsingular for any $t > 0$ .

Other conditions also exist for controllability and observability [35].
