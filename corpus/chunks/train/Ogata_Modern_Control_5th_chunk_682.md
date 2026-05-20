# 9–7 OBSERVABILITY

In this section we discuss the observability of linear systems. Consider the unforced system described by the following equations:

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} \tag {9-63}\mathbf {y} = \mathbf {C x} \tag {9-64}$$

The system is said to be completely observable if every state $\mathbf { x } \big ( t _ { 0 } \big )$ can be determined from the observation of y(t) over a finite time interval, $t _ { 0 } \leq t \leq t _ { 1 }$ The system is, there-. fore, completely observable if every transition of the state eventually affects every element of the output vector. The concept of observability is useful in solving the problem of reconstructing unmeasurable state variables from measurable variables in the minimum possible length of time. In this section we treat only linear, time-invariant systems. Therefore, without loss of generality, we can assume that $t _ { 0 } = 0$ .

The concept of observability is very important because, in practice, the difficulty encountered with state feedback control is that some of the state variables are not accessible for direct measurement, with the result that it becomes necessary to estimate the unmeasurable state variables in order to construct the control signals. It will be shown in Section 10–5 that such estimates of state variables are possible if and only if the system is completely observable.

In discussing observability conditions, we consider the unforced system as given by Equations (9–63) and (9–64). The reason for this is as follows: If the system is described by

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} \mathbf {u}\mathbf {y} = \mathbf {C x} + \mathbf {D u}$$

then

$$\mathbf {x} (t) = e ^ {\mathbf {A} t} \mathbf {x} (0) + \int_ {0} ^ {t} e ^ {\mathbf {A} (t - \tau)} \mathbf {B u} (\tau) d \tau$$

and y(t) is

$$\mathbf {y} (t) = \mathbf {C} e ^ {\mathbf {A} t} \mathbf {x} (0) + \mathbf {C} \int_ {0} ^ {t} e ^ {\mathbf {A} (t - \tau)} \mathbf {B u} (\tau) d \tau + \mathbf {D u}$$

Since the matrices A, B, C, and D are known and u(t) is also known, the last two terms on the right-hand side of this last equation are known quantities. Therefore, they may be subtracted from the observed value of y(t). Hence, for investigating a necessary and sufficient condition for complete observability, it suffices to consider the system described by Equations (9–63) and (9–64).
