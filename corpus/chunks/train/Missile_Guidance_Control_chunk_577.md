Because of the simplifications inherent in the out-of-plane case, the notation used in the in-plane case, where a distinction must be made between error coefficients and error partials, is redundant, and the above four error coefficients are identical to their error partials. That is,

$$(\partial \mathbf {L} / \partial n) _ {\hat {n}} = \partial L / \partial n, (\partial \mathbf {L} / \partial V _ {n}) _ {\hat {n}} = \partial L / \partial V _ {n},$$

and

$$(\partial \mathbf {V} _ {L} / \partial n) _ {\hat {n}} = \partial V _ {L} / \partial n, \quad (\partial \mathbf {V} _ {L} / \partial V _ {n}) _ {\hat {n}} = \partial V _ {L} / \partial V _ {n}. \tag {6.153}$$

![](image/029abc8f2148a98164e3a040e9a3feb927ac3c5abf41c3cb3a790c05d62dda64.jpg)

<details>
<summary>text_image</summary>

Burnout or
thrust cutoff
Z
Y into
paper
Base line
α
r₀ cos
θ₁ - θ₀
θ₀
θ₁
r₁
0
Normal to axis
of separation
(θ' = θ₁ - θ₀)
θ' - α
End of coast
γ₁
V₁
α
Earth
Axis of plane
separation
δn
r₀ sin γ(= r₀ cos α)
β
Side view showing
plane separation
</details>

Fig. 6.19. Geometry for $\left( \partial V _ { L } / \partial n \right)$ and (∂L/∂n).

The equations for generating δL, the lateral vector position error, and $\delta \mathbf { V } _ { L }$ , the lateral vector velocity error, are thus

$$\delta \mathbf {L} = (\partial \mathbf {L} / \partial b _ {n}) _ {\hat {n}} \delta b _ {n} \hat {n} = (\partial L / \partial b _ {n}) \delta b _ {n} \hat {n} \tag {6.154}$$

and

$$\delta \mathbf {V} _ {L} = (\partial \mathbf {V} _ {L} / \partial b _ {n}) _ {\hat {n}} \delta b _ {n} \hat {n} = (\partial V _ {L} / \partial b _ {n}) \delta b _ {n} \hat {n}, \tag {6.155}$$

where $b _ { n }$ includes n and $V _ { n }$ the burnout variables normal to the plane of the nominal trajectory. Equation (6.153) involves two coefficients: $( \partial L / \partial n )$ and $( \partial L / \partial V _ { n } )$ . The first of these is derived with reference to Figure 6.19 (which is also used later for the derivation of $\partial V _ { L } )$ .

The key to the geometry of a perturbation δn is the fact that the axis of separation of the two trajectory planes must be parallel to the initial velocity vector. The plane separation angle $\beta$ is thus

$$\beta = \delta n / r _ {o} \cos \alpha .$$

From Figure 6.19 it is evident that

$$\delta L = \beta r _ {o} \sin (9 0 ^ {\circ} + \alpha - \theta^ {\prime}).$$

Substituting for $\beta$ yields

$$\delta L = (\delta n / (r _ {o} \cos \alpha)) r _ {1} \sin (9 0 ^ {\circ} + \alpha - \theta^ {\prime}),$$
