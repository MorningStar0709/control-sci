$$\tilde {x} ^ {0} (z) = \overline {{x}} ^ {0} (\overline {{y}} ^ {0} (z)) \qquad \tilde {w} ^ {0} (z) = \overline {{w}} ^ {0} (\tilde {x} ^ {0} (z)) = \overline {{w}} ^ {0} (\overline {{x}} ^ {0} (\overline {{y}} ^ {0} (z)))$$

For the reader interested in trying some exercises to reinforce the concepts of DP, Exercise 1.15 considers finding the function $\tilde { \boldsymbol { w } } ^ { 0 } ( z )$ with backward DP instead of forward DP as we just did here. Exercise C.1 discusses showing that the nested optimizations indeed give the same answer as simultaneous optimization over all decision variables.

Finally, if we optimize over all four variables, including the one considered as a fixed parameter in the two versions of DP we used, then we have two equivalent ways to express the value of the complete optimization

$$\min _ {w, x, y, z} f (w, x) + g (x, y) + h (y, z) = \min _ {w} \underline {{f}} ^ {0} (w) = \min _ {z} \overline {{h}} ^ {0} (z)$$

The result in the next example proves useful in combining quadratic functions to solve the LQ problem.
