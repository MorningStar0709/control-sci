# A Controller Structure

In a state-space design it is natural to assume that servo performance is specified in terms of a model that gives the desired response of the output or the state variables to changes in the command signal. This can be specified with the model

$$x _ {m} (k + 1) = \Phi_ {m} x _ {m} (k) + \Gamma_ {m} u _ {c} (k) \tag {4.54}y _ {m} (k) = C _ {m} x _ {m} (k)$$

It is then natural to use the control law

$$u (k) = L \left(x _ {m} (k) - \hat {x} (k)\right) + u _ {f f} (k) \tag {4.55}$$

where $x_{m}$ is the desired state, and $u_{ff}$ is a control signal that gives the desired output when applied to the open-loop system. The coordinates must be chosen so that the states of the system and the model are compatible. In actual applications it is often useful to choose them so that the components of the state have good physical interpretations.

The term $u_{fb} = L(x_m - \hat{x})$ represents the feedback and $u_{ff}$ represents the feedforward signal. Equation (4.55) has a good physical interpretation. The feedforward signal $u_{ff}$ will ideally produce the desired time variation in the process state. If the estimated process state $\hat{x}$ equals the desired state $x_m$ , the feedback signal $L(x_m - \hat{x})$ is zero. If there is a difference between $\hat{x}$ and $x_m$ , the feedback will generate corrective actions. The feedback term can be viewed as a generalization of error feedback in ordinary control systems, because the error represents deviations of all state variables and not just the output errors. A block diagram of the system is shown in Fig. 4.13.
