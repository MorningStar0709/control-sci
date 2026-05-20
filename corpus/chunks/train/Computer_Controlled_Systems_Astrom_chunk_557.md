There is also an increased use of computer-controlled systems implemented using special-purpose VLSI circuits. In these applications the word length is a design parameter that can be chosen freely. Such a choice naturally requires a more detailed investigation than a simple choice between single or double precision. There are applications of custom VLSI both in the aerospace industry and for mass-produced consumer goods like VCRs and CD players. For these applications it is of major concern to minimize chip area. A typical example is a CD player in which both audio and servo functions are implemented on one chip. For a stationary CD player there are fewer demands on the servo than for a CD player for a car. The chip area for the control system can thus be smaller for the stationary player.

There are many number representations used in digital computers. Integers are typically 16, 32, or 48 bits. For a long time there were many representations of floating-point numbers. The IEEE did, however, take the initiative to standardize them, and a standard ANSI-IEEE 754 was published in 1985. In this standard the numbers are represented as

$$\pm a \cdot 2 ^ {\dot {b}}$$

where $0 \leq a < 2$ is the significand, also called the mantissa, and $b$ is the exponent. In the standard there are three types of floating-point numbers:

<table><tr><td>short real (32 bits)</td><td>1 sign</td><td>8 exponent</td><td>23 significand</td></tr><tr><td>long real (64 bits)</td><td>1 sign</td><td>11 exponent</td><td>52 significand</td></tr><tr><td>short temporary real (80 bits)</td><td>1 sign</td><td>15 exponent</td><td>64 significand</td></tr></table>

The IEEE standard has gained widespread acceptance, and the floating-point chips from Intel and Motorola are based on it.
