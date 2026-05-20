# 3.2 Actuator saturation

A feedback controller calculates its output based on the error between the reference and the current state. Plant in the real world don’t have unlimited control authority available for the feedback controller to apply. When the actuator limits are reached, the feedback controller acts as if the gain has been temporarily reduced (i.e., it will have reduced control authority).

We’ll try to explain this through a bit of math. Let’s say we have a controller $u \_ =$ $k ( r - x )$ where u is the control effort, k is the gain, r is the reference, and x is the current state. Let $u _ { m a x }$ be the limit of the actuator’s output which is less than the uncapped value of u and $k _ { m a x }$ be the associated maximum gain. We will now compare the capped and uncapped controllers for the same reference and current state.

$$u _ {m a x} < uk _ {m a x} (r - x) < k (r - x)k _ {m a x} < k$$

For the inequality to hold, $k _ { m a x }$ must be less than the original value for k. This reduced gain is evident in a system response when there is a linear change in state instead of an exponential one as it approaches the reference. This is due to the control effort no longer following a decaying exponential plot. Once the system is closer to the reference, the controller will stop saturating and produce realistic controller values again.

This page intentionally left blank
