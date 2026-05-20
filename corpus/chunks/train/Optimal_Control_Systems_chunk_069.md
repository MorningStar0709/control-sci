# Example 2.5

Let $f(t) = t^2 + 2t$ . Find the increment and the derivative of the function $f(t)$ .

Solution: By definition, the increment $\Delta f$ is

$$
\begin{array}{l} \Delta f \triangleq f (t + \Delta t) - f (t), \\ = (t + \Delta t) ^ {2} + 2 (t + \Delta t) - (t ^ {2} + 2 t), \\ = 2 t \Delta t + 2 \Delta t + \dots + \text { higher   order   terms }, \\ = 2 (t + 1) \Delta t, \\ = \dot {f} (t) \Delta t. \tag {2.1.13} \\ \end{array}
$$

Here, $\dot{f}(t)=2(t+1)$ .

(b) Variation of a Functional: Consider the increment of a functional

$$\Delta J \triangleq J (x (t) + \delta x (t)) - J (x (t)). \tag {2.1.14}$$

Expanding $J(x(t) + \delta x(t))$ in a Taylor series, we get

$$
\begin{array}{l} \Delta J = J (x (t)) + \frac {\partial J}{\partial x} \delta x (t) + \frac {1}{2 !} \frac {\partial^ {2} J}{\partial x ^ {2}} (\delta x (t)) ^ {2} + \dots - J (x (t)) \\ = \frac {\partial J}{\partial x} \delta x (t) + \frac {1}{2 !} \frac {\partial^ {2} J}{\partial x ^ {2}} (\delta x (t)) ^ {2} + \dots \\ = \delta J + \delta^ {2} J + \dots , \tag {2.1.15} \\ \end{array}
$$

where,

$$\delta J = \frac {\partial J}{\partial x} \delta x (t) \quad \text { and } \quad \delta^ {2} J = \frac {1}{2 !} \frac {\partial^ {2} J}{\partial x ^ {2}} (\delta x (t)) ^ {2} \tag {2.1.16}$$

are called the first variation (or simply the variation) and the second variation of the functional J, respectively. The variation $\delta J$ of a functional J is the linear (or first order approximate) part (in $\delta x(t)$ ) of the increment $\Delta J$ . Figure 2.2 shows the relation between increment and the first variation of a functional.

![](image/249eacd7432e8ee259c924c100b34e03d60cf8abae287ab6e18ec767d46679e6.jpg)

<details>
<summary>line</summary>

| x(t) | J(x(t)) | J(x*(t)+δx(t)) |
| --- | --- | --- |
| 0 | - | - |
| x*(t) | - | - |
| x*(t)+δx(t) | δx(t) | δx(t) |
| >δx(t) | >δx(t) | >δx(t) |
</details>

Figure 2.2 Increment $\Delta J$ and the First Variation $\delta J$ of the Functional J
