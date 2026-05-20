where P is the roll rate, Q is the pitch rate, and R is the yaw rate. Note that some authors use lowercase letters for roll, pitch, and yaw rates instead of uppercase letters. Therefore, these linear and rotational velocity components constitute the 6-DOF of the missile. As stated in the beginning of this section, the rigid-body equations of motion are obtained from Newton’s second law, which states that the summation of all external forces acting on a body is equal to the time rate of the momentum of the body, and the summation of the external moments acting on the body is equal to the time rate of change of moment of momentum (angular momentum). Specifically, Newton’s laws of motion were formulated for a single particle. Assuming that the mass m of the particle is multiplied by its velocity V, then the product

$$\mathbf {p} = m \mathbf {V} \tag {2.15}$$

is called the linear momentum. Thus, the linear momentum is a vector quantity having the same direction and sense as V. For a system of n particles, the linear momentum is the summation of the linear momenta of all particles in the system. Thus [8],

$$\mathbf {p} = \sum_ {i = 1} ^ {n} (m _ {i} \mathbf {V} _ {i}) = m _ {1} \mathbf {V} _ {1} + m _ {2} \mathbf {V} _ {2} + \dots + m _ {n} \mathbf {V} _ {n}, \tag {2.16}$$

where i denotes the ith particle, and n denotes the number of particles in the system. Note that the time rates of change of linear and angular momentum are referred to an absolute or inertial reference frame. For many problems of interest in airplane and missile dynamics, an axis system fixed to the Earth can be used as an inertial reference frame (see Figure 2.1). Mathematically, Newton’s second law can be expressed in terms of conservation of both linear and angular momentum by the following vector equations [1], [8], [11]:

$$\left. \sum \mathbf {F} = \frac {d (m \mathbf {V} _ {M})}{d t} \right] _ {I}, \tag {2.17a}\left. \sum \mathbf {M} = \frac {d \mathbf {H}}{d t} \right] _ {I}, \tag {2.17b}$$

where m is the mass, H the angular momentum, and the symbol ]I indicates the time rate of change of the vector with respect to inertial space. Note that (2.17a) is simply

$$\mathbf {F} = \frac {d \mathbf {p}}{d t}, \tag {2.18a}$$

or

$$\mathbf {F} = m \left(\frac {d \mathbf {V}}{d t}\right) = m \mathbf {a}. \tag {2.18b}$$

Equations (2.17a) and (2.17b) can be rewritten in scalar form, consisting of three force equations and three moment equations as follows:
