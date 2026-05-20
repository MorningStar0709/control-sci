where $Q_{1c}$ is a symmetric positive semidefinite matrix. The control signal and the state at the end time can be penalized in a similar way. This leads to a control problem where we want to minimize the loss function

$$
\begin{array}{l} J = \mathrm{E} \left(\int_ {0} ^ {N h} \left(x ^ {T} (t) Q _ {1 c} x (t) + 2 x ^ {T} (t) Q _ {1 2 c} u (t) \right. \right. \\ \left. + u ^ {T} (t) Q _ {2 c} u (t)\right) d t + x ^ {T} (N h) Q _ {0 c} x (N h) \Bigg) \tag {11.4} \\ = \mathrm{E} \left(\int_ {0} ^ {N h} \left( \begin{array}{l l} x ^ {T} (t) & u ^ {T} (t) \end{array} \right) Q _ {c} \binom{x (t)}{u (t)} d t + x ^ {T} (N h) Q _ {0 c} x (N h)\right) \\ \end{array}
$$

with

$$
Q _ {c} = \left( \begin{array}{l l} Q _ {1 c} & Q _ {1 2 c} \\ Q _ {1 2 c} ^ {T} & Q _ {2 c} \end{array} \right)
$$

and where the matrices $Q_{0c}, Q_{1c}$ , and $Q_{2c}$ are symmetric and at least positive semidefinite. The matrices in the loss function may depend on time.

Admissible control laws. It is important to specify the data available for determining the control signal. The first assumption is that periodic sampling is used and that the control signal is constant over the sampling periods. The control problem can then easily be translated into a discrete time problem.

If C equals the unit matrix and if $e(kh) = 0$ in (11.3), then the full-state vector is available. The control signal is then allowed to be a function of the state up to and including time kh. This is called complete state information. In many cases only the outputs can be measured. This implies that only noise-corrupted measurements are available for the controller. This is called incomplete state information. In this case the control signal at time kh is allowed to be a function of the outputs and inputs up to and including either time kh - h or time kh.

The problem. The optimal control problem is now defined to be finding the admissible control signal that minimizes the loss function of (11.4) when the process is described by the model of (11.1) or the equivalent model of (11.3). The design parameters are the matrices in the loss function and the sampling period.
