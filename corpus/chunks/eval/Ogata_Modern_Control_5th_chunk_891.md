$$
\begin{array}{l} f (t) = \mathscr {L} ^ {- 1} [ F (s) ] \\ = \mathscr {L} ^ {- 1} \left[ \frac {1}{s + 1} \right] + \mathscr {L} ^ {- 1} \left[ \frac {0}{(s + 1) ^ {2}} \right] + \mathscr {L} ^ {- 1} \left[ \frac {2}{(s + 1) ^ {3}} \right] \\ = e ^ {- t} + 0 + t ^ {2} e ^ {- t} \\ = (1 + t ^ {2}) e ^ {- t}, \quad \text {   for   } t \geq 0 \\ \end{array}
$$

Comments. For complicated functions with denominators involving higher-order polynomials, partial-fraction expansion may be quite time consuming. In such a case, use of MATLAB is recommended.

Partial-Fraction Expansion with MATLAB. MATLAB has a command to obtain the partial-fraction expansion of $B ( s ) / A ( s )$ . Consider the following function $B ( s ) / A ( s )$ :

$$\frac {B (s)}{A (s)} = \frac {\text { num }}{\text { den }} = \frac {b _ {0} s ^ {n} + b _ {1} s ^ {n - 1} + \cdots + b _ {n}}{s ^ {n} + a _ {1} s ^ {n - 1} + \cdots + a _ {n}}$$

where some of $a _ { i }$ and $b _ { j }$ may be zero. In MATLAB row vectors num and den specify the coefficients of the numerator and denominator of the transfer function. That is,

$$\text { num } = [ b _ {0} b _ {1} \ldots b _ {n} ]\mathrm{den} = [ 1 \quad a _ {1} \dots a _ {n} ]$$

The command

$$[ r, p, k ] = \text { residue } (\text { num }, \text { den })$$

finds the residues (r), poles (p), and direct terms (k) of a partial-fraction expansion of the ratio of two polynomials $B ( s )$ and $A ( s )$ .

The partial-fraction expansion of $B ( s ) / A ( s )$ is given by

$$\frac {B (s)}{A (s)} = \frac {r (1)}{s - p (1)} + \frac {r (2)}{s - p (2)} + \dots + \frac {r (n)}{s - p (n)} + k (s) \tag {B-4}$$

Comparing Equations (B–1) and (B–4), we note that $p ( 1 ) = - p _ { 1 } , p ( 2 ) = - p _ { 2 } , . . .$ , $p ( n ) = - p _ { n } ; r ( 1 ) = a _ { 1 } , r ( 2 ) = a _ { 2 } , \ldots , r ( n ) = a _ { n } . [ k ( s )$ is a direct term.]

EXAMPLE B–4 Consider the following transfer function,

$$\frac {B (s)}{A (s)} = \frac {2 s ^ {3} + 5 s ^ {2} + 3 s + 6}{s ^ {3} + 6 s ^ {2} + 1 1 s + 6}$$

For this function,

$$
\begin{array}{l} \mathrm{num} = \left[ \begin{array}{c c c c} 2 & 5 & 3 & 6 \end{array} \right] \\ \mathrm{den} = [ 1 \quad 6 \quad 1 1 \quad 6 ] \\ \end{array}
$$

The command

$$[ r, p, k ] = \text { residue } (\text { num }, \text { den })$$

gives the following result:

$$
\begin{array}{c} \hline [ r, p, k ] = \text { residue(num,den) } \\ r = \\ \quad - 6. 0 0 0 0 \\ \quad - 4. 0 0 0 0 \\ \quad 3. 0 0 0 0 \\ p = \\ \quad - 3. 0 0 0 0 \\ \quad - 2. 0 0 0 0 \\ \quad - 1. 0 0 0 0 \\ k = \\ \quad 2 \end{array}
$$
