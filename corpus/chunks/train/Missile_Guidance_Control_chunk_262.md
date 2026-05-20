The rate of variation of the LOS, dλ/dt, is measured by the seeker, and the tracking error related to the system of measurement is neglected. In other words, the axis of the seeker is assumed to lie always along the LOS. The seeker head will be limited to a cone with a maximum half-angle equal to $4 5 ^ { \circ }$ , which imposes the saturation constraint $| \lambda - \theta | \leq 4 5 ^ { \circ }$ . The variable $q$ is by definition the pitch rate $d \theta / d t$ of the longitudinal axis of the missile about the $O Y ^ { \prime }$ axis. Therefore, the kinematic equations can be grouped together, forming an eighth-order nonlinear system represented by the deterministic state space equation (see Section 4.8),

$$\frac {d x}{d t} = f (\boldsymbol {x}),$$

with the state vector represented by

$$\boldsymbol {x} = [ u \quad w \quad q \quad \theta \quad \delta_ {z} \quad \delta_ {z d} \quad r \quad \lambda ] ^ {T}$$

and the control vector

$$\boldsymbol {u} = [ \delta_ {z e l} ],$$

where

$$\delta_ {z} = \text { tail fin (or thrust) deflection angle },\delta_ {z d} = \text { gyroscopic feedback },\delta_ {z e l} = \text { steering fin actuator signal }.$$

Figure 4.10 shows the interceptor missile maneuver capability and geometry for a hypothetical air-to-air interceptor missile.

We conclude this section by presenting some additional mathematical expressions and algorithms of the following guidance laws: (1) pure pursuit, (2) collision course interception, and (3) line-of-sight (LOS) interception.
