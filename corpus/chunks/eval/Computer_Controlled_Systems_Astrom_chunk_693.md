# Choice of Sampling Period

The choice of the sampling period is influenced by how the specifications are given for the control problem. Two different cases are considered.

In the first case it is assumed that the specifications are given as a desired damping and response of the closed-loop system without using overly large control signals. It is then natural to determine the controller by iterating in the weightings of the sampled loss function of (11.9). To do this, a first choice of the sampling period has to be made based on the specifications. It is reasonable to choose the sampling period in relation to the dynamics of the closed-loop system, as discussed in Sec. 4.3. This means that it may be necessary to make one or two iterations in the sampling period. The closed-loop dynamics is a complicated function of the loss function.

In the second case it is assumed that the specifications are given in terms of the continuous-time loss function of $(11.4)$ . The continuous-time LQ-controller then minimizes the loss. It is possible to get an approximation of the increase in the loss due to an increase in the sampling period (see the References). When good interactive design programs are available, it is easy to check the loss and the performance for some sampling periods.
