$$\dot {x} _ {1} = x _ {2}\dot {x} _ {2} = - \frac {D (x _ {2})}{M} + \frac {u}{M} \tag {2.5}$$

so that, comparing with Equation 2.3,

$$f _ {1} (x _ {1}, x _ {2}, u, t) = x _ {2}f _ {2} (x _ {1}, x _ {2}, u, t) = - \frac {D (x _ {2})}{M} + \frac {u}{M}.$$

The output equations depend on the choices of output variables. For example, if $x$ is considered the output of interest, then

$$y _ {1} = x _ {1} \tag {2.6}$$

is the output equation, and

$$y _ {1} = h _ {1} (x _ {1}, x _ {2}, u, t) = x _ {1}. \tag {2.7}$$

The right-hand sides in Equations 2.3 and 2.4 are explicit functions of t, which means that the equations themselves, rather than just the variables, are changing with time. The right-hand sides in Equations 2.5 and 2.6 do not depend explicitly on time; Equation 2.5 would if, for example, M represented the mass of a container that was simultaneously moving and being filled with water. Systems in which neither the f's nor the h's depend explicitly on t are called time-invariant; other systems are time-varying.

If the $f$ 's and $h$ 's are linear functions of the state and input variables, the system is called a linear system. Equations 2.5 and 2.6 represent a linear system if the function $D(v)$ is linear in $v$ .

It is very cumbersome to carry so many variables and equations, and we use vector notation to reduce the clutter. Define the following vectors:

$$
\mathbf {x} = \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ \vdots \\ x _ {n} \end{array} \right], \quad \mathbf {y} = \left[ \begin{array}{c} y _ {1} \\ y _ {2} \\ \vdots \\ y _ {m} \end{array} \right], \quad \mathbf {u} = \left[ \begin{array}{c} u _ {1} \\ u _ {2} \\ \vdots \\ u _ {r} \end{array} \right].
$$

Define also the vector functions

$$
\mathbf {f} (\mathbf {\theta}) = \left[ \begin{array}{c} f _ {1} (\mathbf {\theta}) \\ f _ {2} (\mathbf {\theta}) \\ \vdots \\ f _ {n} (\mathbf {\theta}) \end{array} \right], \quad \mathbf {h} (\mathbf {\theta}) = \left[ \begin{array}{c} h _ {1} (\mathbf {\theta}) \\ h _ {2} (\mathbf {\theta}) \\ \vdots \\ h _ {m} (\mathbf {\theta}) \end{array} \right].
$$

Then Equations 2.3 and 2.4 are written compactly as

$$\dot {\mathbf {x}} = \mathbf {f} (\mathbf {x}, \mathbf {u}, t) \tag {2.8}\mathbf {y} = \mathbf {h} (\mathbf {x}, \mathbf {u}, t). \tag {2.9}$$
