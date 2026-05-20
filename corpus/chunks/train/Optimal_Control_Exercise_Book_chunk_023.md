# Solution:

We can pick an arbitrary feasible direction $d \in \ R ^ { n }$ . Then $x ^ { * } + \alpha d \in D$ for all small enough $\alpha > 0$ . We can define a new function $g ( \alpha )$ as following:

$$g (\alpha) := f (x ^ {*} + \alpha d), \quad \alpha > 0 \tag {23}$$

Via the Taylor expansion, we obtain:

$$g (\alpha) = g (0) + g ^ {\prime} (0) \alpha + \frac {1}{2} g ^ {\prime \prime} (0) \alpha^ {2} + o \left(\alpha^ {2}\right) \tag {24}$$

In which the terms $g ^ { \prime } ( 0 )$ and $g ^ { \prime \prime } ( 0 )$ are, according to our hypotesis:

$$g ^ {\prime} (0) = \left\langle \nabla f \left(x ^ {*}\right), d \right\rangle \geq 0 \tag {25}\therefore g ^ {\prime} (0) \geq 0 \tag {26}$$

and (27)

$$g ^ {\prime \prime} (0) = d ^ {T} \nabla^ {2} f (x ^ {*}) d > 0 \tag {28}\therefore g ^ {\prime \prime} (0) > 0 \tag {29}$$

If the residual $o ( \alpha ^ { 2 } ) \ge 0$ , then we have:

$$g (\alpha) - g (0) = g ^ {\prime} (0) \alpha + \frac {1}{2} g ^ {\prime \prime} (0) \alpha^ {2} + o \left(\alpha^ {2}\right) > 0 \tag {30}$$

Thus implying

$$f (x ^ {*} + \alpha d) - f (x ^ {*}) > 0 \tag {31}$$

which implies that $x ^ { * }$ is a local minimum for f for every nonzero feasible direction d. We now need to show the same for the non-positive case.

If the residual $o ( \alpha ^ { 2 } ) \ < \ 0$ , there exists a small enough $\varepsilon > 0$ such that for all α satisfying $0 < \alpha < \varepsilon$ we have, following from the definition of small o:

$$\left| \frac {o \left(\alpha^ {2}\right)}{\alpha^ {2}} \right| < \frac {1}{2} g ^ {\prime \prime} (0) \tag {32}\left| o \left(\alpha^ {2} \right. \right| < \frac {1}{2} g ^ {\prime \prime} (0) \alpha^ {2} \tag {33}$$

$\mathrm { g i v e n ~ t h a t ~ } o ( \alpha ^ { 2 } ) < 0 ,$ (34)

$$o \left(\alpha^ {2}\right) > - \frac {1}{2} g ^ {\prime \prime} (0) \alpha^ {2} \tag {35}\therefore \frac {1}{2} g ^ {\prime \prime} (0) \alpha^ {2} + o \left(\alpha^ {2}\right) > 0 \tag {36}$$

Therefore, as in the previous case, we get

$$g (\alpha) - g (0) = g ^ {\prime} (0) \alpha + \frac {1}{2} g ^ {\prime \prime} (0) \alpha^ {2} + o \left(\alpha^ {2}\right) > 0 \tag {37}$$

Thus implying

$$f (x ^ {*} + \alpha d) - f (x ^ {*}) > 0 \tag {38}$$

which implies that $x ^ { * }$ is a local minimum for f for every nonzero feasible direction d.

We have thus proved that given the conditions $\langle \nabla f ( x ^ { * } ) , d \rangle \geq 0$ and $d ^ { T } \nabla ^ { 2 } f ( x ^ { * } ) d > 0 .$ , $x ^ { * }$ is a local minimum for f for every nonzero feasible direction d. 
