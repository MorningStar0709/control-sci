# 7.2.1 Problem Formulation and Statement

Consider a simple motion of an inertial load in a frictionless environment. The motion is described by

$$m \ddot {y} (t) = f (t) \tag {7.2.1}$$

where, m is the mass of a body (system or plant), $y(t)$ , $\dot{y}(t)$ , and $\ddot{y}(t)$ are the position, velocity and acceleration, respectively, and $f(t)$ is the external force applied to the system. Defining a set of state variables as

$$x _ {1} (t) = y (t); \quad x _ {2} (t) = \dot {y} (t) \tag {7.2.2}$$

we have the double integral system described as

$$\dot {x} _ {1} (t) = x _ {2} (t)\dot {x} _ {2} (t) = u (t) \tag {7.2.3}$$

where, $u(t) = f(t) / m$ . Let us assume that the control (input) $u(t)$ to the system is constrained as

$$| u (t) | \leq 1 \forall t \in [ t _ {0}, t _ {f} ]. \tag {7.2.4}$$

This constraint on the control is due to physical limitations such as current in a circuit or thrust of an engine.

Problem Statement: Given the double integral system (7.2.3) and the constraint on the control (7.2.4), find the admissible control that forces the system from any initial state $[x_{1}(0), x_{2}(0)]$ to the origin in minimum time.

Let us assume that we are dealing with normal system and no singular controls are allowed. Now, we attempt to solve the system following the procedure described in the previous section.
