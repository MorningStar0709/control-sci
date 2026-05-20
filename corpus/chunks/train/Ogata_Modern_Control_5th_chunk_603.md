The response of the system to the ramp reference input or acceleration reference input can be made to exhibit no steady-state error. The characteristic of the system of Equation (8–4) is that it generally exhibits a short settling time. If we wish to further shorten the settling time, then we need to allow a larger maximum overshoot—for example,

$$2 \% < \text { maximum overshoot } < 20 \%$$

The controller $G _ { c 2 }$ can now be determined from Equations (8–3) and (8–5). Since

$$G _ {c 1} + G _ {c 2} = \frac {\alpha s + \beta + \gamma s ^ {2}}{s} \frac {1}{A (s)}$$

we have

$$
\begin{array}{l} G _ {c 2} = \left[ \frac {\alpha s + \beta + \gamma s ^ {2}}{s} - \frac {a _ {1} s + a _ {0} + a _ {2} s ^ {2}}{K s} \right] \frac {1}{A (s)} \\ = \frac {(K \alpha - a _ {1}) s + (K \beta - a _ {0}) + (K \gamma - a _ {2}) s ^ {2}}{K s} \frac {1}{A (s)} \tag {8-6} \\ \end{array}
$$

The two controllers $G _ { c 1 }$ and $G _ { c 2 }$ can be determined from Equations (8–5) and (8–6).
