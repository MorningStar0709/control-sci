```mermaid
graph LR
    u --> |+| sum
    sum --> |s+z / (s+p)| | transfer["1/(s²)"]
    transfer --> y
    y --> |feedback| sum
```
</details>

Figure 2–35 Control system.

B–2–9. Consider the system described by

$$\ddot {y} + 3 \dot {y} + 2 \dot {y} = u$$

Derive a state-space representation of the system.

B–2–10. Consider the system described by

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} - 4 & - 1 \\ 3 & - 1 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{c} 1 \\ 1 \end{array} \right] u

y = \left[ \begin{array}{c c} 1 & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right]
$$

Obtain the transfer function of the system.

B–2–11. Consider a system defined by the following statespace equations:

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} - 5 & - 1 \\ 3 & - 1 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{c} 2 \\ 5 \end{array} \right] u

y = \left[ \begin{array}{c c} 1 & 2 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right]
$$

Obtain the transfer function G(s) of the system.

B–2–12. Obtain the transfer matrix of the system defined by

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \end{array} \right] = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - 2 & - 4 & - 6 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right] + \left[ \begin{array}{c c} 0 & 0 \\ 0 & 1 \\ 1 & 0 \end{array} \right] \left[ \begin{array}{c} u _ {1} \\ u _ {2} \end{array} \right]

\left[ \begin{array}{c} y _ {1} \\ y _ {2} \end{array} \right] = \left[ \begin{array}{c c c} 1 & 0 & 0 \\ 0 & 1 & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \end{array} \right]
$$

B–2–13. Linearize the nonlinear equation

$$z = x ^ {2} + 8 x y + 3 y ^ {2}$$

in the region defined by $2 \leq x \leq 4 , 1 0 \leq y \leq 1 2$ .

B–2–14. Find a linearized equation for

$$y = 0. 2 x ^ {3}$$

about a point x=2.

![](image/f289aeb25d703079a0f1e2782394a0cc5541fbadee2e19ffef6bd880a163e89b.jpg)

<details>
<summary>text_image</summary>

3
</details>
