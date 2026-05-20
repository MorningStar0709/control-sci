$$
\Delta_ {i} = \left| \begin{array}{c c c c c c} a _ {1 1} & & & & & * \\ & a _ {2 2} & & & & \\ & & \cdot & & & \\ & & & \cdot & & \\ & & & & \cdot & \\ 0 & & & & & a _ {i i} \end{array} \right|, \quad (i = 1, 2, \dots , n)
$$

where the elements below the diagonal line are all zeros and the elements above the diagonal line any numbers, then the Hurwitz conditions for asymptotic stability become

$$\Delta_ {i} = a _ {1 1} a _ {2 2} \dots a _ {i i} > 0, \quad (i = 1, 2, \dots , n)$$

which are equivalent to the conditions

$$a _ {1 1} > 0, \quad a _ {2 2} > 0, \quad \dots , \quad a _ {n n} > 0$$

We shall show that these conditions are equivalent to

$$a _ {1} > 0, \quad b _ {1} > 0, \quad c _ {1} > 0, \quad \dots$$

where $a _ { 1 } , b _ { 1 } , c _ { 1 } , \ldots$ , are the elements of the first column in the Routh array.

Consider, for example, the following Hurwitz determinant, which corresponds to i=4:

$$
\Delta_ {4} = \left| \begin{array}{c c c c} a _ {1} & a _ {3} & a _ {5} & a _ {7} \\ a _ {0} & a _ {2} & a _ {4} & a _ {6} \\ 0 & a _ {1} & a _ {3} & a _ {5} \\ 0 & a _ {0} & a _ {2} & a _ {4} \end{array} \right|
$$

The determinant is unchanged if we subtract from the ith row k times the jth row. By subtracting from the second row $a _ { 0 } / a _ { 1 }$ times the first row, we obtain

$$
\Delta_ {4} = \left| \begin{array}{c c c c} a _ {1 1} & a _ {3} & a _ {5} & a _ {7} \\ 0 & a _ {2 2} & a _ {2 3} & a _ {2 4} \\ 0 & a _ {1} & a _ {3} & a _ {5} \\ 0 & a _ {0} & a _ {2} & a _ {4} \end{array} \right|
$$

where

$$a _ {1 1} = a _ {1}a _ {2 2} = a _ {2} - \frac {a _ {0}}{a _ {1}} a _ {3}a _ {2 3} = a _ {4} - \frac {a _ {0}}{a _ {1}} a _ {5}a _ {2 4} = a _ {6} - \frac {a _ {0}}{a _ {1}} a _ {7}$$

Similarly, subtracting from the fourth row $a _ { 0 } / a _ { 1 }$ times the third row yields

$$
\Delta_ {4} = \left| \begin{array}{c c c c} a _ {1 1} & a _ {3} & a _ {5} & a _ {7} \\ 0 & a _ {2 2} & a _ {2 3} & a _ {2 4} \\ 0 & a _ {1} & a _ {3} & a _ {5} \\ 0 & 0 & \hat {a} _ {4 3} & \hat {a} _ {4 4} \end{array} \right|
$$

where

$$\hat {a} _ {4 3} = a _ {2} - \frac {a _ {0}}{a _ {1}} a _ {3}\hat {a} _ {4 4} = a _ {4} - \frac {a _ {0}}{a _ {1}} a _ {5}$$

Next, subtracting from the third row $a _ { 1 } / a _ { 2 2 }$ times the second row yields

$$
\Delta_ {4} = \left| \begin{array}{c c c c} a _ {1 1} & a _ {3} & a _ {5} & a _ {7} \\ 0 & a _ {2 2} & a _ {2 3} & a _ {2 4} \\ 0 & 0 & a _ {3 3} & a _ {3 4} \\ 0 & 0 & \hat {a} _ {4 3} & \hat {a} _ {4 4} \end{array} \right|
$$

where

$$a _ {3 3} = a _ {3} - \frac {a _ {1}}{a _ {2 2}} a _ {2 3}a _ {3 4} = a _ {5} - \frac {a _ {1}}{a _ {2 2}} a _ {2 4}$$

Finally, subtracting from the last row $\hat { a } _ { 4 3 } / a _ { 3 3 }$ times the third row yields
