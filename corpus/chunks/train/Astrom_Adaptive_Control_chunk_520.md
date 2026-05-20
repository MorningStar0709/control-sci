# EXAMPLE 7.3 Turn-off

Consider the integrator with unknown gain in Example 7.2 with $R_{1} = 0.09$ and $\varphi_{b} = 0.95$ . Figure 7.4 shows a representative simulation of the cautious controller. The control signal is small for periods of time, and the variance of the estimated gain increases during the turn-off. After some time the control activity suddenly starts again.

The turn-off will generally start when the control signal is small and when the parameter $b_{0}$ is small. The problem with turn-off makes the cautious controller unsuitable for control of systems with quickly varying parameters. The cautious controller can be useful if the parameters of the process are constant or almost constant, but the certainty equivalence controller with some simple safety measures can often be used in such cases also.
