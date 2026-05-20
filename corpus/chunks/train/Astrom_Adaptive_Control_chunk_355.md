# EXAMPLE 5.15 Feedback linearization

Consider the system

$$
\begin{array}{l} \frac {d x _ {1}}{d t} = x _ {2} + f (x _ {1}) \\ \frac {d x _ {2}}{d t} = u \\ \end{array}
$$

where $f$ is a differentiable function. The first step is to introduce new coordinates

$$
\begin{array}{l} \xi_ {1} = x _ {1} \\ \xi_ {2} = x _ {2} + f (x _ {1}) \\ \end{array}
$$

The equations then become

$$
\begin{array}{l} \frac {d \xi_ {1}}{d t} = \xi_ {2} \\ \frac {d \xi_ {2}}{d t} = \xi_ {2} f ^ {\prime} (\xi_ {1}) + u \\ \end{array}
$$

By introducing the control law

$$u = - a _ {2} \xi_ {1} - a _ {1} \xi_ {2} - \xi_ {2} f ^ {\prime} (\xi_ {1}) + v$$

we get a linear closed-loop system described by

$$
\frac {d \xi}{d t} = \left( \begin{array}{c c} 0 & 1 \\ - a _ {2} & - a _ {1} \end{array} \right) \xi + \binom{0}{1} v
$$

This system is linear with the characteristic equation

$$s ^ {2} + a _ {1} s + a _ {2} = 0$$

By transforming back to the original coordinates the control law can be written as

$$u = - a _ {2} x _ {1} - \left(a _ {1} + f ^ {\prime} (x _ {1})\right) \left(x _ {2} + f (x _ {1})\right) + v$$

The closed-loop system obtained in the example will behave like a linear system. This is the reason why the method is called feedback linearization. The system in Example 5.15 is quite special. Applying the same procedure for a system described by

$$\frac {d x}{d t} = f (x) + u g (x)$$

we first pick

$$\xi_ {1} = h (x)$$

as a new state variable. The time derivative of $\xi_{1}$ is

$$\frac {d \xi_ {1}}{d t} = h ^ {\prime} (x) \Big (f (x) + u g (x) \Big)$$

If $h'(x)g(x) = 0$ , we introduce the new state variable

$$\xi_ {2} = h ^ {\prime} (x) f (x)$$

We proceed as long as the control variable u does not appear explicitly on the right-hand side. In this way we obtain the state variables $\xi_{1}\ldots\xi_{r}$ , which are combined to the vector $\xi\in R^{r}$ , where $r\leq n$ . We also introduce the new state variable $\eta_{1}\ldots\eta_{n-r}$ , which are combined into the vector $\eta\in R^{n-r}$ . This can be done in many different ways. We obtain the following system of equations:

$$\frac {d \xi_ {1}}{d t} = \xi_ {2}\frac {d \xi_ {2}}{d t} = \xi_ {3}$$

(5.85)

$$\frac {d \xi_ {r}}{d t} = \alpha (\xi , \eta) + u \beta (\xi , \eta)\frac {d \eta}{d t} = \gamma (\xi , \eta)$$
