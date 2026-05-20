# 1.7 Problems

Problem 1.1 A D.C. motor speed control system is described by a second order state equation,

$$
\begin{array}{l} \dot {x} _ {1} (t) = 2 5 x _ {2} (t) \\ \dot {x} _ {2} (t) = - 4 0 0 x _ {1} (t) - 2 0 0 x _ {2} (t) + 4 0 0 u (t), \\ \end{array}
$$

where, $x_{1}(t) = \text{the speed of the motor}$ , and $x_{2}(t) = \text{the current in the armature circuit}$ and the control input $u(t) = \text{the voltage input to an amplifier supplying the motor}$ . Formulate a performance index and optimal control problem to keep the speed constant at a particular value.

Problem 1.2 [83] In a liquid-level control system for a storage tank, the valves connecting a reservoir and the tank are controlled by gear train driven by a D. C. motor and an electronic amplifier. The dynamics is described by a third order system

$$
\begin{array}{l} \dot {x} _ {1} (t) = - 2 x _ {1} (t) \\ \dot {x} _ {2} (t) = x _ {3} (t) \\ \dot {x} _ {3} (t) = - 1 0 x _ {3} (t) + 9 0 0 0 u (t) \\ \end{array}
$$

where, $x_{1}(t) = \text{is the height in the tank}$ , $x_{2}(t) = \text{is the angular position of the electric motor driving the valves controlling the liquid from reservoir to tank}$ , $x_{3}(t) = \text{the angular velocity of the motor}$ , and $u(t) = \text{is the input to electronic amplifier connected to the input of the motor}$ . Formulate optimal control problem to keep the liquid level constant at a reference value and the system to act only if there is a change in the liquid level.

Problem 1.3 [35] In an inverted pendulum system, it is required to maintain the upright position of the pendulum on a cart. The linearized state equations are

$$
\begin{array}{l} \dot {x} _ {1} (t) = x _ {2} (t) \\ \dot {x} _ {2} (t) = - x _ {3} (t) + 0. 2 u (t) \\ \dot {x} _ {3} (t) = x _ {4} (t) \\ \dot {x} _ {4} (t) = 1 0 x _ {3} (t) - 0. 2 u (t) \\ \end{array}
$$

where, $x_{1}(t) = \text{is horizontal linear displacement of the cart}, x_{2}(t) = \text{is linear velocity of the cart}, x_{3}(t) = \text{is angular position of the pendulum from vertical line}, x_{4}(t) = \text{is angular velocity, and } u(t) = \text{is the horizontal force applied to the cart. Formulate a performance index to keep the pendulum in the vertical position with as little energy as possible.}$
