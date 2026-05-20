Show that the closed-loop poles of the system comprise the closed-loop poles due to pole placement Cthe eigenvalues of matrix $\left( \mathbf { A } - \mathbf { B } \mathbf { K } \right) ]$ ] and the closed-loop poles due to the minimumorder observer [the eigenvalues of matrix $\left( { \bf A } _ { b b } - { \bf K } _ { e } { \bf A } _ { a b } \right) ]$

Solution. The error equation for the minimum-order observer may be derived as given by Equation (10–94), rewritten thus:

$$\dot {\mathbf {e}} = \left(\mathbf {A} _ {b b} - \mathbf {K} _ {e} \mathbf {A} _ {a b}\right) \mathbf {e} \tag {10-164}$$

where

$$\mathbf {e} = \mathbf {x} _ {b} - \widetilde {\mathbf {x}} _ {b}$$

From Equations (10–162) and (10–163), we obtain

$$
\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} - \mathbf {B} \mathbf {K} \widetilde {\mathbf {x}} = \mathbf {A} \mathbf {x} - \mathbf {B} \mathbf {K} \left[ \begin{array}{c} x _ {a} \\ \widetilde {\mathbf {x}} _ {b} \end{array} \right] = \mathbf {A} \mathbf {x} - \mathbf {B} \mathbf {K} \left[ \begin{array}{c} x _ {a} \\ \mathbf {x} _ {b} - \mathbf {e} \end{array} \right]

= \mathbf {A} \mathbf {x} - \mathbf {B} \mathbf {K} \left\{\mathbf {x} - \left[ \begin{array}{l} 0 \\ \dots \\ \mathbf {e} \end{array} \right] \right\} = (\mathbf {A} - \mathbf {B} \mathbf {K}) \mathbf {x} + \mathbf {B} \mathbf {K} \left[ \begin{array}{l} 0 \\ \dots \\ \mathbf {e} \end{array} \right] \tag {10-165}
$$

Combining Equations (10–164) and (10–165) and writing

$$
\mathbf {K} = \left[ \begin{array}{c c} K _ {a} & \mathbf {K} _ {b} \end{array} \right]
$$

we obtain

$$
\left[ \begin{array}{c} \dot {\mathbf {x}} \\ \dot {\mathbf {e}} \end{array} \right] = \left[ \begin{array}{c c} \mathbf {A} - \mathbf {B K} & \mathbf {B K} _ {b} \\ \mathbf {0} & \mathbf {A} _ {b b} - \mathbf {K} _ {e} \mathbf {A} _ {a b} \end{array} \right] \left[ \begin{array}{c} \mathbf {x} \\ \mathbf {e} \end{array} \right] \tag {10-166}
$$

Equation (10–166) describes the dynamics of the observed-state feedback control system with a minimum-order observer. The characteristic equation for this system is

$$
\left| \begin{array}{c c} s \mathbf {I} - \mathbf {A} + \mathbf {B K} & - \mathbf {B K} _ {b} \\ \mathbf {0} & s \mathbf {I} - \mathbf {A} _ {b b} + \mathbf {K} _ {e} \mathbf {A} _ {a b} \end{array} \right| = 0
$$

or

$$\left| s \mathbf {I} - \mathbf {A} + \mathbf {B K} \right| \left| s \mathbf {I} - \mathbf {A} _ {b b} + \mathbf {K} _ {e} \mathbf {A} _ {a b} \right| = 0$$
