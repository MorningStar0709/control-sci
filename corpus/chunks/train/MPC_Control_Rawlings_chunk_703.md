# 6.3.2 Coupled Input Constraints

By contrast, in the coupled constraint case, the constraints are of the form

$$H _ {1} \mathbf {u} _ {1} + H _ {2} \mathbf {u} _ {2} \leq h \quad \text {or} \quad (\mathbf {u} _ {1}, \mathbf {u} _ {2}) \in \mathbb {U} \tag {6.21}$$

These constraints represent the players sharing some common resource. An example would be different subsystems in a chemical plant drawing steam or some other utility from a single plantwide generation plant. The total utility used by the different subsystems to meet their control objectives is constrained by the generation capacity.

The players solve the same optimization problems as in the uncoupled constraint case, with the exception that both players’ input constraints are given by (6.21). This modified game provides only two of the three properties established for the uncoupled constraint case. These are

1. The iterates are feasible: $( \mathbf { u } _ { 1 } , \mathbf { u } _ { 2 } ) ^ { p } \in \mathbb { U }$ implies $( \mathbf { u } _ { 1 } , \mathbf { u } _ { 2 } ) ^ { p + 1 } \in \mathbb { U }$ . This follows from convexity of U and the convex combination of the feasible points $( \mathbf { u } _ { 1 } ^ { p } , \mathbf { u } _ { 2 } ^ { p } )$ and $( \mathbf { u } _ { 1 } ^ { 0 } , \mathbf { u } _ { 2 } ^ { 0 } )$ to make $( { \bf u } _ { 1 } , { \bf u } _ { 2 } ) ^ { p + 1 }$ .

2. The cost decreases on iteration: $V ( x _ { 1 } ( 0 ) , x _ { 2 } ( 0 ) , ( { \bf u } _ { 1 } , { \bf u } _ { 2 } ) ^ { p + 1 } ) \ \le$ $V ( x _ { 1 } ( 0 ) , x _ { 2 } ( 0 ) , ( { \bf u } _ { 1 } , { \bf u } _ { 2 } ) ^ { p } )$ for all $x _ { 1 } ( 0 ) , x _ { 2 } ( 0 )$ , and for all feasible $( \mathbf { u } _ { 1 } , \mathbf { u } _ { 2 } ) ^ { p } \in \mathbb { U }$ . The systemwide cost satisfies the same inequalities established for the uncoupled constraint case giving

$$V (x (0), \mathbf {u} _ {1} ^ {p + 1}, \mathbf {u} _ {2} ^ {p + 1}) \leq V (x (0), \mathbf {u} _ {1} ^ {p}, \mathbf {u} _ {2} ^ {p})$$

Because the cost is bounded below, the cost iteration converges.

![](image/52febad05a8aed3a00fc9ee1df760b321f24e9db9d811622ea885e09f9b34210.jpg)

<details>
<summary>text_image</summary>

cost decrease for player two
u2
uce
vp
cost decrease for player one
U
u1
</details>

Figure 6.6: Cooperative control stuck on the boundary of U under coupled constraints; $u ^ { p + 1 } = u ^ { p } \neq u _ { \mathrm { c e } }$ .
