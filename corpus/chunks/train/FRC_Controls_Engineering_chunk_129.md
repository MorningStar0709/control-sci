# 6.1 From PID control to model-based control

As mentioned before, controls engineers have a more general framework to describe control theory than just PID control. PID controller designers are focused on fiddling with controller parameters relating to the current, past, and future error rather than the underlying system states. Integral control is a commonly used tool, and some people use integral action as the majority of the control action. While this approach works in a lot of situations, it is an incomplete view of the world.

Model-based control has a completely different mindset. Controls designers using model-based control care about developing an accurate model of the system, then driving the states they care about to zero (or to a reference). Integral control is added with $u _ { e r r o r }$ estimation if needed to handle model uncertainty, but we prefer not to use it because its response is hard to tune and some of its destabilizing dynamics aren’t visible during simulation.

Why use model-based control in FRC? Poor build season schedule management often leads to the software team:

1. Not getting enough time to verify basic functionality and test/tune feedback controllers.   
2. Spending dedicated software testing time troubleshooting mechanical/electrical issues within recently integrated subsystems instead.

Model-based control (one of the focuses of this book) avoids both problems because it lets software teams test basic functionality in simulation much earlier in the build season and tune their feedback controllers automatically.
