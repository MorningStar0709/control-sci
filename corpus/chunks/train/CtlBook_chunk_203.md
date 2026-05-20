# 7.4 Root Locus Steps

Evans gured out a set of rules, based on the mathematical properties of the closed loop characteristic polynomial, that allow us to sketch the Root Locus diagram quickly. Recall that the loop gain is the product of all transfer functions around the loop. For a simple system like that of Example 7.2, the loop gain is $K C ( s ) P ( s ) H ( s )$ (where we have assumed that the controller has a constant gain term K and separated it out). Now we solve the closed loop gain using Equation 6.2.

$$\frac {Y (s)}{X (s)} = \frac {K C (s) P (s)}{1 + K C (s) P (s) H (s)}$$

Poles of this closed loop transfer function are values of s where its denominator is zero. In other words

$$1 + K C (s) P (s) H (s) = 0$$

giving

$$K C (s) P (s) H (s) = - 1$$

Since the transfer functions are complex, we have

$$| K C (s) P (s) H (s) | = 1 \quad \text { and } \quad \angle K C (s) P (s) H (s) = 1 8 0 ^ {\circ}$$

These two conditions are called the magnitude condition and the angle condition respectively. All points on the Root Locus are poles of the closed loop transfer function (CLTF) for dierent values of K. Since K is positive and real, it always contributes $0 ^ { \circ }$ to the angle, and can be dropped from the angle condition. Thus all points on the Root Locus, for any value of $K \ ( 0 < K < \infty )$ , must observe both conditions.

The following Root Locus drawing rules derive from either the Magnitude Condition, the Angle Condition, or fundamental properties of polynomials.
