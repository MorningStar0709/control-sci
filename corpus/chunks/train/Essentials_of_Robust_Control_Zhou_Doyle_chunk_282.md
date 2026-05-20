$$\mu_ {\Delta} (G (j \omega)) \leq \sqrt {\kappa (W _ {1} ^ {- 1} W _ {d})} (\| W _ {2} T _ {o} W _ {1} \| + \| W _ {e} S _ {o} W _ {d} \|).$$

Note that this sufficient condition is not easy to get from the approach taken in Chapter 8 and is potentially less conservative than the bounds derived there.

Next we consider the skewed specification problem, but first the following lemma is needed in the sequel.

Lemma 10.9 Suppose $\overline { { \sigma } } = \sigma _ { 1 } \geq \sigma _ { 2 } \geq . . . \geq \sigma _ { m } = \underline { { \sigma } } > 0$ , then

$$\inf _ {d \in \mathbb {R} _ {+}} \max _ {i} \left\{(d \sigma_ {i}) ^ {2} + \frac {1}{(d \sigma_ {i}) ^ {2}} \right\} = \frac {\overline {{\sigma}}}{\underline {{\sigma}}} + \frac {\underline {{\sigma}}}{\overline {{\sigma}}}.$$

Proof. Consider a function $y = x + 1 / x ;$ then $y$ is a convex function and the maximization over a closed interval is achieved at the boundary of the interval. Hence for any fixed d

$$\max _ {i} \left\{(d \sigma_ {i}) ^ {2} + \frac {1}{(d \sigma_ {i}) ^ {2}} \right\} = \max \left\{(d \overline {{\sigma}}) ^ {2} + \frac {1}{(d \overline {{\sigma}}) ^ {2}}, (d \underline {{\sigma}}) ^ {2} + \frac {1}{(d \underline {{\sigma}}) ^ {2}} \right\}.$$

Then the minimization over d is obtained iff

$$(d \overline {{\sigma}}) ^ {2} + \frac {1}{(d \overline {{\sigma}}) ^ {2}} = (d \underline {{\sigma}}) ^ {2} + \frac {1}{(d \underline {{\sigma}}) ^ {2}},$$

which gives $\begin{array} { r } { d ^ { 2 } = \frac { 1 } { \overline { { \sigma } } _ { \mathrm { ~ } \underline { { \sigma } } } } } \end{array}$ . The result then follows from substituting d.

Example 10.6 As another example, consider again the skewed specification problem from Chapter 8. Then the corresponding G matrix is given by

$$
G = \left[ \begin{array}{c c} - W _ {2} T _ {i} W _ {1} & - W _ {2} K S _ {o} W _ {d} \\ W _ {e} S _ {o} P W _ {1} & W _ {e} S _ {o} W _ {d} \end{array} \right].
$$

So the robust performance specification is satisfied iff

$$
\mu_ {\boldsymbol {\Delta}} (G (j \omega)) = \inf _ {d _ {\omega} \in \mathbb {R} _ {+}} \overline {{\sigma}} \left(\left[ \begin{array}{c c} - W _ {2} T _ {i} W _ {1} & - d _ {\omega} W _ {2} K S _ {o} W _ {d} \\ \frac {1}{d _ {\omega}} W _ {e} S _ {o} P W _ {1} & W _ {e} S _ {o} W _ {d} \end{array} \right]\right) \leq 1
$$

for all $\omega \ge 0$ . As in the last example, an upper-bound can be obtained by taking

$$d _ {\omega} = \sqrt {\frac {\| W _ {e} S _ {o} P W _ {1} \|}{\| W _ {2} K S _ {o} W _ {d} \|}}.$$

Then
