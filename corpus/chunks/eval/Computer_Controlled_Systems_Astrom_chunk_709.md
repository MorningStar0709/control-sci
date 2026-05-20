# Criteria

In steady-state regulation it makes sense to express the criteria in terms of steady-state variances of the control variable and the process output. For regulation of systems with one output, the criterion may be to minimize the variance of the output. This is discussed in Sec.6.6. Also compare with Fig. 6.7. This leads to the criterion

$$J _ {m v} = \mathrm{E} y ^ {2} (k) \tag {12.6}$$

where it is assumed that the scales are chosen so that y = 0 corresponds to the desired set point. A control law that minimizes the criterion (12.6) is called minimum-variance control. The criterion may also be expressed as

$$J _ {\infty} = \lim _ {N \rightarrow \infty} \mathrm{E} \left\{\frac {1}{N} \sum_ {k = 1} ^ {N} y ^ {2} (k) \right\}$$

Notice that this criterion is an approximation of the continuous-time loss function

$$J _ {\infty} = \lim _ {T \rightarrow \infty} \mathrm{E} \left\{\frac {1}{T} \int_ {0} ^ {T} y ^ {2} (t) d t \right\} \tag {12.7}$$

A more accurate approximation, which takes the behavior of the signals between the sampling instants into account, is given in Sec. 11.1. Some consequences of the approximation are discussed in Sec. 12.6. The properties of the control signal under minimum-variance control depend critically on the sampling period. A short sampling period gives a large variance of the control signal and a long sampling period gives a small variance.

In some cases it is desired to trade variances of control and output signals. This may be done by introducing the loss function

$$J _ {l q} = \mathrm{E} \left(y ^ {2} (k) + \rho u ^ {2} (k)\right) \tag {12.8}$$

The control law that minimizes this criterion is called the linear quadratic control law.
