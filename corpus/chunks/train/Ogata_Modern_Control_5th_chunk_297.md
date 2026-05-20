![](image/a6a07934acf2f64fd0a1e29edbbbecca2ae67c06646c504781fbdd12d2bde93a.jpg)

<details>
<summary>text_image</summary>

ζ = 0.7 line
145°
jω
j2
j1
-4
-3
-2
-1
0
1
σ
-j1
-j2
x
</details>

Figure 6–10 Root-locus plot.

The value of the gain K at any point on root locus can be found by applying the magnitude condition or by use of MATLAB (see Section 6–3). For example, the value of K at which the complex-conjugate closed-loop poles have the damping ratio z=0.7 can be found by locating the roots, as shown in Figure 6–10, and computing the value of K as follows:

$$K = \left| \frac {(s + 1 - j \sqrt {2}) (s + 1 + j \sqrt {2})}{s + 2} \right| _ {s = - 1. 6 7 + j 1. 7 0} = 1. 3 4$$

Or use MATLAB to find the value of K. (See Section 6–4.)

It is noted that in this system the root locus in the complex plane is a part of a circle. Such a circular root locus will not occur in most systems. Circular root loci may occur in systems that involve two poles and one zero, two poles and two zeros, or one pole and two zeros. Even in such systems, whether circular root loci occur depends on the locations of poles and zeros involved.

To show the occurrence of a circular root locus in the present system, we need to derive the equation for the root locus. For the present system, the angle condition is

$$\underline {{s + 2}} - \underline {{s + 1 - j \sqrt {2}}} - \underline {{s + 1 + j \sqrt {2}}} = \pm 1 8 0 ^ {\circ} (2 k + 1)$$

If s=s+jv is substituted into this last equation, we obtain

$$\underline {{\left/ \sigma + 2 + j \omega \left. \right.}} - \underline {{\left/ \sigma + 1 + j \omega - j \sqrt {2} \left. \right.}} - \underline {{\left/ \sigma + 1 + j \omega + j \sqrt {2} \left. \right.}} = \pm 1 8 0 ^ {\circ} (2 k + 1)$$

which can be written as

$$\tan^ {- 1} \left(\frac {\omega}{\sigma + 2}\right) - \tan^ {- 1} \left(\frac {\omega - \sqrt {2}}{\sigma + 1}\right) - \tan^ {- 1} \left(\frac {\omega + \sqrt {2}}{\sigma + 1}\right) = \pm 1 8 0 ^ {\circ} (2 k + 1)$$

or

$$\tan^ {- 1} \left(\frac {\omega - \sqrt {2}}{\sigma + 1}\right) + \tan^ {- 1} \left(\frac {\omega + \sqrt {2}}{\sigma + 1}\right) = \tan^ {- 1} \left(\frac {\omega}{\sigma + 2}\right) \pm 1 8 0 ^ {\circ} (2 k + 1)$$

Taking tangents of both sides of this last equation using the relationship

$$\tan (x \pm y) = \frac {\tan x \pm \tan y}{1 \mp \tan x \tan y} \tag {6-10}$$

we obtain
