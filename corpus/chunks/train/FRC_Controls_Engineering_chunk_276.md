# 9.3.9 Conditional probability density functions

Let us assume that we know the joint PDF $p ( x , y )$ and the exact value for $y .$ . The conditional PDF gives the probability of x in the interval $[ x , x + d x ]$ for the given value y. The probability of x given y is denoted by $p ( x | y )$ .

If $p ( x , y )$ is known, then we also know $p ( x , y = y ^ { * } )$ ). However, note that the latter is not the conditional density $p ( x | y ^ { * } )$ , instead

$$C (y ^ {*}) = \int_ {- \infty} ^ {\infty} p (x, y = y ^ {*}) d xp (x | y ^ {*}) = \frac {1}{C (y ^ {*})} p (x, y = y ^ {*})$$

The scale factor $\frac { 1 } { C ( y ^ { * } ) }$ is used to scale the area under the PDF to 1.
