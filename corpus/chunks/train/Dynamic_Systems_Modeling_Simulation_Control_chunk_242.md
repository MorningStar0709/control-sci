# Example 5.13

Figure 5.7 shows a simple two-mass mechanical system. We wish to derive the I/O equation with the displacement of mass $m _ { 1 }$ as the output variable, $\mathrm { o r } y = z _ { 1 }$ , and the applied force $F _ { a } ( t )$ as the input variable.

Displacements $z _ { 1 }$ and $z _ { 2 }$ are measured from their respective equilibrium (unstretched) positions. The mathematical model can be derived using a free-body diagram and the methods from Chapter 2. The result is

$$m _ {1} \ddot {z} _ {1} + b \dot {z} _ {1} + k (z _ {1} - z _ {2}) = 0m _ {2} \ddot {z} _ {2} + k (z _ {2} - z _ {1}) = F _ {a} (t) \tag {5.90}$$

Therefore, the mathematical model (5.90) becomes

$$m _ {1} \ddot {y} + b \dot {y} + k (y - z _ {2}) = 0m _ {2} \ddot {z} _ {2} + k (z _ {2} - y) = u \tag {5.91}$$

Clearly, we need to eliminate $z _ { 2 }$ from the differential equation containing ÿ in order to obtain the I/O equation, that is, in terms of output y only. By applying the D operator, we can rewrite Eq. (5.91) as

$$m _ {1} D ^ {2} y + b D y + k \left(y - z _ {2}\right) = 0 \tag {5.92}m _ {2} D ^ {2} z _ {2} + k \left(z _ {2} - y\right) = u \tag {5.93}$$

We can solve Eq. (5.93) for displacement $z _ { 2 }$

$$z _ {2} = \frac {u + k y}{m _ {2} D ^ {2} + k}$$

![](image/b913750b2247c1494f8d23e3df49a3c90fb61d773bc6ed7e93e74d7cacef6e24.jpg)

<details>
<summary>text_image</summary>

b
m₁
k
m₂
z₁
z₂
Fₐ(t)
</details>

Figure 5.7 Two-mass mechanical system for Example 5.13.

and substitute into Eq. (5.92). The result is

$$m _ {1} D ^ {2} y + b D y + k y - \frac {k (u + k y)}{m _ {2} D ^ {2} + k} = 0$$

Multiplying this equation by $m _ { 2 } D ^ { 2 } + k$ in order to clear the fraction yields

$$m _ {1} D ^ {2} (m _ {2} D ^ {2} + k) y + b D (m _ {2} D ^ {2} + k) y + k (m _ {2} D ^ {2} + k) y - k (u + k y) = 0$$

Finally, we can convert this equation from operator form to a differential equation by replacing the $D ^ { k }$ terms with the respective time derivatives

$$m _ {1} m _ {2} y ^ {(4)} + b m _ {2} \ddot {y} + (m _ {1} k + m _ {2} k) \ddot {y} + b k \dot {y} = k u \tag {5.94}$$

where $y ^ { ( 4 ) } = d ^ { 4 } y / d t ^ { 4 }$ . Equation (5.94) is the I/O equation of the dual-mass system with output $y = z _ { 1 }$ . Note that the governing mathematical model (5.90) is fourth order (i.e., we would need four state variables for an SSR). Consequently, the I/O equation (5.94) is of order four.
