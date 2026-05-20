the unit lift vector is

$$\mathbf {1} _ {L} = (\boldsymbol {\omega} \times \mathbf {V} _ {M}) / | \boldsymbol {\omega} \times \mathbf {V} _ {M} |,$$

and the desired lift acceleration magnitude is

$$a _ {L d} = G _ {1} | \pmb {\omega} \times \mathbf {V} _ {M} |.$$

The basic proportional navigation trajectory is sensitive to variations in certain parameters. The degree of sensitivity reflects the impact of the parameter on the proportional navigation equation and on the mechanization considerations. The following parameters are considered significant (but they are by no means exhaustive):

1. Missile Time Constant: The pursuit time constant $T _ { p }$ is the time required for the missile to respond to a measured $d \lambda / d t$ . If the missile is executing normal acceleration $a _ { n m }$ , then in $T _ { p }$ seconds the missile will travel $\frac { 1 } { 2 } a _ { n m } \ T _ { p } ^ { 2 }$ feet before corrections are applied. Thus, reducing $T _ { p }$ tends to reduce overshoot or undershoot. However, reducing $T _ { p }$ increases the missile bandwidth, thus making the missile more susceptible to guidance noise.   
2. Effective Navigation Ratio $N ^ { \prime } \colon$ : As the effective navigation ratio is increased, smaller values of $d \lambda / d t$ will produce given amounts of commanded $g ^ { \ast } \mathbf { s }$ . However, as $N ^ { \prime }$ is increased, the effects of guidance noise associated with $d \lambda / d t$ become more significant.   
3. Heading Error: The effect of heading error is strongly dependent on $N ^ { \prime }$ . The higher $N ^ { \prime }$ , the greater the allowable heading error that can be successfully guided against.   
4. Target Maneuver: As $N ^ { \prime }$ is increased, the greater is the amount of target maneuver that can be allowed while still permitting successful intercept of the target. However, since unwanted bias levels are indistinguishable from target maneuvers, increasing $N ^ { \prime }$ aggravates the effect of bias errors.   
5. Noise: The fundamental effect of noise is to mask (or hide) the true value of $d \lambda / d t$ . Noise can occur due to target effects or receiver (missile) effects. Target effects are fading and scintillation noise. In addition, the radome contributes a bias error (known as boresight error) due to refraction effects.
