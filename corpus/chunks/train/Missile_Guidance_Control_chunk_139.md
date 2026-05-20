Because of the presence of lags in the seeker tracking loop and radome refraction effects, the seeker will not point directly at the actual target. Instead, the seeker will point to the apparent target. The reader should be cautioned that radar reflectivity from a target is affected by the frequency of the radar. An aircraft design that is invisible to high-frequency fire-control radar may be plainly obvious to low-frequency search radar. The half-wave-length phenomena can be a factor. Parts of an aircraft that equal one-half of radar’s wavelength create a resonance that greatly increases radar reflectivity. The aberration (or refraction) angle error is the result of nonlinear distortions in the received energy as it passes through the protective covering (e.g., radome in the case of a radar homing sensor) over the antenna. This distortion produces a false boresight error signal, $\varepsilon ^ { \prime }$ which is interpreted as an error in the angular position and motion of the target by the guidance system. Referring to Figure 3.25, we note that the indicated boresight error $\varepsilon ^ { \prime }$ in the presence of radome aberration or refraction angle error $\theta _ { r }$ is given by the expression [3], [5], [12]

$$\varepsilon^ {\prime} = \lambda + \theta_ {r} - \theta_ {m} - \theta_ {h}, \tag {3.73c}$$

where the radome aberration angle error $\theta _ { r }$ is in general not constant, but is a function of the gimbal angle $\theta _ { h }$ ; that is, the radome angle error is a nonlinear function of the gimbal angle $\theta _ { h }$ . Mathematically, this can be expressed by the relation $\theta _ { r } = f ( \theta _ { h } )$ . It should be noted here that the size of the measurement error, that is, the angle $\theta _ { r }$ , depends on the orientation of the antenna with respect to the radome (antenna cover), which is fixed to the missile airframe.

![](image/3b6bc0cad6884455cc5d286671c03944722f322f68b3ede5c9eb07a237cc24af.jpg)

<details>
<summary>text_image</summary>

Apparent LOS to target
True LOS to target
Missile
Antenna
ε′
θᵣ
ε
λ
Radome
Radome slope, R
Non-rotating
reference line
Radar antenna,
optics, etc.
θₕ
θₘ
</details>

Fig. 3.25. Effect of radome aberration error.
