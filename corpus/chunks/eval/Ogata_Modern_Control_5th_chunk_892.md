(Note that the residues are returned in column vector r, the pole locations in column vector p, and the direct term in row vector k.) This is the MATLAB representation of the following partialfraction expansion of $B ( s ) / A ( s )$ :

$$
\begin{array}{l} \frac {B (s)}{A (s)} = \frac {2 s ^ {3} + 5 s ^ {2} + 3 s + 6}{s ^ {3} + 6 s ^ {2} + 1 1 s + 6} \\ = \frac {- 6}{s + 3} + \frac {- 4}{s + 2} + \frac {3}{s + 1} + 2 \\ \end{array}
$$

Note that if $p ( j ) = p ( j + 1 ) = \cdots = p ( j + m - 1 )$ Cthat is, $p _ { j } = p _ { j + 1 } = \cdots = p _ { j + m - 1 } \forall$ , the pole $p ( j )$ is a pole of multiplicity m. In such a case, the expansion includes terms of the form

$$\frac {r (j)}{s - p (j)} + \frac {r (j + 1)}{\left[ s - p (j) \right] ^ {2}} + \dots + \frac {r (j + m - 1)}{\left[ s - p (j) \right] ^ {m}}$$

For details, see Example B–5.

EXAMPLE B–5 Expand the following $B ( s ) / A ( s )$ into partial fractions with MATLAB.

$$\frac {B (s)}{A (s)} = \frac {s ^ {2} + 2 s + 3}{(s + 1) ^ {3}} = \frac {s ^ {2} + 2 s + 3}{s ^ {3} + 3 s ^ {2} + 3 s + 1}$$

For this function, we have

$$
\begin{array}{l} \text { num } = [ 1 2 3 ] \\ \mathrm{den} = [ 1 \quad 3 \quad 3 \quad 1 ] \\ \end{array}
$$

The command

$$[ r, p, k ] = \text { residue } (\text { num }, \text { den })$$

gives the result shown next:

$$
\begin{array}{l} \hline \text {num = [1 2 3];} \\ \text {den = [1 3 3 1];} \\ \text {[r,p,k] = residue(num,den)} \\ \text {r =} \\ \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \text {p =} \\ \quad \quad \quad - 1. 0 0 0 0 \\ \quad \quad - 1. 0 0 0 0 \\ \quad - 1. 0 0 0 0 \\ k = \\ \quad [ ] \\ \hline \end{array}
$$

It is the MATLAB representation of the following partial-fraction expansion of $B ( s ) / A ( s )$ :

$$\frac {B (s)}{A (s)} = \frac {1}{s + 1} + \frac {0}{(s + 1) ^ {2}} + \frac {2}{(s + 1) ^ {3}}$$

Note that the direct term k is zero.
