# Controllable Canonical Form

Assume that $\Phi$ has the characteristic equation

$$\det (\lambda I - \Phi) = \lambda^ {n} + a _ {1} \lambda^ {n - 1} + \dots + a _ {n} = 0 \tag {3.18}$$

and that $W_{c}$ is nonsingular. Then there exists a transformation such that the transformed system is

$$
z (k + 1) = \left( \begin{array}{c c c c c} - a _ {1} & - a _ {2} & \dots & - a _ {n - 1} & - a _ {n} \\ 1 & 0 & \dots & 0 & 0 \\ 0 & 1 & \dots & 0 & 0 \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ 0 & 0 & \dots & 1 & 0 \end{array} \right) z (k) + \left( \begin{array}{l} 1 \\ 0 \\ 0 \\ \vdots \\ 0 \end{array} \right) u (k) \tag {3.19}

y (k) = \left( \begin{array}{c c c} b _ {1} & \dots & b _ {n} \end{array} \right) z (k)
$$

which is called the controllable canonical form. The advantage of this form is that it is easy to compute the input-output model and to compute a state-feedback-control law. There are simple ways of finding the transformation to controllable canonical form.

For a single-input system it follows from (3.17) that the transformation matrix to the controllable canonical form is $T = \bar{W}_{c} W_{c}^{-1}$ , where $\bar{W}_{c}$ is the controllability matrix for the representation (3.19). The following example shows that the inverse of the controllability matrix has a simple form.
