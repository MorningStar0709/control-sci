# 6.2 Pontryagin Minimum Principle

(Theorem 2.1), i.e., the necessary condition of minimization is that the first variation $\delta J$ must be zero for an arbitrary variation $\delta\mathbf{u}(t)$ . But now we place restrictions on the control $\mathbf{u}(t)$ such as

$$\left| \left| \mathbf {u} (t) \right| \right| \leq \mathbf {U} \tag {6.2.3}$$

or component wise,

$$\left| u _ {j} (t) \right| \leq U _ {j} \longrightarrow U _ {j} ^ {-} \leq u _ {j} (t) \leq U _ {j} ^ {+} \tag {6.2.4}$$

where, $U_{j}^{-}$ and $U_{j}^{+}$ are the lower and upper bounds or limits on the control function $u_{j}(t)$ . Then, we can no longer assume that the control variation $\delta\mathbf{u}(t)$ is arbitrary for all $t \in [t_{0}, t_{f}]$ . In other words, the variation $\delta\mathbf{u}(t)$ is not arbitrary if the extremal control $\mathbf{u}^{*}(t)$ lies on the boundary condition or reaches a limit. If, for example, an extremal control $\mathbf{u}^{*}(t)$ lies on the boundary during some interval $[t_{a}, t_{b}]$ of the entire interval $[t_{0}, t_{f}]$ , as shown in Figure 6.1(a), then the negative admissible control variation $-\delta\mathbf{u}(t)$ is not allowable as shown in Figure 6.1(b) [79]. The reason for taking $+\delta\mathbf{u}(t)$ and $-\delta\mathbf{u}(t)$ the way it is shown will be apparent later. Then, assuming that all the admissible variations $||\delta\mathbf{u}(t)||$ is small enough that the sign of the increment $\Delta J$ is determined by the sign of the variation $\delta J$ , the necessary condition for $\mathbf{u}^{*}(t)$ to minimize J is that the first variation

$$\delta J (\mathbf {u} ^ {*} (t), \delta \mathbf {u} (t)) \geq 0. \tag {6.2.5}$$

Summarizing, the relation for the first variation (6.2.5) is valid if $\mathbf{u}^{*}(t)$ lies on the boundary (or has a constraint) during any portion of the time interval $[t_{0}, t_{f}]$ and the first variation $\delta J = 0$ if $\mathbf{u}^{*}(t)$ lies within the boundary (or has no constraint) during the entire time interval $[t_{0}, t_{f}]$ . Next, let us see how the constraint affects the necessary conditions (6.1.5) to (6.1.6) which were derived by using the assumption that the admissible control values $\mathbf{u}(t)$ are unconstrained. Using the results of Chapter 2, we have the first variation as
