# Systems with Unstable Inverses

A continuous-time system with a rational transfer function is nonminimum-phase if it has right half-plane zeros or time delays. Analogously, a discrete-time system is often defined to be nonminimum-phase if it has zeros outside the unit disc. That definition implies that a time delay does not make the system nonminimum-phase. On the other hand, time delays do not pose the same severe problems as they do for continuous-time systems. For discrete-systems it is therefore more relevant to talk about systems with or without stable inverses, which are defined as follows.

DEFINITION 2.3 UNSTABLE INVERSE A discrete-time system has an unstable inverse if it has zeros outside the unit disc.

A continuous-time system with a stable inverse may become a discrete-time system with an unstable inverse when it is sampled. It follows from Table 2.4 that the inverse system is always unstable if the pole excess of the continuous-time system is larger than 2, and if the sampling period is sufficiently short. Further, a continuous-time nonminimum-phase system will not always become a discrete-time system with an unstable inverse, as shown in the following example.
