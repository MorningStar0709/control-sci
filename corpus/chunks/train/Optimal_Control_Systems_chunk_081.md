# 2.3.2 Discussion on Euler-Lagrange Equation

We provide some comments on the Euler-Lagrange equation [47, 46].

1. The Euler-Lagrange equation (2.3.14) can be written in many different forms. Thus (2.3.14) becomes

$$V _ {x} - \frac {d}{d t} (V _ {\dot {x}}) = 0 \tag {2.3.16}$$

where,

$$V _ {x} = \frac {\partial V}{\partial x} = V _ {x} (x ^ {*} (t), \dot {x} ^ {*} (t), t); \quad V _ {\dot {x}} = \frac {\partial V}{\partial \dot {x}} = V _ {\dot {x}} (x ^ {*} (t), \dot {x} ^ {*} (t), t). \tag {2.3.17}$$

Since $V$ is a function of three arguments $x^{*}(t)$ , $\dot{x}^{*}(t)$ , and $t$ , and

that $x^{*}(t)$ and $\dot{x}^{*}(t)$ are in turn functions of $t$ , we get

$$
\begin{array}{l} \frac {d}{d t} \left(\frac {\partial V}{\partial \dot {x}}\right) _ {*} = \frac {d}{d t} \left(\frac {\partial V (x ^ {*} (t) , \dot {x} ^ {*} (t) , t)}{\partial \dot {x}}\right) _ {*}, \\ = \frac {d}{d t} \left(\frac {\partial^ {2} V}{\partial x \partial \dot {x}} d x + \frac {\partial^ {2} V}{\partial \dot {x} \partial \dot {x}} d \dot {x} + \frac {\partial^ {2} V}{\partial t \partial \dot {x}} d t\right) _ {*}, \\ = \left(\frac {\partial^ {2} V}{\partial x \partial \dot {x}}\right) _ {*} \left(\frac {d x}{d t}\right) _ {*} + \left(\frac {\partial^ {2} V}{\partial \dot {x} \partial \dot {x}}\right) _ {*} \left(\frac {d ^ {2} x}{d t ^ {2}}\right) _ {*} + \left(\frac {\partial^ {2} V}{\partial t \partial \dot {x}}\right) _ {*} \\ = V _ {x \dot {x}} \dot {x} ^ {*} (t) + V _ {\dot {x} \dot {x}} \ddot {x} ^ {*} (t) + V _ {t \dot {x}}. \tag {2.3.18} \\ \end{array}
$$

Combining (2.3.16) and (2.3.18), we get an alternate form for the EL equation as

$$\boxed {V _ {x} - V _ {t \dot {x}} - V _ {x \dot {x}} \dot {x} ^ {*} (t) - V _ {\dot {x} \dot {x}} \ddot {x} ^ {*} (t) = 0.} \tag {2.3.19}$$

2. The presence of $\frac{d}{dt}$ and/or $\dot{x}^*(t)$ in the EL equation (2.3.14) means that it is a differential equation.

3. In the EL equation (2.3.14), the term $\frac{\partial V(x^{*}(t),\dot{x}^{*}(t),t)}{\partial\dot{x}}$ is in general a function of $x^{*}(t)$ , $\dot{x}^{*}(t)$ , and t. Thus when this function is differentiated w.r.t. t, $\ddot{x}^{*}(t)$ may be present. This means that the differential equation (2.3.14) is in general of second order. This is also evident from the alternate form (2.3.19) for the EL equation.
