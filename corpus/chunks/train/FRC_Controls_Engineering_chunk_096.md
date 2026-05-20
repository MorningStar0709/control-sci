# 4.3 Change of variables

Change of variables is a technique for simplifying problems in which expressions are replaced with new variables to make the problem more tractable. This can mean either the problem is more straightforward or it matches a common form for which tools for finding solutions are readily available. Here’s an example of integration which utilizes it.

$$\int \cos \omega t d t$$

Let $u = \omega t .$ .

$$d u = \omega d td t = \frac {1}{\omega} d u$$

Now substitute the expressions for u and dt in.

$$
\begin{array}{l} \int \cos u \frac {1}{\omega} d u \\ \frac {1}{\omega} \int \cos u d u \\ \frac {1}{\omega} \sin u + C \\ \frac {1}{\omega} \sin \omega t + C \\ \end{array}
$$

Another example, which will be relevant when we actually cover state-space notation $( \dot { \mathbf { x } } = \mathbf { A } \mathbf { x } + \mathbf { B } \mathbf { u } )$ , is a closed-loop state-space system.

$$\dot {\mathbf {x}} = (\mathbf {A} - \mathbf {B K}) \mathbf {x} + \mathbf {B K r}\dot {\mathbf {x}} = \mathbf {A} _ {c l} \mathbf {x} + \mathbf {B} _ {c l} \mathbf {u} _ {c l}$$

where $\mathbf { A } _ { c l } = \mathbf { A } - \mathbf { B } \mathbf { K } , \mathbf { B } _ { c l } = \mathbf { B } \mathbf { K }$ , and $\mathbf { u } _ { c l } = \mathbf { r }$ . Since it matches the form of the open-loop system, all the same analysis tools will work with it.
