# Example 9.3 Scalar-product calculations

Consider the vectors

$$
\begin{array}{l} a = \left( \begin{array}{c c c} 1 0 0 & 1 & 1 0 0 \end{array} \right) \\ b = \left( \begin{array}{c c c} 1 0 0 & 1 & - 1 0 0 \end{array} \right) \\ \end{array}
$$

The scalar product is $(a, b) = 1$ . If the scalar product is computed in floating-point representation with a precision corresponding to three decimal places, the result will be zero because $100 \cdot 100 + 1 \cdot 1$ is rounded to 10,000. Notice that the result obtained depends on the order of the operations. Finite-word-length operations are neither associative nor distributive.

The difficulty may be avoided without using complete double-precision calculation by adding the terms in double precision and rounding to single precision afterwards. This method can be applied to fixed-point and floating-point calculations. Notice that the multiply instruction for many computers is implemented so that the product is available in double precision. Many high-level languages also have constructions that support this type of calculation. Generally speaking, roundoff and quantization will give rise to small errors, whereas the effects of overflow will be disastrous.

Digital-signal processors (DSPs) are now commonly used to implement computer-controlled systems when short sampling periods are required. The low-cost signal processors are all using fixed-point calculations. For the TMS family from Texas Instruments, the standard word length is 16 bits but the accumulator is 32 bits wide. A 16-bit DSP from AT&T has a 36-bit accumulator, and Motorola has a DSP with 24-bit word length and a 56-bit accumulator. The architecture with a long accumulator is ideal for computing scalar products, which is the key operation when implementing linear filters, because the products of the terms can be accumulated in double precision. The signal processors are very fast. The operation of multiply and accumulate (MAP) typically takes 100 nanoseconds. There are also more expensive signal processors with floating-point hardware.
