Also, we know from Chapter 2 that the state and costate are related by

$$\dot {\boldsymbol {\lambda}} ^ {*} (t) = - \left(\frac {\partial \mathcal {H}}{\partial \mathbf {x}}\right) _ {*} \tag {6.4.12}$$

and the optimal control $\mathbf{u}^{*}(t)$ is obtained from

$$\left(\frac {\partial \mathcal {H}}{\partial \mathbf {u}}\right) _ {*} = 0 \longrightarrow \mathbf {u} ^ {*} (t) = \mathbf {h} (\mathbf {x} ^ {*} (t), J _ {\mathbf {x}} ^ {*}, t). \tag {6.4.13}$$

Here, comparing (6.4.11) and (6.4.12), we get

$$
\begin{array}{l} \frac {d}{d t} \left(\frac {\partial J ^ {*} (\mathbf {x} ^ {*} (t) , t)}{\partial \mathbf {x} ^ {*}}\right) = \frac {d}{d t} [ \boldsymbol {\lambda} ^ {*} (t) ] \\ = - \frac {\partial \mathcal {H} \left(\mathbf {x} ^ {*} (t) , \frac {\partial J ^ {*} (\mathbf {x} ^ {*} (t) , t)}{\partial \mathbf {x}} , \mathbf {u} ^ {*} (t) , t\right)}{\partial \mathbf {x} ^ {*}}. \tag {6.4.14} \\ \end{array}
$$

Using

$$J _ {t} ^ {*} = \frac {\partial J ^ {*} (\mathbf {x} ^ {*} (t) , t)}{\partial t}; \quad J _ {\mathbf {x}} ^ {*} = \frac {\partial J ^ {*} (\mathbf {x} ^ {*} (t) , t)}{\partial \mathbf {x} ^ {*}} \tag {6.4.15}$$

The HJB equation (6.4.8) becomes

$$\boxed {J _ {t} ^ {*} + \mathcal {H} \left(\mathbf {x} ^ {*} (t), J _ {\mathbf {x}} ^ {*}, \mathbf {u} ^ {*} (t), t\right) = 0.} \tag {6.4.16}$$

This equation, in general, is a nonlinear partial differential equation in $J^{*}$ , which can be solved for $J^{*}$ . Once $J^{*}$ is known, its gradient $J_{x}^{*}$ can be calculated and the optimal control $\mathbf{u}^{*}(t)$ is obtained from (6.4.13). Often, the solution of HJB equation is very difficult. The entire procedure is summarized in Table 6.4. Let us now illustrate the

Table 6.4 Procedure Summary of Hamilton-Jacobi-Bellman (HJB) Approach
