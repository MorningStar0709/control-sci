# 6.5.2 Velocity-to-Be-Gained

The velocity-to-be-gained vector $\mathbf { V } _ { g }$ is the difference between the present missile velocity and the velocity required at that point in space and time for the missile to fall freely from that point to impact at the target at the prescribed time. This relation was expressed mathematically in Section 6.5.1 as

$$\mathbf {V} _ {g} = \mathbf {V} _ {c} - \mathbf {V} _ {m}, \tag {6.170}$$

where $\mathbf { V } _ { c }$ is the correlated velocity vector and $\mathbf { V } _ { m }$ is the current missile velocity vector. Thus, if at any point in the powered part of the flight trajectory the velocity-tobe-gained were to vanish, the thrust of the missile could be terminated at that point, and the desired end condition would be realized. Specifically, it is the function of the guidance control system to steer the missile so that the desired cut-off condition $\mathbf { V } _ { g } = 0$ will be achieved. Figure 6.21 illustrates these concepts.

The desired cut-off condition, that is, the vanishing of the velocity-to-be-gained vector, implies the simultaneous vanishing of all three components of that vector. A useful approach to this matter comes from noticing that if it is possible to orient the time rate of change of a vector in direct opposition to the vector itself, then the vector will maintain a fixed orientation in space and simply shrink in magnitude until at one instant the vector is zero in the sense that all of its components are simultaneously zero. In this case, we are interested in controlling $\mathbf { V } _ { g }$ ; thus, we would like to control the vector $- ( d \mathbf { V } _ { g } / d t )$ so that it is oriented along $\mathbf { V } _ { g }$ . The vector $- ( d \mathbf { V } _ { g } / d t )$ can be expressed mathematically as

$$- \left(\frac {d \mathbf {V} _ {g}}{d t}\right) = \mathbf {a} _ {T} + Q \mathbf {V} _ {g},$$

or

$$\left(\frac {d \mathbf {V} _ {g}}{d t}\right) = - \mathbf {a} _ {T} - Q \mathbf {V} _ {g}, \tag {6.178}$$

where

aT = the thrust acceleration vector (i.e., acceleration due to nonfield forces),

which is dominated by the missile thrust.

Q = matrix of partials (or directional derivatives; that is, $Q _ { i j } = \partial V _ { c i } / \partial r _ { j } | _ { i , j = 1 , 2 , 3 } )$

(Note that the Q-matrix can also be designated as $\| Q \| . )$
