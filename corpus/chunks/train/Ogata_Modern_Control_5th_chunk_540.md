then $\hat { F } ( s )$ has a zero of kth order at $s = - z _ { 1 }$ . Differentiating $F ( s )$ with respect to s yields

$$\hat {F} ^ {\prime} (s) = k \left(s + z _ {1}\right) ^ {k - 1} X (s) + \left(s + z _ {1}\right) ^ {k} X ^ {\prime} (s)$$

Hence,

$$\frac {\hat {F} ^ {\prime} (s)}{\hat {F} (s)} = \frac {k}{s + z _ {1}} + \frac {X ^ {\prime} (s)}{X (s)} \tag {7-31}$$

We see that by taking the ratio $\hat { F } ^ { \prime } { \left( s \right) } / \hat { F } \left( s \right)$ , the kth-order zero of $\hat { F } ( s )$ becomes a simple pole of $\hat { F } ^ { \prime } { \left( s \right) } / \hat { F } \left( s \right)$ .

\# For the definition of an analytic function, see the footnote on page 447.

If the last term on the right-hand side of Equation (7–31) does not contain any poles or zeros in the closed contour in the s plane, $F ^ { \prime } ( s ) / F ( s )$ is analytic in this contour except at point $s = - z _ { 1 }$ 1 . Then, referring to Equation (7–30) and using the residue theorem, which states that the integral of $F ^ { \prime } ( s ) / F ( s )$ taken in the clockwise direction around a closed contour in the s plane is equal to $- 2 \pi j$ times the residues at the simple poles of $F ^ { \prime } ( s ) / F ( s )$ , or

$$\oint \frac {F ^ {\prime} (s)}{F (s)} d s = - 2 \pi j \left(\sum \text { residues }\right)$$

we have

$$\oint \frac {F ^ {\prime} (s)}{F (s)} d s = - 2 \pi j \left[ \left(k _ {1} + k _ {2} + \dots\right) - \left(m _ {1} + m _ {2} + \dots\right) \right] = - 2 \pi j (Z - P)$$

where $Z = k _ { 1 } + k _ { 2 } + \cdots =$ total number of zeros of $F ( s )$ enclosed in the closed contour in the s plane

$$
\begin{array}{l} P = m _ {1} + m _ {2} + \dots = \text { total   number   of   poles   of } F (s) \text { enclosed   in   the   closed } \\ \text { contour   in   the } s \text { plane } \end{array}
$$

[The k multiple zeros (or poles) are considered k zeros (or poles) located at the same point.] Since $F ( s )$ is a complex quantity, $F ( s )$ can be written

$$F (s) = | F | e ^ {j \theta}$$

and

$$\ln F (s) = \ln | F | + j \theta$$

Noting that $F ^ { \prime } ( s ) / F ( s )$ can be written

$$\frac {F ^ {\prime} (s)}{F (s)} = \frac {d \ln F (s)}{d s}$$

we obtain

$$\frac {F ^ {\prime} (s)}{F (s)} = \frac {d \ln | F |}{d s} + j \frac {d \theta}{d s}$$

If the closed contour in the s plane is mapped into the closed contour in theG $F ( s )$ plane, then

$$\oint \frac {F ^ {\prime} (s)}{F (s)} d s = \oint_ {\Gamma} d \ln | F | + j \oint_ {\Gamma} d \theta = j \int d \theta = 2 \pi j (P - Z)$$
