# 6.4 The Hamilton-Jacobi-Bellman Equation

In this section, we present an alternate method of obtaining the closed-loop optimal control, using the principle of optimality and the Hamilton-Jacobi-Bellman (HJB) equation. First we need to state Bellman's principle of optimality [12]. It simply states that any portion of the optimal trajectory is optimal. Alternatively, the optimal policy (control) has the property that no matter what the previous decisions (i.e., controls) have been, the remaining decision must constitute an optimal policy. In Chapter 2, we considered the plant as

$$\dot {\mathbf {x}} (t) = \mathbf {f} (\mathbf {x} (t), \mathbf {u} (t), t) \tag {6.4.1}$$

and the performance index (PI) as

$$J (\mathbf {x} (t _ {0}), t _ {0}) = \int_ {t _ {0}} ^ {t _ {f}} V (\mathbf {x} (t), \mathbf {u} (t), t) d t. \tag {6.4.2}$$

Now, we provide the alternative approach, called Hamilton-Jacobi-Bellman approach and obtain a control law as a function of the state variables, leading to closed-loop optimal control. This is important from the practical point of view in implementation of the optimal control.

Let us define a scalar function $J^{*}(\mathbf{x}^{*}(t), t)$ as the minimum value of the performance index J for an initial state $\mathbf{x}^{*}(t)$ at time t, i.e.,

$$J ^ {*} (\mathbf {x} ^ {*} (t), t) = \int_ {t} ^ {t _ {f}} V (\mathbf {x} ^ {*} (\tau), \mathbf {u} ^ {*} (\tau), \tau) d \tau . \tag {6.4.3}$$

In other words, $J^{*}(\mathbf{x}^{*}(t), t)$ is the value of the performance index when evaluated along the optimal trajectory starting at $\mathbf{x}(t)$ . Here, we used the principle of optimality in saying that the trajectory from t to $t_{f}$ is optimal. However, we are not interested in finding the optimal control for specific initial state $\mathbf{x}(t)$ , but for any unspecified initial conditions. Thus, our interest is in $J(\mathbf{x}(t_{0}), t_{0})$ as a function of $\mathbf{x}(t_{0})$ and $t_{0}$ . Now consider
