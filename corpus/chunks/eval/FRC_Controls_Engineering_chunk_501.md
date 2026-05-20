# C.1.1 Setup

Let’s start with the equation for the reference dynamics

$$\mathbf {r} _ {k + 1} = \mathbf {A r} _ {k} + \mathbf {B u} _ {k}$$

where $\mathbf { u } _ { k }$ is the feedforward input. Note that this feedforward equation does not and should not take into account any feedback terms. We want to find the optimal $\mathbf { u } _ { k }$ such that we minimize the tracking error between $\mathbf { r } _ { k + 1 }$ and $\mathbf { r } _ { k }$ .

$$\mathbf {r} _ {k + 1} - \mathbf {A r} _ {k} = \mathbf {B u} _ {k}$$

To solve for $\mathbf { u } _ { k }$ , we need to take the inverse of the nonsquare matrix B. This isn’t possible, but we can find the pseudoinverse given some constraints on the state tracking error and control effort. To find the optimal solution for these sorts of trade-offs, one can define a cost function and attempt to minimize it. To do this, we’ll first solve the expression for 0.

$$\mathbf {0} = \mathbf {B u} _ {k} - (\mathbf {r} _ {k + 1} - \mathbf {A r} _ {k})$$

This expression will be the state tracking cost we use in our cost function.

Our cost function will use an $H _ { 2 }$ norm with Q as the state cost matrix with dimensionality states × states and R as the control input cost matrix with dimensionality inputs × inputs.

$$\mathbf {J} = (\mathbf {B u} _ {k} - (\mathbf {r} _ {k + 1} - \mathbf {A r} _ {k})) ^ {\top} \mathbf {Q} (\mathbf {B u} _ {k} - (\mathbf {r} _ {k + 1} - \mathbf {A r} _ {k})) + \mathbf {u} _ {k} ^ {\top} \mathbf {R u} _ {k}$$
