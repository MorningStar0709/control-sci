# Loss of Reachability and Observability Through Sampling

Sampling of a continuous-time system gives a discrete-time system with system matrices that depend on the sampling period. How will that influence the reachability and observability of the sampled system? To get a reachable discrete-time system, it is necessary that the continuous-time system also be reachable, because the allowable control signals for the sampled system—piecewise-constant signals—are a subset of the allowable control signals for the continuous-time system.

However, it may happen that the reachability is lost for some sampling periods. The conditions for unobservability are more restricted in the continuous-time case because the output has to be zero over a time interval, whereas the sampled-data output has to be zero only at the sampling instants. This means that the continuous output may oscillate between the sampling times and remain zero at the sampling instants. This condition is sometimes called hidden oscillation. The sampled-data system thus can be unobservable even if the corresponding continuous-time system is observable.

The harmonic oscillator can be used to illustrate the preceding discussion.
