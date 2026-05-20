<table><tr><td>Full-Order State Observer</td><td>Minimum-Order State Observer</td></tr><tr><td> $\widetilde{\mathbf{x}}$ </td><td> $\widetilde{\mathbf{x}}_b$ </td></tr><tr><td> $\mathbf{A}$ </td><td> $\mathbf{A}_{bb}$ </td></tr><tr><td> $\mathbf{B}u$ </td><td> $\mathbf{A}_{ba}x_a + \mathbf{B}_b u$ </td></tr><tr><td>y</td><td> $\dot{x}_a - A_{aa}x_a - B_a u$ </td></tr><tr><td> $\mathbf{C}$ </td><td> $\mathbf{A}_{ab}$ </td></tr><tr><td> $\mathbf{K}_e$  (n × 1 matrix)</td><td> $\mathbf{K}_e$  [(n - 1) × 1 matrix]</td></tr></table>

To avoid this difficulty, we eliminate ${ \dot { x } } _ { a }$ in the following way. First rewrite Equation (10–86) as

$$
\begin{array}{l} \widetilde {\mathbf {x}} _ {b} - \mathbf {K} _ {e} \dot {x} _ {a} = \left(\mathbf {A} _ {b b} - \mathbf {K} _ {e} \mathbf {A} _ {a b}\right) \widetilde {\mathbf {x}} _ {b} + \left(\mathbf {A} _ {b a} - \mathbf {K} _ {e} A _ {a a}\right) y + \left(\mathbf {B} _ {b} - \mathbf {K} _ {e} B _ {a}\right) u \\ = \big (\mathbf {A} _ {b b} - \mathbf {K} _ {e} \mathbf {A} _ {a b} \big) \big (\widetilde {\mathbf {x}} _ {b} - \mathbf {K} _ {e} y \big) \\ + \left[ \left(\mathbf {A} _ {b b} - \mathbf {K} _ {e} \mathbf {A} _ {a b}\right) \mathbf {K} _ {e} + \mathbf {A} _ {b a} - \mathbf {K} _ {e} A _ {a a} \right] y \\ + \left(\mathbf {B} _ {b} - \mathbf {K} _ {e} B _ {a}\right) u \tag {10-87} \\ \end{array}
$$

Define

$$\mathbf {x} _ {b} - \mathbf {K} _ {e} y = \mathbf {x} _ {b} - \mathbf {K} _ {e} x _ {a} = \boldsymbol {\eta}$$

and

$$\widetilde {\mathbf {x}} _ {b} - \mathbf {K} _ {e} y = \widetilde {\mathbf {x}} _ {b} - \mathbf {K} _ {e} x _ {a} = \widetilde {\boldsymbol {\eta}} \tag {10-88}$$

Then Equation (10–87) becomes

$$
\begin{array}{l} \dot {\widetilde {\boldsymbol {\eta}}} = \left(\mathbf {A} _ {b b} - \mathbf {K} _ {e} \mathbf {A} _ {a b}\right) \widetilde {\boldsymbol {\eta}} + \left[ \left(\mathbf {A} _ {b b} - \mathbf {K} _ {e} \mathbf {A} _ {a b}\right) \mathbf {K} _ {e} \right. \\ \left. + \mathbf {A} _ {b a} - \mathbf {K} _ {e} A _ {a a} \right] y + \left(\mathbf {B} _ {b} - \mathbf {K} _ {e} B _ {a}\right) u \tag {10-89} \\ \end{array}
$$

Define

$$\hat {\mathbf {A}} = \mathbf {A} _ {b b} - \mathbf {K} _ {e} \mathbf {A} _ {a b}\hat {\mathbf {B}} = \hat {\mathbf {A}} \mathbf {K} _ {e} + \mathbf {A} _ {b a} - \mathbf {K} _ {e} A _ {a a}\hat {\mathbf {F}} = \mathbf {B} _ {b} - \mathbf {K} _ {e} B _ {a}$$

Then Equation (10–89) becomes
