$$
\Delta_ {4} = \left| \begin{array}{c c c c} a _ {1} & a _ {3} & 0 & 0 \\ a _ {0} & a _ {2} & a _ {4} & 0 \\ 0 & a _ {1} & a _ {3} & 0 \\ 0 & a _ {0} & a _ {2} & a _ {4} \end{array} \right|
$$

For all the roots to have negative real parts, it is necessary and sufficient that succesive principal minors of $\Delta _ { 4 }$ be positive. The successive principal minors are

$$
\begin{array}{l} \Delta_ {1} = \left| a _ {1} \right| = 2 \\ \Delta_ {2} = \left| \begin{array}{c c} a _ {1} & a _ {3} \\ a _ {0} & a _ {2} \end{array} \right| = \left| \begin{array}{c c} 2 & 9 \\ 1 & 4 + K \end{array} \right| = 2 K - 1 \\ \Delta_ {3} = \left| \begin{array}{l l l} a _ {1} & a _ {3} & 0 \\ a _ {0} & a _ {2} & a _ {4} \\ 0 & a _ {1} & a _ {3} \end{array} \right| = \left| \begin{array}{c c c} 2 & 9 & 0 \\ 1 & 4 + K & 2 5 \\ 0 & 2 & 9 \end{array} \right| = 1 8 K - 1 0 9 \\ \end{array}
$$

For all principal minors to be positive, we require that $\Delta _ { i } ( i = 1 , 2 , 3 )$ be positive.Thus, we require

$$2 K - 1 > 01 8 K - 1 0 9 > 0$$

from which we obtain the region of K for stability to be

$$K > \frac {1 0 9}{1 8}$$

A–5–22. Explain why the proportional control of a plant that does not possess an integrating property (which means that the plant transfer function does not include the factor $1 / s )$ suffers offset in response to step inputs.

Solution. Consider, for example, the system shown in Figure 5–66.At steady state, if c were equal to a nonzero constant r, then $e = 0$ and $u = K e = 0$ , resulting in $c = 0$ , which contradicts the assumption that c=r=nonzero constant.

A nonzero offset must exist for proper operation of such a control system. In other words, at steady state, if e were equal to $r / ( 1 + K )$ , then $u = K r / ( 1 + K )$ and $c = K r / ( 1 + K )$ , which results in the assumed error signal $e = r / ( 1 + K )$ ). Thus the offset of $r / ( 1 + K )$ must exist in such a system.

![](image/98d596ebf2fd143428da1b623fee6a20e4c51a727d774d32c8620c9238f3f10c.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    r --> |+| sum
    sum --> e --> K --> u --> |1/(Ts+1)| c
    c --> |feedback| sum
```
</details>

Figure 5–66 Control system.

A–5–23. The block diagram of Figure 5–67 shows a speed control system in which the output member of the system is subject to a torque disturbance. In the diagram, $\varOmega _ { r } ( s ) , \varOmega ( s ) , T ( s )$ and, $D ( s )$ are the Laplace transforms of the reference speed, output speed, driving torque, and disturbance torque, respectively. In the absence of a disturbance torque, the output speed is equal to the reference speed.
