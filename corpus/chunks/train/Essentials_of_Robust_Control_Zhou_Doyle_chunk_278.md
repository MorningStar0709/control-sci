Now generate the singular value frequency responses of $G _ { p } { \mathrm { : } }$

w=logspace(-3,3,300);   
$\gg \bf G p f = \bf f r s p ( G _ { p } , w )$ ; % Gpf is the frequency response of $G _ { p } ;$   
$\begin{array} { r } { \gg [ \mathbf { u } , \mathbf { s } , \mathbf { v } ] = \mathbf { v s v d } ( \mathbf { G p f } ) ; } \end{array}$

$\gg \bf v p l o t ( ' l i v , m ^ { \prime } , s )$

The singular value frequency responses of $G _ { p }$ are shown in Figure 10.6. To test the robust stability, we need to compute $\| G _ { p 1 1 } \| _ { \infty } .$

$\begin{array} { r } { \gg  { \mathbf { G } } _ { \mathbf { p } 1 1 } = \mathbf { s e l } (  { \mathbf { G } } _ { \mathbf { p } } , 1 : 2 , 1 : 2 ) ; } \end{array}$   
norm of $\mathbf { \tilde { G } _ { p 1 1 } } = \mathbf { h i n f n o r m } ( \mathbf { G _ { p 1 1 } } , \mathbf { 0 . 0 0 1 } )$

which gives $\| G _ { P 1 1 } \| _ { \infty } = 0 . 9 3 3 < 1$ . So the system is robustly stable. To check the robust performance, we shall compute the $\mu _ { \Delta _ { P } } ( G _ { p } ( j \omega ) )$ for each frequency with

$$
\Delta_ {P} = \left[ \begin{array}{c c} \Delta & \\ & \Delta_ {f} \end{array} \right], \Delta \in \mathbb {C} ^ {2 \times 2}, \Delta_ {f} \in \mathbb {C} ^ {4 \times 2}.
$$

![](image/02f71c9ab310866c75f21c6798a3b69be72f201db384d542c474da29999704d5.jpg)

<details>
<summary>line</summary>

| frequency (rad/sec) | maximum singular value |
| --- | --- |
| 10⁻³ | 0.8 |
| 10⁻² | 0.8 |
| 10⁻¹ | 0.8 |
| 10⁰ | 1.2 |
| 10¹ | 0.9 |
| 10² | 1.8 |
| 10³ | 0.5 |
</details>

Figure 10.7: $\mu _ { \Delta _ { P } } ( G _ { p } ( j \omega ) )$ and $\overline { { \sigma } } ( G _ { p } ( j \omega ) )$

$\mathbf { b l k { = } [ 2 , 2 ; 4 , 2 ] }$ ;   
$[ \mathbf { b n d s } , \mathbf { d v e c } , \mathbf { s e n s } , \mathbf { p v e c } ] { = } \mathbf { m u } ( \mathbf { G p f } , \mathbf { b l k } ) ;$   
vplot(0 liv, m0 , vnorm(Gpf ), bnds)   
title(0 Maximum Singular Value and mu0 )   
xlabel(0 frequency(rad/sec)0 )

text(0.01, 1.7, 0 maximum singular value0 )   
text(0.5, 0.8, 0 mu bounds0 )

The structured singular value $\mu _ { \Delta _ { P } } ( G _ { p } ( j \omega ) )$ and $\overline { { \sigma } } ( G _ { p } ( j \omega ) )$ are shown in Figure 10.7. It is clear that the robust performance is not satisfied. Note that

$$
\max _ {\| \Delta \| _ {\infty} \leq 1} \| \mathcal {F} _ {u} (G _ {p}, \Delta) \| _ {\infty} \leq \gamma \Longleftrightarrow \sup _ {\omega} \mu_ {\Delta_ {P}} \left(\left[ \begin{array}{c c} G _ {p 1 1} & G _ {p 1 2} \\ G _ {p 2 1} / \gamma & G _ {p 2 2} / \gamma \end{array} \right]\right) \leq 1.
$$

Using a bisection algorithm, we can also find the worst performance:

$$\max _ {\| \Delta \| _ {\infty} \leq 1} \| \mathcal {F} _ {u} (G _ {p}, \Delta) \| _ {\infty} = 1 2. 7 8 2 4.$$
