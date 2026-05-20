Vc
VcΔt
-VgΔt
M
VmΔt
Vm
Vg
</details>

(b)   
Fig. 6.22. Vector representation of correlated velocity, missile velocity, and velocity-to-begained vector.

where $\mathbf { r } _ { m }$ is the inertial location of the missile, $\mathbf { r } _ { t }$ is the inertial location of the target, $t _ { A }$ is the specified time of arrival at the target, and t is the current time. We now define a Q-matrix, which forms the so-called Q-guidance, of variable coefficients that form the heart of the systems considered here [3]. More specifically, the Q-matrix, or directional derivative, is a matrix whose elements consist of the time-offlight-constrained correlated velocity vector $\mathbf { V } _ { c }$ . Let an arbitrary set of Earth-centered nonrotating orthogonal coordinate axes (x, y, z) be assigned, and let i, j, and k be the unit vectors along the respective axes. Writing r and ${ \bf V } _ { c }$ in the form

$$\mathbf {r} = x \mathbf {i} + y \mathbf {j} + z \mathbf {k},\mathbf {V} _ {c} = u _ {c} \mathbf {i} + v _ {c} \mathbf {j} + w _ {c} \mathbf {k}. \tag {6.174}$$

The elements of the Q-matrix may be defined by the relations

$$Q _ {x x} = \partial u _ {c} / \partial x, \quad Q _ {x y} = \partial u _ {c} / \partial y, \quad Q _ {x z} = \partial u _ {c} / \partial z,Q _ {y x} = \partial v _ {c} / \partial x, \quad Q _ {y y} = \partial v _ {c} / \partial y, \quad Q _ {y z} = \partial v _ {c} / \partial z, \tag {6.175}Q _ {z x} = \partial w _ {c} / \partial x, \quad Q _ {z y} = \partial w _ {c} / \partial y, \quad Q _ {z z} = \partial w _ {c} / \partial z,$$

or in matrix form,

$$
Q = \left[ \begin{array}{c c c} Q _ {x x} & Q _ {x y} & Q _ {x z} \\ Q _ {y x} & Q _ {y y} & Q _ {y z} \\ Q _ {z x} & Q _ {z y} & Q _ {z z} \end{array} \right].
$$

It is understood that in carrying out the indicated differentiation, the target location vector $\mathbf { r } _ { t }$ and the total time of flight $t _ { T f }$ are held fixed in the process, as is t itself. In an abbreviated notation, Q may be expressed in the equivalent form [3]

$$Q = \| \partial \mathbf {V} _ {c} (\mathbf {r}, t) / \partial \mathbf {r} \| _ {\mathbf {r} _ {t}, t _ {f f}}. \tag {6.176}$$

It is noted in the last expression that $t _ { f f }$ is indicated as being held fixed; this is equivalent to fixing $t _ { T f }$ by virtue of (6.172) and the fact that t is fixed. In terms of $\mathbf { V } _ { c } ,$ , the Q-matrix can be written in the form
