# 6.7 APPLICATION OF AVERAGING TECHNIQUES

In the previous sections, idealized cases were investigated. The convergence and stability analysis of self-tuning regulators were based on Assumptions A1-A4 and the premise that there are no disturbances. In Chapter 5 the stability of MRAS was proved under the SPR assumption on certain transfer functions. Assumption A2 in Theorem 6.7 implies that the model used to design the adaptive controller must be at least as complex as the process to be controlled. This is highly unrealistic because real processes are often distributed and also nonlinear.

In practice, adaptive controllers are based on simplified models. It is therefore of interest to investigate what happens when the process is more complex than assumed in the design of the controller. In this case the process is said to have unmodeled dynamics. If a controller is able to control processes with unmodeled dynamics and/or disturbances, we say that the controller is robust.
