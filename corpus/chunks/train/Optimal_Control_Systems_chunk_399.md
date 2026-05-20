# 7.3.3 Problem Solution

The solution to the fuel-optimal system is provided first under the following list of steps and then explained in detail.

- Step 1: Hamiltonian   
- Step 2: Optimal Condition   
- Step 3: Optimal Control   
- Step 4: Costate Solutions   
- Step 5: State Trajectories   
- Step 6: Minimum Fuel   
- Step 7: Switching Sequences   
- Step 8: Control Law

\- Step 1: Hamiltonian: Let us formulate the Hamiltonian as

$$\mathcal {H} (\mathbf {x} (t), \boldsymbol {\lambda} (t), u (t)) = | u (t) | + \lambda_ {1} (t) x _ {2} (t) + \lambda_ {2} (t) u (t). \tag {7.3.4}$$

\- Step 2: Optimal Condition: According to the Minimum Principle, the optimal condition is

$$
\begin{array}{l} \mathcal {H} (\mathbf {x} ^ {*} (t), \boldsymbol {\lambda} ^ {*} (t), u ^ {*} (t)) \leq \mathcal {H} (\mathbf {x} ^ {*} (t), \boldsymbol {\lambda} ^ {*} (t), u (t)), \\ = \min _ {| u (t) | \leq 1} \left\{\mathcal {H} (\mathbf {x} ^ {*} (t), \boldsymbol {\lambda} ^ {*} (t), u (t)) \right\}. \tag {7.3.5} \\ \end{array}
$$

Using (7.3.4) in (7.3.5), we have

$$
\begin{array}{l} | u ^ {*} (t) | + \lambda_ {1} ^ {*} (t) x _ {2} ^ {*} (t) + \lambda_ {2} ^ {*} (t) u ^ {*} (t) \\ \leq | u (t) | + \lambda_ {1} ^ {*} (t) x _ {2} ^ {*} (t) + \lambda_ {2} ^ {*} (t) u (t), \tag {7.3.6} \\ \end{array}
$$

which reduces to

$$| u ^ {*} (t) | + u ^ {*} (t) \lambda_ {2} ^ {*} (t) \leq | u (t) | + u (t) \lambda_ {2} ^ {*} (t). \tag {7.3.7}$$

\- Step 3: Optimal Control: Let us note at this point that

$$\min _ {| u (t) | \leq 1} \left\{| u (t) | + u (t) \lambda_ {2} ^ {*} (t) \right\} = | u ^ {*} (t) | + u ^ {*} (t) \lambda_ {2} ^ {*} (t) \tag {7.3.8}$$

and

$$
| u (t) | = \left\{ \begin{array}{l l} + u (t) & \text { if } \quad u (t) \geq 0, \\ - u (t) & \text { if } \quad u (t) \leq 0. \end{array} \right. \tag {7.3.9}
$$

Hence, we have

$$
\begin{array}{l} \min _ {| u (t) | \leq 1} \left\{\left| u (t) \right| + u (t) \lambda_ {2} ^ {*} (t) \right\} \\ = \left\{ \begin{array}{l} \min _ {| u (t) | \leq 1} \left\{\left[ + 1 + \lambda_ {2} ^ {*} (t) \right] u (t) \right\} \text {   if   } u (t) \geq 0 \\ \min _ {| u (t) | \leq 1} \left\{\left[ - 1 + \lambda_ {2} ^ {*} (t) \right] u (t) \right\} \text {   if   } u (t) \leq 0. \end{array} \right. \tag {7.3.10} \\ \end{array}
$$

Let us now explore all the possible values of $\lambda_{2}^{*}(t)$ and the corresponding optimal values of $u^{*}(t)$ . Thus, we have the following table.
