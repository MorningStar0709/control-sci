1. The characteristic equation is independent of the missile–target approach angle. This is because of the definition of the navigation ratio.   
2. As N - is increased, the required missile acceleration for any input target acceleration decreases. Further, the system becomes more responsive.   
3. $N ^ { \prime } > 2$ in order to obtain a stable system.   
4. A region of instability occurs when $t _ { g } < 2 t _ { s }$ , the smoothing time constant. This implies that the missile control loop is no longer fast enough to solve the geometry.   
5. No missile maneuver is required if the missile speed is constant $( d V _ { M } / d t = 0 )$ and the target flies a constant-speed straight-line course $( d V _ { T } / d t = V _ { T } ( d \gamma / d t ) = 0 )$ .

All of the above certainly indicates that if only the dynamics are considered, $N ^ { \prime }$ should be made as large as possible and $t _ { s }$ as small as possible. Unfortunately, the system must also contend with noise. In a homing system such as this, the type of noise that predominates is glint noise, which is present because the seeker is not tracking a point source but wanders randomly over the target’s cross section. As the range from the missile to target decreases, the angular magnitude of this wander increases.

The above results will now be a extended to a line-of-sight command missile. A line-of-sight missile could be of the beam-rider type, which automatically keeps itself centered in a radar beam transmitted by the ground station. However, in the command guidance system, the ground station tracks both the missile and the target, sending command signals to the missile to cause it to correct any deflection from the LOS path. To determine the acceleration requirements for the missile, an equation must be obtained that describes the acceleration as a function of target motion. As seen in Figure 4.28, the effect of $\theta _ { M }$ , the angle of the LOS to the interceptor missile, on the missile velocity vector angle γ must first be determined.

The equations of motion of the missile with respect to the tracking radar are

$$R _ {O M} \left(\frac {d \theta_ {M}}{d t}\right) = V _ {M} \sin (\gamma - \theta_ {M}), \tag {11}\frac {d R _ {O M}}{d t} = V _ {M} \cos (\gamma - \theta_ {M}), \tag {12}$$

where

$R o _ { { \cal M } }$ = distance from missile to ground station,

$V _ { M }$ = missile velocity,

$\gamma$ = missile velocity vector angle with respect to the reference axis,
