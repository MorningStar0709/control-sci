# 15.3.3 High-fidelity modeling

High-fidelity modeling allows us to use more sophisticated mathematical tools to achieve peak drivetrain performance, sometimes at the expense of robustness. Successful applications require accurate modeling and sufficient control input margin to compensate for disturbances. Replanning after large disturbances is theoretically possible but not always computationally tractible.

Choreo[6] is in this category. Choreo poses and solves a nonlinear constrained optimization problem (see chapter 17). It finds the time-minimizing trajectory through a set of waypoints subject to differential or swerve drivetrain dynamics, control input limits, velocity and acceleration limits, keep-in and keep-out regions, and pointing constraints.

The dynamics are derived via sum-of-forces and sum-of-torques with user-provided drivetrain geometry and mass properties. Most constraints can be applied to either the whole trajectory or specific segments.

Choreo requires a lot of physical information about the drivetrain, but it tends to generate feasible trajectories that robots can execute well on their first try (assuming welltuned wheel velocity controllers). These trajectories are too expensive to replan ondemand.
