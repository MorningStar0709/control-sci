# The δ-Operator

The system (9.21) can be written as

$$x (k + 1) = x (k) + h (\bar {F} x (k) + \bar {G} y (k)) \tag {9.22}$$

where

$$h \bar {F} = F - 1h \bar {G} = G$$

Instead of the shift operator we can now introduce the $\delta$ -operator that is defined by

$$\delta = \frac {q - 1}{h} \tag {9.23}$$

Equation (9.22) can now be written as

$$\delta x (k) = \bar {F} x (k) + \bar {G} y (k)$$

A general pulse-transfer operator can be transformed from shift form to $\delta$ -form as

$$H (q) = \frac {B (q)}{A (q)} = \frac {B (\delta h + 1)}{A (\delta h + 1)} = \frac {\bar {B} (\delta)}{\bar {A} (\delta)} = \bar {H} (\delta)$$

The $\delta$ -operator is thus equivalent to the shift operator. All the analysis done for the shift operator can be translated into $\delta$ -form. The $\delta$ -operator has the property

$$\delta f (k h) = \frac {f (k h + h) - f (k h)}{h}$$

that is, it can be interpreted as the forward-difference approximation of the differential operator $p = d / dt$ . In this respect the $\delta$ -operator is "closer" to the continuous-time domain than the shift operator. For instance, the stability region in the $\delta$ -form is a circle with radius $1 / h$ and with the origin in $-1 / h$ . When $h \to 0$ the stability region becomes the left half-plane.

The $\delta$ -operator representation has the property that it translates into the corresponding continuous-time system when the sampling interval approaches zero. Hence

$$\lim _ {h \rightarrow 0} \bar {H} (\delta) = G (\delta)$$

where G is the continuous-time transfer function. This implies, for instance, that the zeros of the transfer function in the $\delta$ -form approach the zeros (finite as well as infinite) of the continuous-time transfer function.
