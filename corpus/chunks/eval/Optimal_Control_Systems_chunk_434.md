$$
\begin{array}{l} \dot {\mathbf {x}} (t) = f (\mathbf {x} (t), g (\mathbf {x} (t), \alpha (t), \alpha) 1 (t),, \dots , \alpha_ {p} (t), t), x (t = t _ {0}) = \mathbf {x} _ {0} \\ \dot {\alpha} = \alpha_ {1}, \quad \alpha (t = t _ {0}) = \alpha (t _ {0}) \\ \dot {\alpha_ {1}} = \alpha_ {2}, \quad \alpha_ {1} (t = t _ {0}) = \alpha_ {1} (t _ {0}) \\ \dot {\alpha} _ {p - 1} = \alpha_ {p}, \quad \alpha_ {p - 1} (t = t _ {0}) = \alpha_ {p - 1} (t _ {0}). \tag {7.6.39} \\ \end{array}
$$

The new cost functional is then given by

$$J = F (\mathbf {x} (t _ {f}), t _ {f}) + \int_ {t _ {o}} ^ {t _ {f}} V (\mathbf {x} (t), g (\mathbf {x} (t), \alpha (t), \alpha) (t),, \dots , \alpha_ {p} (t), t), t) d t \tag {7.6.40}$$

The new initial conditions $\alpha(t_{0}),\ldots,\alpha_{p-1}(t_{0})$ are required to satisfy (7.6.35) and (7.6.36), so after some algebraic manipulations, we get

$$
\begin{array}{l} \alpha (t _ {0}) = \pm \sqrt {- 2 S (\mathbf {x} (t _ {0}) , t _ {0})} \\ \alpha_ {1} (t _ {0}) = - S _ {1} (\mathbf {x} (t _ {0}), t _ {0}) / \alpha (t _ {0}) \\ \alpha_ {2} (t _ {0}) = - [ S _ {2} (\mathbf {x} (t _ {0}), t _ {0}) + \alpha_ {1} ^ {2} (t _ {0}) ] / \alpha (t _ {0}) \\ \dots \tag {7.6.41} \\ \end{array}
$$

With this choice of boundary conditions, the original relations w.r.t. the constraints (7.6.35) and (7.6.36) are satisfied for all t for any control function $\alpha_{p}(\cdot)$ . In other words, any function $\alpha_{p}(\cdot)$ will produce an admissible trajectory. Thus, the original constrained problem is transformed into an unconstrained problem.

Now we apply the Pontryagin Principle to this unconstrained problem. [68, 27, 40, 62]. In general terms, we define a new $n + p$ th state vector

$$\mathcal {Z} (t) = \left[ \mathbf {x} (t), \alpha (t), \dots \alpha_ {p - 1} \right] ^ {\prime} \tag {7.6.42}$$

then, the new plant (7.6.39) becomes

$$\dot {\mathcal {Z}} = \mathcal {F} (\mathcal {Z} (t), \alpha_ {p} (t), t) \tag {7.6.43}$$

where the $(n + p)$ -dimensional vector function $\mathcal{F}$ represents the right-hand side of (7.6.39). Next, we define the Hamiltonian as

$$\mathcal {H} = V + \lambda \mathcal {F} \tag {7.6.44}$$

where $\lambda$ is an $n + p$ -dimensional Lagrange multiplier. Then, for the state

$$\dot {\mathcal {Z}} (t) = \mathcal {H} _ {\boldsymbol {\lambda}}, \quad \mathcal {Z} (t _ {0}), \tag {7.6.45}$$

for the costate
