# Solution

Because the two random variables are independent, the probability of drawing a sample with values $( x _ { i } , y _ { j } )$ is given by

$$p _ {s a} (x _ {i}, y _ {j}) = p _ {s a} (x _ {i}) p _ {\mathrm{sa}} (y _ {j}) = p _ {\xi} (x _ {i}) p _ {\eta} (y _ {j}) = p _ {\xi , \eta} (x _ {i}, y _ {j})$$

Denote the samples as $\boldsymbol { z } _ { k } = ( x _ { i ( k ) } , y _ { j ( k ) } )$ . We have for all three choices

$$p _ {\mathrm{sa}} (z _ {k}) = p _ {\xi , \eta} (z _ {k}) \quad k = 1, \dots , s \tag {4.44}$$

(a) For this case,

$$
\begin{array}{l} i (k) = \operatorname{mod} (k - 1, s _ {x}) + 1 \quad j (k) = \operatorname{ceil} (k / s _ {x}) \\ w _ {k} = \frac {1}{s _ {x} s _ {y}}, \quad k = 1, \ldots , s _ {x} s _ {y} \\ \end{array}
$$

in which ceil(x) is the smallest integer not less than x.
