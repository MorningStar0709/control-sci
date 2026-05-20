# DESIGN WITH UNMEASURED CONSTANT DISTURBANCES

In this section, the problem includes an unmeasured constant disturbance, so the dc steady-state input to the system is not given. It is worthwhile to study this in general, to show that the observer-based controller automatically contains integration.

We begin with the system description obtained by linearizing about the dc steady state defined by the output $y = y_{d} = constant$ . We assume that a constant input does exist that results in $y = y_{d}$ in the steady state. The linearized equations are

$$\Delta \dot {\mathbf {x}} = A \Delta \mathbf {x} + B \Delta \mathbf {u} \tag {7.94}\Delta \mathbf {y} = C \Delta \mathbf {x}. \tag {7.95}$$

We express $\Delta \mathbf{u}$ as $\mathbf{u} - \mathbf{u}^*$ , where $\mathbf{u}^*$ is the (unknown) constant steady-state input. Since $\mathbf{u}^*$ is constant, we write

$$\Delta \dot {\mathbf {x}} = A \Delta \mathbf {x} - B \mathbf {u} ^ {*} + B \mathbf {u}\dot {\mathbf {u}} ^ {*} = 0\Delta \mathbf {y} = C \Delta \mathbf {x}$$

and consider $\mathbf{u}^*$ as part of the state to be estimated, along with $\Delta \mathbf{x}$ . This is rewritten as the composite system

$$
\frac {d}{d t} \left[ \begin{array}{c} \Delta \mathbf {x} \\ - - \\ \mathbf {u} ^ {*} \end{array} \right] = \left[ \begin{array}{c c} A & - B \\ - - & - - \\ 0 & 0 \end{array} \right] \left[ \begin{array}{c} \Delta \mathbf {x} \\ - - \\ \mathbf {u} ^ {*} \end{array} \right] + \left[ \begin{array}{c} B \\ - - \\ 0 \end{array} \right] \mathbf {u} \tag {7.96}

\Delta \mathbf {y} = \left[ \begin{array}{c c c} C & 0 \end{array} \right] \left[ \begin{array}{l} \Delta \mathbf {x} \\ \mathbf {u} ^ {*} \end{array} \right]. \tag {7.97}
$$

The next step will be to construct an observer for this system. Before we do, however, we must verify that it is observable.

■ Theorem 7.10

The system of Equations 7.96 and 7.97 is observable if, and only if, (i) the original system of Equations 7.94 and 7.95 is observable and (ii) this original system has no transmission zeros at $s = 0$ .

Proof: This theorem is just the dual of Theorem 7.7 and is proved in a similar manner.

Next, we examine the observer-based controller
