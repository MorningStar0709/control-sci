# Poles and Zeros of Laplace Transforms

In general, a Laplace transform can be expressed using the form

$$F (s) = \frac {a (s + z _ {1}) (s + z _ {2}) \cdot \cdot \cdot (s + z _ {m})}{(s + p _ {1}) (s + p _ {2}) \cdot \cdot \cdot (s + p _ {n})}$$

where a is a constant. The values $s = - z _ { 1 } , s = - z _ { 2 } , \ldots , s = - z _ { m }$ that make $F ( s ) = 0$ are called the zeros of the transform $F ( s )$ while the values $s = - p _ { 1 } , s = - p _ { 2 } , \ldots , s = - p _ { n }$ that make $F ( s ) = \infty$ (or, the denominator of $F ( s )$ equals zero) are called the poles of $F ( s )$ .

As a first example, consider the following Laplace transform

$$F _ {1} (s) = \frac {1}{s + 3}$$

we see that the single pole is at $s = - 3$ (this Laplace transform has no zeros). Table 8.1 (number 6) shows us that the time function corresponding to this Laplace transform is the exponential function $f _ { 1 } ( t ) = e ^ { - 3 t }$ t . As a second example consider the Laplace transform

$$F _ {2} (s) = \frac {s}{s ^ {2} + 1 6}$$

This Laplace transform has a single zero at s = 0 (the origin) and two complex poles at $s = j 4$ and $s = - j 4$ (the reader should recall that by definition $j ^ { 2 } = - 1$ and, therefore, $( j 4 ) ^ { 2 } = ( - j 4 ) ^ { 2 } = j ^ { 2 } 1 6 = - 1 6 )$ . The time function corresponding to this Laplace transform (see number 9 in Table 8.1) is the cosine function $f _ { 2 } ( t ) = \cos { 4 t }$ .

These two simple examples demonstrate that the poles of the Laplace transform $F ( s )$ determine the nature of the corresponding time function f (t). In general, when the poles of $F ( s )$ are real numbers that are distinct (not repeated), the corresponding time function f (t) is composed of exponential functions (see number 6 in Table 8.1). When the poles of $F ( s )$ are imaginary numbers (which must appear in conjugate pairs), the corresponding f (t) is composed of sinusoidal functions (see numbers 8 and 9 in Table 8.1). If a Laplace transform has n poles at $s = 0$ (origin) then the corresponding time function is composed of n polynomial functions, or $f ( t ) = \sum t ^ { k - 1 } , k = 1 , 2 , \ldots , n$ (see numbers 2, 4, and 5 in Table 8.1). Finally, if $F ( s )$ has complex conjugate poles (real and imaginary parts) then $f ( t )$ is the product of an exponential function and a sinusoidal functions (see numbers 10 and 11 in Table 8.1). We further discuss the connection between a Laplace transform’s poles and the corresponding time response in Sections 8.3 and 8.4.
