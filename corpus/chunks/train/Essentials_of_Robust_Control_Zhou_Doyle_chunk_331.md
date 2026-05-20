# 13.1 Introduction to Regulator Problem

Consider the following dynamical system:

$$\dot {x} = A x + B _ {2} u, \quad x (t _ {0}) = x _ {0} \tag {13.1}$$

where $x _ { 0 }$ is given but arbitrary. Our objective is to find a control function $u ( t )$ defined on $[ t _ { 0 } , T ]$ , which can be a function of the state $x ( t )$ , such that the state $x ( t )$ is driven to a (small) neighborhood of origin at time T . This is the so-called regulator problem. One might suggest that this regulator problem can be trivially solved for any $T > t _ { 0 }$ if the system is controllable. This is indeed the case if the controller can provide arbitrarily large amount of energy since, by the definition of controllability, one can immediately construct a control function that will drive the state to zero in an arbitrarily short time. However, this is not practical since any physical system has energy limitation $( \mathrm { i . e . } ,$ , the actuator will eventually saturate). Furthermore, large control action can easily drive the system out of the region, where the given linear model is valid. Hence certain limitations have to be imposed on the control in practical engineering implementation. The constraints on control u may be measured in many different ways; for example,

$$\int_ {t _ {0}} ^ {T} \| u \| d t, \quad \int_ {t _ {0}} ^ {T} \| u \| ^ {2} d t, \quad \sup _ {t \in [ t _ {0}, T ]} \| u \|;$$

That is, in terms of $\mathcal { L } _ { 1 }$ norm, $\mathcal { L } _ { 2 }$ norm, and $\mathcal { L } _ { \infty }$ norm $_ { \mathrm { o r } } ,$ more generally, weighted $\mathcal { L } _ { 1 }$ norm, $\mathcal { L } _ { 2 }$ norm, and $\mathcal { L } _ { \infty }$ norm

$$\int_ {t _ {0}} ^ {T} \| W _ {u} u \| d t, \quad \int_ {t _ {0}} ^ {T} \| W _ {u} u \| ^ {2} d t, \quad \sup _ {t \in [ t _ {0}, T ]} \| W _ {u} u \|$$

for some constant weighting matrix $W _ { u }$ .

Similarly, one might also want to impose some constraints on the transient response $x ( t )$ in a similar fashion:

$$\int_ {t _ {0}} ^ {T} \| W _ {x} x \| d t, \quad \int_ {t _ {0}} ^ {T} \| W _ {x} x \| ^ {2} d t, \quad \sup _ {t \in [ t _ {0}, T ]} \| W _ {x} x \|$$
