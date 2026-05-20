# 2.8.1 Stage I: Optimization of a Functional

Consider the optimal of

$$J = \int_ {t _ {0}} ^ {t _ {f}} V (\mathbf {x} (t), \dot {\mathbf {x}} (t), t) d t \tag {2.8.1}$$

with the given boundary conditions

$$\mathbf {x} (t _ {0}) \text { fixed and } \mathbf {x} (t _ {f}) \text { free. } \tag {2.8.2}$$

Then, the optimal function $\mathbf{x}^{*}(t)$ should satisfy the Euler-Lagrange equation

$$\left. \overline {\left(\frac {\partial V}{\partial \mathbf {x}}\right) _ {*} - \frac {d}{d t} \left(\frac {\partial V}{\partial \dot {\mathbf {x}}}\right) _ {*}} = 0. \right| \tag {2.8.3}$$

The general boundary condition to be satisfied at the free-final point is given by [79]

$$\left[ V - \dot {\mathbf {x}} ^ {\prime} (t) \left(\frac {\partial V}{\partial \dot {\mathbf {x}}}\right) \right] _ {* t _ {f}} \delta t _ {f} + \left(\frac {\partial V}{\partial \dot {\mathbf {x}}}\right) _ {* t _ {f}} ^ {\prime} \delta \mathbf {x} _ {f} = 0. \tag {2.8.4}$$

This boundary condition is to be modified depending on the nature of the given $t_{f}$ and $\mathbf{x}(t_{f})$ . Although the previous general boundary condition is not derived in this book, it can be easily seen to be similar to the general boundary condition (2.7.26) in terms of the Lagrangian which embeds a performance index and a dynamical plant into a single augmented performance index with integrand L.

The sufficient condition for optimum is the Legendre condition given by

$$\boxed {\left(\frac {\partial^ {2} V}{\partial \dot {\mathbf {x}} ^ {2}}\right) _ {*} > 0} \text {for minimum} \tag {2.8.5}$$

and

$$\boxed {\left(\frac {\partial^ {2} V}{\partial \dot {\mathbf {x}} ^ {2}}\right) _ {*} < 0} \text { for maximum. } \tag {2.8.6}$$
