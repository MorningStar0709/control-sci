# 9.4 NONLINEAR TRANSFORMATIONS

It is of great interest to find transformations such that the transformed system is linear and independent of the operating conditions. The process in Example 9.3 is one example in which this can be done by time scaling. The obtained sampled model is independent of the flow because the time is scaled as

$$t _ {s} = \frac {V _ {d}}{q} t$$

This means that the key variable is distance traveled by a particle instead of time. All processes associated with material flows—rolling mills, band transporters, flows in pipes, and so on—have this property.

A system of the form

$$\frac {d x (t)}{d t} = f (x (t)) + g (x (t)) u (t)$$

can also be transformed into a linear system, provided that all states of the system can be measured and a generalized observability condition holds. (Compare Section 5.10.) The system is first transformed into a fixed linear system. The transformation is usually nonlinear and depends on the states of the process. A controller is then designed for the transformed model, and the control signals of the model are retransformed into the original control signals. The result is a special type of nonlinear controller, which can be interpreted as a gain-scheduling controller. Knowledge about the nonlinearities in the model is built into the controller. The method with nonlinear transformations is illustrated by an example.
