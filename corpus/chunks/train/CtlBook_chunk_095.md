# 3.4.1 Gear Kinematic Relationships

A common system element in rotary systems is gears. The corresponding element in translational systems, levers, seem to appear less often in control systems.

Consider two meshed gears, gear 1 and gear 2 (Figure 3.2). Each gear has $N _ { i }$ teeth. The size of each tooth is $2 \pi r _ { i } / N _ { i }$ . The number of teeth which pass when a gear is rotated by $\theta _ { i }$ is $N _ { i } \frac { \theta _ { i } } { 2 \pi }$ . Since the teeth must be the same size for the gears to mesh, we can write

$$\frac {N _ {1} \theta_ {1}}{2 \pi} = \frac {N _ {2} \theta_ {2}}{2 \pi}$$

or

$$\frac {\theta_ {1}}{\theta_ {2}} = \frac {N _ {2}}{N _ {1}}$$

dierentiating we also have

$$\frac {\dot {\theta} _ {1}}{\dot {\theta} _ {2}} = \frac {N _ {2}}{N _ {1}} \qquad \frac {\ddot {\theta} _ {1}}{\ddot {\theta} _ {2}} = \frac {N _ {2}}{N _ {1}}$$

Commonly we dene $n = N _ { 1 } / N _ { 2 }$ . Thus

$$\dot {\theta_ {2}} = n \dot {\theta_ {1}}$$

etc.

![](image/7f033359dd0d36511af7dfcad30860851754dec0a13989cd1a1fb398fa38e7f4.jpg)

<details>
<summary>text_image</summary>

N₁
r₁
1
f
τ₂, θ₂
2
r₂
N₂
τ₁, θ₁
</details>

Figure 3.2: Two meshed gears.

![](image/dcc16fc4b4599c9da92301d0f13f1d40239b0bffb12572023492df41c1dea10c.jpg)

<details>
<summary>text_image</summary>

N₁
τ₁,θ₁
N₂
B
τ₂,θ₂
</details>

Figure 3.3: A viscous load (damper) driven by a set of gears.

There is a force exerted by one tooth on the other in the tangential direction, f (Figure 3.2). Since it is tangential, we can relate it easily to the torques:

$$\tau_ {1} = r _ {1} f \qquad \tau_ {2} = r _ {2} f$$

This gives

$$\tau_ {1} = \frac {r _ {1}}{r _ {2}} \tau_ {2} = n \tau_ {2}\tau_ {2} = \frac {1}{n} \tau_ {1}$$
