# 9.2.3 Steady State Error Summary

We've seen examples of how changing the system type or changing the input can make a big dierence in the amount of steady state error. You might even notice a pattern in the examples above relating the input type (the power of s in the Laplace transform of the input signal) and the system type to the nature of the SSE. To see this relationship, let's take a closer look at Example 9.4.

Writing out the limit again without canceling any terms,

$$\mathrm{SSE} = \lim _ {s \rightarrow 0} \frac {s B s (s + 1 0)}{s ^ {2} (s (s + 1 0) + 5 0 0)}$$

We have two s's on the top. One comes from the nal value theorem, and the second one from the denominator of C(s). On the bottom, we have s2, which comes from the ramp input. The FVT term and the C(s) denominator term combine to cancel the s2 from the ramp input. Thus, if the input is

$$X (s) = \frac {A}{s ^ {n}}$$

then we need at least n − 1 poles at the origin in the combined controller and plant (again assuming H = 1).
