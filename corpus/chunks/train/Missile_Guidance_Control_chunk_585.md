# Normal to Plane

Vector Error Equations:

$$\delta \mathbf {V} = [ (\partial \mathbf {V} _ {L} / \partial n) _ {\hat {\mathbf {n}}} \delta n + (\partial \mathbf {V} _ {L} / \partial V _ {n}) _ {\hat {\mathbf {n}}} \delta V _ {n} ] \hat {\mathbf {n}},\delta \mathbf {L} = [ (\partial \mathbf {L} / \partial n) _ {\hat {\mathbf {n}}} \delta n + (\partial \mathbf {L} / \partial V _ {n}) _ {\hat {\mathbf {n}}} \delta V _ {n} ] \hat {\mathbf {n}}.$$

Velocity Error Coefficients:

$$
\begin{array}{l} (\partial \mathbf {V} _ {L} / \partial n) _ {\hat {\mathbf {n}}} = \partial V _ {L} / \partial n, \\ (\partial \mathbf {V} _ {L} / \partial V _ {n}) _ {\hat {\mathbf {n}}} = \partial V _ {L} / \partial V _ {n}. \\ \end{array}
$$

Velocity Error Partials:

$$\partial V _ {L} / \partial n = (- V / r _ {o}) [ (\cos (\gamma - \theta^ {\prime}) - \cos \gamma) / \lambda \sin^ {2} \gamma) ],\partial V _ {L} / \partial V _ {n} = 1 - \left\{\left(1 - \cos \theta^ {\prime}\right) / \lambda \sin^ {2} \gamma \right\}.$$

Position Error Coefficients:

$$
\begin{array}{l} (\partial \mathbf {L} / \partial n) _ {\hat {\mathbf {n}}} = \partial L / \partial n, \\ (\partial \mathbf {L} / \partial V _ {n}) _ {\hat {\mathbf {n}}} = \partial L / \partial V _ {n}. \\ \end{array}
$$

Position Error Partials:

$$\partial L / \partial n = r _ {1} \sin [ \gamma - (\theta_ {1} - \theta_ {o}) ] / r _ {o} \sin \gamma ,\partial L / \partial V _ {n} = r _ {1} \sin (\theta_ {1} - \theta_ {o}) / V \sin \gamma .$$

Example. In this example we will discuss the error sensitivities of the various parameters describing the motion of a ballistic missile. Specifically, we will derive the error sensitivities of the free-fall time-of-flight (tff ), the semimajor axis (a), the eccentricity (e), etc. We begin the development with the free-fall time-of-flight, (6.92),

$$
\begin{array}{l} t _ {f f} = (\sqrt {a ^ {3} / \mu}) [ E _ {2} - E _ {1} - e (\sin E _ {2} - \sin E _ {1}) ] \\ = (\sqrt {a ^ {3} / \mu}) [ E _ {2} - E _ {1} - e \sin E _ {2} + e \sin E _ {1} ], \\ \end{array}
$$

where the $E \ ' \mathbf { s }$ are the eccentric anomalies of the initial and final points. Now, taking the partial derivative of the free-fall time-of-flight, we have
