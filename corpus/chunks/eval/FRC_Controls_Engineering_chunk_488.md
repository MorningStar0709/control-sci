Factor out $\begin{array} { r } { \left[ \mathbf { x } _ { k } \right] ^ { \top } } \\ { \left[ \mathbf { u } _ { k } \right] ^ { \top } } \end{array}$ xk from the left side and $\left[ { \bf { x } } _ { k } \right]$ from the right side of each term.

$$
\begin{array}{l} J = \sum_ {k = 0} ^ {\infty} \left(\left[ \begin{array}{c} \mathbf {x} _ {k} \\ \mathbf {u} _ {k} \end{array} \right] ^ {\mathsf {T}} \left[ \begin{array}{c} (\mathbf {C A} - \mathbf {A} _ {r e f} \mathbf {C}) ^ {\mathsf {T}} \\ (\mathbf {C B}) ^ {\mathsf {T}} \end{array} \right] \mathbf {Q} \left[ \begin{array}{c c} \mathbf {C A} - \mathbf {A} _ {r e f} \mathbf {C} & \mathbf {C B} \end{array} \right] \left[ \begin{array}{c} \mathbf {x} _ {k} \\ \mathbf {u} _ {k} \end{array} \right]\right) \\ \left. + \left[ \begin{array}{c} \mathbf {x} _ {k} \\ \mathbf {u} _ {k} \end{array} \right] ^ {\top} \left[ \begin{array}{c c} \mathbf {0} & \mathbf {0} \\ \mathbf {0} & \mathbf {R} \end{array} \right] \left[ \begin{array}{c} \mathbf {x} _ {k} \\ \mathbf {u} _ {k} \end{array} \right]\right) \\ \end{array}

\begin{array}{l} J = \sum_ {k = 0} ^ {\infty} \left(\left[ \begin{array}{c} \mathbf {x} _ {k} \\ \mathbf {u} _ {k} \end{array} \right] ^ {\mathsf {T}} \left(\left[ \begin{array}{c} (\mathbf {C A} - \mathbf {A} _ {r e f} \mathbf {C}) ^ {\mathsf {T}} \\ (\mathbf {C B}) ^ {\mathsf {T}} \end{array} \right] \mathbf {Q} \left[ \begin{array}{c c} \mathbf {C A} - \mathbf {A} _ {r e f} \mathbf {C} & \mathbf {C B} \end{array} \right] \right. \right. \\ \left. + \left[ \begin{array}{c c} \mathbf {0} & \mathbf {0} \\ \mathbf {0} & \mathbf {R} \end{array} \right]\right) \left[ \begin{array}{c} \mathbf {x} _ {k} \\ \mathbf {u} _ {k} \end{array} \right) \\ \end{array}
$$

Multiply in $\mathbf { Q }$

$$
\begin{array}{l} J = \sum_ {k = 0} ^ {\infty} \left(\left[ \begin{array}{c} \mathbf {x} _ {k} \\ \mathbf {u} _ {k} \end{array} \right] ^ {\mathsf {T}} \left(\left[ \begin{array}{c} (\mathbf {C A} - \mathbf {A} _ {r e f} \mathbf {C}) ^ {\mathsf {T}} \mathbf {Q} \\ (\mathbf {C B}) ^ {\mathsf {T}} \mathbf {Q} \end{array} \right] \left[ \begin{array}{c c} \mathbf {C A} - \mathbf {A} _ {r e f} \mathbf {C} & \mathbf {C B} \end{array} \right] \right. \right. \\ \left. + \left[\begin{array}{c c}\mathbf {0}&\mathbf {0}\\\mathbf {0}&\mathbf {R}\end{array}\right]\right)\left[\begin{array}{c}\mathbf {x} _ {k}\\\mathbf {u} _ {k}\end{array}\right]\left. \right) \\ \end{array}
$$
