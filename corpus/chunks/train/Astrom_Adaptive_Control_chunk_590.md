# 9.6 CONCLUSIONS

Gain scheduling is a good way to compensate for known nonlinearities. With such a scheme the controller reacts quickly to changing conditions. One drawback of the method is that the design may be time-consuming if it is not possible to use nonlinear transformations or auto-tuning. Another drawback is that the controller parameters are changed in open loop, without feedback from the performance of the closed-loop system. This makes the method impossible to use if the dynamics of the process or the disturbances are not known accurately enough.

Example 9.3 and the ship steering example in Section 9.5 show that it is often useful to introduce normalized variables. The processes then become constant in the new variables, and the gain scheduling of the controllers is easily derived.
