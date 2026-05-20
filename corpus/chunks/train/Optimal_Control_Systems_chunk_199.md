Using the initial condition $x(0)=1$ in the optimal state (3.5.39), and the final condition (for $\delta x_{f}$ being free) $\lambda(t_{f}=\infty)=0$ in the optimal costate (3.5.40), we get

$$x (0) = 1 \longrightarrow C _ {1} + C _ {2} = 1\lambda (\infty) = 0 \longrightarrow C _ {1} = 0. \tag {3.5.41}$$

Then, the previous optimal state and costate are given as

$$x ^ {*} (t) = e ^ {- \sqrt {1 0} t}; \quad \lambda^ {*} (t) = 2 (\sqrt {1 0} - 3) e ^ {- \sqrt {1 0} t}. \tag {3.5.42}$$

\- Step 5: Using the previous costate solution (3.5.34) of Step 2, we get the open-loop optimal control as

$$u ^ {*} (t) = - (\sqrt {1 0} - 3) e ^ {- \sqrt {1 0} t}. \tag {3.5.43}$$

(b) Closed-Loop Optimal Control: Here, we use the matrix algebraic Riccati equation (ARE) to find the closed-loop optimal control, as summarized in Table 3.3. First of all, comparing the present plant (3.5.30) and the PI (3.5.31) with the general formulation of the plant (3.5.12) and the PI (3.5.13), respectively, we identify the various coefficients and matrices as

$$\mathbf {A} = a = - 3; \quad \mathbf {B} = b = 1;\mathbf {Q} = q = 2; \quad \mathbf {R} = r = 2; \quad \bar {\mathbf {P}} = \bar {p}. \tag {3.5.44}$$

Note the PI (3.5.31) does not contain the factor $1/2$ as in the general PI (3.5.13) and accordingly, we have $\mathbf{Q} = q = 2$ and $\mathbf{R} = r = 2$ .

\- Step 1: With the previous values, the ARE (3.5.15) becomes

$$\bar {p} (- 3) + (- 3) \bar {p} - \bar {p} (1) (\frac {1}{2}) (1) \bar {p} + 2 = 0 \longrightarrow\bar {p} ^ {2} + 1 2 \bar {p} - 4 = 0, \tag {3.5.45}$$

the solution of which is

$$\bar {p} = - 6 \pm 2 \sqrt {1 0}. \tag {3.5.46}$$

\- Step 2: Using the positive value of the Riccati coefficient (3.5.46), the closed-loop optimal control (3.5.14) becomes

$$
\begin{array}{l} u ^ {*} (t) = - r ^ {- 1} b \bar {p} x ^ {*} (t) = - \frac {1}{2} (- 6 + 2 \sqrt {1 0}) x ^ {*} (t) \\ = - (- 3 + \sqrt {1 0}) x ^ {*} (t). \tag {3.5.47} \\ \end{array}
$$

\- Step 3: Using the optimal control (3.5.47), the optimal state is solved from (3.5.16) as

$$\dot {x} (t) = - 3 x ^ {*} (t) - (- 3 + \sqrt {1 0}) x ^ {*} (t) = - \sqrt {1 0} x ^ {*} (t). \tag {3.5.48}$$

Solving the previous along with the initial condition $x(0) = 1$ , we get the optimal state as

$$x ^ {*} (t) = e ^ {- \sqrt {1 0} t} \tag {3.5.49}$$

with which the optimal control (3.5.47) becomes

$$u ^ {*} (t) = - (\sqrt {1 0} - 3) e ^ {- \sqrt {1 0} t}. \tag {3.5.50}$$
