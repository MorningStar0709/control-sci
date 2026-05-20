$$
\begin{array}{c c c c c c} 4 & | & 1 & 3 & 2 & 0 \\ 3 & | & - 1 & 0 & 0 & 0 \\ 2 & | & 3 & 2 & 0 & 0 \\ 1 & | & \frac {2}{3} & 0 \\ 0 & | & 2 \end{array}
$$

Two sign changes occur in the first column, between rows 4 and 3 and between rows 3 and 2. The polynomial has two RHP roots.

There are two special cases of interest.

1. If a row has a zero in the first column and has at least one nonzero element, replace the zero in the first column with $\epsilon$ , an infinitesimally small positive quantity, and continue building the array.   
2. An entire row of zeros may be encountered, always in an odd-numbered row—say, $k - 1$ . To take care of this situation, use the preceding row (row $k$ ) to form a polynomial in even powers of $s$ , as follows:

$$p (s) = A _ {1} s ^ {k} + A _ {2} s ^ {k - 2} + \dots .$$

Here, $A_1, A_2, \ldots$ are the entries of row $k$ . The entries of the new row $(k - 1)$ are just the coefficients of the derivative of $p(s)$ .

There is a bonus in this last case: the roots of $p(s)$ are also roots of the original polynomial.

Example 5.2 Repeat Example 5.1 for $Q(s) = s^4 - s^2 + 2s + 2$ .

Solution The Routh array begins with the two lines

$$
\begin{array}{c c c c c} 4 & | & 1 & - 1 & 2 \\ 3 & | & 0 & 2 & 0 \end{array}
$$

We replace the zero in the first column with $\epsilon$ , and go on:

$$
\begin{array}{c c c c c} 4 & 1 & - 1 & 2 \\ 3 & \epsilon & 2 & 0 \\ 2 & \frac {- \epsilon - 2}{\epsilon} & 2 & 0 \\ 1 & (\frac {- \epsilon}{2 + \epsilon}) (- 2 \frac {(\epsilon + 2)}{\epsilon} - 2 \epsilon) & 0 \\ 0 & 2 \end{array}
$$

For small, positive $\epsilon$ , the leading term in row 2 is approximately $-2/\epsilon$ and the leading term in row 1 is approximately 2. There are two sign changes and hence two roots in the RHP.

In control systems design, the Routh–Hurwitz criterion is most often used to ascertain the ranges of design parameters that lead to stability. An example illustrates this.
