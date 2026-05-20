# 1.2 Models and Modeling

Model predictive control has its roots in optimal control. The basic concept of MPC is to use a dynamic model to forecast system behavior, and optimize the forecast to produce the best decision — the control move at the current time. Models are therefore central to every form of MPC. Because the optimal control move depends on the initial state of the dynamic system, a second basic concept in MPC is to use the past record of measurements to determine the most likely initial state of the system. The state estimation problem is to examine the record of past data, and reconcile these measurements with the model to determine the most likely value of the state at the current time. Both the regulation problem, in which a model forecast is used to produce the optimal control action, and the estimation problem, in which the past record of measurements is used to produce an optimal state estimate, involve dynamic models and optimization.

We first discuss the dynamic models used in this text. We start with the familiar differential equation models

$$\frac {d x}{d t} = f (x, u, t)y = h (x, u, t)x \left(t _ {0}\right) = x _ {0}$$

in which $x \in \mathbb { R } ^ { n }$ is the state, $u \in \mathbb { R } ^ { m }$ is the input, $y \in \mathbb { R } ^ { p }$ is the output, and $t \in \mathbb R$ is time. We use $\mathbb { R } ^ { n }$ to denote the set of real-valued n-vectors. The initial condition specifies the value of the state x at time $t = t _ { 0 }$ , and we seek a solution to the differential equation for time greater than $t _ { 0 } , t \in \mathbb { R } _ { \geq t _ { 0 } }$ . Often we define the initial time to be zero, with a corresponding initial condition, in which case $t \in \mathbb { R } _ { \geq 0 }$ .
