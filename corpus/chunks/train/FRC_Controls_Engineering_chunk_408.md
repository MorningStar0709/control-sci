$$
\begin{array}{l} - a = \left[ \begin{array}{c c} - A _ {1} & A _ {2} \end{array} \right] v + \left[ \begin{array}{c c} - B _ {1} & B _ {2} \end{array} \right] \left[ K _ {v, a n g} v + K _ {a, a n g} a \right] \\ - a = - v A _ {1} + v A _ {2} - (K _ {v, a n g} v + K _ {a, a n g} a) B _ {1} + (K _ {v, a n g} v + K _ {a, a n g} a) B _ {2} \\ - a = \left[ \begin{array}{c c c c} - v & v & - (K _ {v, a n g} v + K _ {a, a n g} a) & K _ {v, a n g} v + K _ {a, a n g} a \end{array} \right] \left[ \begin{array}{c} A _ {1} \\ A _ {2} \\ B _ {1} \\ B _ {2} \end{array} \right] \\ a = \left[ \begin{array}{c c c c} v & - v & K _ {v, a n g} v + K _ {a, a n g} a & - (K _ {v, a n g} v + K _ {a, a n g} a) \end{array} \right] \left[ \begin{array}{c} A _ {1} \\ A _ {2} \\ B _ {1} \\ B _ {2} \end{array} \right] \\ \end{array}
$$

Now stack the rows.

$$
{\left[ \begin{array}{l} 0 \\ a \\ 0 \\ a \end{array} \right]} = {\left[ \begin{array}{l l l l} 1 & 1 & K _ {v, l i n} & K _ {v, l i n} \\ v & v & K _ {v, l i n} v + K _ {a, l i n} a & K _ {v, l i n} v + K _ {a, l i n} a \\ - 1 & 1 & - K _ {v, a n g} & K _ {v, a n g} \\ v & - v & K _ {v, a n g} v + K _ {a, a n g} a & - (K _ {v, a n g} v + K _ {a, a n g} a) \end{array} \right]} {\left[ \begin{array}{l} A _ {1} \\ A _ {2} \\ B _ {1} \\ B _ {2} \end{array} \right]}
$$

Solve for matrix elements with Wolfram Alpha. Let $b = K _ { v , l i n } , c = K _ { a , l i n } , d =$ $K _ { v , a n g }$ , and $f = K _ { a , a n g }$ .

$$
\begin{array}{l} \text { inverse   of } \{\{1, 1, b, b \}, \\ \{v, v, b v + c a, b v + c a \}, \\ \{- 1, \quad 1, \quad - d, \quad d \}, \\ \left\{v, - v, d v + f a, - (d v + f a) \right\} \\ * \{\{0 \}, \{a \}, \{0 \}, \{a \} \} \\ \end{array}

\left[ \begin{array}{c} A _ {1} \\ A _ {2} \\ B _ {1} \\ B _ {2} \end{array} \right] = \frac {1}{2 c f} \left[ \begin{array}{c} - c d - b f \\ c d - b f \\ c + f \\ f - c \end{array} \right]

\left[ \begin{array}{c} A _ {1} \\ A _ {2} \\ B _ {1} \\ B _ {2} \end{array} \right] = \frac {1}{2 K _ {a , l i n} K _ {a , a n g}} \left[ \begin{array}{c} - K _ {a, l i n} K _ {v, a n g} - K _ {v, l i n} K _ {a, a n g} \\ K _ {a, l i n} K _ {v, a n g} - K _ {v, l i n} K _ {a, a n g} \\ K _ {a, l i n} + K _ {a, a n g} \\ K _ {a, a n g} - K _ {a, l i n} \end{array} \right]
