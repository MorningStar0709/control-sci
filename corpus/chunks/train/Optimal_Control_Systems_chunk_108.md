# 2.7.1 Terminal Cost Problem

Here we consider the optimal control system where the performance index is of general form containing a final (terminal) cost function in addition to the integral cost function. Such an optimal control problem is called the Bolza problem. Consider the plant as

$$\dot {\mathbf {x}} (t) = \mathbf {f} (\mathbf {x} (t), \mathbf {u} (t), t), \tag {2.7.1}$$

the performance index as

$$J (\mathbf {u} (t)) = S \left(\mathbf {x} \left(t _ {f}\right), t _ {f}\right) + \int_ {t _ {0}} ^ {t _ {f}} V (\mathbf {x} (t), \mathbf {u} (t), t) d t \tag {2.7.2}$$

and given boundary conditions as

$$\mathbf {x} (t _ {0}) = \mathbf {x} _ {0}; \quad \mathbf {x} (t _ {f}) \text { is free and } t _ {f} \text { is free } \tag {2.7.3}$$

where, $\mathbf{x}(t)$ and $\mathbf{u}(t)$ are $n$ - and $r$ -dimensional state and control vectors respectively. This problem of Bolza is the one with the most general form of the performance index.

The Lagrange problem was first discussed in 1762, Mayer considered his problem in 1878, and the problem of Bolza was formulated in 1913.

Before we begin illustrating the Pontryagin procedure for this problem, let us note that

$$\int_ {t _ {0}} ^ {t _ {f}} \frac {d S (\mathbf {x} (t) , t)}{d t} d t = S (\mathbf {x} (t), t) | _ {t _ {0}} ^ {t _ {f}} = S (\mathbf {x} (t _ {f}), t _ {f}) - S (\mathbf {x} (t _ {0}), t _ {0}). \tag {2.7.4}$$

Using the equation (2.7.4) in the original performance index (2.7.2), we get

$$
\begin{array}{l} J _ {2} (\mathbf {u} (t)) = \int_ {t _ {0}} ^ {t _ {f}} \left[ V (\mathbf {x} (t), \mathbf {u} (t), t) + \frac {d S}{d t} \right] d t \\ = \int_ {t _ {0}} ^ {t _ {f}} V (\mathbf {x} (t), \mathbf {u} (t), t) d t + S (\mathbf {x} (t _ {f}), t _ {f}) - S (\mathbf {x} (t _ {0}), t _ {0}). \tag {2.7.5} \\ \end{array}
$$

Since $S(\mathbf{x}(t_{0}), t_{0})$ is a fixed quantity, the optimization of the original performance index J in (2.7.2) is equivalent to that of the performance index $J_{2}$ in (2.7.5). However, the optimal cost given by (2.7.2) is different from the optimal cost (2.7.5). Here, we are interested in finding the optimal control only. Once the optimal control is determined, the optimal cost is found using the original performance index J in (2.7.2) and not $J_{2}$ in (2.7.5). Also note that

$$\frac {d [ S (\mathbf {x} (t) , t) ]}{d t} = \left(\frac {\partial S}{\partial \mathbf {x}}\right) ^ {\prime} \dot {\mathbf {x}} (t) + \frac {\partial S}{\partial t}. \tag {2.7.6}$$
