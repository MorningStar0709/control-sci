# 11.5 Tustin's Method

Suppose we have a continuous time system (i.e. a Laplace Transform transfer function), $H ( s )$ . Arnold Tustin developed the following way to derive a Z-transform transfer function which is a digital approximation to $H ( s )$ :

$$H (z) = H (s) \big | _ {s = \frac {2 (z - 1)}{T (z + 1)}}$$

Where T is the sampling time. In words, to generate a discrete version of $H ( s )$ , substitute $\frac { 2 ( z - 1 ) } { T ( z + 1 ) }$ for s in $H ( s )$ .
