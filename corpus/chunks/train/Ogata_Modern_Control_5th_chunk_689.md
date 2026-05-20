The principle of duality states that the system $S _ { 1 }$ is completely state controllable (observable) if and only if system $S _ { 2 }$ is completely observable (state controllable).

To verify this principle, let us write down the necessary and sufficient conditions for complete state controllability and complete observability for systems $S _ { 1 }$ and $S _ { 2 }$ .

For system $S _ { 1 }$ :

1. A necessary and sufficient condition for complete state controllability is that the rank of the n\*nr matrix

$$
\left[ \begin{array}{c c c c} \mathbf {B} & \mathbf {A B} & \dots & \mathbf {A} ^ {n - 1} \mathbf {B} \end{array} \right]
$$

be n.

2. A necessary and sufficient condition for complete observability is that the rank of the n\*nm matrix

$$
\left[ \begin{array}{c c c c} \mathbf {C} ^ {*} & \mathbf {A} ^ {*} \mathbf {C} ^ {*} & \dots & (\mathbf {A} ^ {*}) ^ {n - 1} \mathbf {C} ^ {*} \end{array} \right]
$$

be n.

For system $S _ { 2 }$ :

1. A necessary and sufficient condition for complete state controllability is that the rank of the n\*nm matrix

$$
\left[ \begin{array}{c c c c} \mathbf {C} ^ {*} & \mathbf {A} ^ {*} \mathbf {C} ^ {*} & \dots & (\mathbf {A} ^ {*}) ^ {n - 1} \mathbf {C} ^ {*} \end{array} \right]
$$

be n.

2. A necessary and sufficient condition for complete observability is that the rank of the n\*nr matrix

$$
\left[ \begin{array}{c c c c} \mathbf {B} & \mathbf {A B} & \dots & \mathbf {A} ^ {n - 1} \mathbf {B} \end{array} \right]
$$

be n.

By comparing these conditions, the truth of this principle is apparent. By use of this principle, the observability of a given system can be checked by testing the state controllability of its dual.

Detectability. For a partially observable system, if the unobservable modes are stable and the observable modes are unstable, the system is said to be detectable. Note that the concept of detectability is dual to the concept of stabilizability.
