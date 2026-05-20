# 1.5.3 Range of Approximation

We have seen that linearization works in the neighborhood of the linearization point. Here we will dive deeper into what we mean by works and neighborhood.

First we must dene our requirement for accuracy (i.e. how much error we can have while the approximation still works). Often this is dictated by some external requirement. For example,

The linearized model shall have less than 10% error.

By this we mean that if we dene a linear function ˆf(x) which is a linear approximation of a non-linear function, f (x), about the point x = x0 then

$$\frac {| f (x) - \hat {f} (x) |}{f (x)} < 0. 1 0$$

Second, we must dene neighborhood. By this we mean the range of x values for which the approximation is good enough (i.e. works). Suppose we have

$$x _ {m i n} < x _ {0} < x _ {m a x}$$

such that

$$\frac {| f (x _ {m i n}) - \hat {f} (x _ {m i n}) |}{f (x _ {m i n})} = 0. 1 0$$

and
