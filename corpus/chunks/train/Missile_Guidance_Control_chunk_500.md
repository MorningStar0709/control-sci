where $\rho = V _ { M } / V _ { T }$ . The negative root is of no interest (it corresponds to negative flight time). In most cases, the missile velocity is not constant. For this reason, a two-step iteration is normally used to refine the estimate of average velocity. The first step uses the AI velocity to calculate an impact point (earliest collision point on target path that AI can reach). The range from the AI to this point is used to estimate the average missile speed. This speed is then used to find a second impact point, which is used to calculate the range to impact and the heading error (angle between the AI velocity vector and the LOS vector to the impact point).

The following checks are made to determine whether a missile launch is possible:

The range to impact must be greater than the input minimum range and less than the maximum range.   
• The heading error must be less than the input maximum.   
• The velocity to impact must be greater than the target velocity.   
• The current AI acceleration must be less than the input maximum g-limit.

Additional criteria are imposed depending on the type of missile:

• IR missiles must be within the aspect-dependent lock-on range.   
• Semiactive missiles must have seeker lock-on.   
No additional checks are made for active missiles, but they must achieve lock-on during flight before an input time limit prior to impact.

Seeker lock-on for all types of missiles includes gimbal (if used) limit checks. RF missiles (both active and semiactive) require the signal-to-interference ratio to be greater than an input threshold. RF missiles can be launched only if the AI radar is tracking on noise jamming. In this mode, no impact predictions are made, since the radar is presumed to have no range or range rate data. Only three checks are made:

The heading error (which in this case is the angle between the AI velocity vector and the jam strobe) is less than the allowed heading error.   
• The current AI acceleration is less than the maximum allowed.   
The missile (either active or semiactive RF) has a home-on-jam capability, and the J/N ratio exceeds an input threshold level.

Since no checks are made on range or velocity, it is quite possible for missiles to be launched that have no chance of reaching the target.

On November 22, 2002, the Air Force completed the flight tests of the F/A-22 with the successful launching of a guided AIM-9 Sidewinder missile over the White Sands Missile Range. The mission demonstrated the aircraft’s ability to fire an AIM-9 at Mach speed using an unmanned, full-scale QF-4 Phantom II aircraft as a target. During the test, the F/A-22 was flying at 1.4 Mach at 24,000 ft, while the target was traveling at 1.0 Mach at 14,000 ft.
