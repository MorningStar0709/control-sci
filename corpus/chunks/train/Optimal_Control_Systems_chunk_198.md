# Example 3.3

Consider a simple first order system

$$\dot {x} (t) = - 3 x (t) + u (t) \tag {3.5.30}$$

and the cost function (CF) as

$$J = \int_ {0} ^ {\infty} [ x ^ {2} (t) + u ^ {2} (t) ] d t \tag {3.5.31}$$

where, $x(0) = 1$ and the final state $x(\infty) = 0$ . Find the open-loop and closed-loop optimal controllers.

Solution: (a) Open-Loop Optimal Control: We use the Pontryagin procedure given in Chapter 2 (see Table 2.1). First of all, comparing the given plant (3.5.30) and the CF (3.5.31) with the general formulations (see Table 2.1), identify that

$$V (x (t), u (t)) = x ^ {2} (t) + u ^ {2} (t),f (x (t), u (t)) = - 3 x (t) + u (t). \tag {3.5.32}$$

Now, we use the step-by-step procedure given in Table 2.1.

\- Step 1: Formulate the Hamiltonian as

$$\mathcal {H} = V (x (t), u (t)) + \lambda (t) f (x (t), u (t))= x ^ {2} (t) + u ^ {2} (t) + \lambda (t) [ - 3 x (t) + u (t) ]. \tag {3.5.33}$$

\- Step 2: The optimal control $u^{*}(t)$ is obtained by minimizing the previous Hamiltonian w.r.t. $u$ as

$$\frac {\partial \mathcal {H}}{\partial u} = 0 \longrightarrow 2 u ^ {*} (t) + \lambda^ {*} (t) = 0 \longrightarrow u ^ {*} (t) = - \frac {1}{2} \lambda^ {*} (t). \tag {3.5.34}$$

\- Step 3: Using optimal control (3.5.34) in the Hamiltonian function (3.5.33), find the optimal Hamiltonian function as

$$\mathcal {H} ^ {*} = x ^ {* ^ {2}} (t) - \frac {1}{4} \lambda^ {* ^ {2}} (t) - 3 \lambda^ {*} (t) x ^ {*} (t). \tag {3.5.35}$$

\- Step 4: Using the previous optimal $\mathcal{H}^*$ , obtain the set of state and costate equations

$$\dot {x} ^ {*} (t) = \frac {\partial \mathcal {H} ^ {*}}{\partial \lambda} \longrightarrow \dot {x} ^ {*} (t) = - \frac {1}{2} \lambda^ {*} (t) - 3 x ^ {*} (t), \tag {3.5.36}\dot {\lambda} ^ {*} (t) = - \frac {\partial \mathcal {H} ^ {*}}{\partial x} \longrightarrow \dot {\lambda} ^ {*} (t) = - 2 x ^ {*} (t) + 3 \lambda^ {*} (t), \tag {3.5.37}$$

yielding

$$\ddot {x} ^ {*} (t) - 1 0 x ^ {*} (t) = 0, \tag {3.5.38}$$

the solution of which becomes

$$x ^ {*} (t) = C _ {1} e ^ {\sqrt {1 0} t} + C _ {2} e ^ {- \sqrt {1 0} t}. \tag {3.5.39}$$

Using the optimal state (3.5.39) in (3.5.36), we have the costate as

$$
\begin{array}{l} \lambda^ {*} (t) = 2 \left[ - \dot {x} ^ {*} (t) - 3 x ^ {*} (t) \right] \\ = - 2 C _ {1} (\sqrt {1 0} + 3) e ^ {\sqrt {1 0} t} + 2 C _ {2} (\sqrt {1 0} - 3) e ^ {- \sqrt {1 0} t}. \tag {3.5.40} \\ \end{array}
$$
