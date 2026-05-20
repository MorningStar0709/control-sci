# Exercise 1.15: Are we going forward or backward today?

In the chapter we derived the solution to

$$\min _ {w, x, y} f (w, x) + g (x, y) + h (y, z)$$

in which z is a fixed parameter using forward dynamic programming (DP)

$$
\begin{array}{l} \overline {{y}} ^ {0} (z) \\ \tilde {x} ^ {0} (z) = \overline {{x}} ^ {0} (\overline {{y}} ^ {0} (z)) \\ \tilde {w} ^ {0} (z) = \overline {{w}} ^ {0} (\overline {{x}} ^ {0} (\overline {{y}} ^ {0} (z))) \\ \end{array}
$$

(a) Solve for optimal w as a function of z using backward DP.

(b) Is forward or backward DP more efficient if you want optimal w as a function of z?
