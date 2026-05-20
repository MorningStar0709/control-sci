$$
Q = \left[ \begin{array}{l l l} \partial V _ {c x} / \partial x & \partial V _ {c x} / \partial y & \partial V _ {c x} / \partial z \\ \partial V _ {c y} / \partial x & \partial V _ {c y} / \partial y & \partial V _ {c y} / \partial z \\ \partial V _ {c z} / \partial x & \partial V _ {c z} / \partial y & \partial V _ {c z} / \partial z \end{array} \right]. \tag {6.177}
$$

Thus, the Q-matrix consists of at most of nine elements, six of which are distinct. For any given present missile position, target position, and time remaining before the specified time of arrival at the target, the elements of the Q-matrix may be computed. The elegance of the Q-guidance equations lies in the fact that these equations take accelerometer output as a function of time and yield at the output the velocity-to-begained $\mathbf { V } _ { g }$ .

A guidance technique that is applicable for a variety of powered flight guidance phases will now be presented. Specifically, a convenient and efficient guidance law will be developed in which the direction of the thrust acceleration is such that the vector $\mathbf { V } _ { g }$ and its derivative are parallel. Thus,

$$\left(\frac {d \mathbf {V} _ {g}}{d t}\right) \times \mathbf {V} _ {g} = 0.$$

Since (see also Section 6.5.2, (6.179))

$$\left(\frac {d \mathbf {V} _ {m}}{d t}\right) = \mathbf {a} _ {T} + \mathbf {g},$$

where g is the acceleration of gravity and aT is the thrust acceleration vector provided by the engine (and measured by the IMU accelerometers), the rate of change of the velocity-to-be-gained can be expressed as

$$\frac {d \mathbf {V} _ {g}}{d t} = \left(\frac {d \mathbf {V} _ {c}}{d t}\right) - \mathbf {a} _ {T} - \mathbf {g} = \mathbf {b} - \mathbf {a} _ {T},$$

where

$$\mathbf {b} = \left(\frac {d \mathbf {V} _ {c}}{d t}\right) - \mathbf {g}.$$

It is evident that at cut-off, the required velocity is attained simultaneously as b $ 0$ . The essential principle of steering is to point the thrust so that

$$\mathbf {a} _ {T} \times \mathbf {V} _ {g} = c \mathbf {b} \times \mathbf {V} _ {g},$$
