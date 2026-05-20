During turns, the crosstrack error may be defined as follows. A turn center is defined (see Figure 7.3) that is the center of the circle containing the desired ground track during the turn. As a result, the crosstrack error then becomes the difference in the lengths of two vectors from the turn center. One of the vectors defines air vehicle position, and the other, the ground velocity. The third module, the vertical guidance module, calculates the vertical acceleration commands used by the autopilot module (i.e., vertical acceleration control) to control air vehicle altitude. Specifically, the vertical guidance module commands normal accelerations based on clearance altitude error and a selected form of feedback. Note that climbing flight generally employs a clearance rate feedback, while diving flight is executed with inertial rate feedback.

![](image/1eed0de3a35f382e3e79e249527997ee34a4fe88a193ad4371cd3cfd89d47934.jpg)

<details>
<summary>text_image</summary>

N
Waypoint
ΔΨ
P
V_G, missile ground velocity
Y
Missile
Ψ_G
Ψ_R
R
Nominal path from previous waypoint
To next waypoint
Y = Lateral path error
Ψ_E = Ψ_G - Ψ_R = Heading error
bank command eqn.:
φ_C = φ_N + K_Y Y + K_ΨΨ_E
φ_N = Nominal bank
= Zero on straight path
and constant during
transition arc
Y and Ψ_E measured from straight path unless
distance from P is less than R tan (ΔΨ/2)
then Y is measured from curved arc,
Ψ_R varies, and φ_N is specified value (not zero)
</details>

Fig. 7.3. Waypoint lateral path steering and turn control.
