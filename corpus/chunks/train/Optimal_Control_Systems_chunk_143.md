# 3. Optimization of Hamiltonian

(a) The control equation (2.8.32) indicates the optimization of the Hamiltonian w.r.t. the control $\mathbf{u}(t)$ . That is, the optimization of the original performance index (2.8.17), which is a functional subject to the plant equation (2.8.15), is equivalent to the optimization of the Hamiltonian function w.r.t. $\mathbf{u}(t)$ . Thus, we “reduced” our original functional optimization problem to an ordinary function optimization problem.

(b) We note that we assumed unconstrained or unbounded control $\mathbf{u}(t)$ and obtained the control relation $\partial\mathcal{H}/\partial\mathbf{u}=0$ .

(c) If $\mathbf{u}(t)$ is constrained or bounded as being a member of the set U, i.e., $\mathbf{u}(t) \in \mathbf{U}$ , we can no longer take $\partial H/\partial u = 0$ , since $\mathbf{u}(t)$ , so calculated, may lie outside the range of the permissible region U. In practice, the control $\mathbf{u}(t)$ is always limited by such things as saturation of amplifiers, speed of a motor, or thrust of a rocket. The constrained optimal control systems are discussed in Chapter 7.

(d) Regardless of any constraints on $\mathbf{u}(t)$ , Pontryagin had shown that $\mathbf{u}(t)$ must still be chosen to minimize the Hamiltonian. A rigorous proof of the fact that $\mathbf{u}(t)$ must be chosen to optimize $\mathcal{H}$ function is Pontryagin's most notable contribution to optimal control theory. For this reason, the approach is often called Pontryagin Principle. So in the case of constrained control, it is shown that

$$\boxed {\min _ {\mathbf {u} \in \mathbf {U}} \mathcal {H} (\mathbf {x} ^ {*} (t), \boldsymbol {\lambda} ^ {*} (t), \mathbf {u} (t), t) = \mathcal {H} (\mathbf {x} ^ {*} (t), \boldsymbol {\lambda} ^ {*} (t), \mathbf {u} ^ {*} (t), t)} \tag {2.8.49}$$

or equivalently

$$\boxed {\mathcal {H} \left(\mathbf {x} ^ {*} (t), \boldsymbol {\lambda} ^ {*} (t), \mathbf {u} ^ {*} (t), t\right) \leq \mathcal {H} \left(\mathbf {x} ^ {*} (t), \boldsymbol {\lambda} ^ {*} (t), \mathbf {u} (t), t\right).} \tag {2.8.50}$$

4. Pontryagin Maximum Principle: Originally, Pontryagin used a slightly different performance index which is maximized rather
