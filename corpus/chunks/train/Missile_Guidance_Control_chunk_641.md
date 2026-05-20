# 6.6.1 Equations of Motion

For long, slender ballistic missiles it is necessary to consider the actual missile dynamics. Therefore, only rigid-body dynamics will be considered here. The translational equations of rigid-body motion are solved in an inertially fixed rectangular $( X , Y , Z )$ coordinate system with origin at the center of the Earth. This frame will be assumed here to be parallel to the (X, Y, Z) guidance axes: The Z-axis is pointing up, the Y -axis is in the local horizontal plane at launch, and the X-axis is above the horizontal by an angle $\alpha _ { X }$ . Furthermore, the XZ-plane is pointed downrange (the guidance azimuth measuring the angle that the XZ-plane makes with the local north, positive clockwise). The launch latitude $\varphi _ { L P }$ , X erection $( \alpha _ { X } )$ , and the guidance azimuth $( \psi )$ are input quantities.

In such a coordinate system, the equations of motion (XY Z components always implied) are

$$\mathbf {V} = \mathbf {V} _ {0} + \int_ {t _ {0}} ^ {t} (\mathbf {a} _ {T} + \mathbf {g}) d t, \tag {6.222}\mathbf {R} = \mathbf {R} _ {0} + \int_ {t _ {0}} ^ {t} \mathbf {V} d t, \tag {6.223}$$

where

aT = specific force vector acting on the missile,

g = gravitational acceleration vector due to the Earth,

V = inertial velocity vector of the missile,

R = inertial position vector of the missile,

t = time measured from computer start,

$t _ { o } , \mathbf { R } _ { o } , \mathbf { V } _ { o } = t , \mathbf { R } , \mathbf { V }$ at time of nominal first-stage ignition.

It is convenient for output purposes to actually consider V to be the sum of missile velocity relative to the launch point $( \mathbf { V } _ { m } )$ and the velocity of the launch point with respect to inertial space $( \mathbf { V } _ { L P } = \mathrm { c o n s t a n t } )$ , so that the equations of motion become

$$\mathbf {V} _ {m} = \mathbf {V} _ {m o} + \int_ {t _ {0}} ^ {t} (\mathbf {a} _ {T} + \mathbf {g}) d t, \tag {6.224a}\mathbf {R} = \mathbf {R} _ {o} + \int_ {t _ {0}} ^ {t} (\mathbf {V} _ {m} + \mathbf {V} _ {L P}) d t. \tag {6.224b}$$

This constitutes what may be called the navigation portion of the missile motion. The computation of $\mathbf { a } _ { T }$ and g will be required for the navigation process and will simulate the guidance phase. Specifically, the guidance phase of a simulation models the generalized computation of the velocity-to-be-gained and indicated Z-velocity $( V _ { Z I } )$ , with
