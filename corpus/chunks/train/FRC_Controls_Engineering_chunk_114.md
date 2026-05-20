# Pseudoinverse

The $^ +$ in ${ { \bf A } ^ { + } }$ denotes the Moore-Penrose pseudoinverse, which is a generalization of the inverse matrix to nonsquare matrices. The pseudoinverse is an approximate inverse in the least-squares sense, so it can solve least-squares problems of the form Ax = b via ${ \bf x } = { \bf A } ^ { + } { \bf b }$ .

<table><tr><td>System type</td><td>Shape of A</td><td>Name of  $A^{+}$ </td><td>Value of  $A^{+}$ </td></tr><tr><td>Well-determined</td><td>Square</td><td>Inverse</td><td> $A^{-1}$ </td></tr><tr><td>Overdetermined</td><td>Tall</td><td>Left pseudoinverse</td><td> $(A^{\mathsf{T}}A)^{-1}A^{\mathsf{T}}$ </td></tr><tr><td>Underdetermined</td><td>Wide</td><td>Right pseudoinverse</td><td> $A^{\mathsf{T}}(AA^{\mathsf{T}})^{-1}$ </td></tr></table>

Table 5.1: Pseudoinverses by system type.
