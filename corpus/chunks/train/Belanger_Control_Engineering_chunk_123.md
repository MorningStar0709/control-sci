# DEFINITION

A state $x^{*} \neq 0$ is said to be uncontrollable if the zero-state response $\mathbf{x}(t)$ is orthogonal to $x^{*}$ for all t > 0 and all input functions.

In the circuit of Example 3.2, it is clear that, due to symmetry, the zero-state response is such that $x_{1}(t) = x_{2}(t)$ , regardless of the form of the input $i_{s}(t)$ . In Figure 3.6, the only state values reachable if $\mathbf{x}(0) = \mathbf{0}$ are those on the line $x_{1} = x_{2}$ . The zero-state response is orthogonal to $x^{*}$ , i.e., has no component in that direction; $x^{*}$ is an uncontrollable state.

Mathematically, this condition is

$$\mathbf {x} ^ {* T} \int_ {0} ^ {t} e ^ {A \tau} B \mathbf {u} (t - \tau) d \tau = \int_ {0} ^ {t} \mathbf {x} ^ {* T} e ^ {A \tau} B \mathbf {u} (t - \tau) d \tau = 0 \tag {3.47}$$

![](image/d1182a15c1ccd86a42c65b2920852b24434a35065175a802f692d469ab42f312.jpg)

<details>
<summary>text_image</summary>

x
x₂
Locus of reachable states
x₁
</details>

Figure 3.6 Illustration of controllability for the circuit of Example 3.2

for all t. Equation 3.47 must hold for all possible functions $\mathbf{u}(t-\tau)$ . This can be only if $x^{*T}e^{A\tau}B=0$ for all $\tau,0<\tau\leq t$ ; otherwise, $\mathbf{u}(t-\tau)$ could always be chosen to make the integrand positive for all values of $\tau$ where $x^{*T}e^{A\tau}B\neq0$ , and the integral would not be zero. Thus, an uncontrollable state $x^{*}$ satisfies the equation

$$\mathbf {x} ^ {* T} e ^ {A t} B = \mathbf {0} \quad \text { for all } t \geq 0. \tag {3.48}$$

We can now relate the existence of uncontrollable states to controllability through the following theorem.
