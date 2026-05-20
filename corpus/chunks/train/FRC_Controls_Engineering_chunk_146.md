# Caveats

First, unconstrained integral control exhibits integral windup on a unit step input. When the error reaches zero, the integrator may still have a large positive accumulated error from the initial ramp-up. The integrator makes the system overshoot until the accumulated error is unwound by negative errors. Poor tuning can lead to instability.[6] Integrating only when close to the reference somewhat mitigates integral windup.

Second, unconstrained integral control is a poor choice for modeled dynamics compensation. Feedforwards provide more precise compensation since we already know beforehand how to counteract the undesirable dynamics.

Third, unconstrained integral control is a poor choice for unmodeled dynamics compensation. To choose proper gains, the integrator must be tuned online when the unmodeled dynamics are present, which may be inconvenient or unsafe in some circumstances. Furthermore, accumulation even when the system is following the model means it still compensates for modeled dynamics despite our intent otherwise. Prefer the approach in subsection 6.7.2.
