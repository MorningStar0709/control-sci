# 4.3.3 Constrained Estimation

Constraints in estimation may be a useful way to add information to the estimation problem. We may wish to enforce physically known facts such as: concentrations of impurities, although small, must be nonnegative, fluxes of mass and energy must have the correct sign given temperature and concentration gradients, and so on. Unlike the regulator, the estimator has no way to enforce these constraints on the system. Therefore, it is important that any constraints imposed on the estimator are satisfied by the system generating the measurements. Otherwise we may prevent convergence of the estimated state to the system state. For this reason, care should be used in adding constraints to estimation problems.

Because we have posed state estimation as an optimization problem, it is straightforward to add constraints to the formulation. We assume that the system generating the data satisfy the following constraints.
