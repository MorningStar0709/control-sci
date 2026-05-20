# Example 9.2

$$C = 1 0 \qquad P = \frac {5 0}{s + 1 0} \qquad H = 1 \qquad x (t) = B t \qquad X (s) = \frac {B}{s ^ {2}}$$

This is the same as above, but the input is now a ramp.

$$E (s) = \frac {B / s ^ {2}}{1 + \frac {5 0 0}{(s + 1 0)}} = \frac {B (s + 1 0)}{s ^ {2} (s + 1 0 + 5 0 0)} = \frac {B (s + 1 0)}{s ^ {3} + 5 1 0 s ^ {2}}$$

Applying the FVT:

$$\lim _ {t \to \infty} e (t) = \lim _ {s \to 0} s \frac {B (s + 1 0)}{s ^ {3} + 5 1 0 s ^ {2}} = \lim _ {s \to 0} \frac {B (s + 1 0)}{s ^ {2} + 5 1 0 s} = \infty$$

The system is the same, but with a ramp input the steady state error is innite!

$$
\begin{array}{l} C = \frac {1 0}{s} = \rightarrow \boxed {1 0} \rightarrow \boxed {\frac {1}{s}} \rightarrow \\ = \rightarrow 1 0 \int_ {0} ^ {t} d t \\ \end{array}
$$

Figure 9.2: A simple controller which has a single pole at the origin can be called an Integral controller
