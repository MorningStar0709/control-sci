# 15.3.2 Some modeling required

By investing a bit of effort into system modeling, one can obtain trajectories with reasonable default performance and limited feasibility guarantees.

PathPlanner[3] is in this category. PathPlanner plans the shape of the path with a series of cubic or quintic Hermite splines, time-parameterizes each spline with a chassis velocity trapezoid profile, then iteratively constrains the profile based on differential or swerve drivetrain kinematics and user-defined velocity and acceleration limits. Trajectories can be replanned on-demand (useful for auto-aim/auto-score strategies).

A Dive into WPILib Trajectories by Declan Freeman-Gleason[4] describes 2-DOF trajectory planning with Hermite splines in more detail. Planning Motion Trajectories for Mobile Robots Using Splines by Christoph Sprunk provides a more general treatment of spline-based trajectory generation[5].
