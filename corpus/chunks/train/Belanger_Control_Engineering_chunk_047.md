$$
\frac {\partial \mathbf {f}}{\partial \mathbf {x}} = \left[ \begin{array}{c c c c} \frac {\partial f _ {1}}{\partial x _ {1}} & \frac {\partial f _ {1}}{\partial x _ {2}} & \dots & \frac {\partial f _ {1}}{\partial x _ {n}} \\ \frac {\partial f _ {2}}{\partial x _ {1}} & \frac {\partial f _ {2}}{\partial x _ {2}} & \dots & \frac {\partial f _ {2}}{\partial x _ {n}} \\ \vdots & & & \\ \frac {\partial f _ {n}}{\partial x _ {1}} & \dots & \dots & \frac {\partial f _ {n}}{\partial x _ {n}} \end{array} \right]
$$

is the Jacobian of $\mathbf{f}$ with respect to $\mathbf{x}$ , with a similar definition for $\frac{\partial\mathbf{f}}{\partial\mathbf{u}}$ , the Jacobian with respect to $\mathbf{u}$ . Thus, Equation 2.44 becomes approximately

$$\Delta \dot {\mathbf {x}} = \frac {\partial \mathbf {f}}{\partial \mathbf {x}} \Bigg | _ {*} \quad \Delta \mathbf {x} + \frac {\partial \mathbf {f}}{\partial \mathbf {u}} \Bigg | _ {*} \quad \Delta \mathbf {u}. \tag {2.48}$$

As for Equation 2.45, since $\mathbf{y}^{*} = \mathbf{h}(\mathbf{x}^{*},\mathbf{u}^{*})$ , we have

$$\Delta \mathbf {y} = \frac {\partial \mathbf {h}}{\partial \mathbf {x}} \left| _ {*} \quad \Delta \mathbf {x} + \frac {\partial \mathbf {h}}{\partial \mathbf {u}} \right| _ {*} \quad \Delta \mathbf {u} \tag {2.49}$$

for small $\Delta \mathbf{x},\Delta \mathbf{u}$

Note that the Jacobians in Equations 2.48 and 2.49 are constant matrices, because they are evaluated at specific values $x^{*}$ and $u^{*}$ . Note also that the right-hand sides of those equations are linear functions of $\Delta x$ and $\Delta u$ , so the incremental system is linear and time-invariant.

It is also possible to linearize about a trajectory—a nominal set of time functions, $\mathbf{x}^{*}(t)$ and $\mathbf{u}^{*}(t)$ , that satisfy the state equations. An example would be a robotic manipulator following a preset path. In such a case, the linearized system is time-varying (see Problem 2.21).

If some of the inputs are disturbances, it is often desirable to separate them from the control inputs. The linearized equations become
