# LEMMA 2.1

If for every function $g(t)$ which is continuous,

$$\int_ {t _ {0}} ^ {t _ {f}} g (t) \delta x (t) d t = 0 \tag {2.3.13}$$

where the function $\delta x(t)$ is continuous in the interval $[t_{0}, t_{f}]$ , then the function $g(t)$ must be zero everywhere throughout the interval $[t_{0}, t_{f}]$ . (see Figure 2.5.)

Proof: We prove this by contradiction. Let us assume that $g(t)$ is nonzero (positive or negative) during a short interval $[t_{a}, t_{b}]$ . Next, let us select $\delta x(t)$ , which is arbitrary, to be positive (or negative) throughout the interval where $g(t)$ has a nonzero value. By this selection of $\delta x(t)$ , the value of the integral in (2.3.13) will be nonzero. This contradicts our assumption that $g(t)$ is non-zero during the interval. Thus $g(t)$ must be identically zero everywhere during the entire interval $[t_{0}, t_{f}]$ in (2.3.13). Hence the lemma.

![](image/6eea703cbd7270a2a559acbf9f601378cfe3b726d0d6b5738fb638f9ef24ab6e.jpg)

<details>
<summary>line</summary>

| t | g(t) | δx(t) |
| --- | --- | --- |
| t₀ |  |  |
| tₐ |  |  |
| t_b |  |  |
| t_f |  |  |
</details>

Figure 2.5 A Nonzero $g(t)$ and an Arbitrary $\delta x(t)$

\- Step 6: Euler-Lagrange Equation: Applying the previous lemma to (2.3.12), a necessary condition for $x^{*}(t)$ to be an optimal of the functional $J$ given by (2.3.1) is

$$\left(\frac {\partial V (x ^ {*} (t) , \dot {x} ^ {*} (t) , t)}{\partial x}\right) _ {*} - \frac {d}{d t} \left(\frac {\partial V (x ^ {*} (t) , \dot {x} ^ {*} (t) , t)}{\partial \dot {x}}\right) _ {*} = 0 \tag {2.3.14}$$
