$\theta _ { M }$ = angle of sight line from ground station to the missile.

Differentiating (11) with the assumption that $V _ { M }$ remains constant yields

$$\dot {R} _ {O M} \dot {\theta} _ {M} + R _ {O M} \ddot {\theta} _ {M} = V _ {M} \cos (\gamma - \theta_ {M}) (\dot {\gamma} - \dot {\theta} _ {M}). \tag {13}$$

![](image/b07f3b51d8b0c2030f76e53a5426f964fcb9bfbc2d11542c091d1d57e9e8e9d0.jpg)

<details>
<summary>text_image</summary>

V_T
R_OT
Line of sight to target
V_M
γ
e
R_C
0
Ground station
Reference axis (chosen parallel to V_T)
θ_M
θ_T
</details>

Fig. 4.28. Geometric relationship for a line-of-sight command system.

Substituting (12) into (13) and dividing by $( d R _ { O M } / d t )$ yields

$$\dot {\gamma} = 2 \dot {\theta} _ {M} + \frac {R _ {O M}}{\dot {R} _ {O M}} \ddot {\theta} _ {M},$$

and since the missile lateral acceleration is equal to $V _ { M } ( d \gamma / d t )$ ,

$$a _ {M} = 2 V _ {M} \dot {\theta} _ {M} + \frac {R _ {O M} V _ {M}}{\dot {R} _ {O M}} \ddot {\theta} _ {M}.$$

If it is assumed that there are no errors in the system, then $\theta _ { M } = \theta _ { T }$ and

$$a _ {M} = 2 V _ {M} \dot {\theta} _ {T} + \frac {R _ {O M} V _ {M}}{\dot {R} _ {O M}} \ddot {\theta} _ {T}. \tag {14}$$

This equation yields missile acceleration as a function of motion of the target tracking line. Now, if the reference axis is chosen as parallel to the target velocity vector, the equations of motion of the target are

$$R _ {O T} \left(\frac {d \theta_ {T}}{d t}\right) = V _ {T} \sin \theta_ {T}, \tag {15}\frac {d R _ {O T}}{d t} = - V _ {T} \cos \theta_ {T}, \tag {16}$$

where $R o { \tau }$ is the distance from the ground station to the target and $V _ { T }$ is the velocity of the target. From the geometry,

$$\sin \theta_ {T} = R _ {C} / R _ {O T}, \tag {17}$$

where $R _ { C }$ is the crossover range, or the perpendicular distance from the ground station to the line of the target velocity vector. Substituting (17) into (15) gives

$$R _ {O T} ^ {2} \left(\frac {d \theta_ {T}}{d t}\right) = V _ {T} R _ {C}. \tag {18}$$

For a target flying a constant-speed straight-line course, $V _ { T } R _ { C }$ is constant. Realizing this and differentiating (18), we obtain

$$\frac {d ^ {2} \theta_ {T}}{d t ^ {2}} = - (2 \dot {R} _ {O T} / R _ {O T}) \theta_ {T}. \tag {19}$$

Substituting (16) and (19) into (14), we obtain

$$a _ {M} = 2 V _ {M} \dot {\theta} _ {T} \left[ 1 + \frac {\dot {R} _ {O M} V _ {T} \cos \theta_ {T}}{\dot {R} _ {O M} R _ {O T}} \right]. \tag {20}$$
