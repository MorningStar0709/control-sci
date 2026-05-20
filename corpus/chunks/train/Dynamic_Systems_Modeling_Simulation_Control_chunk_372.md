# Case 3: two complex conjugate roots

If the radicand in Eq. (7.51) is negative (and coefficient $a _ { 1 }$ is not zero), then the two roots are complex and will be composed of a real part ?? and an imaginary part $\beta$

$$r _ {1} = \alpha + j \beta \quad \text { and } \quad r _ {2} = \alpha - j \beta \tag {7.54}$$

These roots are complex conjugates because they have the same real part (??) and the imaginary parts $( j \beta$ and $- j \beta )$ have equal magnitudes but opposite signs. Therefore, complex conjugate roots exhibit symmetry about the real or x-axis when plotted in the complex plane. The homogeneous solution has the form

$$y _ {H} (t) = c _ {1} e ^ {(\alpha + j \beta) t} + c _ {2} e ^ {(\alpha - j \beta) t} = e ^ {\alpha t} \left(c _ {1} e ^ {j \beta t} + c _ {2} e ^ {- j \beta t}\right) \tag {7.55}$$

Using Euler’s formula, $e ^ { j \theta } = \cos \theta + j$ sin ?? with $\theta = \beta t ,$ , Eq. (7.55) becomes

$$
\begin{array}{l} y _ {H} (t) = e ^ {\alpha t} [ c _ {1} (\cos \beta t + j \sin \beta t) + c _ {2} (\cos \beta t - j \sin \beta t) ] \\ = e ^ {\alpha t} \left[ \left(c _ {1} + c _ {2}\right) \cos \beta t + j \left(c _ {1} - c _ {2}\right) \sin \beta t \right] \tag {7.56} \\ \end{array}
$$

Because the response $y _ { H } ( t )$ must be a real number, the sine factor $( c _ { 1 } - c _ { 2 } )$ must be an imaginary number, while the cosine factor $( c _ { 1 } + c _ { 2 } )$ must be a real number. Therefore, the constants $c _ { 1 }$ and $c _ { 2 }$ are complex conjugates. Defining two new real constants $c _ { 3 } = c _ { 1 } + c _ { 2 }$ and $c _ { 4 } = j ( c _ { 1 } - c _ { 2 } )$ , we can rewrite Eq. (7.56) as

$$y _ {H} (t) = e ^ {\alpha t} \left[ c _ {3} \cos \beta t + c _ {4} \sin \beta t \right] \tag {7.57}$$

Another (perhaps simpler) form of the free response Eq. (7.57) is

$$y _ {H} (t) = K e ^ {\alpha t} \cos (\beta t + \phi) \tag {7.58}$$

where we have used the trigonometric identity for linear combinations of sine and cosine functions

$$A \cos \beta t + B \sin \beta t = \sqrt {A ^ {2} + B ^ {2}} \cos \left(\beta t - \tan^ {- 1} \frac {B}{A}\right)$$

The reader should note that Eqs. (7.57) and (7.58) are equivalent, and both involve two unknown constants. We will use Eq. (7.58) for the free response of a second-order system with complex roots, where the two unknowns are amplitude K and phase angle ??, which can be determined from the two initial conditions $y _ { 0 }$ and $\dot { y } _ { 0 }$ .
