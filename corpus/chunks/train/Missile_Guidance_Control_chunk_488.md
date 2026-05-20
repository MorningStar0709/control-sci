$$C _ {3 1} ^ {\prime} = C _ {3 1} + \left[ \left(C _ {3 3} C _ {3 1} \Delta N + C _ {3 2} \Delta E\right) / R _ {E} \cos \lambda \right], \tag {5.67a}C _ {3 2} ^ {\prime} = C _ {3 2} + \left[ \left(C _ {3 3} C _ {3 2} \Delta N - C _ {3 1} \Delta E\right) / R _ {E} \cos \lambda \right], \tag {5.67b}C _ {3 3} ^ {\prime} = C _ {3 2} - \left[ (\cos \lambda \cdot \Delta N) / R _ {E} \right]. \tag {5.67c}$$

Summarizing, (5.66a)–(5.66c) are exact and apply during the dead reckoning mode of navigation. Equations (5.67a)–(5.67c) are approximate and apply with inertial navigation.

It is noted here that the great circle path in the centerline recovery mode is continuous. Therefore, the approach or overfly of a destination is not a problem. In the direct mode, the desired path is always to the destination, thus presenting a potential problem when a destination is to be overflown. As stated previously, the predicted crosstrack drift of the bomb, CI , must be considered to deliver a weapon on target. The crosstrack error $Y _ { e }$ computed in the navigation equations is modified by CI as follows:

$$Y _ {e} ^ {\prime} = Y _ {e} + C I, \tag {5.68}$$

$Y _ { e }$ is negative, as shown in Figure 5.30, and CI is positive when the predicted bomb drift is to the left. The steering equation uses $Y _ { e } ^ { \prime }$ when in the bomb mode instead of $Y _ { e }$ . If there is no crosstrack drift of the bomb, then $Y _ { e } ^ { \prime } = Y _ { e }$ .

![](image/f24680bf9e8d01ac25346cbc8be9e7eb14c79d1d89de52ee877f9d862e732898.jpg)

<details>
<summary>text_image</summary>

Target
CI = computed bomb-drift
from bomb algorithm
ψe = Angle between the
ground velocity vector
Vg and the great circle
path
CI
Ye
Ye'
ψe
A/C → Vg
IP
Ye = Crosstrack position
error as calculated in
the navigation equations
IP = Initial point for start of
weapon delivery
</details>

Fig. 5.30. Centerline recovery mode geometry.

![](image/eff0a910142e6583c5307c8d0b2810fb1ee75b52a76dbfe74cc728e2d7b07544.jpg)

<details>
<summary>text_image</summary>

Vg
ψe
ψ'e
A/C
Cl
Target
Current computer
great circle path
●IP
</details>

Fig. 5.31. Direct mode geometry.

In order to account for the crosstrack drift CI of the bomb, the track angle error $\psi _ { e }$ of the basic navigation equation is modified as follows:

$$\psi_ {e} ^ {\prime} = \psi_ {e} + \sin^ {- 1} (C I / D _ {o}), \tag {5.69}$$

where
