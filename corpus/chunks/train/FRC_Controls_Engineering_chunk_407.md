Let $\mathbf { u } \ = \ \left\lceil - K _ { v , a n g } v - K _ { a , a n g } a \quad K _ { v , a n g } v + K _ { a , a n g } a \right\rceil ^ { \mathsf { T } }$ be the input that rotates the drivetrain in place where each wheel has an initial speed of v and accelerates by a. Therefore, $\mathbf { x } = \left[ - v \quad v \right] ^ { \mathsf { T } }$ and $\dot { \mathbf { x } } = \left[ - a \quad a \right] ^ { \mathsf { T } }$ .

$$
\begin{array}{l} \left[ \begin{array}{c} - a \\ a \end{array} \right] = \left[ \begin{array}{c c} A _ {1} & A _ {2} \\ A _ {2} & A _ {1} \end{array} \right] \left[ \begin{array}{c} - v \\ v \end{array} \right] + \left[ \begin{array}{c c} B _ {1} & B _ {2} \\ B _ {2} & B _ {1} \end{array} \right] \left[ \begin{array}{c} - K _ {v, a n g} v - K _ {a, a n g} a \\ K _ {v, a n g} v + K _ {a, a n g} a \end{array} \right] \\ \left[ \begin{array}{c} - a \\ a \end{array} \right] = \left[ \begin{array}{c c} - A _ {1} & A _ {2} \\ - A _ {2} & A _ {1} \end{array} \right] \left[ \begin{array}{c} v \\ v \end{array} \right] + \left[ \begin{array}{c c} - B _ {1} & B _ {2} \\ - B _ {2} & B _ {1} \end{array} \right] \left[ \begin{array}{c} K _ {v, a n g} v + K _ {a, a n g} a \\ K _ {v, a n g} v + K _ {a, a n g} a \end{array} \right] \\ \left[ \begin{array}{c} - a \\ a \end{array} \right] = \left[ \begin{array}{c c} - A _ {1} & A _ {2} \\ A 1 & - A _ {2} \end{array} \right] \left[ \begin{array}{c} v \\ v \end{array} \right] + \left[ \begin{array}{c c} - B _ {1} & B _ {2} \\ B _ {1} & - B _ {2} \end{array} \right] \left[ \begin{array}{c} K _ {v, a n g} v + K _ {a, a n g} a \\ K _ {v, a n g} v + K _ {a, a n g} a \end{array} \right] \\ \end{array}
$$

Since the column vectors contain the same element, the elements in the second row can be rearranged.

$$
\left[ \begin{array}{c} - a \\ - a \end{array} \right] = \left[ \begin{array}{c c} - A _ {1} & A _ {2} \\ - A _ {1} & A _ {2} \end{array} \right] \left[ \begin{array}{c} v \\ v \end{array} \right] + \left[ \begin{array}{c c} - B _ {1} & B _ {2} \\ - B _ {1} & B _ {2} \end{array} \right] \left[ \begin{array}{c} K _ {v, a n g} v + K _ {a, a n g} a \\ K _ {v, a n g} v + K _ {a, a n g} a \end{array} \right]
$$

Since the rows are linearly dependent, we can use just one of them.
