# C.2 Steady-state feedforward

Steady-state feedforwards apply the control effort required to keep a system at the reference if it is no longer moving (i.e., the system is at steady-state). The first steady-state feedforward converts desired outputs to desired states.

$$\mathbf {x} _ {c} = \mathbf {N} _ {x} \mathbf {y} _ {c}$$

${ \bf N } _ { x }$ converts desired outputs $\mathbf { y } _ { c }$ to desired states $\mathbf { x } _ { c }$ (also known as r). For steady-state, that is

$$\mathbf {x} _ {s s} = \mathbf {N} _ {x} \mathbf {y} _ {s s} \tag {C.1}$$

The second steady-state feedforward converts the desired outputs y to the control input required at steady-state.

$$\mathbf {u} _ {c} = \mathbf {N} _ {u} \mathbf {y} _ {c}$$

$\mathbf { N } _ { u }$ converts the desired outputs y to the control input u required at steady-state. For steady-state, that is

$$\mathbf {u} _ {s s} = \mathbf {N} _ {u} \mathbf {y} _ {s s} \tag {C.2}$$
