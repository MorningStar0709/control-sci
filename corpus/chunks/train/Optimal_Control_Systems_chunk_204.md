# 3.7 Problems

Problem 3.7 Consider a second order system

$$\ddot {x} (t) + b \dot {x} (t) + c x (t) = u (t)$$

and the performance index to be minimized as

$$J = \int_ {0} ^ {\infty} [ q x ^ {2} (t) + r u ^ {2} (t) ] d t.$$

Determine the closed-loop optimal control in terms of the state $x(t)$ and its derivative $\dot{x}(t)$ .

Problem 3.8 Given a third order plant,

$$
\begin{array}{l} \dot {x} _ {1} (t) = x _ {2} (t) \\ \dot {x} _ {2} (t) = x _ {3} (t) \\ \dot {x} _ {3} (t) = - 5 x _ {1} (t) + - 7 x _ {2} (t) - 1 0 x _ {3} (t) + 4 u (t) \\ \end{array}
$$

and the performance index

$$J = \int_ {0} ^ {\infty} [ q _ {1 1} x _ {1} ^ {2} (t) + q _ {2 2} x _ {2} ^ {2} (t) + q _ {3 3} x _ {3} ^ {2} (t) + r u ^ {2} (t) ] d t,$$

for

1. $q_{11} = q_{22} = q_{33} = 1, r = 1,$   
2. $q_{11} = 10, q_{22} = 1, q_{33} = 1, r = 1$ , and   
3. $q_{11} = q_{22} = q_{33} = 1, r = 10,$

find the positive definite solution for Riccati coefficient matrix $\bar{P}$ , optimal feedback gain matrix $\bar{K}$ and the eigenvalues of the closed-loop system matrix $A - B\bar{K}$ .

Problem 3.9 Determine the optimal feedback coefficients and the optimal control law for the multi-input, multi-output (MIMO) system

$$
\dot {\mathbf {x}} (t) = \left[ \begin{array}{l l} 0 & 1 \\ 1 & 1 \end{array} \right] \mathbf {x} (t) + \left[ \begin{array}{l l} 1 & 1 \\ 0 & 1 \end{array} \right] \mathbf {u} (t)
$$

and the cost function

$$J = \int_ {0} ^ {\infty} [ 2 x _ {1} ^ {2} (t) + 4 x _ {2} ^ {2} (t) + 0. 5 u _ {1} ^ {2} (t) + 0. 2 5 u _ {2} ^ {2} (t) ] d t.$$

Problem 3.10 For the D.C. motor speed control system described in Problem 1.1, find the closed-loop optimal control to keep the speed constant at a particular value and the system to respond for any disturbances from the regulated value.

Problem 3.11 For the liquid-level control system described in Problem 1.2, find the closed-loop optimal control to keep the liquid level constant at a reference value and the system to act only if there is a change in the liquid level.

Problem 3.12 [35] For the inverted pendulum control system described in Problem 1.3, find the closed-loop optimal control to keep the pendulum in a vertical position.

Problem 3.13 For the mechanical control system described in Problem 1.4, find the closed-loop optimal control to keep the system at equilibrium condition and act only if there is a disturbance.

Problem 3.14 For the automobile suspension system described in Problem 1.5, find the closed-loop optimal control to keep the system at equilibrium condition and act only if there is a disturbance.

Problem 3.15 For the chemical control system described in Problem 1.6, find the closed-loop optimal control to keep the system at equilibrium condition and act only if there is a disturbance.
