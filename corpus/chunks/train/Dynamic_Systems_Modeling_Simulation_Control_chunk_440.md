# Partial-fraction expansion with repeated poles

When the poles of the Laplace transform $Y ( s )$ are repeated, the partial-fraction expansion (Eq. 8.15) is no longer valid. To show this, consider the following simple example with two repeated poles

$$Y (s) = \frac {2 s + 8}{s ^ {3} + 7 s ^ {2} + 1 6 s + 1 2} = \frac {2 s + 8}{(s + 2) (s + 2) (s + 3)} \tag {8.17}$$

This Laplace transform has two repeated poles at $s = - 2$ and a single pole at $s = - 3$ . If we simply used (Eq. 8.15) for the partial-fraction expansion then the corresponding time function would be $y ( t ) = a _ { 1 } e ^ { - 2 t } +$ $a _ { 2 } e ^ { - 2 t } + a _ { 3 } e ^ { - 3 t }$ , which is not correct as the first two terms could be written as $A e ^ { - 2 t }$ t where $A = a _ { 1 } + a _ { 2 }$ . The correct partial-fraction expansion of Eq. (8.17) is

$$Y (s) = \frac {a _ {1}}{(s + 2) ^ {2}} + \frac {a _ {2}}{s + 2} + \frac {a _ {3}}{s + 3} \tag {8.18}$$

The inverse Laplace transform can be obtained by using entries 6 and 7 from Table 8.1:

$$y (t) = a _ {1} t e ^ {- 2 t} + a _ {2} e ^ {- 2 t} + a _ {3} e ^ {- 3 t}$$

The difficulty lies with obtaining the residues $a _ { i }$ for the case with repeated poles. We do not show the derivation of the technique for obtaining the residues; instead, we present the resulting method (the reader can consult References 2 and 3 for the details of the derivation).

Using the Laplace transform (Eq. 8.17) as an example, the three residues for the partial-fraction expansion (Eq. 8.18) can be computed as

$$
\begin{array}{l} a _ {1} = (s + 2) ^ {2} Y (s) | _ {s = - 2} = \left. \frac {2 s + 8}{s + 3} \right| _ {s = - 2} = \frac {4}{1} = 4 \\ a _ {2} = \frac {d}{d s} [ (s + 2) ^ {2} Y (s) ] | _ {s = - 2} = \left. \frac {d}{d s} \left[ \frac {2 s + 8}{s + 3} \right] \right| _ {s = - 2} = \left. \frac {2}{s + 3} - \frac {2 s + 8}{(s + 3) ^ {2}} \right| _ {s = - 2} = \frac {2}{1} - \frac {4}{1} = - 2 \\ a _ {3} = (s + 3) Y (s) | _ {s = - 3} = \left. \frac {2 s + 8}{(s + 2) ^ {2}} \right| _ {s = - 3} = \frac {2}{1} = 2 \\ \end{array}
$$

Therefore, the partial-fraction expansion is

$$Y (s) = \frac {4}{(s + 2) ^ {2}} + \frac {- 2}{s + 2} + \frac {2}{s + 3}$$

and the inverse Laplace transform is

$$y (t) = 4 t e ^ {- 2 t} - 2 e ^ {- 2 t} + 2 e ^ {- 3 t}$$

This result can be verified using the following MATLAB commands

$$
\begin{array}{l} > > \text { numY } = [ 2 8 ]; \\ > > \text {   denY   } = [ 1 7 1 6 1 2 ]; \\ > > [ b, p, k ] = \text { residue } (\text { numY }, \text { denY }) \\ \end{array}
$$

The result is b = [2 -2 4](residues), p = [-3 -2 -2](poles), and k = [] (null). The convention for MATLAB’s residue command reverses the order of the partial-fraction expansion in Eq. (8.18), and, therefore, $b _ { 1 } = a _ { 3 } , b _ { 2 } = a _ { 2 }$ , and $b _ { 3 } = a _ { 1 }$ .
