# 9.5.3 Single noisy observations: a Gaussian case

$$p (z _ {1} | x) = \frac {1}{\sigma \sqrt {2 \pi}} e ^ {- \frac {1}{2} \left(\frac {z _ {1} - x}{\sigma}\right) ^ {2}} \quad \mathrm{and} \quad p (x) = \frac {1}{\sigma_ {0} \sqrt {2 \pi}} e ^ {- \frac {1}{2} \left(\frac {x - x _ {0}}{\sigma_ {0}}\right) ^ {2}}$$

$z _ { 1 } , x _ { 0 } , \sigma ^ { 2 }$ , and $\sigma _ { 0 } ^ { 2 }$ are given.

$$
\begin{array}{l} p (x | z _ {1}) = \frac {p (x , z _ {1})}{p (z _ {1})} \\ p (x | z _ {1}) = \frac {p (z _ {1} | x) p (x)}{p (z _ {1})} \\ p (x | z _ {1}) = \frac {1}{C} p (z _ {1} | x) p (x) \\ p (x | z _ {1}) = \frac {1}{C} \frac {1}{\sigma \sqrt {2 \pi}} e ^ {- \frac {1}{2} \left(\frac {z _ {1} - x}{\sigma}\right) ^ {2}} \frac {1}{\sigma_ {0} \sqrt {2 \pi}} e ^ {- \frac {1}{2} \left(\frac {x - x _ {0}}{\sigma_ {0}}\right) ^ {2}} \\ \end{array}
$$

Absorb the leading coefficients of the two probability distributions into a new constant $C _ { 1 }$ .

$$p (x | z _ {1}) = \frac {1}{C _ {1}} e ^ {- \frac {1}{2} \left(\frac {z _ {1} - x}{\sigma}\right) ^ {2}} e ^ {- \frac {1}{2} \left(\frac {x - x _ {0}}{\sigma_ {0}}\right) ^ {2}}$$

Combine the exponents.

$$p (x | z _ {1}) = \frac {1}{C _ {1}} e ^ {- \frac {1}{2} \left(\frac {(z _ {1} - x) ^ {2}}{\sigma^ {2}} + \frac {(x - x _ {0}) ^ {2}}{\sigma_ {0} ^ {2}}\right)}$$

Expand the exponent into separate terms.

$$p (x | z _ {1}) = \frac {1}{C _ {1}} e ^ {- \frac {1}{2} \left(\frac {z _ {1} ^ {2}}{\sigma^ {2}} - \frac {2 z _ {1} x}{\sigma^ {2}} + \frac {x ^ {2}}{\sigma^ {2}} + \frac {x ^ {2}}{\sigma_ {0} ^ {2}} - \frac {2 x x _ {0}}{\sigma_ {0} ^ {2}} + \frac {x _ {0} ^ {2}}{\sigma_ {0} ^ {2}}\right)}$$

Multiply in σ2 $\frac { \sigma ^ { 2 } } { \sigma ^ { 2 } }$ or $\frac { \sigma _ { 0 } ^ { 2 } } { \sigma _ { 0 } ^ { 2 } }$ as appropriate to give all terms a denominator of $\sigma ^ { 2 } \sigma _ { 0 } ^ { 2 }$

$$p (x | z _ {1}) = \frac {1}{C _ {1}} e ^ {- \frac {1}{2} \left(\frac {\sigma_ {0} ^ {2} z _ {1} ^ {2}}{\sigma^ {2} \sigma_ {0} ^ {2}} - 2 \frac {\sigma_ {0} ^ {2} z _ {1}}{\sigma^ {2} \sigma_ {0} ^ {2}} x + \frac {\sigma_ {0} ^ {2}}{\sigma^ {2} \sigma_ {0} ^ {2}} x ^ {2} + \frac {\sigma^ {2}}{\sigma^ {2} \sigma_ {0} ^ {2}} x ^ {2} - 2 \frac {\sigma^ {2} x _ {0}}{\sigma^ {2} \sigma_ {0} ^ {2}} x + \frac {\sigma^ {2} x _ {0} ^ {2}}{\sigma^ {2} \sigma_ {0} ^ {2}}\right)}$$

Reorder terms in the exponent.
