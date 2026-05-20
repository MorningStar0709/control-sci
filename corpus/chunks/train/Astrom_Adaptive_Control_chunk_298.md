# THEOREM 5.4 Boundedness and convergence set

Let $D = \{x \in R^n | \| x\| < r\}$ and suppose that $f(x, t)$ is locally Lipschitz on $D \times [0, \infty)$ . Let $V$ be a continuously differentiable function such that

$$\alpha_ {1} (\| x \|) \leq V (x, t) \leq \alpha_ {2} (\| x \|)$$

and

$$\frac {d V}{d t} = \frac {\partial V}{\partial t} + \frac {\partial V}{\partial x} f (x, t) \leq - W (x) \leq 0$$

$\forall t \geq 0, \forall x \in D$ , where $\alpha_{1}$ and $\alpha_{2}$ are class $K$ functions defined on $[0, r)$ and $W(x)$ is continuous on $D$ . Further, it is assumed that $dV/dt$ is uniformly continuous in $t$ .

Then all solutions to Eq. (5.25) with $\|x(t_{0})\| < \alpha_{2}^{-1}(\alpha_{1}(r))$ are bounded and satisfy

$$W (x (t)) \rightarrow 0 \quad \text { as } \quad t \rightarrow \infty$$

Moreover, if all the assumptions hold globally and $\alpha_{1}$ belongs to class $K_{\infty}$ , the statement is true for all $x(t_0) \in R^n$ .

A proof of a slight modification of this theorem can be found in Khalil (1992). The theorem states that the states of the system are bounded and that they approach the set $\{x \in D \mid W(x) = 0\}$ . In the theorem it is assumed that dV/dt is uniformly continuous, that is, that the continuity is independent of t. A sufficient condition for this is that $\ddot{V}$ is bounded.
