# 8.1 Nonlinear system notation

Recall from linear system theory that we defined systems as having the following form:

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} \mathbf {u} + \mathbf {w}\mathbf {y} = \mathbf {C x} + \mathbf {D u} + \mathbf {v}$$

In this equation, A and B are constant matrices, which means they are both timeinvariant and linear (all transformations on the system state are linear ones, and those transformations remain the same for all time). In nonlinear and time-variant systems, the state evolution and output are defined by arbitrary functions of the current states and inputs.

$$\dot {\mathbf {x}} = f (\mathbf {x}, \mathbf {u}, \mathbf {w})\mathbf {y} = h (\mathbf {x}, \mathbf {u}, \mathbf {v})$$

Nonlinear functions come up regularly when attempting to control the pose of a vehicle in the global coordinate frame instead of the vehicle’s rotating local coordinate frame.

Converting from one to the other requires applying a rotation matrix, which consists of sine and cosine operations. These functions are nonlinear.
