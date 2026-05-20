# 2.5 LINEARIZATION

The task of a control system is often to maintain given constant operating conditions—for example, constant speed, level, position, or basis weight. To achieve this objective, we use a two-step procedure:

1. Select a dc steady state that corresponds to desired constant values of u and/or y.   
2. Design a control strategy to generate increments in the control in response to deviations from the dc steady state.

To do this, we need to study (i) the dc steady state of a system and (ii) the model that relates the deviations from steady state, i.e., the small-signal, or incremental, model.

We begin with

$$\dot {\mathbf {x}} = \mathbf {f} (\mathbf {x}, \mathbf {u}) \tag {2.41}\mathbf {y} = \mathbf {h} (\mathbf {x}, \mathbf {u}). \tag {2.42}$$

Note that the functions $\mathbf{f}$ and $\mathbf{h}$ are not explicitly functions of $t$ , so the system is time-invariant.

For constant $\mathbf{u} = \mathbf{u}^*$ , $\mathbf{x}^*$ is an equilibrium state if $\mathbf{f}(\mathbf{x}^*, \mathbf{u}^*) = \mathbf{0}$ . We shall use the symbol $\mathbf{0}$ to denote a vector whose elements are all 0. If $\mathbf{x} = \mathbf{x}^*$ and $\mathbf{u} = \mathbf{u}^*$ , then $\dot{\mathbf{x}} = \mathbf{0}$ and the state remains at $\mathbf{x}^*$ ; i.e., $\mathbf{x}^*$ is an equilibrium point with $\mathbf{u} = \mathbf{u}^*$ .

The output corresponding to an equilibrium state $\mathbf{x}^*$ is $\mathbf{y}^{*} = \mathbf{h}(\mathbf{x}^{*},\mathbf{u}^{*})$ . Therefore, the dc steady-state quantities satisfy

$$\mathbf {f} \left(\mathbf {x} ^ {*}, \mathbf {u} ^ {*}\right) = \mathbf {0}\mathbf {h} \left(\mathbf {x} ^ {*}, \mathbf {u} ^ {*}\right) = \mathbf {y} ^ {*}. \tag {2.43}$$

A dc steady state is defined by choosing some of the variables in Equation (2.43) and solving for the others. There is no guarantee that a solution will exist, or that it will be unique. With n states, r inputs, and m outputs, Equation 2.43 represents $n + m$ nonlinear equations with $n + m + r$ variables. In most cases, it will not be possible to predetermine more than r of those variables. For example, it will not usually be possible to set 2 outputs (m = 2) at arbitrary values if the system has only one input (r = 1).

The next step is to write equations for incremental variables, i.e., for deviations from equilibrium. Let
