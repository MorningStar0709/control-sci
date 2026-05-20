During coasting periods, $T = 0$ . Note that missile thrust comes from rocket engines, ramjet engines, or both in combination. The rocket engines use either solid or liquid propellant. Mass and inertial characteristics are commonly defined in terms of launch and burnout conditions, and equivalent sea-level impulse. The missile’s mass, m, is computed according to one of two equations, depending on which form of thrust calculation is being used. For the constant-thrust model, mass decreases linearly with time and is given by [2]

$$m = (1 / g) \{W _ {o} - (W _ {o} - W _ {f}) [ (t - t _ {1}) / t _ {b} ] \}, \tag {4.4a}$$

and for the variable thrust model,

$$m = (W _ {o} / g) [ W _ {f} / W _ {o} ] ^ {(t - t _ {1}) / t _ {b})}. \tag {4.4b}$$

During coasting, m remains constant at $W _ { o } / g$ or $W _ { f } / g$ for preignition or postburnout coasts, respectively. The aerodynamic coefficients $C _ { x }$ and $C _ { N }$ are generally expressed as functions of M and α, where the Mach number M is obtained from the missile’s velocity by the relation $M = | \mathbf { v } | / c$ . Either or both of these functions may be input to the program in tabular form. Alternatively, functional expressions must be employed. The total mass can also be expressed as

$$m (t) = m _ {L} + C _ {m} \int_ {0} ^ {t} T _ {S L} (t) d t, \tag {4.4c}$$

where

$$m _ {L} = \text { missile mass at launch },m _ {B O} = \mathrm{missilemassatmotorburnout},T _ {S L} (t) = \mathrm{motorsea-levelthrusthistory},$$

and

$$C _ {m} = (m _ {B O} - m _ {L}) / \int_ {0} ^ {t} T _ {S L} (t) d t.$$

The expression for $C _ { x }$ represents a simplified theoretical model for the axial force coefficient of a cone:

$$
C _ {x} = \left\{ \begin{array}{l l} 2 \sin^ {2} \theta_ {c} + C _ {x 2} \alpha^ {2}, & M \leq 0. 5, \\ 2 \sin^ {2} \theta_ {c} \{1. 0 + [ ((k _ {1} + k _ {2} \sin \theta_ {c}) / (k _ {3} + k _ {4} \sin \theta_ {c})) - 1. 0 \\ \quad + (k _ {5} \kappa / 2 \sin^ {2} \theta_ {c}) (M - 0. 5) \} + C _ {x 2} \alpha^ {2}, & 0. 5 \leq M \leq 0. 5, \\ 2 \sin^ {2} \theta_ {c} [ (k _ {6} + \sqrt {M ^ {2} - 1} \sin \theta_ {c}) / (k _ {7} + \sqrt {M ^ {2} - 1} \sin \theta_ {c}) ] \\ \quad + \kappa / M ^ {2} + C _ {x 2} \alpha^ {2}, & M \geq 1. 5, \end{array} \right.
$$

where $k _ { 1 } , \ldots , k _ { 7 }$ represent design values depending on the missile configuration, and $\kappa = 0$ during powered flight, and $\kappa = 1$ during coasting flight. The expression for $C _ { N }$ is a quadratic in α as follows:

$$C _ {N} = C _ {N 1} \alpha + C _ {N 2} \alpha^ {2}.$$
