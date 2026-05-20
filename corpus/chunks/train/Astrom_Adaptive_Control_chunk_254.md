In analogy with Eq. (4.54) we get

$$y (t + 1) = R _ {1} ^ {*} \left(q ^ {- 1}\right) \Delta u (t + 1 - d _ {0}) + \bar {y} _ {1} (t) - F _ {1} ^ {*} e (t + 1)y (t + 2) = R _ {2} ^ {*} \left(q ^ {- 1}\right) \Delta u (t + 2 - d _ {0}) + y _ {2} (t) + F _ {2} ^ {*} e (t - 2)$$

•
•
•

$$y (t + N) = R _ {N} ^ {*} \left(q ^ {- 1}\right) \Delta u (t + N - d _ {0}) + \bar {y} _ {N} (t) + F _ {N} ^ {*} e (t + N)$$

Each output value depends on future control signals (if $d > d_{0}$ ), measured inputs, and future noise signals. The equations above can be written as

$$\mathbf {y} = \mathbf {R} \Delta \mathbf {u} + \bar {\mathbf {y}} + \mathbf {e}$$

where

$$
\mathbf {y} = \left( \begin{array}{c c c} y (t + 1) & \dots & y (t + N) \end{array} \right) ^ {T}

\boldsymbol {\Delta} \mathbf {u} = \left( \begin{array}{l l l} \Delta u (t + 1 - d _ {0}) & \dots & \Delta u (t + N - d _ {0}) \end{array} \right) ^ {T}

\bar {y} = \left( \begin{array}{c c c} \bar {y} _ {1} (t) & \dots & \bar {y} _ {N} (t) \end{array} \right) ^ {T}

\mathbf {e} = \left( \begin{array}{c c c} F _ {1} ^ {*} e (t + 1) & \dots & F _ {N} ^ {*} e (t + N) \end{array} \right) ^ {T}
$$

From Eq. (4.53) it follows that the coefficients of $R_{d}^{*}$ are the first $d - d_{0} + 1$ terms of the pulse response of $q^{-d_{0}}B^{*}/(A^{*}\Delta)$ , which are the same as the first $d - d_{0} + 1$ terms of the step response of $q^{-d_{0}}B^{*}/A^{*}$ . The matrix R is thus a lower triangular matrix:

$$
\mathbf {R} = \left( \begin{array}{c c c c} r _ {0} & 0 & \dots & 0 \\ r _ {1} & r _ {0} & \dots & 0 \\ \vdots & & \ddots & \vdots \\ r _ {N - 1} & r _ {N - 2} & \dots & r _ {0} \end{array} \right)
$$

If there is a dead time in the system, $d_{0} > 1$ , then the first $d_{0} - 1$ rows of R will be zero. Also introduce

$$
\mathbf {y} _ {\mathbf {m}} = \left( \begin{array}{l l l} y _ {m} (t + 1) & \dots & y _ {m} (t + N) \end{array} \right) ^ {T}
$$

The expected value of the loss function can be written as

$$
\begin{array}{l} J (1, N, N) = E \left\{\left(\mathbf {y} - \mathbf {y} _ {\mathbf {m}}\right) ^ {T} \left(\mathbf {y} - \mathbf {y} _ {\mathbf {m}}\right) + \rho \boldsymbol {\Delta} \mathbf {u} ^ {T} \boldsymbol {\Delta} \mathbf {u} \right\} \\ = \left(\mathbf {R} \boldsymbol {\Delta} \mathbf {u} + \bar {\mathbf {y}} - \mathbf {y} _ {\mathrm{m}}\right) ^ {T} \left(\mathbf {R} \boldsymbol {\Delta} \mathbf {u} + \bar {\mathbf {y}} - \mathbf {y} _ {\mathrm{m}}\right) + \rho \boldsymbol {\Delta} \mathbf {u} ^ {T} \boldsymbol {\Delta} \mathbf {u} \tag {4.65} \\ \end{array}
$$
