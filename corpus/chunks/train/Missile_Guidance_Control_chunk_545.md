$\mathbf { R } _ { j } ^ { H }$ = approximate midpoint position for this cycle,

${ \bf R } _ { j - 1 }$ = position at the end of the preceding cycle,

$\mathbf { V } _ { j - 1 }$ = velocity at the end of the preceding cycle,

$\Delta \mathbf { V } _ { g }$ = estimated time integral of gravitation across the computation cycle,

J = coefficient of the second zonal harmonic in the expansion of the gravitational field,

D = coefficient of the fourth zonal harmonic in the expansion of the gravitational field,

$\Delta t$ = computation cycle time.

Equations:

$$\mathbf {R} _ {j} ^ {H} = \mathbf {R} _ {j - 1} + (\Delta t / 2) \mathbf {V} _ {j - 1}, \tag {1}(R ^ {2}) = (\mathbf {R} _ {j} ^ {H} \cdot \mathbf {R} _ {j} ^ {H}), \tag {2}(1 / R) _ {j} = (1 / R) _ {j - 1} [ 1. 5 - 0. 5 (R ^ {2}) (1 / R) _ {j - 1} ^ {2} ], \tag {3}(a ^ {2} / R ^ {2}) = [ (a) (1 / R) _ {j} ] ^ {2}, \tag {4}(\sin^ {2} \psi) = [ (R _ {3 j} ^ {H}) (1 / R) _ {j} ] ^ {2}, \tag {5}g = \mu (1 / R _ {j} ^ {3}) [ 1 + J (a ^ {2} / R ^ {2}) \{1 - 5 (\sin^ {2} \psi) \}+ 3 D (a ^ {2} / R ^ {2}) ^ {2} \{(1 / 7) - (\sin^ {2} \psi) \} \{2 - 3 (\sin^ {2} \psi) \} ], \tag {6}g _ {1} = - R _ {1} ^ {H} g, \tag {7}g _ {2} = - R _ {2} ^ {H} g, \tag {8}g _ {3} = - R _ {3} ^ {H} (g + 2 \mu (1 / R) ^ {3}) (a ^ {2} / R ^ {2}) [ J + 2 D (a ^ {2} / R ^ {2}) ((3 / 7) - \sin^ {2} \psi) ], (9)\Delta \mathbf {V} _ {g j} = \Delta t \mathbf {g} \tag {10}$$

(see also the example in Section 6.8; in that example, $J _ { 2 } = J$ and $J _ { 4 } = D )$ .

Integration Errors: For a given missile path during the computation cycle, gravitation may be expressed as a function of time only. Now, expanding $\pmb { g }$ about the cycle midpoint time gives

$$\mathbf {g} (t) = \mathbf {g} _ {H} + \frac {d \mathbf {g} _ {H} (t - t _ {H})}{d t} + (1 / 2) \left(\frac {d ^ {2} \mathbf {g} (t - t _ {H})}{d t ^ {2}}\right) + \dots .$$

Integrating g(t) between $( t _ { H } - ( \Delta t / 2 ) )$ and $( t _ { H } + ( \Delta t / 2 ) )$ ) gives

$$\Delta \mathbf {V} _ {g} = \int_ {0} ^ {t} \mathbf {g} (t) d t = \Delta t \mathbf {g} _ {H} + (\Delta t ^ {3} / 2 4)) \left(\frac {d ^ {2} \mathbf {g} (t _ {H})}{d t ^ {2}}\right) + \text { higher (even) derivatives }.$$

Since the equations use $\Delta { \bf V } _ { g } \cong \Delta t { \bf g } _ { H }$ , the error (for the j th computation cycle) is

$$\varepsilon (\Delta \mathbf {V} _ {g}) _ {j} \cong (\Delta t ^ {3} / 2 4)) \left(\frac {d ^ {2} \mathbf {g} (t _ {H})}{d t ^ {2}}\right) _ {j}.$$

If these errors are summed to time T , the total velocity error is
