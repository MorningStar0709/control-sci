# 12. Newtonian mechanics examples

A model is a set of differential equations describing how the system behaves over time. There are two common approaches for developing them.

1. Collecting data on the physical system’s behavior and performing system identification with it.   
2. Using physics to derive the system’s model from first principles.

This chapter covers the second approach using Newtonian mechanics.

The models derived here should cover most types of motion seen on an FRC robot. Furthermore, they can be easily tweaked to describe many types of mechanisms just by pattern-matching. There’s only so many ways to hook up a mass to a motor in FRC. The flywheel model can be used for spinning mechanisms, the elevator model can be used for spinning mechanisms transformed to linear motion, and the single-jointed arm model can be used for rotating servo mechanisms (it’s just the flywheel model augmented with a position state).

These models assume all motor controllers driving DC motors are set to brake mode instead of coast mode. Brake mode behaves the same as coast mode except where the applied voltage is zero. In brake mode, the motor leads are shorted together to prevent movement. In coast mode, the motor leads are an open circuit.
