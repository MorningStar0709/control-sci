$$
\begin{array}{l} u = \text {   control   signal   (scalar)   } \\ y = \text { output   signal   (scalar) } \\ \xi = \text { output   of   the   integrator   (state   variable   of   the   system,   scalar) } \\ r = \text { reference   input   signal   (step   function,   scalar) } \\ \end{array}

\begin{array}{l} \mathbf {A} = n \times n \text { constant   matrix } \\ \mathbf {B} = n \times 1 \text { constant   matrix } \\ \mathbf {C} = 1 \times n \text { constant   matrix } \\ \end{array}
$$

We assume that the plant given by Equation (10–31) is completely state controllable.The transfer function of the plant can be given by

$$G _ {p} (s) = \mathbf {C} (s \mathbf {I} - \mathbf {A}) ^ {- 1} \mathbf {B}$$

To avoid the possibility of the inserted integrator being canceled by the zero at the origin of the plant, we assume that $G _ { p } ( s )$ has no zero at the origin.

Assume that the reference input (step function) is applied at $t = 0 .$ . Then, for $t > 0 .$ , the system dynamics can be described by an equation that is a combination of Equations (10–31) and (10–34):

$$
\left[ \begin{array}{l} \dot {\mathbf {x}} (t) \\ \dot {\xi} (t) \end{array} \right] = \left[ \begin{array}{l l} \mathbf {A} & \mathbf {0} \\ - \mathbf {C} & 0 \end{array} \right] \left[ \begin{array}{l} \mathbf {x} (t) \\ \xi (t) \end{array} \right] + \left[ \begin{array}{l} \mathbf {B} \\ 0 \end{array} \right] u (t) + \left[ \begin{array}{l} \mathbf {0} \\ 1 \end{array} \right] r (t) \tag {10-35}
$$

We shall design an asymptotically stable system such that x(q), j(q), and u(q) approach# constant values, respectively. Then, at steady state, $\dot { \boldsymbol \xi } ( t ) = 0$ and we, $\quad \operatorname* { g e t } y ( \infty ) = r .$ .

Notice that at steady state we have

$$
\left[ \begin{array}{l} \dot {\mathbf {x}} (\infty) \\ \dot {\xi} (\infty) \end{array} \right] = \left[ \begin{array}{c c} \mathbf {A} & \mathbf {0} \\ - \mathbf {C} & 0 \end{array} \right] \left[ \begin{array}{l} \mathbf {x} (\infty) \\ \xi (\infty) \end{array} \right] + \left[ \begin{array}{c} \mathbf {B} \\ 0 \end{array} \right] u (\infty) + \left[ \begin{array}{c} \mathbf {0} \\ 1 \end{array} \right] r (\infty) \tag {10-36}
$$

Noting that $r ( t )$ is a step input, we have $r ( \infty ) = r ( t ) = r$ (constant) for $t > 0$ . By subtracting Equation (10–36) from Equation (10–35), we obtain
