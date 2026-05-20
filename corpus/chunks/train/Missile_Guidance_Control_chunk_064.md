From the definition of the above variables, the orientation of the velocity vector V is through the angles $\beta$ and $\gamma _ { : }$ , while the orientation of the aircraft body axes relative to the velocity vector is through the angle µ and the AOA α in the pitch plane. The yaw of the aircraft about the velocity vector, V, is assumed to be zero (i.e., sufficient control power exists that all maneuvers are coordinated). For this 5-DOF (x, y, z, α, µ) point mass model, the equations of motion are as follows:

$$
\begin{array}{l} x = V \cos \gamma \cos \beta , \\ y = V \cos \gamma \sin \beta , \\ z = V \sin \gamma , \\ \dot {V} = \frac {1}{m} [ T \cos \alpha - D ] - g \sin \gamma , \\ \dot {\beta} = \frac {1}{m V} [ T \sin \alpha + L ] (\sin \mu / \cos \gamma), \\ \dot {\gamma} = \frac {1}{m V} [ T \sin \alpha + L ] \cos \mu - (g / V) \cos \gamma , \\ m = m (M, z, n), \\ \dot {n} = \dot {n} (\alpha , V _ {I A S}), \\ \dot {\alpha} = \dot {\alpha} (\alpha , V _ {I A S}), \\ \dot {\mu} = \dot {\mu} (\alpha , V _ {I A S}), \\ \end{array}
$$

where

$$
\begin{array}{l} M = \text { Mach   number }, \\ g = \text { acceleration   of   gravity }, \\ m = \text { mass }, \\ n = \text { throttle   setting }, \\ V _ {I A S} = \text { indicated   airspeed }, \\ T = \text { Thrust } = T (M, z, n), \\ D = \operatorname{drag} = \frac {1}{2} \rho V ^ {2} S C _ {D} (\text { see   Section   3.1 }), \\ L = \mathrm{lift} = \frac {1}{2} \rho V ^ {2} S C _ {L} (\mathrm{seeSection3.1}), \\ \rho = \text { atmospheric   density } = \rho (z) \\ (i. e., a \text {   function   of   altitude }), \\ S = \text { aerodynamic   reference   area }, \\ C _ {D} = \text { coefficient   of   drag }, \\ C _ {L} = \text { coefficient   of   lift. } \\ \end{array}
$$

Several approximations can be made in the above model. These are:

1. The $d \beta / d t$ equation of motion becomes undefined for vertical (i.e., $\gamma = \pm 9 0 ^ { \circ } )$ flight.   
2. The dn/dt , dα/dt , dµ/dt equations are at best first-order approximations to actual aircraft control response.

From the above results and discussion, a 6-DOF model can be implemented that approximates an actual 6-DOF control response with a standard transfer function/filter whose input constants can be selected by the designer to more accurately match actual aircraft/missile control response. The roll, pitch, and yaw transfer functions are then as follows:

Roll: $\frac { P _ { \mathrm { s t a b } } ( s ) } { P _ { \mathrm { s t a b } _ { \mathrm { c m d } } } ( s ) } = \frac { 1 } { \tau s + 1 }$
