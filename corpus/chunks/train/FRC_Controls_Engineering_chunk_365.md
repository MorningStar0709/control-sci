# 12.1 DC motor

We will be deriving a first-order model for a DC motor. A second-order model would include the inductance of the motor windings as well, but we’re assuming the time constant of the inductor is small enough that its affect on the model behavior is negligible for FRC use cases (see subsection 6.10.7 for a demonstration of this for a real DC motor).

![](image/f90832b79ab388390f906051bd1989f123ef6e0233ac48d71a0e273190096d87.jpg)

For the brushless motor commutation methods currently available in FRC (trapezoidal commutation, field-oriented control), brushed and brushless DC motors have the same dynamics. However, more advanced commutation methods can break the linear back-EMF assumption of the brushed motor model.

The first-order model will only require numbers from the motor’s datasheet. The secondorder model would require measuring the motor inductance as well, which generally isn’t in the datasheet. It can be difficult to measure accurately without the right equipment.
