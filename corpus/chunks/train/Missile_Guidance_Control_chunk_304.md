$$
\begin{array}{l} \begin{array}{l} \dot {R} _ {M T} \dot {\sigma} + R _ {M T} \ddot {\sigma} = - \dot {V} _ {M} \sin (\gamma - \sigma) - V _ {M} \cos (\gamma - \sigma) (\dot {\gamma} - \dot {\sigma}) \\ + \dot {V} _ {M} \sin (\pi - \nu_ {1}) + V _ {M} \cos (\pi - \nu_ {2}) (\dot {\pi} - \dot {\pi}). \end{array} \tag {3} \\ + \dot {V} _ {T} \sin (\sigma - \gamma_ {T}) + V _ {T} \cos (\sigma - \gamma_ {T}) (\dot {\sigma} - \dot {\gamma} _ {T}). \\ \end{array}
$$

Expanding (3) and substituting (2) into (3) yields the following equation:

$$
\begin{array}{l} 2 \dot {R} _ {M T} \dot {\sigma} + R _ {M T} \ddot {\sigma} = - \dot {V} _ {M} \sin (\gamma - \sigma) - V _ {M} \cos (\gamma - \sigma) \dot {\gamma} + \dot {V} _ {M} \sin (\gamma - \sigma) - V _ {M} \cos (\gamma - \sigma) \dot {\gamma} \tag {4} \\ + \dot {V} _ {T} \sin (\sigma - \gamma_ {T}) - V _ {T} \cos (\sigma - \gamma_ {T}) \dot {\gamma} _ {T}. \\ \end{array}
$$

The four terms on the right-hand side of (4) denote accelerations due to both the missile and the target. For the missile, d $l V _ { M } / d t$ is the longitudinal acceleration and $V _ { M } \dot { \gamma }$ is the lateral maneuver. For the target, $d V _ { T } / d t$ and $V _ { T } \dot { \gamma } _ { T }$ are the corresponding accelerations. Figure 4.27 shows how the homing action is represented as a feedback loop that keeps constant the direction in space of the line joining the missile and the target.

Note that (4) corresponds to the block labeled geometry in Figure 4.27, showing the kinematic coupling between missile and target velocities, accelerations, and the resultant motion of the line of sight. Taking the Laplace transform of (4) results in the following equation:

$$\frac {d \sigma}{d t} = \frac {\left[ - \dot {V} _ {M} \sin (\gamma - \sigma) - V _ {M} \dot {\gamma} \cos (\gamma - \sigma) + V _ {T} \sin (\gamma - \gamma_ {T}) - V _ {T} \dot {\gamma} _ {T} \cos (\sigma - \gamma_ {T}) \right]}{2 \dot {R} _ {M T} (1 + \frac {R _ {M T}}{2 \dot {R} _ {M T}} s)} \tag {5}$$

where s is the Laplace operator. Later in this example (5) will be used to represent the dynamic relation between target and missile in closing the guidance loop. It should be pointed out, however, that the coefficients of (5) are not constant and that therefore taking the Laplace transform is not rigorously accurate. However, the closed-loop behavior can be evaluated at discrete times along the trajectory at which the coefficients are assumed constant.
