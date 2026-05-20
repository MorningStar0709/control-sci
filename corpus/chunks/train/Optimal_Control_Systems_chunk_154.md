# 3.2 Finite-Time Linear Quadratic Regulator

Now we proceed with the linear quadratic regulator (LQR) system, that is, to keep the state near zero during the interval of interest. For the sake of completeness we shall repeat the plant and performance index equations described in the earlier section. Consider a linear, time-varying plant described by

$$\dot {\mathbf {x}} (t) = \mathbf {A} (t) \mathbf {x} (t) + \mathbf {B} (t) \mathbf {u} (t) \tag {3.2.1}$$

with a cost functional

$$
\begin{array}{l} J (\mathbf {u}) = J \left(\mathbf {x} \left(t _ {0}\right), \mathbf {u} (t), t _ {0}\right) \\ = \frac {1}{2} \mathbf {x} ^ {\prime} \left(t _ {f}\right) \mathbf {F} \left(t _ {f}\right) \mathbf {x} \left(t _ {f}\right) \\ + \frac {1}{2} \int_ {t _ {0}} ^ {t _ {f}} \left[ \mathbf {x} ^ {\prime} (t) \mathbf {Q} (t) \mathbf {x} (t) + \mathbf {u} ^ {\prime} (t) \mathbf {R} (t) \mathbf {u} (t) \right] d t \\ = \frac {1}{2} \mathbf {x} ^ {\prime} (t _ {f}) \mathbf {F} (t _ {f}) \mathbf {x} (t _ {f}) \\ + \frac {1}{2} \int_ {t _ {0}} ^ {t _ {f}} \left[ \mathbf {x} ^ {\prime} (t) \mathbf {u} ^ {\prime} (t) \right] \left[ \begin{array}{c c} \mathbf {Q} (t) & \mathbf {0} \\ \mathbf {0} & \mathbf {R} (t) \end{array} \right] \left[ \begin{array}{c} \mathbf {x} (t) \\ \mathbf {u} (t) \end{array} \right] d t \tag {3.2.2} \\ \end{array}
$$

where, the various vectors and matrices are defined in the last section. Let us note that here, the reference or desired state $\mathbf{z}(t)=0$ and hence the error $\mathbf{e}(t)=0-\mathbf{x}(t)$ itself is the state, thereby implying a state regulator system. We summarize again various assumptions as follows.

1. The control $\mathbf{u}(t)$ is unconstrained. However, in many physical situations, there are limitations on the control and state and the case of unconstrained control is discussed in a later chapter.
