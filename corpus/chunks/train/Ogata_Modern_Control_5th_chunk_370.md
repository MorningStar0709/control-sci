$$\underline {{\sigma - 1 + j \omega}} + \underline {{\sigma + 2 + j \omega + j \sqrt {3}}} + \underline {{\sigma + 2 + j \omega - j \sqrt {3}}} = \pm 1 8 0 ^ {\circ} (2 k + 1)$$

or

$$\underline {{\left/ \sigma + 2 + j (\omega + \sqrt {3}) \left. \right.}} + \underline {{\left/ \sigma + 2 + j (\omega - \sqrt {3}) \left. \right.}} = - \underline {{\left/ \sigma - 1 + j \omega \left. \right.}} \pm 1 8 0 ^ {\circ} (2 k + 1)$$

which can be rewritten as

$$\tan^ {- 1} \left(\frac {\omega + \sqrt {3}}{\sigma + 2}\right) + \tan^ {- 1} \left(\frac {\omega - \sqrt {3}}{\sigma + 2}\right) = - \tan^ {- 1} \left(\frac {\omega}{\sigma - 1}\right) \pm 1 8 0 ^ {\circ} (2 k + 1)$$

Taking tangents of both sides of this last equation, we obtain

$$\frac {\frac {\omega + \sqrt {3}}{\sigma + 2} + \frac {\omega - \sqrt {3}}{\sigma + 2}}{1 - \left(\frac {\omega + \sqrt {3}}{\sigma + 2}\right) \left(\frac {\omega - \sqrt {3}}{\sigma + 2}\right)} = - \frac {\omega}{\sigma - 1}$$

or

$$\frac {2 \omega (\sigma + 2)}{\sigma^ {2} + 4 \sigma + 4 - \omega^ {2} + 3} = - \frac {\omega}{\sigma - 1}$$

which can be simplified to

$$2 \omega (\sigma + 2) (\sigma - 1) = - \omega \left(\sigma^ {2} + 4 \sigma + 7 - \omega^ {2}\right)$$

or

$$\omega (3 \sigma^ {2} + 6 \sigma + 3 - \omega^ {2}) = 0$$

Further simplification of this last equation yields

$$\omega \left(\sigma + 1 + \frac {1}{\sqrt {3}} \omega\right) \left(\sigma + 1 - \frac {1}{\sqrt {3}} \omega\right) = 0$$

which defines three lines:

$$\omega = 0, \quad \sigma + 1 + \frac {1}{\sqrt {3}} \omega = 0, \quad \sigma + 1 - \frac {1}{\sqrt {3}} \omega = 0$$

Thus the root-locus branches consist of three lines. Note that the root loci for K>0 consist of portions of the straight lines as shown in Figure 6–69(b). (Note that each straight line starts from an open-loop pole and extends to infinity in the direction of 180°, 60°, or –60° measured from the real axis.) The remaining portion of each straight line corresponds to K<0.

A–6–8. Consider a unity-feedback control system with the following feedforward transfer function:

$$G (s) = \frac {K}{s (s + 1) (s + 2)}$$

Using MATLAB, plot the root loci and their asymptotes.

Solution. We shall plot the root loci and asymptotes on one diagram. Since the feedforward transfer function is given by

$$
\begin{array}{l} G (s) = \frac {K}{s (s + 1) (s + 2)} \\ = \frac {K}{s ^ {3} + 3 s ^ {2} + 2 s} \\ \end{array}
$$

the equation for the asymptotes may be obtained as follows: Noting that
