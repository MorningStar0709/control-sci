# Partial-fraction expansion with distinct poles

When its poles are distinct, the Laplace transform $Y ( s )$ can be expanded as

$$Y (s) = \frac {a _ {1}}{s + p _ {1}} + \frac {a _ {2}}{s + p _ {2}} + \dots + \frac {a _ {n}}{s + p _ {n}} \tag {8.15}$$

where $s = - p _ { i }$ are the distinct poles of $Y ( s )$ and constants $a _ { i }$ are called the residues of $Y ( s )$ ). We can evaluate the residue $a _ { 1 }$ by multiplying both sides of Eq. (8.15) by $s + p _ { 1 }$ and setting $s = - p _ { 1 }$ , or

$$a _ {1} = (s + p _ {1}) Y (s) | _ {s = - p _ {1}}$$

The above equation can be generalized for all n residues

$$a _ {i} = (s + p _ {i}) Y (s) | _ {s = - p _ {i}} \quad i = 1, 2, \dots , n \tag {8.16}$$

The MATLAB command residue computes the residues, poles, and “direct” terms of the partialfraction expansion of Y(s)

$$> > [ a, p, k ] = \text { residue } (\text { numY }, \text { denY })$$

where a is the vector of residues, p is the vector of poles corresponding to residues a, k is the vector of “direct” terms, numY is a row vector of the $Y ( s )$ numerator coefficients, and denY is a row vector of the $Y ( s )$ denominator coefficients. The “direct” term k exists only if the order of the numerator (numY) is greater than or equal to the order of the denominator (denY).
