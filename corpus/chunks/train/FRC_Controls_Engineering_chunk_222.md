# 8.2 Linearization

One way to control nonlinear systems is to linearize the model around a reference point. Then, all the powerful tools that exist for linear controls can be applied. This is done by taking the Jacobians of f and h with respect to the state and input vectors. See section 5.12 for more on Jacobians.

$$\mathbf {A} = \frac {\partial f (\mathbf {x} , \mathbf {u} , \mathbf {w})}{\partial \mathbf {x}}\mathbf {B} = \frac {\partial f (\mathbf {x} , \mathbf {u} , \mathbf {w})}{\partial \mathbf {u}}\mathbf {C} = \frac {\partial h (\mathbf {x} , \mathbf {u} , \mathbf {v})}{\partial \mathbf {x}}\mathbf {D} = \frac {\partial h (\mathbf {x} , \mathbf {u} , \mathbf {v})}{\partial \mathbf {u}}$$

Linearization of a nonlinear equation is a Taylor series expansion to only the first-order terms (that is, terms whose variables have exponents on the order of x1). This is where the small angle approximations for sin θ and cos θ (θ and 1 respectively) come from.

Higher order partial derivatives can be added to better approximate the nonlinear dynamics. We typically only linearize around equilibrium points[1] because we are interested in how the system behaves when perturbed from equilibrium. The FAQ Why do we have to linearize around an equilibrium point? by Sean Humbert[2] goes into more detail on this. To be clear though, linearizing the system around the current state as the system evolves does give a closer approximation over time.

Note that linearization with static matrices (that is, with a time-invariant linear system) only works if the original system in question is feedback linearizable.
