[See Problems A–10–2 and A–10–3 for the derivation of Equations (10–8) and (10–9).] Equation (10–7) is in the controllable canonical form.Thus, given a state equation, Equation (10–1), it can be transformed into the controllable canonical form if the system is completely state controllable and if we transform the state vector x into state vector  xˆ by use of the transformation matrix T given by Equation (10–4).

Let us choose a set of the desired eigenvalues as $\mu _ { 1 } , \mu _ { 2 } , \ldots , \mu _ { n }$ . Then the desired characteristic equation becomes

$$(s - \mu_ {1}) (s - \mu_ {2}) \dots (s - \mu_ {n}) = s ^ {n} + \alpha_ {1} s ^ {n - 1} + \dots + \alpha_ {n - 1} s + \alpha_ {n} = 0 \tag {10-10}$$

Let us write

$$
\mathbf {K T} = \left[ \begin{array}{l l l l} \delta_ {n} & \delta_ {n - 1} & \dots & \delta_ {1} \end{array} \right] \tag {10-11}
$$

When $\boldsymbol { u } = - \mathbf { K } \mathbf { T } \hat { \mathbf { x } }$ is used to control the system given by Equation (10–7), the system equation becomes

$$\dot {\hat {\mathbf {x}}} = \mathbf {T} ^ {- 1} \mathbf {A} \mathbf {T} \hat {\mathbf {x}} - \mathbf {T} ^ {- 1} \mathbf {B} \mathbf {K} \mathbf {T} \hat {\mathbf {x}}$$

The characteristic equation is

$$\left| s \mathbf {I} - \mathbf {T} ^ {- 1} \mathbf {A T} + \mathbf {T} ^ {- 1} \mathbf {B K T} \right| = 0$$

This characteristic equation is the same as the characteristic equation for the system, defined by Equation (10–1), when is used as the control signal. This can beu = -Kx seen as follows: Since

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} \mathbf {u} = (\mathbf {A} - \mathbf {B} \mathbf {K}) \mathbf {x}$$

the characteristic equation for this system is

$$\left| s \mathbf {I} - \mathbf {A} + \mathbf {B K} \right| = \left| \mathbf {T} ^ {- 1} (s \mathbf {I} - \mathbf {A} + \mathbf {B K}) \mathbf {T} \right| = \left| s \mathbf {I} - \mathbf {T} ^ {- 1} \mathbf {A T} + \mathbf {T} ^ {- 1} \mathbf {B K T} \right| = 0$$

Now let us simplify the characteristic equation of the system in the controllable canonical form. Referring to Equations (10–8), (10–9), and (10–11), we have
