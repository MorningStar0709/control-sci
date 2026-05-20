The general shape of the polar plot of $G ( j \omega )$ is shown in Figure 7–31. The G(jv) plot is asymptotic to the vertical line passing through the point (–T, 0). Since this transfer function involves an integrator (1/s), the general shape of the polar plot differs substantially from those of second-order transfer functions that do not have an integrator.

EXAMPLE 7–9 Obtain the polar plot of the following transfer function:

$$G (j \omega) = \frac {e ^ {- j \omega L}}{1 + j \omega T}$$

Since G(jv) can be written

$$G (j \omega) = \left(e ^ {- j \omega L}\right) \left(\frac {1}{1 + j \omega T}\right)$$

the magnitude and phase angle are, respectively,

$$\left| G (j \omega) \right| = \left| e ^ {- j \omega L} \right| \cdot \left| \frac {1}{1 + j \omega T} \right| = \frac {1}{\sqrt {1 + \omega^ {2} T ^ {2}}}$$

and

$$\underline {{G (j \omega)}} = \underline {{e ^ {- j \omega L}}} + \underline {{\frac {1}{1 + j \omega T}}} = - \omega L - \tan^ {- 1} \omega T$$

Since the magnitude decreases from unity monotonically and the phase angle also decreases monotonically and indefinitely, the polar plot of the given transfer function is a spiral, as shown in Figure 7–32.

Figure 7–32 Polar plot of $e ^ { - j { \omega } L } / \bar { ( 1 + j { \omega } T ) } .$   
![](image/274a5b5052d284891ae75a7206c2d94660da96f806b5b80331a0adf5d4e519fe.jpg)

<details>
<summary>text_image</summary>

Im
1
Re
</details>

General Shapes of Polar Plots. The polar plots of a transfer function of the form

$$
\begin{array}{l} G (j \omega) = \frac {K (1 + j \omega T _ {a}) (1 + j \omega T _ {b}) \cdots}{(j \omega) ^ {\lambda} (1 + j \omega T _ {1}) (1 + j \omega T _ {2}) \cdots} \\ = \frac {b _ {0} (j \omega) ^ {m} + b _ {1} (j \omega) ^ {m - 1} + \cdots}{a _ {0} (j \omega) ^ {n} + a _ {1} (j \omega) ^ {n - 1} + \cdots} \\ \end{array}
$$

where $n > m$ or the degree of the denominator polynomial is greater than that of the numerator, will have the following general shapes:
