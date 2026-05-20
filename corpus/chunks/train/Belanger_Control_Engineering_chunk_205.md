We also need sensitivity expressions to complete our survey of basics. Let

$$T = H _ {d} = \frac {F P}{1 + F P}. \tag {4.32}$$

Then, from Equation 4.12,

$$
\begin{array}{l} \text { sensitivity } = S = \frac {\partial T}{\partial P} \frac {P}{T} \\ = \frac {(1 + F P) F - F ^ {2} P}{(1 + F P) ^ {2}} \cdot P \cdot \frac {1 + F P}{F P} \\ = \frac {1}{1 + F P}. \tag {4.33} \\ \end{array}
$$

The sensitivity, $S(s)$ , is seen to be small if the loop gain is large in magnitude. For large loop gain FP, this means that changes in the plant P do not significantly affect the closed-loop transfer function T. This is not surprising, in hindsight. For example, let F = 1 and P = 100. Then

$$T = \frac {1 0 0}{1 0 1} = 0. 9 9 0 0 9 9.$$

Now try

$$
\begin{array}{l} F = 1, P = 2 0 0: \\ T = \frac {2 0 0}{2 0 1} = \frac {1 0 0}{1 0 0 . 5} = 0. 9 9 5 0 2. \\ \end{array}
$$

Despite a doubling of $P, T$ changes by only about half a percent. As long as $|FP| \gg 1$ , the denominator of $T$ will be close to $FP$ and $T$ will be near 1.

By comparison of Equations 4.29 and 4.33, the sensitivity S is equal to $H_{wd}$ , the response to disturbance. Thus, making S small simultaneously achieves two positive results: it desensitizes the system and produces disturbance attenuation.

From Equations 4.32 and 4.33,

$$T (s) + S (s) = \frac {F P}{1 + F P} + \frac {1}{1 + F P} = 1. \tag {4.34}$$

Equation 4.34 is the reason $T(s)$ is called the complementary sensitivity:

Finally, note that Equations 4.26 and 4.27 can be written

$$y (s) = T (s) y _ {d} (s) + S (s) d (s) \tag {4.35}e (s) = S (s) y _ {d} (s) - S (s) d (s). \tag {4.36}$$

Since $H_{d} = T$ and $H_{wd} = S$ , the design objective is to make $T \approx 1$ and $S$ small over the desired passband. Fortunately, since $S = 1 - T$ , the two desiderata are compatible.

It is useful to think of closed-loop control in terms of $T$ and $S$ . Given $S$ and $T = 1 - S$ , the compensator $F$ is easily derived as follows. From Equations 4.32 and 4.33,

$$1 + F P = \frac {1}{S}F = \frac {1}{P} \left(\frac {1}{S} - 1\right) = \frac {1}{P S} (1 - S)$$

or

$$F (s) = \frac {T (s)}{S (s) P (s)}. \tag {4.37}$$

This result implies that a design may be carried out by specifying $S$ (or $T$ ). Equation 4.38 then finds, uniquely, a controller that yields the desired $S$ (or $T$ ).
