$$\mathbf {x} (t) = \mathbf {x} ^ {*} + \Delta \mathbf {x} (t), \quad \mathbf {u} (t) = \mathbf {u} ^ {*} + \Delta \mathbf {u} (t), \quad \mathbf {y} (t) = \mathbf {y} ^ {*} + \Delta \mathbf {y} (t).$$

Because $\dot{\mathbf{x}}^{*} = \mathbf{0}$ , substitution in Equations 2.41 and 2.42 yields

$$\Delta \dot {\mathbf {x}} = \mathbf {f} (\mathbf {x} ^ {*} + \Delta \mathbf {x}, \mathbf {u} ^ {*} + \Delta \mathbf {u}) \tag {2.44}\Delta \mathbf {y} = \mathbf {h} (\mathbf {x} ^ {*} + \Delta \mathbf {x}, \mathbf {u} ^ {*} + \Delta \mathbf {u}) - \mathbf {y} ^ {*}. \tag {2.45}$$

Expanding the components of f in a Taylor series, we obtain

$$
\begin{array}{l} f _ {i} \left(\mathbf {x} ^ {*} + \Delta \mathbf {x}, \mathbf {u} ^ {*} + \Delta \mathbf {u}\right) = f _ {i} \left(\mathbf {x} ^ {*}, \mathbf {u} ^ {*}\right) + \frac {\partial f _ {i}}{\partial x _ {1}} \Bigg | _ {*} \Delta x _ {1} + \frac {\partial f _ {i}}{\partial x _ {2}} \Bigg | _ {*} \Delta x _ {2} + \dots \\ + \frac {\partial f _ {i}}{\partial x _ {m}} \left| _ {*} \Delta x _ {n} + \frac {\partial f _ {i}}{\partial u _ {1}} \right| _ {*} \Delta u _ {1} + \dots + \frac {\partial f _ {i}}{\partial u _ {r}} \left| _ {*} \Delta u _ {r} \right. \\ + \text { higher - order   terms   in } \Delta x, \Delta u. \tag {2.46} \\ \end{array}
$$

Here, the notation “” means “evaluated at $x^{*}$ , $u^{*}$ .” At this point, it is assumed that the $\Delta x$ 's and $\Delta u$ 's are sufficiently small to justify neglecting the higher-order terms. If the control system to be designed works at all well, that assumption should be satisfied.

Without the higher-order terms, and with $\mathbf{f}(\mathbf{x}^{*},\mathbf{u}^{*})=\mathbf{0}$ , the RHS of Equation 2.46 is the ith member of a set of n equations, written in matrix form as

$$\mathbf {f} \left(\mathbf {x} ^ {*} + \Delta \mathbf {x}, \mathbf {u} ^ {*} + \Delta \mathbf {u}\right) = \frac {\partial \mathbf {f}}{\partial \mathbf {x}} \Bigg | _ {*} \Delta \mathbf {x} + \frac {\partial \mathbf {f}}{\partial \mathbf {u}} \Bigg | _ {*} \Delta \mathbf {u} \tag {2.47}$$

where
