# Example 9.4

$$C = \frac {1 0}{s} \qquad P = \frac {5 0}{s + 1 0} \qquad H = 1 \qquad x (t) = B t \qquad X (s) = \frac {B}{s ^ {2}}$$

This is the same as Example 9.3, but the input is now a ramp.

$$E (s) = \frac {B s (s + 1 0)}{s ^ {2} (s ^ {2} + 1 0 s + 5 0 0)}$$

Applying the FVT:

$$
\begin{array}{l} \mathrm{SSE} = \lim _ {s \rightarrow 0} \frac {s B s (s + 1 0)}{s ^ {2} \left(s ^ {2} + 1 0 s + 5 0 0\right)} = \lim _ {s \rightarrow 0} \frac {B (s + 1 0)}{s ^ {2} + 1 0 s + 5 0 0} \\ = \frac {1 0}{5 0 0} B = 0. 0 2 B \\ \end{array}
$$

With the new controller, we have changed the SSE for ramp input from ∞ to 2%! Our controller has increased the system type by one and this made a big dierence on SSE with the ramp input. Note that calling the error ${ \bf \dot { \bar { 2 } } } \% ^ { \bf \vec { , } \vec { , } }$ is somewhat unclear for a ramp input. Since B is a constant, but the input signal is $x ( t ) = \breve { B } t$ , the error is a smaller and smaller percentage of the total input as time goes on. In the steady state this error is nite but 0%!.
