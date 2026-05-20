$$
\begin{array}{l} \frac {d J ^ {*} (\mathbf {x} ^ {*} (t) , t)}{d t} = \left(\frac {\partial J ^ {*} (\mathbf {x} ^ {*} (t) , t)}{\partial \mathbf {x} ^ {*}}\right) ^ {\prime} \dot {\mathbf {x}} ^ {*} (t) + \frac {\partial J ^ {*} (\mathbf {x} ^ {*} (t) , t)}{\partial t}, \\ = \left(\frac {\partial J ^ {*} (\mathbf {x} ^ {*} (t) , t)}{\partial \mathbf {x} ^ {*}}\right) ^ {\prime} \mathbf {f} (\mathbf {x} ^ {*} (t), \mathbf {u} ^ {*} (t), t) + \frac {\partial J ^ {*} (\mathbf {x} ^ {*} (t) , t)}{\partial t}. \tag {6.4.4} \\ \end{array}
$$

From (6.4.3), we have

$$\frac {d J ^ {*} (\mathbf {x} ^ {*} (t) , t)}{d t} = - V (\mathbf {x} ^ {*} (t), \mathbf {u} ^ {*} (t), t). \tag {6.4.5}$$

Using (6.4.4) and (6.4.5), we get

$$
\begin{array}{l} \frac {\partial J ^ {*} (\mathbf {x} ^ {*} (t) , t)}{\partial t} + V (\mathbf {x} ^ {*} (t), \mathbf {u} ^ {*} (t), t) \\ + \left(\frac {\partial J ^ {*} (\mathbf {x} ^ {*} (t) , t)}{\partial \mathbf {x} ^ {*}}\right) ^ {\prime} \mathbf {f} (\mathbf {x} ^ {*} (t), \mathbf {u} ^ {*} (t), t) = 0. \tag {6.4.6} \\ \end{array}
$$

Let us introduce the Hamiltonian as

$$\mathcal {H} = V (\mathbf {x} (t), \mathbf {u} (t), t) + \left(\frac {\partial J ^ {*} (\mathbf {x} ^ {*} (t) , t)}{\partial \mathbf {x} ^ {*}}\right) ^ {\prime} \mathbf {f} (\mathbf {x} (t), \mathbf {u} (t), t) \tag {6.4.7}$$

Using (6.4.7) in (6.4.6), we have

$$\boxed {\frac {\partial J ^ {*} \left(\mathbf {x} ^ {*} (t) , t\right)}{\partial t} + \mathcal {H} \left(\mathbf {x} ^ {*} (t), \frac {\partial J ^ {*} \left(\mathbf {x} ^ {*} (t) , t\right)}{\partial \mathbf {x} ^ {*}}, \mathbf {u} ^ {*} (t), t\right) = 0; \forall t \in \left[ t _ {0}, t _ {f}\right)} \tag {6.4.8}$$

with boundary condition from (6.4.3) as

$$J ^ {*} (\mathbf {x} ^ {*} (t _ {f}), t _ {f}) = 0, \tag {6.4.9}$$

or

$$J ^ {*} (\mathbf {x} ^ {*} (t _ {f}), t _ {f}) = S (\mathbf {x} ^ {*} (t _ {f}), t _ {f}) \tag {6.4.10}$$

if the original PI (6.4.2) contains a terminal cost function. This equation (6.4.8) is called the Hamilton-Jacobi equation. Since this equation is the continuous-time analog of Bellman's recurrence equations in dynamic programming [15], it is also called the Hamilton-Jacobi-Bellman (HJB) equation. Comparing the Hamiltonian function (6.4.7) with that given in earlier chapters, we see that the costate function $\lambda^{*}(t)$ is given by

$$\boldsymbol {\lambda} ^ {*} (t) = \frac {\partial J ^ {*} (\mathbf {x} ^ {*} (t) , t)}{\partial \mathbf {x} ^ {*}}. \tag {6.4.11}$$
