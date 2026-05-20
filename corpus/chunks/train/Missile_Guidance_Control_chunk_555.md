$$
\begin{array}{l} \mathbf {r} _ {v} (t) = \mathbf {r} _ {v} \left(t _ {o}\right) + \int_ {t _ {0}} ^ {t} \mathbf {V} _ {v} (t) d t \\ = \mathbf {r} _ {v} (t _ {o}) + \int_ {t _ {0}} ^ {t} \mathbf {V} _ {v} (t _ {o}) d t + \int_ {t _ {0}} ^ {t} \int_ {t _ {0}} ^ {t} \mathbf {f} d t d t \\ = \mathbf {r} _ {v} (t _ {o}) + \mathbf {V} _ {v} (t _ {o}) (t - t _ {o}) + \int_ {t _ {0}} ^ {t} \int_ {t _ {0}} ^ {t} \mathbf {f} d t d t \tag {5} \\ \end{array}
$$

where $\mathbf { r } _ { v } ( \mathfrak { t } _ { o } )$ is the vehicle position at time $t _ { o }$ . Now, in order for the vehicle to impact the target at some time $t _ { I }$ , it is necessary that

$$\mathbf {r} _ {t} (t _ {i}) = \mathbf {r} _ {v} (t _ {i}). \tag {6}$$

Substituting (1) and (5) into (6) yields

$$\mathbf {r} _ {t} (t _ {o}) + \int_ {t _ {0}} ^ {t} \left(\frac {d \mathbf {r} _ {t}}{d t}\right) d t = \mathbf {r} _ {v} (t _ {o}) + \mathbf {V} _ {v} (t _ {o}) (t - t _ {o}) + \int_ {t _ {0}} ^ {t} \int_ {t _ {0}} ^ {t} \mathbf {f} d t d t. \tag {7}$$

Equation (7) is the generalized form of the hit equation discussed earlier. If we let time $\left( t _ { o } \right)$ be the thrust cut-off time for the ballistic missile under consideration, we see that (7) can be satisfied if we control both vehicle position and velocity.

Long-range ballistic missiles, however, use exclusively forms of velocity control. Two primary reasons are (1) the complexity of the guidance if both position and velocity are controlled, and (2) the fact that impulsive corrections can be made to velocity, which is not true of position. Therefore, all long-range ballistic missile guidance systems effect guidance by determining and obtaining the correct ${ \bf V } _ { v } ( t _ { o } )$ in (7) for the position $\mathbf { r } _ { v } ( t _ { o } )$ . The following are several of the possible “required velocity” schemes of guidance.

(1) Required Velocity: Amplitude and Directional Control Scheme From (7) we see that there are seven variables on the right-hand side of the equation. These are (a) 3 position variables, (b) 3 required velocity variables, and (c) the time of flight $( t _ { f f } = t _ { i } - t _ { o } )$ . Since we wish to effect guidance as a function of vehicle position, it is therefore necessary to apply a constraint to (7) in order to reduce the dependent variables to three. For the scheme to be described in this section, the following constraint is used:
