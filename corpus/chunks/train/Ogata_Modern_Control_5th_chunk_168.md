$$\frac {P _ {c} (s)}{E (s)} = \frac {\frac {b}{a + b} K}{1 + K \frac {a}{a + b} \frac {A}{k _ {s}} \left(\frac {T _ {i} s}{T _ {i} s + 1}\right) \left(\frac {1}{T _ {d} s + 1}\right)}$$

For a practical controller, under normal operation $\left| K a A T _ { i } s / [ ( a + b ) k _ { s } ( T _ { i } s + 1 ) ( T _ { d } s + 1 ) ] \right|$ is very much greater than unity and $T _ { i } \gg T _ { d }$ Therefore, the transfer function can be simplified as. follows:

$$
\begin{array}{l} \frac {P _ {c} (s)}{E (s)} \doteq \frac {b k _ {s} \left(T _ {i} s + 1\right) \left(T _ {d} s + 1\right)}{a A T _ {i} s} \\ = \frac {b k _ {s}}{a A} \left(\frac {T _ {i} + T _ {d}}{T _ {i}} + \frac {1}{T _ {i} s} + T _ {d} s\right) \\ \doteq K _ {p} \left(1 + \frac {1}{T _ {i} s} + T _ {d} s\right) \\ \end{array}
$$

where

$$K _ {p} = \frac {b k _ {s}}{a A}$$

Thus the controller shown in Figure 4–30 is a proportional-plus-integral-plus-derivative one.

If the resistance $R _ { d }$ is removed, or $R _ { d } = 0$ , the action becomes that of a proportional-plusintegral controller.

![](image/e1cd3086a96cf97a076ab2d4653c3867acb9042dd89d872015d98807f0098e83.jpg)

<details>
<summary>flowchart</summary>
