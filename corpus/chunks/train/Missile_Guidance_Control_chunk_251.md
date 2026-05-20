The vector functions $\mathbf { f } ( t _ { i } ) , \mathbf { g } ( t _ { i } )$ , and $\mathbf { h } ( t _ { i } )$ are calculated as in $_ { ( 4 . 7 \mathrm { a } , \mathrm { b } , \mathrm { c } ) }$ so as to satisfy the Taylor series expansion in $( t - t _ { i } )$ for r, v, and t over the time interval $t _ { i } \leq t < t _ { i + 1 }$ . Then, using (4.2c,d,e) as stored quantities, we can compute r(t), v(t), and ${ \bf a } ( t )$ as follows:

$$\mathbf {r} (t) = \mathbf {r} (t _ {i}) + \mathbf {v} (t _ {i}) (t - t _ {i}) + 0. 5 \mathbf {a} (t _ {i}) (t - t _ {i}) ^ {2} + \mathbf {f} (t _ {i}) (t - t _ {i}) ^ {3}+ \mathbf {g} (t _ {i}) (t - t _ {i}) ^ {4} + \mathbf {h} (t _ {i}) (t - t _ {i}) ^ {5}, \tag {4.8a}\mathbf {v} (t) = \mathbf {v} (t _ {i}) + \mathbf {a} (t - t _ {i}) + 3 \mathbf {f} (t _ {i}) (t - t _ {i}) ^ {2} + 4 \mathbf {g} (t _ {i}) (t - t _ {i}) ^ {3} + 5 \mathbf {h} (t _ {i}) (t - t _ {i}) ^ {4}, \tag {4.8b}\mathbf {a} (t) = \mathbf {a} (t _ {i}) + 6 \mathbf {f} (t _ {i}) (t - t _ {i}) + 1 2 \mathbf {g} (t _ {i}) (t - t _ {i}) ^ {2} + 2 0 \mathbf {h} (t _ {i}) (t - t _ {i}) ^ {3}. \tag {4.8c}$$

We will now discuss the target motion model. The target aircraft trajectory is described by its initial conditions (position and velocity) and a maneuver start time. Maneuver direction will be defined as follows: A plane, which we shall call the “lift plane,” is perpendicular to the instantaneous velocity vector. The unit lift vector $\mathbf { 1 } _ { L }$ will lie in this plane and will be in the direction as shown in Figure 4.6, given the roll direction angle $\phi$ . The lift magnitude $a _ { L }$ is computed as

$$a _ {L} = \omega_ {v} | \mathbf {v} _ {T} |, \tag {4.9}$$

where $\omega _ { v }$ is the input velocity vector turn rate and ${ \bf v } _ { T }$ is the instantaneous target velocity vector.

In general, the target equations of motion can be written as follows [2]:

$$\frac {d \mathbf {r} _ {T}}{d t} = \mathbf {v} _ {T}, \tag {4.10a}\frac {d \mathbf {v} _ {T}}{d t} = \mathbf {a} _ {T} = a _ {v} \mathbf {1} _ {v} + a _ {L} \mathbf {1} _ {L}, \tag {4.10b}$$

![](image/c7ef6327efd4261eb1b7394d666e6a874f4aff535635c07dc003c1e31d373e7a.jpg)

<details>
<summary>text_image</summary>

Plane normal to
target velocity vector
1z (unit vector
upward)
Target
v × 1z
φ
v × (v × 1z)
Maneuver
direction
1L
v
(target velocity vector)
z
y
x
</details>

(a) Coordinate system for specifying target maneuver direction

![](image/81a7f5a5a75da599287d9117649de2cdfa6f2f58db9ad8fb75955224ecff8c36.jpg)

<details>
<summary>text_image</summary>
