![](image/24b2887d9d3622ab90be66764b05e73c1a56dff44b59c96d248c7916e5ce08bf.jpg)

<details>
<summary>text_image</summary>

Perturbed
vehicle at
t = t₁
γ₁
V₁
Unperturbed
vehicle at
t = t₁
Unit vector
r̂
Burnout
point
t = t₀
Unit vector
θ̂
Nominal
path
r
δθ
rᵢ
h
rₒ
Arbitrary
base line
Earth
Perturbed
end point
δr
δr
V₁ₚ
δv
V₁ₚ
δθ
V₁
Nominal
end point
</details>

Fig. 6.18. In-plane geometry.

6.4.3.1.1. Velocity Errors The velocity errors are first derived by differentiating (119) with respect to any of the four burnout variables, which we will symbolize by the letter b.

$$
\begin{array}{l} \partial \mathbf {V} / \partial b = (\partial / \partial b) (\dot {r} \hat {\mathbf {r}}) + (\partial / \partial b) (r \dot {\theta} \hat {\boldsymbol {\theta}}) \\ = (\partial \dot {r} / \partial b) \hat {\mathbf {r}} + \dot {r} (\partial \hat {\mathbf {r}} / \partial b) + (\partial / \partial b) (r \dot {\theta}) \hat {\boldsymbol {\theta}} + r \dot {\theta} (\partial \hat {\boldsymbol {\theta}} / \partial b). \tag {6.121} \\ \end{array}
$$

Since $\hat { \pmb { \theta } }$ and rˆ are functions of θ only, then

$$\partial \hat {\mathbf {r}} / \partial b = (\partial \hat {\mathbf {r}} / \partial \theta) (\partial \theta / \partial b) \quad \text { and } \quad (\partial \hat {\boldsymbol {\theta}} / \partial b) = (\partial \hat {\boldsymbol {\theta}} / \partial \theta) (\partial \theta / \partial b). \tag {6.122a}$$

Now, using

$$\partial \hat {\mathbf {r}} / \partial \theta = d \hat {\mathbf {r}} / d \theta \quad \text { and } \quad d \hat {\mathbf {r}} / d \theta = \hat {\boldsymbol {\theta}}, \tag {6.122b}$$

(6.122a) becomes

$$\partial \hat {\mathbf {r}} / \partial b = (\partial \hat {\boldsymbol {\theta}} / \partial b) \hat {\boldsymbol {\theta}}. \tag {6.122c}$$

Similarly,

$$\partial \hat {\pmb {\theta}} / \partial b = (d \hat {\pmb {\theta}} / d \theta) (\partial \theta / \partial b) \quad \mathrm{and} \quad d \hat {\pmb {\theta}} / d \theta = - \hat {\mathbf {r}},$$

so that

$$\partial \hat {\boldsymbol {\theta}} / \partial b = (- \partial \theta / \partial b) \hat {\mathbf {r}}. \tag {6.123}$$

Substituting (6.122c) and (6.123) into (6.121), we obtain
