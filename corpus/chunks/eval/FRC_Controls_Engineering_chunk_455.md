# Other applications

In retrospect, the solution here seems obvious: if you want to reach the desired position in the minimum time, you just apply positive max input to accelerate to the max speed, coast for a while, then apply negative max input to decelerate to a stop at the desired position. Optimization problems can get more complex than this though. In fact, we can use this same framework to design optimal trajectories for a drivetrain while satisfying dynamics constraints, avoiding keep-out regions, and driving through points of interest.

Sleipnir’s examples[1] and tests[2][3] demonstrate constrained AprilTag pose estimation, subsystem current allocation, and various direct transcription, direct collocation, and single shooting trajectory optimization problems.
