# 5.2.2 Free-Final State and Open-Loop Optimal Control

Let us, first of all, note that for a free-final state system, it is usual to obtain closed-loop optimal control configuration. However, we reserve this to the next section. Let us consider the free-final state condition as

$$\mathbf {x} (k _ {f}) \text { is free, and } k _ {f} \text { is fixed. } \tag {5.2.35}$$

Then, the final condition (5.2.9) along with the Lagrangian (5.2.5) becomes

$$\left. \left[ - \boldsymbol {\lambda} ^ {*} (k) + \frac {\partial S (\mathbf {x} ^ {*} (k) , k)}{\partial \mathbf {x} ^ {*} (k)} \right] ^ {\prime} \right| _ {k _ {f}} \delta \mathbf {x} (k _ {f}) = 0. \tag {5.2.36}$$

Now, for this free-final point system with $k_{f}$ fixed, and $\mathbf{x}(k_{f})$ being free, $\delta x(k_{f})$ becomes arbitrary and its coefficient in (5.2.36) should be zero. Thus, the boundary condition (5.2.36) along with the performance index (5.2.3) becomes

$$\boldsymbol {\lambda} (k _ {f}) = \frac {\partial S (\mathbf {x} (k _ {f}) , k _ {f})}{\partial \mathbf {x} (k _ {f})} = \frac {\partial}{\partial \mathbf {x} (k _ {f})} \left[ \frac {1}{2} \mathbf {x} ^ {\prime} (k _ {f}) \mathbf {F} (k _ {f}) \mathbf {x} (k _ {f}) \right] \tag {5.2.37}$$

which gives

$$\boldsymbol {\lambda} \left(k _ {f}\right) = \mathbf {F} \left(k _ {f}\right) \mathbf {x} \left(k _ {f}\right). \tag {5.2.38}$$

The state and costate system (5.2.22) along with the initial condition (5.2.2) and the final condition (5.2.38) constitute a TPBVP. The solution of this TPBVP, which is difficult because of the coupled nature of the solutions (i.e., the state $\mathbf{x}^{*}(k)$ has to be solved forward starting from its initial condition $\mathbf{x}(k_{0})$ and the costate $\boldsymbol{\lambda}^{*}(k)$ has to be solved backward starting from its final condition $\boldsymbol{\lambda}(k_{f})$ ) leads us to open-loop optimal control. The entire procedure is now summarized in Table 5.2.
