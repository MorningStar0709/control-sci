# 6.7 Integral control

A common way of implementing integral control is to add an additional state that is the integral of the error of the variable intended to have zero steady-state error.

We’ll present two methods:

1. Augment the plant. For an arm, one would add an “integral of position” state.   
2. Estimate the “error” in the control input (the difference between what was applied versus what was observed to happen) via the observer and compensate for it. We’ll call this “input error estimation”.

In FRC, avoid integral control unless you have a very good reason to use it. Integral control adds significant complexity, and steady-state error can often be avoided with a motion profile, a well-tuned feedforward, and proportional feedback (i.e., more deterministic options you should be using anyway).
