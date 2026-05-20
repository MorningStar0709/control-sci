# 2.7 Finding Errors through Dimensional Analysis

Once the numerator and denominator of the transfer function are normalized, we can exploit dimensional analysis to check our work for errors. We rely on the fact that for quantities to be added together they must have the same units. What are the units of s?

s represents frequency and so has the units of inverse seconds, sec−1. Also each physical parameter has units. The MKS system has only three fundamental units, meters, kg, and seconds. Assuming the MKS system, each physical parameter has the units given in Table 2.2.

Now suppose the denominator of a transfer function has been normalized and then begins with s4. Then through dimensional analysis, we know that all the subsequent terms in the polynomial must have the same units, namely sec−4. This can often be an easy way to nd an error in the transfer function without checking each step. Note that you can also apply this to the tabular version of Example 2.10 by making sure all entries in each column have the same units.

<table><tr><td>Name</td><td>Fundamental Units</td><td>Name</td><td>Fundamental Units</td></tr><tr><td>s</td><td> $\sec^{-1}$ </td><td>B</td><td> $\frac{kg}{\sec}$ </td></tr><tr><td> $s^n$ </td><td> $\sec^{-n}$ </td><td>K</td><td> $\frac{kg}{\sec^2}$ </td></tr><tr><td></td><td></td><td>M</td><td>kg</td></tr></table>

Table 2.2: Fundamental MKS units for s and the physical parameters.
