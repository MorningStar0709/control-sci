$$\inf _ {k _ {0} \in [ k _ {1}, k _ {2} ]} \sup _ {k \in [ k _ {1}, k _ {2} ]} \delta_ {g} (P, P _ {0}) = \frac {\sqrt {k _ {2}} - \sqrt {k _ {1}}}{\sqrt {k _ {2}} + \sqrt {k _ {1}}}.$$

To answer question $\mathrm { ( b ) }$ , we note that by Theorem 17.3, a family of plants satisfying $\delta _ { g } ( P , P _ { 0 } ) \leq r$ with $P _ { 0 } = k _ { 0 } / ( s + 1 )$ is stabilizable a priori by any controller satisfying $b _ { P _ { 0 } , K } = b _ { \mathrm { o b t } } ( P _ { 0 } )$ if, and only $\mathrm { i f } , r < b _ { P _ { 0 } , K }$ . Since $P _ { 0 } = N _ { 0 } / M _ { 0 }$ with

$$N _ {0} = \frac {k _ {0}}{s + \sqrt {1 + k _ {0} ^ {2}}}, M _ {0} = \frac {s - 1}{s + \sqrt {1 + k _ {0} ^ {2}}}$$

is a normalized coprime factorization, it is easy to show that

$$
\left\| \left[ \begin{array}{l} N _ {0} \\ M _ {0} \end{array} \right] \right\| _ {H} = \frac {\sqrt {k _ {0} ^ {2} + (1 - \sqrt {1 + k _ {0} ^ {2}}) ^ {2}}}{2 \sqrt {1 + k _ {0} ^ {2}}}
$$

and

$$b _ {\mathrm{obt}} (P _ {0}) = \sqrt {\frac {1}{2} \left(1 + \frac {1}{\sqrt {1 + k _ {0} ^ {2}}}\right)}.$$

Hence we need to find a $k _ { 0 }$ such that

$$b _ {\mathrm{obt}} (P _ {0}) \geq \max \left\{\frac {k _ {0} - k _ {1}}{k _ {0} + k _ {1}}, \frac {k _ {2} - k _ {0}}{k _ {2} + k _ {0}} \right\};$$

that is,

$$\sqrt {\frac {1}{2} \left(1 + \frac {1}{\sqrt {1 + k _ {0} ^ {2}}}\right)} \geq \max \left\{\frac {k _ {0} - k _ {1}}{k _ {0} + k _ {1}}, \frac {k _ {2} - k _ {0}}{k _ {2} + k _ {0}} \right\}$$

for a largest possible $k _ { 2 }$ . The optimal $k _ { 0 }$ is given by the solution of the equation:

$$\sqrt {\frac {1}{2} \left(1 + \frac {1}{\sqrt {1 + k _ {0} ^ {2}}}\right)} = \frac {k _ {0} - k _ {1}}{k _ {0} + k _ {1}}$$

and the largest $k _ { 2 } = k _ { 0 } ^ { 2 } / k _ { 1 }$ . For example, if $k _ { 1 } = 1$ , then $k _ { 0 } = 7 . 1 4 7$ and $k _ { 2 } = 5 1 . 0 7 9 3$ .

In general, given a family of plant P , it is not easy to see how to choose a best nominal model $P _ { 0 }$ such that (a) or (b) is true. This is still a very important open question.
