The sensitivity of the time of flight to errors in position and velocity in the horizontal directions is such that they will not introduce errors that must be considered in a first-order error analysis. It should be noted that the time of free flight depends on $V _ { R }$ , which in turn is a function of the impact position. Hence, an iterative procedure must be used to calculate the required velocity and the time of free flight. This iteration process may be thought of as follows [9]:

(1) A future target position is assumed.   
(2) The corresponding required velocity $V _ { R }$ is computed.   
(3) Compute the elements of the resulting ellipse.   
(4) Compute the time of free flight.

![](image/f4e962e0a987c3d827b81e50c8c67fe439264ef1f8cdf5ea2311b4899a5cade3.jpg)

<details>
<summary>text_image</summary>

0
ω
Δλ + ωt_Tf
B
ψ
ρ
A
φ_t
φ_o
λ_o
λ_t
</details>

Fig. 6.21. Launch site and aiming point at the instant of launch. Originally published in Fundamentals of Astrodynamics, R. R. Bate, D. D. Mueller, and J. E. White, Dover Publications, Inc., Copyright ©1971. Reprinted with permission.

(5) Compute (or assume) a future target position.   
(6) Repeat the above procedure.

In reference [2], the effect of the Earth’s rotation is computed in terms of the range. From Figure 6.21 we can obtain the range ρ (i.e., launch point to target) using the law of cosines for spherical triangles as follows:

$$\cos \rho = \sin \varphi_ {o} \sin \varphi_ {t} + \cos \varphi_ {o} \cos \varphi_ {t} \cos (\Delta \lambda + \omega t _ {T f}),$$

where

$$
\begin{array}{l} \varphi_ {o} = \text { launch   latitude }, \\ \varphi_ {t} = \text { target   latitude }, \\ \Delta \lambda = \text { longitude   differential }, \\ \omega = \text { Earth's   rate   of   rotation }, \\ t _ {T f} = \text { total   time - of - flight   (i.e.,   launch   to   target   intercept) }. \\ \end{array}
$$

Note that here we use the total time-of-flight instead of the free-fall time-of-flight tff , since we consider the launch from the surface of the Earth to a target on the surface of the Earth.

Similarly, using the law of cosines for spherical triangles, we can obtain the launch azimuth angle ψ in terms of the range ρ as follows:

$$\cos \psi = (\sin \varphi_ {t} - \sin \varphi_ {o} \cos \rho) / \cos \varphi_ {o} \sin \rho .$$

The total time-of-flight $t _ { T f }$ can be computed, as before, by iteration. In order to do this, one must first use a reasonable time or “guess” $t _ { T f }$ . This first guess can be used to compute an initial estimate for $\rho$ , which in turn would allow one to get a first estimate of $t _ { f f }$ . By adding the times of powered flight and reentry (which also depend somewhat on $\rho )$ to $t _ { f f }$ , one obtains a value of $t _ { T f }$ , which can be used as a second “guess.” The entire process is then repeated until the computed value of $t _ { T f }$ agrees with the estimated value.
