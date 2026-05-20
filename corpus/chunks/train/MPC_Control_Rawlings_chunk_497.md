# 4.7 Particle Filtering

Letting $\eta \mathrm { { s } }$ sampled density be $\{ y _ { i } , \overline { { w } } _ { i } \}$ , and using $\xi \mathbf { s }$ sampled density give

$$\sum_ {i = 1} ^ {s} \overline {{w}} _ {i} g (y _ {i}) = \sum_ {i = 1} ^ {s} w _ {i} g (f (x _ {i}))$$

and setting ${ \overline { { w } } } _ { i } = w _ { i } , y _ { i } = f ( x _ { i } ) , i = 1 , \dots , s$ achieves equality for all $g ( \cdot )$ , and we have established the result. The difference between the noninvertible and invertible cases is that we do not have a method to obtain samples of $\xi$ from samples of $\eta$ in the noninvertible case. We can transform the sampled density in only one direction, from $p _ { \xi }$ to $p _ { \eta }$ .
