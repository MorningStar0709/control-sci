# A.3 Complex Number Concepts required for EE447

 $j = \sqrt { - 1 }$   
 complex number is the sum of a real part, σ + an imaginary part jω (where ω is a real number to be multiplied by j.)   
 The magnitude of a complex number is the Pythagorean sum of the real and imaginary parts: If $x = a + j b$ is a complex number, then the magnitude is

$$| x | = \sqrt {a ^ {2} + b ^ {2}}$$

 To add together two complex numbers, add their real and imaginary parts separately.

$$x = a + b j \quad y = c + d jx + y = (a + c) + j (b + d)$$

 To multiply two complex numbers, multiply them together like two rst order polynomials in j (using the denitions above)

$$x * y = (a + b j) * (c + d j) = a c + a d j + b c j + b d j ^ {2}$$

since $j ^ { 2 } = - 1$ we have

$$x * y = (a c - b d) + (a d + b c) j$$

 Complex numbers describe a point in the complex plane. The X axis of the complex plain is the real part of the complex number and the Y axis is the imaginary part.   
 To plot the point $a + j b$ on the complex plane, plot a point at $X = a , Y = b .$ .   
 The magnitude of a complex number is the distance from the origin to its point on the complex plane.   
 The angle of a complex number is the angle formed from the positive real axis $( X > 0 )$ and the line between the origin and the point.   
 There is an exponential form of any complex number:

$$e ^ {j \theta} = \cos (\theta) + j \sin (\theta)$$

 To convert a complex number to exponential form we invert the previous equation:

$$a + b j = | a + b j | e ^ {j \tan^ {- 1} (b / a)}$$

 The $\tan ^ { - 1 } ( )$ function traditionally limits us to quadrants I and IV of the complex plain. More generally we can use the 4-quadrant 2-argument arctan function (atan2(b,a)) .   
 A consequence of multiplication of complex numbers and the exponential represenation of complex numbers is that when we multiply two complex numbers:

angles add and magnitudes multiply

if $A , B , C$ are complex numbers and $C = A * B$

$$\angle C = \angle A + \angle B \quad | C | = | A | * | B |$$
