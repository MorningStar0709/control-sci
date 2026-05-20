# Eigenvalues of closed-loop observer

The eigenvalues of the system matrix can be used to determine whether a state observer’s estimate will converge to the true state.

Plugging equation (9.4) into equation (9.3) gives

$$\hat {\mathbf {x}} _ {k + 1} = \mathbf {A} \hat {\mathbf {x}} _ {k} + \mathbf {B} \mathbf {u} _ {k} + \mathbf {L} (\mathbf {y} _ {k} - \hat {\mathbf {y}} _ {k})\hat {\mathbf {x}} _ {k + 1} = \mathbf {A} \hat {\mathbf {x}} _ {k} + \mathbf {B} \mathbf {u} _ {k} + \mathbf {L} (\mathbf {y} _ {k} - (\mathbf {C} \hat {\mathbf {x}} _ {k} + \mathbf {D} \mathbf {u} _ {k}))\hat {\mathbf {x}} _ {k + 1} = \mathbf {A} \hat {\mathbf {x}} _ {k} + \mathbf {B} \mathbf {u} _ {k} + \mathbf {L} (\mathbf {y} _ {k} - \mathbf {C} \hat {\mathbf {x}} _ {k} - \mathbf {D} \mathbf {u} _ {k})$$

Plugging in $\mathbf { y } _ { k } = \mathbf { C } \mathbf { x } _ { k } + \mathbf { D } \mathbf { u } _ { k }$ gives

$$\hat {\mathbf {x}} _ {k + 1} = \mathbf {A} \hat {\mathbf {x}} _ {k} + \mathbf {B} \mathbf {u} _ {k} + \mathbf {L} ((\mathbf {C x} _ {k} + \mathbf {D u} _ {k}) - \mathbf {C} \hat {\mathbf {x}} _ {k} - \mathbf {D u} _ {k})\hat {\mathbf {x}} _ {k + 1} = \mathbf {A} \hat {\mathbf {x}} _ {k} + \mathbf {B} \mathbf {u} _ {k} + \mathbf {L} (\mathbf {C x} _ {k} + \mathbf {D u} _ {k} - \mathbf {C} \hat {\mathbf {x}} _ {k} - \mathbf {D u} _ {k})\hat {\mathbf {x}} _ {k + 1} = \mathbf {A} \hat {\mathbf {x}} _ {k} + \mathbf {B} \mathbf {u} _ {k} + \mathbf {L} (\mathbf {C x} _ {k} - \mathbf {C} \hat {\mathbf {x}} _ {k})\hat {\mathbf {x}} _ {k + 1} = \mathbf {A} \hat {\mathbf {x}} _ {k} + \mathbf {B} \mathbf {u} _ {k} + \mathbf {L C} (\mathbf {x} _ {k} - \hat {\mathbf {x}} _ {k})$$

Let $\mathbf { e } _ { k } = \mathbf { x } _ { k } - { \hat { \mathbf { x } } } _ { k }$ be the error in the estimate $\hat { \mathbf { x } } _ { k }$ .

$$\hat {\mathbf {x}} _ {k + 1} = \mathbf {A} \hat {\mathbf {x}} _ {k} + \mathbf {B} \mathbf {u} _ {k} + \mathbf {L C e} _ {k}$$

Subtracting this from $\mathbf { x } _ { k + 1 } = \mathbf { A } \mathbf { x } _ { k } + \mathbf { B } \mathbf { u } _ { k }$ gives
