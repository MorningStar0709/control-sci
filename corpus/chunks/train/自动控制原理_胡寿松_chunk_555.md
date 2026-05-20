$$B _ {1} = \frac {1}{\pi} \int_ {0} ^ {2 \pi} y (t) \sin \omega t d \omega t = \frac {4}{\pi} \int_ {0} ^ {\frac {\pi}{2}} y (t) \sin \omega t d \omega t= \frac {4}{\pi} \left[ \int_ {\psi_ {1}} ^ {\psi_ {2}} [ K (A \sin \omega t - \Delta) ] \sin \omega t d \omega t + \int_ {\psi_ {2}} ^ {\frac {\pi}{2}} K (a - \Delta) \sin \omega t d \omega t \right]= \frac {4 K}{\pi} \left[ \int_ {\psi_ {1}} ^ {\psi_ {2}} \left(A \sin^ {2} \omega t - \Delta \sin \omega t\right) d \omega t + \int_ {\psi_ {2}} ^ {\frac {\pi}{2}} (a - \Delta) \sin \omega t d \omega t \right]= \frac {4 K}{\pi} \left[ A \left(\frac {\omega t}{2} - \frac {1}{4} \sin 2 \omega t\right) \Big | _ {\psi_ {1}} ^ {\psi_ {2}} + \Delta \cos \omega t \Big | _ {\psi_ {1}} ^ {\psi_ {2}} - (a - \Delta) \cos \omega t \Big | _ {\psi_ {2}} ^ {\frac {\pi}{2}} \right]= \frac {4 K}{\pi} \left[ \frac {A}{2} \left(\psi_ {2} - \psi_ {1}\right) - \frac {A}{4} \sin 2 \psi_ {2} + \frac {A}{4} \sin 2 \psi_ {1} + \Delta \cos \psi_ {2} - \Delta \cos \psi_ {1} + (a - \Delta) \cos \psi_ {2} \right]= \frac {4 K}{\pi} \left[ \frac {A}{2} \arcsin \frac {a}{A} - \frac {A}{2} \arcsin \frac {\Delta}{A} - \frac {A}{2} \cdot \frac {a}{A} \sqrt {1 - \left(\frac {a}{A}\right) ^ {2}} \right.\left. + \frac {A}{2} \cdot \frac {\Delta}{A} \sqrt {1 - \left(\frac {\Delta}{A}\right) ^ {2}} + a \sqrt {1 - \left(\frac {a}{A}\right) ^ {2}} - \Delta \sqrt {1 - \left(\frac {\Delta}{A}\right) ^ {2}} \right]= \frac {2 K A}{\pi} \left[ \arcsin \frac {a}{A} - \arcsin \frac {\Delta}{A} + \frac {a}{A} \sqrt {1 - \left(\frac {a}{A}\right) ^ {2}} - \frac {\Delta}{A} \sqrt {1 - \left(\frac {\Delta}{A}\right) ^ {2}} \right]$$

死区饱和特性的描述函数

$$N (A) = \frac {2 K}{\pi} \left[ \arcsin \frac {a}{A} - \arcsin \frac {\Delta}{A} + \frac {a}{A} \sqrt {1 - \left(\frac {a}{A}\right) ^ {2}} \right.\left. - \frac {\Delta}{A} \sqrt {1 - \left(\frac {\Delta}{A}\right) ^ {2}} \right], \quad A \geqslant a \tag {8-70}$$

取 $\Delta = 0$ ，由式(8-70)得饱和特性的描述函数

$$N (A) = \frac {2 K}{\pi} \left[ \arcsin \frac {a}{A} + \frac {a}{A} \sqrt {1 - \left(\frac {a}{A}\right) ^ {2}} \right], \quad A \geqslant a \tag {8-71}$$

对于死区特性， $\psi_{2} = \frac{\pi}{2}$ 。由式(8-69)得 $\frac{a}{A} = 1$ ，则由式(8-70)得死区特性的描述函数

$$N (A) = \frac {2 K}{\pi} \left[ \frac {\pi}{2} - \arcsin \frac {\Delta}{A} - \frac {\Delta}{A} \sqrt {1 - \left(\frac {\Delta}{A}\right) ^ {2}} \right], \quad A \geqslant \Delta \tag {8-72}$$
