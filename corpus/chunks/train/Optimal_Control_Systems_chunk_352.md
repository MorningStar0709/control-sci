# 6.3.4 Optimal Control of Continuous-Time Systems

Here, we describe dynamic programming (DP) technique as applied to finding optimal control of continuous-time systems. First of all, we note that although in the previous sections, the DP is explained w.r.t. the discrete-time situation, DP can also be applied to continuous-time systems. However, one can either

1. discretize the continuous-time systems in one or other ways and use the DP as applicable to discrete-time systems, as explained in previous sections, or   
2. apply directly the DP to continuous-time systems leading to the celebrated Hamilton-Jacobi-Bellman (HJB) equation, as presented in the next section.

In using the discretization of continuous-time processes, we can either employ

1. the Euler method, or

2. sampler and zero-order hold method.

Let us now briefly discuss these two approaches.

1. Euler Method: Let us first take up the Euler approximation of a linear time invariant (LTI) system (although it can be used for nonlinear systems as well) for which the plant is

$$\dot {\mathbf {x}} (t) = \mathbf {A} \mathbf {x} (t) + \mathbf {B} \mathbf {u} (t) \tag {6.3.32}$$

and the cost function is

$$
\begin{array}{l} J (0) = \frac {1}{2} \mathbf {x} ^ {\prime} (t _ {f}) \mathbf {F} (t _ {f}) \mathbf {x} (t _ {f}) \\ + \frac {1}{2} \int_ {0} ^ {t _ {f}} \left[ \mathbf {x} ^ {\prime} (t) \mathbf {Q x} (t) + \mathbf {u} ^ {\prime} (t) \mathbf {R u} (t) \right] d t \tag {6.3.33} \\ \end{array}
$$

where, the state vector $\mathbf{x}(t)$ and control vector $\mathbf{u}(t)$ and the various system and weighted matrices and are defined in the usual manner. Assume some typical boundary conditions for finding the optimal control $\mathbf{u}^{*}(t)$ .

Using the Euler approximation of the derivative in (6.3.32) as

$$\dot {\mathbf {x}} (t) = \frac {\mathbf {x} (k + 1) - \mathbf {x} (k)}{T} \tag {6.3.34}$$

where, $T$ is the discretization (sampling) interval and $\mathbf{x}(k) = \mathbf{x}(kT)$ , the discretized version of the state model (6.3.32) becomes

$$\mathbf {x} (k + 1) = [ \mathbf {I} + T \mathbf {A} ] \mathbf {x} (k) + T \mathbf {B u} (k). \tag {6.3.35}$$

Also, replacing the integration process in continuous-time cost function (6.3.33) by the summation process, we get

$$
\begin{array}{l} J (0) = \frac {1}{2} \mathbf {x} ^ {\prime} \left(k _ {f}\right) \mathbf {F x} \left(t _ {f}\right) \\ + \frac {1}{2} \sum_ {k = k _ {0}} ^ {k _ {f} - 1} \left[ \mathbf {x} ^ {\prime} (k) \mathbf {Q} _ {d} \mathbf {x} (k) + \mathbf {u} (k) \mathbf {R} _ {d} \mathbf {u} (k) \right] \tag {6.3.36} \\ \end{array}
$$

where, $\mathbf{Q}_d = T\mathbf{Q}$ , and $\mathbf{R}_d = T\mathbf{R}$ .
