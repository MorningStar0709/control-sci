As already discussed in Section 3.4.1, the function of the seeker in the missile is to generate a measure of the LOS space rate (i.e., the rate of turning in space of the line joining the missile and the target). A rate gyro mounted on the seeker stabilizes the servo loop and provides an output voltage proportional to the sight line space rate. Because the response of the seeker antenna control loop may be made fast in comparison with the airframe response, it is necessary to smooth the seeker output signal to prevent noise signals from causing excessive missile gyrations. Moreover, since the smoothing time constant must usually be long in comparison with the other time constants in the seeker assembly, the seeker transfer function may be written in the form (see also guidance law equation in summary)

$$\frac {d \sigma^ {\prime}}{d t} = \left(\frac {d \sigma}{d t}\right) / (1 + t _ {s} s), \tag {6}$$

where

$t _ { s }$ = smoothing time constant,

$\sigma ^ { \prime }$ = angle of the seeker antenna axis with respect to space coordinates.

Based on the material presented in Chapters 2 and 3, and Figure 4.26, the following equations can be written:

1. Summation of forces perpendicular to the velocity vector:

$$- V _ {M \dot {\gamma}} = \frac {Z _ {\alpha} - T}{m} \alpha + \frac {Z _ {\delta}}{m} \delta$$

2. Summation of moments about the center of gravity of the missile:

$$\ddot {\theta} = \frac {M _ {\alpha}}{I} \alpha + \frac {M _ {\delta}}{I} \delta + \frac {M _ {\theta}}{I} \dot {\theta}$$

3. The angle-of-attack equation:

$$\theta = \alpha + \gamma ,$$

where

$$\gamma = \text { angle of missile velocity vector in space }\theta = \text { attitude angle of missile body in space }\alpha = \text { angle of attack }\delta = \text { wing or control surface deflection }m = \text { mass of missile }I = \text { moment of inertia of missile }M _ {\alpha}, M _ {\delta} = \text { moments due to } \alpha \text { and } \deltaZ _ {\alpha}, Z _ {\delta} = \text { forces due to } \alpha \text { and } \deltaM _ {\theta} = \text { moment due to viscous damping about } \theta \text { axis }T = \text { thrust }$$

The first two equations are differential equations with nonconstant coefficients. These coefficients are primarily functions of the air density, the velocity, and the missile design. In Figure 4.27, the block labeled navigation ratio will be discussed next. An equation similar to (4.26) that expresses the idea of proportional navigation in this example is
