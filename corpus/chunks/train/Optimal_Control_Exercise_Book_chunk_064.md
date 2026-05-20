# Exercise 4.12 (Control of production and consumption)

Suppose we own a factory whose output we can control. Let us begin to construct a mathematical model by setting

1. x(t): amount of output produced at time $t \in [ 0 , T ]$   
2. u(t): fraction of output reinvested at time $t \in [ 0 , T ]$

This will be our control, and is subject to the obvious constrain that

$$u (t) \in [ 0, 1 ] \tag {246}$$

Given such a control, the corresponding dynamics are provided by the ODE

$$\dot {x} (t) = k u (t) x (t) \tag {247}x (0) = x _ {0} \tag {248}$$

where the constant $k > 0$ modeling the growth rate of our reinvestment and $u ( t ) x ( t )$ is the amount of reinvested output. Let us take as a payoff functional

$$J (u) = \int_ {0} ^ {T} (1 - u (t)) x (t) d t \tag {249}$$

where $( 1 - u ( t ) ) x ( t )$ is our consumption. The meaning is that we want to maximize our total consumption of the output.

The overall problem is:

$$u ^ {*} := \underset {u: [ 0, T ] \rightarrow [ 0, 1 ]} {\operatorname{argmax}} J (u) = \int_ {0} ^ {T} (1 - u (t)) x (t) d t \tag {250}$$

subject to (251)

$$\dot {x} (t) = k u (t) x (t) \tag {252}x (0) = x _ {0} \tag {253}$$

Find an optimal control policy for this problem.
