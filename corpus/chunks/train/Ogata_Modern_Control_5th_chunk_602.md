where we choose the lower limit to be slightly above zero to avoid having overdamped systems. The smaller the upper limit, the harder it is to determine the coefficient $\boldsymbol { a } ^ { \prime } \mathbf { s } .$ In some cases, no combination of the $\boldsymbol { a } ^ { * } \boldsymbol { \mathrm { s } }$ may exist to satisfy the specification, so we must allow a higher upper limit for the maximum overshoot. We use MATLAB to search at least one set of the $\boldsymbol { a } ^ { * } \boldsymbol { \mathrm { s } }$ to satisfy the specification. As a practical computational matter, instead of searching for the a’s, we try to obtain acceptable closed-loop poles by searching a reasonable region in the left-half s plane for each closed-loop pole. Once we determine all closed-loop poles, then all coefficients $a _ { n } , a _ { n - 1 } , \ldots , a _ { 1 } , a _ { 0 }$ will be determined.

Determination of $G _ { c 2 }$ . Now that the coefficients of the transfer function $Y ( s ) / R ( s )$ are all known and $Y ( s ) / R ( s )$ is given by

$$\frac {Y (s)}{R (s)} = \frac {a _ {2} s ^ {2} + a _ {1} s + a _ {0}}{s ^ {n + 1} + a _ {n} s ^ {n} + a _ {n - 1} s ^ {n - 1} + \cdots + a _ {2} s ^ {2} + a _ {1} s + a _ {0}} \tag {8-4}$$

we have

$$
\begin{array}{l} \frac {Y (s)}{R (s)} = G _ {c 1} \frac {Y (s)}{D (s)} \\ = \frac {G _ {c 1} s K A (s)}{s B (s) + (\alpha s + \beta + \gamma s ^ {2}) K} \\ = \frac {G _ {c 1} s K A (s)}{s ^ {n + 1} + a _ {n} s ^ {n} + a _ {n - 1} s ^ {n - 1} + \cdots + a _ {2} s ^ {2} + a _ {1} s + a _ {0}} \\ \end{array}
$$

Since $G _ { c 1 }$ is a PID controller and is given by

$$G _ {c 1} = \frac {\alpha_ {1} s + \beta_ {1} + \gamma_ {1} s ^ {2}}{s} \frac {1}{A (s)}$$

$Y ( s ) / R ( s )$ can be written as

$$\frac {Y (s)}{R (s)} = \frac {K \left(\alpha_ {1} s + \beta_ {1} + \gamma_ {1} s ^ {2}\right)}{s ^ {n + 1} + a _ {n} s ^ {n} + a _ {n - 1} s ^ {n - 1} + \cdots + a _ {2} s ^ {2} + a _ {1} s + a _ {0}}$$

Therefore, we choose

$$K \gamma_ {1} = a _ {2}, \quad K \alpha_ {1} = a _ {1}, \quad K \beta_ {1} = a _ {0}$$

so that

$$G _ {c 1} = \frac {a _ {1} s + a _ {0} + a _ {2} s ^ {2}}{K s} \frac {1}{A (s)} \tag {8-5}$$

The response of this system to the unit-step reference input can be made to exhibit the maximum overshoot between the chosen upper and lower limits, such as

$$2 \% < \text { maximum overshoot } < 10 \%$$
