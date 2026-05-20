# 17.2 ν-Gap Metric

The shortfall of the gap metric is that it is not easily related to the frequency response of the system. On the other hand, the ν-gap metric to be introduced in this section has a clear frequency domain interpolation and can, in general, be computed from frequency response. The presentation given in this section, Sections 17.3, 17.4, and 17.5 are based on Vinnicombe [1993a, 1993b], to which readers are referred for further detailed discussions.

To define the new metric, we shall first review a basic concept from the complex analysis.

Definition 17.1 Let g(s) be a scalar transfer function and let Γ denote a Nyquist contour indented around the right of any imaginary axis poles of g(s), as shown in Figure 17.1. Then the winding number of g(s) with respect to this contour, denoted by wno(g), is the number of counterclockwise encirclements around the origin by g(s) evaluated on the Nyquist contour Γ. (A clockwise encirclement counts as a negative encirclement.)

![](image/c75222d8bc57feaeab6d92616ef51476cea0f62352bac9b44b88772c41fe3306.jpg)

<details>
<summary>text_image</summary>

Γ
O
</details>

Figure 17.1: The Nyquist contour

The following argument principle is standard and can be found from any complex analysis book.

Lemma 17.4 (The Argument Principle) Let Γ be a closed contour in the complex plane. Let f(s) be a function analytic along the contour; that is, f(s) has no poles on Γ. Assume f(s) has Z zeros and P poles inside Γ. Then f(s) evaluated along the contour Γ once in an anticlockwise direction will make Z − P anticlockwise encirclements of the origin.

Let $G ( s )$ be a matrix (or scalar) transfer matrix. We shall denote $\eta ( G )$ and $\eta _ { 0 } ( G )$ , respectively, the number of open right-half plane and imaginary axis poles of $G ( s )$ .

The winding number has the following properties:

Lemma 17.5 Let g and h be biproper rational scalar transfer functions and let F be a square transfer matrix. Then

(a) $\operatorname { w n o } ( g h ) = \operatorname { w n o } ( g ) + \operatorname { w n o } ( h ) ,$   
(b) wno $( g ) = \eta ( g ^ { - 1 } ) - \eta ( g )$ ;   
(c) wno $( g ^ { \sim } ) = - \mathrm { w n o } ( g ) - \eta _ { 0 } ( g ^ { - 1 } ) + \eta _ { 0 } ( g ) _ { }$ ;   
(d) wno(1 + g) = 0 if $g \in \mathcal { R } \mathcal { L } _ { \infty }$ and $\| g \| _ { \infty } < 1$   
(e) wno $\operatorname* { d e t } ( I + F ) = 0 \ i f \ F \in \mathcal { R L } _ { \infty } \ a n d \ \| F \| _ { \infty } < 1 .$
