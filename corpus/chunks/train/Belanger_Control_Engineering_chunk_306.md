# 6.2.2 The dc Steady State

The steady-state error under constant input is perhaps the most important control specification. In regulation problems, the objective is for the output to equal a constant set point. A steady-state error appears as a bias; it is always present.

Furthermore, a regulation problem nearly always includes a constant disturbance, for the following reason. When we linearize about an operating point according to Section 2.6 (Chapter 2), we normally refer inputs, outputs, and states to their values in the desired dc steady state. The output is referred to $y^{*} = y_{d}$ , so that

$$\Delta y = y - y ^ {*} = y - y _ {d} = - e$$

which is defined in terms of quantities that are known or measured and do not depend on the model.

On the other hand, the input is referred to $u^{*}$ , which is the constant value of $u$ that results in a steady-state output of $y^{*} = y_{d}$ . The value of $u^{*}$ calculated by the model is not $u^{*}$ but some approximation $\widehat{u}^{*}$ . The control input $u$ is obtained by adding the quantity $\Delta u$ , the input to the linearized system, to $\widehat{u}^{*}$ . Thus,

$$u = \Delta u + \widehat {u} ^ {*} = \Delta u + (\widehat {u} ^ {*} - u ^ {*}) + u ^ {*}.$$

Therefore, when the input is referred to the true $u^{*}$ , a constant disturbance $\widehat{u}^{*}-u^{*}$ , of unknown magnitude, is effectively added to the controller-generated input $\Delta u$ . This constant disturbance at the input can be referred to the output, where it becomes a constant (or possibly a ramp, or higher-order integral of the step function).

For a single-degree-of-freedom (1-DOF) system, recall that

$$\frac {e}{y _ {d}} = 1 - H _ {d} = S. \tag {6.1}$$

If $y_{d}(t) = Au_{-1}(t)$ , a step, then

$$e (s) = S (s) \frac {A}{s}. \tag {6.2}$$

By the final value theorem, the dc steady-state error is

$$e _ {s s} = \lim _ {t \rightarrow \infty} e (t) = \lim _ {s \rightarrow 0} s e (s) = A \lim _ {s \rightarrow 0} S (s). \tag {6.3}$$

Equation 6.3 assumes that the time limit exists, which is tantamount to assuming $S(s)$ to be stable. Equation 6.3 states that the steady-state error response to a set-point step of height $A$ is $AS(0)$ , if $S(0)$ exists. Since $y / d = H_{wd}(s) = S(s)$ , that is also the steady-state error for a step $A$ in $d(t)$ , the disturbance applied to the output.

From Chapter 4, Equation 6.3 is written in terms of the loop gain $L(s)$ as

$$e _ {s s} = A \lim _ {s \rightarrow 0} \frac {1}{1 + L (s)}. \tag {6.4}$$

It is clear from Equation 6.4 that the key to a small steady-state error is to make $\lim_{s\to 0}L(s)$ large.

If $L(0)$ exists, then

$$e _ {s s} = \frac {A}{1 + L (0)} = \frac {A}{1 + k _ {p}}. \tag {6.5}$$

Here, $k_{p} = L(0)$ is called the position constant.
