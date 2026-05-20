# - Step 7: Optimal Cost

Now we discuss these steps in detail. Also, note that we heavily draw upon the results of the previous Chapters 2 and 3. First of all, let us note from (4.1.1) and (4.1.2) that the error $\mathbf{e}(t)$ can be expressed as a function of $\mathbf{z}(t)$ and $\mathbf{x}(t)$ as

$$\mathbf {e} (t) = \mathbf {z} (t) - \mathbf {C} (t) \mathbf {x} (t). \tag {4.1.4}$$

\- Step 1: Hamiltonian: Formulate the Hamiltonian as (see Table 3.1)

$$\mathcal {H} (\mathbf {x} (t), \mathbf {u} (t), \boldsymbol {\lambda} (t)) = \frac {1}{2} [ \mathbf {z} (t) - \mathbf {C} (t) \mathbf {x} (t) ] ^ {\prime} \mathbf {Q} (t) [ \mathbf {z} (t) - \mathbf {C} (t) \mathbf {x} (t) ]+ \frac {1}{2} \mathbf {u} ^ {\prime} (t) \mathbf {R} (t) \mathbf {u} (t)+ \boldsymbol {\lambda} ^ {\prime} (t) [ \mathbf {A} (t) \mathbf {x} (t) + \mathbf {B} (t) \mathbf {u} (t) ]. \tag {4.1.5}$$

\- Step 2: Open-Loop Optimal Control: Using the Hamiltonian (4.1.5), obtain the control equation from

$$\frac {\partial \mathcal {H}}{\partial \mathbf {u}} = 0 \longrightarrow \mathbf {R} (t) \mathbf {u} (t) + \mathbf {B} ^ {\prime} (t) \boldsymbol {\lambda} (t) = 0 \tag {4.1.6}$$

from which we have the optimal control as

$$\boxed {\mathbf {u} ^ {*} (t) = - \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \boldsymbol {\lambda} ^ {*} (t).} \tag {4.1.7}$$

Since the second partial of H in (4.1.5) w.r.t. $\mathbf{u}^{*}(t)$ is just $\mathbf{R}(t)$ , and we chose $\mathbf{R}(t)$ to be positive definite, we are dealing with a control which minimizes the cost functional (4.1.3).

\- Step 3: State and Costate System: The state is given in terms of the Hamiltonian (4.1.5) as

$$\dot {\mathbf {x}} (t) = \frac {\partial \mathcal {H}}{\partial \boldsymbol {\lambda}} = \mathbf {A} (t) \mathbf {x} (t) + \mathbf {B} (t) \mathbf {u} (t) \tag {4.1.8}$$

and with the optimal control (4.1.7), the optimal state equation (4.1.8) becomes

$$\dot {\mathbf {x}} ^ {*} (t) = \mathbf {A} (t) \mathbf {x} ^ {*} (t) - \mathbf {B} (t) \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \boldsymbol {\lambda} ^ {*} (t). \tag {4.1.9}$$

Using the Hamiltonian (4.1.5), the optimal costate equation becomes
