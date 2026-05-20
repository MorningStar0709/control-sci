Noting that the supply pressure $p _ { s }$ is constant. the flow rate q can be written as a function of the valve displacement x and pressure difference $\Delta p ,$ or,

$$q = C _ {1} \sqrt {\frac {p _ {s} - \Delta p}{2}} \left(\frac {x _ {0}}{2} + x\right) - C _ {2} \sqrt {\frac {p _ {s} + \Delta p}{2}} \left(\frac {x _ {0}}{2} - x\right) = f (x, \Delta p)$$

By applying the linearization technique presented in Section 3–10 to this case, the linearized equation about point $x = \bar { x } , \Delta p = \Delta \bar { p } , q = \bar { q }$ is

$$q - \bar {q} = a (x - \bar {x}) + b (\Delta p - \Delta \bar {p}) \tag {4-26}$$

where

$$
\bar {q} = f (\bar {x}, \Delta \bar {p})a = \frac {\partial f}{\partial x} \Bigg | _ {x = \bar {x}, \Delta p = \Delta \bar {p}} = C _ {1} \sqrt {\frac {p _ {s} - \Delta \bar {p}}{2}} + C _ {2} \sqrt {\frac {p _ {s} + \Delta \bar {p}}{2}}
\begin{array}{l} b = \frac {\partial f}{\partial \Delta p} \Bigg | _ {x = \bar {x}, \Delta p = \Delta \bar {p}} = - \left[ \frac {C _ {1}}{2 \sqrt {2} \sqrt {p _ {s} - \Delta \bar {p}}} \left(\frac {x _ {0}}{2} + \bar {x}\right) \right. \\ \left. + \frac {C _ {2}}{2 \sqrt {2} \sqrt {p _ {s} + \Delta \bar {p}}} \left(\frac {x _ {0}}{2} - \bar {x}\right) \right] <   0 \\ \end{array}
$$

Coefficients a and b here are called valve coefficients. Equation (4–26) is a linearized mathematical model of the spool valve near an operating point $x = \bar { x } , \Delta p = \Delta \bar { p } , q = \bar { q }$ . The values of valve coefficients a and b vary with the operating point. Note that $\partial f / \partial \Delta p$ is negative and so b is negative.

Since the normal operating point is the point where $\bar { x } = 0 , \Delta \bar { p } = 0 , \bar { q } = 0$ near the, normal operating point Equation (4–26) becomes

$$q = K _ {1} x - K _ {2} \Delta p \tag {4-27}$$

where

$$K _ {1} = \left(C _ {1} + C _ {2}\right) \sqrt {\frac {p _ {s}}{2}} > 0K _ {2} = \left(C _ {1} + C _ {2}\right) \frac {x _ {0}}{4 \sqrt {2} \sqrt {p _ {s}}} > 0$$

Equation (4–27) is a linearized mathematical model of the spool valve near the origin $( \bar { x } = 0 , \Delta \bar { p } = 0 , \bar { q } = 0 . )$ Note that the region near the origin is most important in this kind of system, because the system operation usually occurs near this point.

Figure 4–18 shows this linearized relationship among $q , x ,$ , and $\Delta P$ The straight lines. shown are the characteristic curves of the linearized hydraulic servomotor. This family of curves consists of equidistant parallel straight lines, parametrized by x.
