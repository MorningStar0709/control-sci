$$\boldsymbol {\omega} _ {c} = \mathbf {1} _ {x} \times K (\mathbf {V} _ {g} - \mathbf {B}), \tag {6.196}$$

where

$$\omega_ {c} = \text { commanded angular velocity vector of the missile },\mathbf {V} _ {g} = \text { velocity - to - be - gained resolved in body coordinates },\mathbf {B} = \text { control bias },K = \text { control gain },\mathbf {1} _ {x} = \text { unit vector along the body } x (\text { or roll }) \text { axis. }$$

The bias B is readily adjusted to account for variations in target and launch point parameters. It can also be shown that the bias is an exponential function of time during the atmospheric phase of the flight. Thus, it is simple to generate in a guidance computer. By forcing the bias to zero after atmospheric exit, the control acts to null $\mathbf { V } _ { g }$ ; thus, the same system configuration can be used throughout the powered flight. The analysis to follow will show that for stability purposes, it is necessary to add a lead term to the control law of (6.196). There are various ways to accomplish this, so we will select to use the lateral body acceleration. The control equation is

$$\boldsymbol {\omega} _ {c} = \mathbf {1} _ {x} \times \left[ K _ {1} (\mathbf {V} _ {g} - \mathbf {B}) - K _ {2} \left\{\left(\frac {d \mathbf {V} _ {g}}{d t}\right) - \left(\frac {d \mathbf {B}}{d t}\right) \right\} \right],$$

or

$$\boldsymbol {\omega} _ {c} = \mathbf {1} _ {x} \times [ K _ {1} (\mathbf {V} _ {g} - \mathbf {B}) - K _ {2} \mathbf {a} _ {B} ]. \tag {6.197}$$

Since the system accuracy could be degraded by a rollout maneuver at launch, the roll angle should be held at its initial value throughout the flight. In general, this will require both pitch and yaw rate commands in order to remain in the target plane. Assuming no axis coupling, the result is that (6.197) will have two components:

$$\frac {d \theta_ {c}}{d t} = - K _ {1} (V _ {g z} - B _ {z}) + K _ {2} a _ {B z}, \tag {6.198}\frac {d \psi_ {c}}{d t} = K _ {1} (V _ {g y} - B _ {y}) + K _ {2} a _ {B y}. \tag {6.199}$$
