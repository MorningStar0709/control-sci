$$
A = \left( \begin{array}{c c} - \frac {a}{y _ {0}} & - y _ {0} \\ - \gamma \frac {a}{\alpha + y _ {0} ^ {2}} & 1 - \gamma \frac {y _ {0} ^ {2}}{\alpha + y _ {0} ^ {2}} \end{array} \right) \tag {6.10}
$$

This matrix has the characteristic polynomial

$$z ^ {2} + a _ {1} z + a _ {2}$$

![](image/f193ae48a6927a31dd4dcbf584c27f3f0db43ef67aab8b96c2962851026d97e9.jpg)

<details>
<summary>text_image</summary>

y
2(α + y₀²)/y₀²
-y₀
y₀
a
</details>

Figure 6.1 Stability region for the closed-loop system.

where

$$a _ {1} = \frac {a}{y _ {0}} - 1 + \gamma \frac {y _ {0} ^ {2}}{\alpha + y _ {0} ^ {2}}a _ {2} - - \frac {a}{y _ {0}}$$

It follows from the stability criterion for discrete-time systems (Schur-Cohn) that the characteristic polynomial has all its roots inside the unit disc if

$$a _ {2} < 1a _ {2} - a _ {1} + 1 > 0a _ {2} + a _ {1} + 1 > 0$$

Inserting the expressions for $a_{1}$ and $a_{2}$ into these conditions gives

(i) $\frac{a}{y_0} > -1$

(ii) $\gamma < 2\frac{(1 - a / y_0)(\alpha + y_0^2)}{y_0^2}$ (6.11)

(iii) $\gamma > 0$

The equilibrium is stable if parameters $a$ and $\gamma$ are inside the triangular region shown in Fig. 6.1. To have a stable equilibrium, it must thus be required that the magnitude of the disturbance $a$ is less than the magnitude of the command signal $y_0$ . In addition the adaptation gain $\gamma$ should not be too large. It is interesting to see the consequences of unmodeled dynamics. If there are no unmodeled dynamics ( $a = 0$ ), then the condition for local stability of the equilibrium becomes

$$0 < \gamma < 2 \frac {\alpha + y _ {0} ^ {2}}{y _ {0} ^ {2}}$$

Stability is thus guaranteed simply by choosing a reasonable value of $\gamma$ .
