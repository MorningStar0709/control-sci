# 7.7.2 Minimizer ${ \pmb u } ^ { 0 } ( { \pmb x } )$ Is Unique for all $\boldsymbol { x } \in \boldsymbol { x }$

Before proceeding to obtain the solution to a parametric linear program when the minimizer $u ^ { 0 } ( x )$ is unique for each $x \in { \mathcal { X } }$ , we look first at the simple example illustrated in Figure 7.8, which shows the constraint set $\mathcal { U } ( x )$ for various values of the parameter x in the interval $[ x _ { 1 } , x _ { 3 } ]$ . The set $\mathcal { U } ( x _ { 1 } )$ has six faces: $F _ { 1 } ( x _ { 1 } ) , F _ { 2 } ( x _ { 1 } ) , F _ { 3 } ( x _ { 1 } ) , F _ { 4 } ( x _ { 1 } ) , F _ { 5 } ( x _ { 1 } )$ and $F _ { 6 } ( x _ { 1 } )$ . Face $F _ { 1 } ( x )$ lies in the hyperplane $\mathcal { H } _ { 1 } ( x )$ that varies linearly with $x ;$ each face $F _ { i } ( x ) , i \ = \ 2 , \ldots , 6$ , lies in the hyperplane $\mathcal { H } _ { i }$ that does not vary with x. All the faces vary with x as shown so that $\mathcal { U } ( x _ { 2 } )$ has four faces: $F _ { 1 } ( x _ { 2 } ) , F _ { 3 } ( x _ { 2 } ) , F _ { 4 } ( x _ { 2 } )$ and $F _ { 5 } ( x _ { 2 } )$ ; and $\mathcal { U } ( x _ { 3 } )$ has three faces: $F _ { 1 } ( x _ { 3 } ) , F _ { 4 } ( x _ { 3 } )$ and $F _ { 5 } ( x _ { 3 } )$ . The face $F _ { 1 } ( x )$ is shown for three values of $x \colon \ x \ = \ x _ { 1 }$ (the bold line), and $x \ = \ x _ { 2 }$ and $x \ = \ x _ { 3 }$ (dotted lines). It is apparent that for $x \in [ x _ { 1 } , x _ { 2 } ] , u ^ { 0 } ( x ) = u _ { 2 , 3 }$ in which $u _ { 2 , 3 }$ is the intersection of $\mathcal { H } _ { 2 }$ and ${ \mathcal { H } } _ { 3 }$ , and $u ^ { 0 } ( x _ { 3 } ) = u _ { 3 , 4 }$ , in which $u _ { 3 , 4 }$ is the intersection of $\mathcal { H } _ { 3 }$ and ${ \mathcal { H } } _ { 4 }$ . It can also be seen that $u ^ { 0 } ( x )$ is unique for all $x \in { \mathcal { X } }$ .

![](image/27462becc3270f2c441c920c2247eb39b9e01a0d66a66b7b8e36327de8003d04.jpg)

<details>
<summary>text_image</summary>

u2
M4'
3
F4(x1)
u3,4
F3(x1)
U(x1)
u2,3 = u0(x1)
F1(x3)
F5(x1)
F1(x2)
F2(x1)
M2'
M5'
- r
0
F6(x1)
3
u1
M1'
M6'
</details>

Figure 7.8: Solution to a parametric linear program.

We now return to the general case. Suppose, for $\mathrm { s o m e } \in \mathcal { X } , u ^ { 0 } ( x )$ is the unique solution of $\mathbb { P } ( x ) ; u ^ { 0 } ( x )$ is the unique solution of

$$M _ {x} ^ {0} \boldsymbol {u} = N _ {x} ^ {0} \boldsymbol {x} + p _ {x} ^ {0}$$

It follows that $u ^ { 0 } ( x )$ is the trivial solution of the simple equality constrained problem defined by

$$V ^ {0} (x) = \min _ {u} \{V (x, u) \mid M _ {x} ^ {0} u = N _ {x} ^ {0} x + p _ {x} ^ {0} \} \tag {7.20}$$

The solution $u ^ { 0 } ( x )$ of this equality constrained problem is trivial because it is determined entirely by the equality constraints; the cost plays no part.
