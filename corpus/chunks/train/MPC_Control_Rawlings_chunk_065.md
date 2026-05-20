# 1.2.5 Constraints

The manipulated inputs (valve positions, voltages, torques, etc.) to most physical systems are bounded. We include these constraints by linear inequalities

$$E u (k) \leq e \quad k \in \mathbb {I} _ {\geq 0}$$

in which

$$
E = \left[ \begin{array}{c} I \\ - I \end{array} \right] \qquad e = \left[ \begin{array}{c} \overline {{u}} \\ - \underline {{u}} \end{array} \right]
$$

are chosen to describe simple bounds such as

$$\underline {{{u}}} \leq u (k) \leq \overline {{{u}}} \quad k \in \mathbb {I} _ {\geq 0}$$

We sometimes wish to impose constraints on states or outputs for reasons of safety, operability, product quality, etc. These can be stated as

$$F x (k) \leq f \quad k \in \mathbb {I} _ {\geq 0}$$

Practitioners find it convenient in some applications to limit the rate of change of the input, u(k) − u(k − 1). To maintain the state space form of the model, we may augment the state as

$$
\widetilde {x} (k) = \left[ \begin{array}{c} x (k) \\ u (k - 1) \end{array} \right]
$$

and the augmented system model becomes

$$
\begin{array}{l} \tilde {x} ^ {+} = \tilde {A} \tilde {x} + \tilde {B} u \\ y = \tilde {C} \tilde {x} \\ \end{array}
$$
