# Example 9.5

Now we'll consider a general system with a gain factor, K, and n poles at the origin in the controller, as well as a general input (i.e. x(t) = Btm−1, X(s) = B/sm) where, m = 1 means a step input, m = 2 means a ramp input, m = 3 means a parabolic input, etc. n is the System Type.

$$C = \frac {K}{s ^ {n}}, \qquad P = \frac {5 0}{s + 1 0}, \qquad H = 1, \qquad x (t) = B t ^ {m + 1}, \qquad X (s) = \frac {B}{s ^ {m}}\mathrm{SSE} = \lim _ {s \rightarrow 0} \frac {s}{s ^ {m}} \frac {B}{\left(1 + \frac {K}{s ^ {n}} \frac {5 0}{(s + 1 0)}\right)}\lim _ {s \to 0} \frac {1}{s ^ {m - 1}} \frac {B s ^ {n} (s + 1 0)}{(s ^ {n} (s + 1 0) + 5 0 K)} = \lim _ {s \to 0} \frac {B s ^ {n} (s + 1 0)}{s ^ {n + m} + 1 0 s ^ {n + m - 1} + 5 0 K s ^ {m - 1}}$$

For this limit to be nite as s → 0, we need to have no remaining powers of s in the denominator after cancelation. Thus if

$$n > m - 1$$

the error if zero. If n = m − 1 we have after cancellation

$$\mathrm{SSE} = \lim _ {s \rightarrow 0} \frac {B s ^ {n} (s + 1 0)}{s ^ {2 n - 1} + 1 0 s ^ {2 n - 2} + 5 0 K s ^ {n}} = \frac {1 0 B}{5 0 K}$$

All of the relationships illustrated by these examples can be summed up in Table 9.1. It is worth remembering that SSE only applies after transients (due to the non-zero poles) are over. Such transients are illustrated for some typical situations in Figure 9.3
