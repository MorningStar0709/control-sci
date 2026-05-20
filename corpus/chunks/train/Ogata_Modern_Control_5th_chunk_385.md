$$G _ {c} (s) = K _ {c} \left(\frac {s + \frac {1}{T _ {1}}}{s + \frac {\beta}{T _ {1}}}\right) \left(\frac {s + \frac {1}{T _ {2}}}{s + \frac {1}{\beta T _ {2}}}\right) = K _ {c} \frac {(T _ {1} s + 1) (T _ {2} s + 1)}{\left(\frac {T _ {1}}{\beta} s + 1\right) (\beta T _ {2} s + 1)}$$

where $\beta > 1$ . Then

$$
\begin{array}{l} K _ {v} = \lim _ {s \to 0} s G _ {c} (s) G (s) \\ = \lim _ {s \rightarrow 0} s \frac {K _ {c} (T _ {1} s + 1) (T _ {2} s + 1)}{\left(\frac {T _ {1}}{\beta} s + 1\right) (\beta T _ {2} s + 1)} \frac {1}{s (s + 1) (s + 5)} \\ = \frac {K _ {c}}{5} \\ \end{array}
$$

The specification that $K _ { v } = 5 0 \mathrm { s e c } ^ { - 1 }$ determines the value of $K _ { c } ,$ or

$$K _ {c} = 2 5 0$$

We now choose $T _ { 1 } = 1$ so that $s + \left( 1 / T _ { 1 } \right)$ will cancel the $( s + 1 )$ term of the plant. The lead portion then becomes

$$\frac {s + 1}{s + \beta}$$

For the lag portion of the lag–lead compensator we require

$$\left| \frac {s _ {1} + \frac {1}{T _ {2}}}{s _ {1} + \frac {1}{\beta T _ {2}}} \right| \div 1, \quad - 5 ^ {\circ} < \sqrt {\frac {s _ {1} + \frac {1}{T _ {2}}}{s _ {1} + \frac {1}{\beta T _ {2}}}} < 0 ^ {\circ}$$

where $s = s _ { 1 }$ is one of the dominant closed-loop poles. Noting these requirements for the lag portion of the compensator, at $s = s _ { 1 }$ , the open-loop transfer function becomes

$$G _ {c} \left(s _ {1}\right) G \left(s _ {1}\right) \div K _ {c} \left(\frac {s _ {1} + 1}{s _ {1} + \beta}\right) \frac {1}{s _ {1} \left(s _ {1} + 1\right) \left(s _ {1} + 5\right)} = K _ {c} \frac {1}{s _ {1} \left(s _ {1} + \beta\right) \left(s _ {1} + 5\right)}$$

Then at $s = s _ { 1 } .$ , the following magnitude and angle conditions must be satisfied:

$$\left| K _ {c} \frac {1}{s _ {1} (s _ {1} + \beta) (s _ {1} + 5)} \right| = 1 \tag {6-32}\underline {{K _ {c} \frac {1}{s _ {1} (s _ {1} + \beta) (s _ {1} + 5)}}} = \pm 1 8 0 ^ {\circ} (2 k + 1) \tag {6-33}$$

where $k = 0 , 1 , 2 , \ldots$ . In Equations (6–32) and (6–33), $\beta$ and $s _ { 1 }$ are unknowns. Since the damping ratio $\zeta$ of the dominant closed-loop poles is specified as 0.5, the closed-loop pole $s = s _ { 1 }$ can be written as

$$s _ {1} = - x + j \sqrt {3} x$$

where x is as yet undetermined.

Notice that the magnitude condition, Equation (6–32), can be rewritten as

$$\left| \frac {K _ {c}}{(- x + j \sqrt {3} x) (- x + \beta + j \sqrt {3} x) (- x + 5 + j \sqrt {3} x)} \right| = 1$$

Noting that $K _ { c } = 2 5 0 \AA$ we have,

$$x \sqrt {(\beta - x) ^ {2} + 3 x ^ {2}} \sqrt {(5 - x) ^ {2} + 3 x ^ {2}} = 1 2 5 \tag {6-34}$$

The angle condition, Equation (6–33), can be rewritten as
