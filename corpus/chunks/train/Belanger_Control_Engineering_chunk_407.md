The procedure just followed is necessary to obtain convergence of $\Delta\mathbf{y}(t)$ to zero, in cases where the set-point and/or disturbance signals are not decreasing exponentials (i.e., they are steps, sinusoids, ramps, increasing exponentials, and so forth). If they are decreasing exponentials, they tend to zero, and so does $u^{*}$ . Tracking may be desirable (especially for slowly decreasing signals), but the LQ approach may be preferable, to reach the best compromise between control effectiveness and input effort.

To set this up, suppose that w and $y_{d}$ have constant and time-varying components; i.e.,

$$\mathbf {w} (t) = \mathbf {w} ^ {*} + \Delta \mathbf {w} (t)\mathbf {y} _ {d} (t) = \mathbf {y} _ {d} ^ {*} + \Delta \mathbf {y} _ {d} (t).$$

From Equations 7.34 and 7.35,

$$\Delta \dot {\mathbf {x}} = \dot {\mathbf {x}} - \dot {\mathbf {x}} ^ {*} = \dot {\mathbf {x}} = A \mathbf {x} ^ {*} + A \Delta \mathbf {x} + B \mathbf {u} ^ {*} + B \Delta \mathbf {u} + \Gamma \mathbf {w} ^ {*} + \Gamma \Delta \mathbf {w}$$

or, since $A\mathbf{x}^{*} + B\mathbf{u}^{*} + \Gamma \mathbf{w}^{*} = 0$ ,

$$\Delta \dot {\mathbf {x}} = A \Delta \mathbf {x} + B \Delta \mathbf {u} + \Gamma \Delta \mathbf {w}. \tag {7.39}$$

Also,

$$\Delta \mathbf {y} = C \mathbf {x} ^ {*} + C \Delta \mathbf {x} - \mathbf {y} _ {d} ^ {*} - \Delta \mathbf {y} _ {d}\Delta \mathbf {y} = C \Delta \mathbf {x} - \Delta \mathbf {y} _ {d} \tag {7.40}$$

since $C\mathbf{x}^{*} - \mathbf{y}_{d}^{*} = 0$

Next, we model $\Delta\mathbf{w}(t)$ and $\Delta\mathbf{y}_{d}(t)$ as the zero-input responses of stable LTI systems:

$$\dot {\mathbf {z}} _ {w} = A _ {w} \mathbf {z} _ {w}\Delta \mathbf {w} = C _ {w} \mathbf {z} _ {w} \tag {7.41}$$

and

$$\dot {\mathbf {z}} _ {y} = A _ {y} \mathbf {z} _ {y}\Delta \mathbf {y} _ {d} = C _ {y} \mathbf {z} _ {y}. \tag {7.42}$$

The vectors $z_{w}$ and $z_{y}$ may be called the disturbance and reference state vectors, respectively. They may be combined with the plant state $\Delta x$ to form one complete description:

$$
\frac {d}{d t} \left[ \begin{array}{l} \Delta \mathbf {x} \\ \mathbf {z} _ {w} \\ \mathbf {z} _ {y} \end{array} \right] = \left[ \begin{array}{c c c} A & \Gamma C _ {w} & 0 \\ 0 & A _ {w} & 0 \\ 0 & 0 & A _ {y} \end{array} \right] \left[ \begin{array}{l} \Delta \mathbf {x} \\ \mathbf {z} _ {w} \\ \mathbf {z} _ {y} \end{array} \right] + \left[ \begin{array}{l} B \\ 0 \\ 0 \end{array} \right] \Delta \mathbf {u} \tag {7.43}
