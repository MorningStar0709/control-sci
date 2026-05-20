Y
Ẏₜ
Vₜ
γₜ
Ẋₜ
X
Inertial reference
</details>

(b) Target flight trajectory   
Fig. 4.6. Planar target maneuver and trajectory.

where $\mathbf { r } _ { T }$ , ${ \bf v } _ { T }$ , and $\mathbf { a } _ { T }$ are the target’s position, velocity, and acceleration vectors, and ${ \bf 1 } _ { v }$ and $\mathbf { 1 } _ { L }$ are unit vectors in the velocity and lift directions. Assuming that the target trajectory is divided into segments with and without maneuver, $\omega _ { v }$ is nonzero during maneuver segments of the flight, so that these equations can be numerically integrated using a fourth-order Runge–Kutta integration, typically with a 1-second step. Integration is terminated at the end of each maneuver segment and restarted with the next segment. For segments that have $\omega _ { v } = 0$ (i.e., no turning), the numerical integration is bypassed, since the closed-loop solutions

$$\mathbf {r} (t _ {i + 1}) = \mathbf {r} (t _ {i}) + \mathbf {v} (t _ {i}) \Delta_ {i} + 0. 5 \mathbf {a} (t _ {i}) \Delta_ {i} ^ {2}, \tag {4.10c}\mathbf {v} (t _ {i + 1}) = \mathbf {v} (t _ {i}) + \mathbf {a} (t _ {i}) \Delta_ {i}, \tag {4.10d}\mathbf {a} (t _ {i + 1}) = \mathbf {a} (t _ {i}), \tag {4.10e}$$

where $\Delta _ { i } = t _ { i + 1 } - t _ { i }$ , can be used when the acceleration (if any) is only along the velocity vector.

Let us now assume that the target is considered to be a point mass following an evasive circular trajectory beginning at the origin of the inertial reference frame at a constant speed $\mathbf { V } _ { T }$ in the same evolution plane as that of the missile (see Figure 4.6(b)). An evasive maneuver is determined by the absolute acceleration $a _ { T }$ of the target. Under these assumptions, the movement of the target with respect to the inertial reference frame XY is defined by the following equations of motion:

$$\frac {d x _ {T}}{d t} = v _ {T} \cos (\omega_ {T} t + \gamma_ {T _ {o}}), \tag {4.10f}\frac {d y _ {T}}{d t} = v _ {T} \sin (\omega_ {T} t + \gamma_ {T _ {o}}), \tag {4.10g}\frac {d \omega_ {T}}{d t} = \frac {d \gamma_ {T _ {o}}}{d t} = [ g (a _ {T} ^ {2} - 1) ^ {1 / 2} ] / v _ {T}, \tag {4.10h}$$

where

$$
\begin{array}{l} x _ {T} = \text { target   position } [ \mathrm{m} ], \\ y _ {T} = \text { target   position   ordinate } [ m ], \\ a _ {T} = \text { target   absolute   acceleration } [ \mathrm{g} ], \\ v _ {T} = \text { target   velocity } [ \mathrm{m/sec} ], \\ g = \text { acceleration   due   to   gravity } [ \mathrm{m} / \sec^ {2} ], \\ \gamma_ {T _ {o}} = \text { initial   target   flight - path   angle   [rad] }, \\ \gamma_ {T} = \text { target   flight - path   angle   [rad] }, \\ \omega_ {T} = \text { target   angular   speed } [ \mathrm{rad/sec} ]. \\ \end{array}
$$
