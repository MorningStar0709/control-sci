Notice that the closed-loop poles of the observed-state feedback control system consist of the poles due to the pole-placement design alone and the poles due to the observer design alone. This means that the pole-placement design and the observer design are independent of each other. They can be designed separately and combined to form the observed-state feedback control system. Note that, if the order of the plant is n, then the observer is also of nth order (if the full-order state observer is used), and the resulting characteristic equation for the entire closed-loop system becomes of order $2 n$ .

Transfer Function of the Observer-Based Controller. Consider the plant defined by

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} uy = \mathbf {C x}$$

Assume that the plant is completely observable. Assume that we use observed-state feedback control $u = - \mathbf { K } \widetilde { \mathbf { x } }$ Then, the equations for the observer are given by.

$$\tilde {\mathbf {x}} = \left(\mathbf {A} - \mathbf {K} _ {e} \mathbf {C} - \mathbf {B K}\right) \tilde {\mathbf {x}} + \mathbf {K} _ {e} y \tag {10-71}u = - \mathbf {K} \widetilde {\mathbf {x}} \tag {10-72}$$

where Equation (10–71) is obtained by substituting $u = - \mathbf { K } \widetilde { \mathbf { x } }$ into Equation (10–57).

By taking the Laplace transform of Equation (10–71), assuming a zero initial condition, and solving for $\widetilde { \mathbf { X } } ( s )$ we obtain,

$$\widetilde {\mathbf {X}} (s) = \left(s \mathbf {I} - \mathbf {A} + \mathbf {K} _ {e} \mathbf {C} + \mathbf {B K}\right) ^ {- 1} \mathbf {K} _ {e} Y (s)$$

By substituting this $\widetilde { \mathbf { X } } ( s )$ into the Laplace transform of Equation (10–72), we obtain

$$U (s) = - \mathbf {K} \left(s \mathbf {I} - \mathbf {A} + \mathbf {K} _ {e} \mathbf {C} + \mathbf {B K}\right) ^ {- 1} \mathbf {K} _ {e} Y (s) \tag {10-73}$$

Then the transfer function $U ( s ) / Y ( s )$ can be obtained as

$$\frac {U (s)}{Y (s)} = - \mathbf {K} \left(s \mathbf {I} - \mathbf {A} + \mathbf {K} _ {e} \mathbf {C} + \mathbf {B K}\right) ^ {- 1} \mathbf {K} _ {e}$$

Figure 10–13 shows the block diagram representation for the system. Notice that the transfer function

$$\mathbf {K} \big (s \mathbf {I} - \mathbf {A} + \mathbf {K} _ {e} \mathbf {C} + \mathbf {B K} \big) ^ {- 1} \mathbf {K} _ {e}$$

acts as a controller for the system. Hence, we call the transfer function
