0 = \left[ \begin{array}{c c c c} v & v & K _ {v, l i n} v & K _ {v, l i n} v \end{array} \right] \left[ \begin{array}{c} A _ {1} \\ A _ {2} \\ B _ {1} \\ B _ {2} \end{array} \right]

0 = \left[ \begin{array}{c c c c} 1 & 1 & K _ {v, l i n} & K _ {v, l i n} \end{array} \right] \left[ \begin{array}{c} A _ {1} \\ A _ {2} \\ B _ {1} \\ B _ {2} \end{array} \right]
$$

Let $\mathbf { u } = \left[ K _ { v , l i n } v + K _ { a , l i n } a \quad K _ { v , l i n } v + K _ { a , l i n } a \right] ^ { \mathsf { T } }$ be the input that accelerates both sides of the drivetrain by a from an initial velocity of v. Therefore, $\mathbf { x } = { \left[ \begin{array} { l l } { v } & { v } \end{array} \right] } ^ { \mathsf { T } }$ and $\dot { \mathbf { x } } = \left[ a \quad a \right] ^ { \mathsf { T } }$ . Substitute these into the state-space model.

$$
{\left[ \begin{array}{l} a \\ a \end{array} \right]} = {\left[ \begin{array}{l l} A _ {1} & A _ {2} \\ A _ {2} & A _ {1} \end{array} \right]} {\left[ \begin{array}{l} v \\ v \end{array} \right]} + {\left[ \begin{array}{l l} B _ {1} & B _ {2} \\ B _ {2} & B _ {1} \end{array} \right]} {\left[ \begin{array}{l} K _ {v, l i n} v + K _ {a, l i n} a \\ K _ {v, l i n} v + K _ {a, l i n} a \end{array} \right]}
$$

Since the column vectors contain the same element, the elements in the second row can be rearranged.

$$
{\left[ \begin{array}{l} a \\ a \end{array} \right]} = {\left[ \begin{array}{l l} A _ {1} & A _ {2} \\ A _ {1} & A _ {2} \end{array} \right]} {\left[ \begin{array}{l} v \\ v \end{array} \right]} + {\left[ \begin{array}{l l} B _ {1} & B _ {2} \\ B _ {1} & B _ {2} \end{array} \right]} {\left[ \begin{array}{l} K _ {v, l i n} v + K _ {a, l i n} a \\ K _ {v, l i n} v + K _ {a, l i n} a \end{array} \right]}
$$

Since the rows are linearly dependent, we can use just one of them.

$$
\begin{array}{l} a = \left[ \begin{array}{c c} A _ {1} & A _ {2} \end{array} \right] v + \left[ \begin{array}{c c} B _ {1} & B _ {2} \end{array} \right] \left[ \begin{array}{c} K _ {v, l i n} v + K _ {a, l i n} a \end{array} \right] \\ a = \left[ \begin{array}{c c c c} v & v & K _ {v, l i n} v + K _ {a, l i n} a & K _ {v, l i n} + K _ {a, l i n} a \end{array} \right] \left[ \begin{array}{c} A _ {1} \\ A _ {2} \\ B _ {1} \\ B _ {2} \end{array} \right] \\ \end{array}
$$

Let $\mathbf { u } \ = \ \left[ - K _ { v , a n g } v \quad K _ { v , a n g } v \right] ^ { \mathsf { T } }$ be the input that rotates the drivetrain in place where each wheel has a constant velocity v. Therefore, $\mathbf { x } ~ = ~ \left[ - v \quad v \right] ^ { \mathsf { T } }$ and $\dot { \textbf { x } } =$ ${ [ 0 \begin{array} { l l } \end{array}  } 0 { ] } ^ { \mathsf { T } }$ .
