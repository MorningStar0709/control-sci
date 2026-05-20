# Solution.

(a) Impulse response: Referring to Equation (9–43), the solution to the given state equation is

$$\mathbf {x} (t) = e ^ {\mathbf {A} (t - t _ {0})} \mathbf {x} (t _ {0}) + \int_ {t _ {0}} ^ {t} e ^ {\mathbf {A} (t - \tau)} \mathbf {B u} (\tau) d \tau$$

Substituting $t _ { 0 } = 0 ^ { - }$ – into this solution, we obtain

$$\mathbf {x} (t) = e ^ {\mathbf {A} t} \mathbf {x} (0 -) + \int_ {0 -} ^ {t} e ^ {\mathbf {A} (t - \tau)} \mathbf {B u} (\tau) d \tau$$

Let us write the impulse input ${ \bf \delta u } ( t )$ as

$$\mathbf {u} (t) = \delta (t) \mathbf {w}$$

where w is a vector whose components are the magnitudes of r impulse functions applied at t=0. The solution of the state equation when the impulse input $\delta ( t )$ w is given at $t = 0$ is

$$
\begin{array}{l} \mathbf {x} (t) = e ^ {\mathbf {A} t} \mathbf {x} (0 -) + \int_ {0 -} ^ {t} e ^ {\mathbf {A} (t - \tau)} \mathbf {B} \delta (\tau) \mathbf {w} d \tau \\ = e ^ {\mathbf {A} t} \mathbf {x} (0 -) + e ^ {\mathbf {A} t} \mathbf {B} \mathbf {w} \tag {9-95} \\ \end{array}
$$

(b) Step response: Let us write the step input ${ \bf \delta u } ( t )$ as

$$\mathbf {u} (t) = \mathbf {k}$$

where k is a vector whose components are the magnitudes of r step functions applied at $t = 0$ . The solution to the step input at t=0 is given by

$$
\begin{array}{l} \mathbf {x} (t) = e ^ {\mathbf {A} t} \mathbf {x} (0) + \int_ {0} ^ {t} e ^ {\mathbf {A} (t - \tau)} \mathbf {B k} d \tau \\ = e ^ {\mathbf {A} t} \mathbf {x} (0) + e ^ {\mathbf {A} t} \left[ \int_ {0} ^ {t} \left(\mathbf {I} - \mathbf {A} \tau + \frac {\mathbf {A} ^ {2} \tau^ {2}}{2 !} - \dots\right) d \tau \right] \mathbf {B k} \\ = e ^ {\mathbf {A} t} \mathbf {x} (0) + e ^ {\mathbf {A} t} \left(\mathbf {I} t - \frac {\mathbf {A} t ^ {2}}{2 !} + \frac {\mathbf {A} ^ {2} t ^ {3}}{3 !} - \dots\right) \mathbf {B k} \\ \end{array}
$$

If A is nonsingular, then this last equation can be simplified to give

$$
\begin{array}{l} \mathbf {x} (t) = e ^ {\mathbf {A} t} \mathbf {x} (0) + e ^ {\mathbf {A} t} \left[ - (\mathbf {A} ^ {- 1}) \left(e ^ {- \mathbf {A} t} - \mathbf {I}\right) \right] \mathbf {B k} \\ = e ^ {\mathbf {A} t} \mathbf {x} (0) + \mathbf {A} ^ {- 1} \left(e ^ {\mathbf {A} t} - \mathbf {I}\right) \mathbf {B k} \tag {9-96} \\ \end{array}
$$

(c) Ramp response: Let us write the ramp input ${ \bf \delta u } ( t )$ as

$$\mathbf {u} (t) = t \mathbf {v}$$

where v is a vector whose components are magnitudes of ramp functions applied at $t = 0$ .The solution to the ramp input tv given at $t = 0$ is
