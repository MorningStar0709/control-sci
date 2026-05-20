# Example 5.8

Figure 5.3 shows the seat-suspension system presented by Example 2.3 in Chapter 2. Obtain a complete SSR, where the two sensor measurements are displacement and acceleration of the mass that represents the driver.   
![](image/d869fe5e5d3283b8ccfbca3ae80176b5018394417d2ad2b78f5acabfe7688630.jpg)

<details>
<summary>text_image</summary>

Driver mass, m₂
Seat mass, m₁
z₂ Driver displacement
k₂ b₂
z₁ Seat displacement
k₁ b₁
Seat suspension
z₀(t) Cabin floor displacement
</details>

(a)

![](image/3d950f0b39e1b8bbff5a4d1878511414cc8c1aea432d68e7bf5db80806639741.jpg)

<details>
<summary>text_image</summary>

Driver mass
m₂
k₂
b₂
Seat mass
m₁
k₁
b₁
z₂
z₁
z₀(t)
</details>

(b)   
Figure 5.3 (a) Schematic diagram of the seat-suspension system for Example 5.8.   
(b) Mechanical model for the seat-suspension system.

The governing mathematical modeling equations are repeated

$$m _ {1} \ddot {z} _ {1} + b _ {1} \dot {z} _ {1} + b _ {2} (\dot {z} _ {1} - \dot {z} _ {2}) + k _ {1} z _ {1} + k _ {2} (z _ {1} - z _ {2}) = b _ {1} \dot {z} _ {0} (t) + k _ {1} z _ {0} (t) \tag {5.44a}m _ {2} \ddot {z} _ {2} + b _ {2} (\dot {z} _ {2} - \dot {z} _ {1}) + k _ {2} (z _ {2} - z _ {1}) = 0 \tag {5.44b}$$

Recall that the system variables are the vertical displacements of the seat mass $( z _ { 1 } )$ and driver mass $( z _ { 2 } )$ , and that both are measured relative to their static equilibrium positions. The vertical displacement of the cabin floor (due to road vibrations) is $z _ { 0 } ( t )$ , which is considered to be an input to the system. The remaining parameters are the seat and driver masses $( m _ { 1 }$ and $m _ { 2 } )$ , and the passive friction and stiffness coefficients $( b _ { i }$ and $k _ { i } .$ , respectively). The two measurements associated with the test rig are driver displacement $z _ { 2 }$ and driver acceleration $\ddot { z } _ { 2 }$ . Displacement is measured by a linear variable differential transformer (LVDT), an electromechanical device used to measure translational displacement. Acceleration is measured by an accelerometer.
