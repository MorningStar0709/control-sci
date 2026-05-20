# 8.4 Affine systems

Let $\mathbf { x } = \mathbf { x } _ { 0 } + \delta \mathbf { x }$ and $\mathbf { u } = \mathbf { u } _ { 0 } + \delta \mathbf { u }$ where δx and δu are perturbations from $\left( \mathbf { x } _ { 0 } , \mathbf { u } _ { 0 } \right)$ . A first-order linearization of $\dot { \mathbf { x } } = f ( \mathbf { x } , \mathbf { u } )$ around $\left( \mathbf { x } _ { 0 } , \mathbf { u } _ { 0 } \right)$ gives

$$\dot {\mathbf {x}} \approx f (\mathbf {x} _ {0}, \mathbf {u} _ {0}) + \left. \frac {\partial f (\mathbf {x} , \mathbf {u})}{\partial \mathbf {x}} \right| _ {\mathbf {x} _ {0}, \mathbf {u} _ {0}} \delta \mathbf {x} + \left. \frac {\partial f (\mathbf {x} , \mathbf {u})}{\partial \mathbf {u}} \right| _ {\mathbf {x} _ {0}, \mathbf {u} _ {0}} \delta \mathbf {u}\dot {\mathbf {x}} = f (\mathbf {x} _ {0}, \mathbf {u} _ {0}) + \left. \frac {\partial f (\mathbf {x} , \mathbf {u})}{\partial \mathbf {x}} \right| _ {\mathbf {x} _ {0}, \mathbf {u} _ {0}} \delta \mathbf {x} + \left. \frac {\partial f (\mathbf {x} , \mathbf {u})}{\partial \mathbf {u}} \right| _ {\mathbf {x} _ {0}, \mathbf {u} _ {0}} \delta \mathbf {u}$$

An affine system is a linear system with a constant offset in the dynamics. If $\left( \mathbf { x } _ { 0 } , \mathbf { u } _ { 0 } \right)$ is an equilibrium point, $f ( \mathbf { x } _ { 0 } , \mathbf { u } _ { 0 } ) = \mathbf { 0 }$ , the resulting model is linear, and LQR works as usual. If $\left( \mathbf { x } _ { 0 } , \mathbf { u } _ { 0 } \right)$ is, say, the current operating point rather than an equilibrium point, the easiest way to correctly apply LQR is

1. Find a control input $\mathbf { u } _ { 0 }$ that makes $\left( \mathbf { x } _ { 0 } , \mathbf { u } _ { 0 } \right)$ an equilibrium point.   
2. Obtain an LQR for the linearized system.   
3. Add $\mathbf { u } _ { 0 }$ to the LQR’s control input.

A control-affine system is of the form $\dot { \mathbf { x } } = f ( \mathbf { x } ) + g ( \mathbf { x } ) \mathbf { u }$ . Since it has separable control inputs, $\mathbf { u } _ { 0 }$ can be derived via plant inversion as follows.

$$\dot {\mathbf {x}} = f (\mathbf {x} _ {0}) + g (\mathbf {x} _ {0}) \mathbf {u} _ {0}\mathbf {0} = f (\mathbf {x} _ {0}) + g (\mathbf {x} _ {0}) \mathbf {u} _ {0}g (\mathbf {x} _ {0}) \mathbf {u} _ {0} = - f (\mathbf {x} _ {0})\mathbf {u} _ {0} = - g ^ {- 1} \left(\mathbf {x} _ {0}\right) f \left(\mathbf {x} _ {0}\right) \tag {8.1}$$

For the control-affine system $\dot { \mathbf { x } } = f ( \mathbf { x } ) + \mathbf { B } \mathbf { u } , \mathbf { u } _ { 0 }$ would be

$$\mathbf {u} _ {0} = - \mathbf {B} ^ {+} f (\mathbf {x} _ {0}) \tag {8.2}$$
