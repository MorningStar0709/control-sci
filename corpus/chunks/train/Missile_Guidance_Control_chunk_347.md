From (4.157) we note that for large values of $t _ { g o } , N ^ { \prime }$ is asymptotically 3, and the bracketed term in (4.156) is asymptotically zero. Furthermore, if $t _ { g o }$ or v goes to zero, the bracketed term becomes $1 / 2$ , by double application of L’Hospital’s rule. Also, if the constraint on the applied acceleration is removed by setting $\gamma = 0$ , then $N ^ { \prime } { = } 3$ for all values of $t _ { g o }$ . Equation (4.156) indicates that the solution of the optimal control problem, for the simple case of a zero-lag autopilot, is a form of augmented proportional navigation. $\mathrm { I f } \gamma$ and v are zero, then the optimal control is pure augmented proportional navigation with $N ^ { \prime } { = } 3$ and an autopilot bias term equal to $N ^ { \prime } a _ { T } / 2$ (see also Section 4.5).

We will now discuss the above results from a different point of view. Consider the missile/target kinematic relationships in state-space notation:

$$\dot {x} _ {1} = x _ {3},\dot {x} _ {2} = x _ {4},\dot {x} _ {3} = a _ {T x} - a _ {M x},\dot {x} _ {4} = a _ {T y} - a _ {M y}, \tag {4.158}$$

where

$$x _ {1} = r _ {T x} - r _ {M x},x _ {2} = r _ {T y} - r _ {M y},$$

x3 = missile/target relative velocity in the x-direction,

x4 = missile/target relative velocity in the y-direction.

In Chapter 3 we saw that for aerodynamic control, the airframe must undergo rotations in order to produce the proper angle of attack, which in turn results in normal forces, the magnitude of which are controlled through a feedback loop using accelerometers that measure the actual normal accelerations. However, in the present model under discussion, the rotational and translational inertial properties of the missile have been neglected. Furthermore, we have assumed a perfect control loop. Equation (4.158) can now be written in the form

$$\dot {x} _ {1} = x _ {3},\dot {x} _ {2} = x _ {4},\dot {x} _ {3} = u _ {1} = - a _ {M x}, \tag {4.159}\dot {x} _ {4} = u _ {2} = - a _ {M y}.$$

These equations can be put in the canonical equation (4.120) as follows:

$$
\begin{array}{l} \frac {d \mathbf {x}}{d t} = \mathbf {A x} + \mathbf {B u} \\ = \left[ \begin{array}{c c c} 0 & | & I \\ - & + & - \\ I & | & 0 \end{array} \right] \mathbf {x} + \left[ \begin{array}{l} 0 \\ I \end{array} \right] \mathbf {u}, \tag {4.160} \\ \end{array}
$$

where I is the $2 \times 2$ identity matrix. Writing the performance index as in (4.121), we have
