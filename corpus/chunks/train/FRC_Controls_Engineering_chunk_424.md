# 15.1.4 Other profile types

The ultimate goal of any profile is to match the profile’s motion characteristics to the desired application. Trapezoid and S-curve profiles work well when the system’s torque response curve is fairly flat. In other words, when the output torque does not vary that much over the range of velocities the system will be experiencing. This is true for most servo motor systems, whether DC brushed or DC brushless.

Step motors, however, do not have flat torque/speed curves. Torque output is nonlinear, sometimes has a large drop at a location called the “mid-range instability”, and generally drops off at higher velocities.

Mid-range instability occurs at the step frequency when the motor’s natural resonance frequency matches the current step rate. To address mid-range instability, the most common technique is to use a nonzero starting velocity. This means that the profile instantly “jumps” to a programmed velocity upon initial acceleration, and while decelerating. While crude, this technique sometimes provides better results than a smooth ramp for zero, particularly for systems that do not use a microstepping drive technique.

To address torque drop-off at higher velocities, a parabolic profile can be used. The corresponding acceleration curve has the smallest acceleration when the velocity is highest.

This is a good match for stepper motors because there is less torque available at higher speeds. However, notice that starting and ending accelerations are very high, and there is no “S” phase where the acceleration smoothly transitions to zero. If load oscillation is a problem, parabolic profiles may not work as well as an S-curve despite the fact that a standard S-curve profile is not optimized for a stepper motor from the standpoint of the torque/speed curve.
