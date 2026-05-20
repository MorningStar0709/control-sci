$$
\begin{array}{l} \left\lfloor K _ {c} \frac {1}{(- x + j \sqrt {3} x) (- x + \beta + j \sqrt {3} x) (- x + 5 + j \sqrt {3} x)} \right. \\ = - 1 2 0 ^ {\circ} - \tan^ {- 1} \left(\frac {\sqrt {3} x}{- x + \beta}\right) - \tan^ {- 1} \left(\frac {\sqrt {3} x}{- x + 5}\right) = - 1 8 0 ^ {\circ} \\ \end{array}
$$

or

$$\tan^ {- 1} \left(\frac {\sqrt {3} x}{- x + \beta}\right) + \tan^ {- 1} \left(\frac {\sqrt {3} x}{- x + 5}\right) = 6 0 ^ {\circ} \tag {6-35}$$

We need to solve Equations (6–34) and (6–35) for $\beta$ and x. By several trial-and-error calculations, it can be found that

$$\beta = 1 6. 0 2 5, \quad x = 1. 9 0 5 4$$

Thus

$$s _ {1} = - 1. 9 0 5 4 + j \sqrt {3} (1. 9 0 5 4) = - 1. 9 0 5 4 + j 3. 3 0 0 2$$

The lag portion of the lag–lead compensator can be determined as follows: Noting that the pole and zero of the lag portion of the compensator must be located near the origin, we may choose

$$\frac {1}{\beta T _ {2}} = 0. 0 1$$

That is,

$$\frac {1}{T _ {2}} = 0. 1 6 0 2 5 \quad \text { or } \quad T _ {2} = 6. 2 5$$

With the choice of $T _ { 2 } = 6 . 2 5$ we find,

$$
\begin{array}{l} \left| \frac {s _ {1} + \frac {1}{T _ {2}}}{s _ {1} + \frac {1}{\beta T _ {2}}} \right| = \left| \frac {- 1 . 9 0 5 4 + j 3 . 3 0 0 2 + 0 . 1 6 0 2 5}{- 1 . 9 0 5 4 + j 3 . 3 0 0 2 + 0 . 0 1} \right| \\ = \left| \frac {- 1 . 7 4 5 1 5 + j 3 . 3 0 0 2}{- 1 . 8 9 0 5 4 + j 3 . 3 0 0 2} \right| = 0. 9 8 \div 1 \tag {6-36} \\ \end{array}
$$

and

$$
\begin{array}{l} \left\lfloor \frac {s _ {1} + \frac {1}{T _ {2}}}{s _ {1} + \frac {1}{\beta T _ {2}}} = \right. \left\lfloor \frac {- 1 . 9 0 5 4 + j 3 . 3 0 0 2 + 0 . 1 6 0 2 5}{- 1 . 9 0 5 4 + j 3 . 3 0 0 2 + 0 . 0 1} \right. \\ = \tan^ {- 1} \left(\frac {3 . 3 0 0 2}{- 1 . 7 4 5 1 5}\right) - \tan^ {- 1} \left(\frac {3 . 3 0 0 2}{- 1 . 8 9 0 5 4}\right) = - 1. 9 3 7 ^ {\circ} \tag {6-37} \\ \end{array}
$$

Since

$$- 5 ^ {\circ} < - 1. 9 3 7 ^ {\circ} < 0 ^ {\circ}$$

our choice of $T _ { 2 } = 6 . 2 5$ is acceptable. Then the lag–lead compensator just designed can be written as

$$G _ {c} (s) = 2 5 0 \left(\frac {s + 1}{s + 1 6 . 0 2 5}\right) \left(\frac {s + 0 . 1 6 0 2 5}{s + 0 . 0 1}\right)$$

Therefore, the compensated system has the following open-loop transfer function:

$$G _ {c} (s) G (s) = \frac {2 5 0 (s + 0 . 1 6 0 2 5)}{s (s + 0 . 0 1) (s + 5) (s + 1 6 . 0 2 5)}$$

A root-locus plot of the compensated system is shown in Figure 6–91(a). An enlarged root-locus plot near the origin is shown in Figure 6–91(b).

The closed loop transfer function becomes

$$\frac {C (s)}{R (s)} = \frac {2 5 0 (s + 0 . 1 6 0 2 5)}{s (s + 0 . 0 1) (s + 5) (s + 1 6 . 0 2 5) + 2 5 0 (s + 0 . 1 6 0 2 5)}$$

The closed-loop poles are located at

$$s = - 1. 8 3 0 8 \pm j 3. 2 3 5 9s = - 0. 1 6 8 4s = - 1 7. 2 0 5$$
