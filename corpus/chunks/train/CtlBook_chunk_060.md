# 2.4.1 Parallel and Series Combinations

We were able to simplify the EOM in Example 2.3 in a way which added the two dampers together. If you think about a simple modication to Example 2.3, you can see that the same could be done with springs as well. The general principle is that springs and dampers combine (like capacitors in electric circuits) (Figure 2.2) as follows:

Springs and dampers in parallel can be combined by addition.

Springs and dampers in series can be combined like parallel resistors:

![](image/1d13bde16be4090ffca509bbbb0633350443527a2ea9f130436dfb455e33b8fd.jpg)

<details>
<summary>text_image</summary>

K₁
→ K₁+K₂
K₂
K₁ K₂ → (K₁K₂)/(K₁+K₂)
</details>

Figure 2.2: Springs in parallel and series can be combined (like capacitors).

Proof: Consider two springs in series. The force, f is the same throughout all elements of a serial chain, and both springs independently obey Hooke's Law:

$$f = K _ {1} \Delta x _ {1} = K _ {2} \Delta x _ {2}$$

The total change in length due to the applied force, f, is

$$\Delta x = \Delta x _ {1} + \Delta x _ {2}\Delta x = \frac {f}{K _ {1}} + \frac {f}{K _ {2}}K _ {T} = \frac {f}{\Delta x} = \frac {1}{1 / K _ {1} + 1 / K _ {2}} = \frac {K _ {1} K _ {2}}{K _ {1} + K _ {2}} \tag {2.2}$$

An almost identical proof can be made for series connected dampers.

However, Mass, M is dierent (Figure 2.3) because of the unique property that the force on a mass depends on the acceleration only with respect to the inertial frame:

$$f = m \ddot {x}, \quad \text { NOT } \quad f = m (\ddot {x} _ {i} - \ddot {x} _ {j})$$

Thus

![](image/225e967633588db04c65e6afb031149714bfb03e97ab93e7b4b9504812fed84b.jpg)

<details>
<summary>text_image</summary>

-M₁
= -M₁ -M₂ = -M₁ + M₂
</details>

Figure 2.3: Add two masses which ever way they are combined.

What about the case where a spring and damper are connected in series (Figure 2.4)?

Using a similar analysis based on the fact that f is the same in both elements of a serial chain:

$$f = K (x _ {1} - x _ {2}) = B (\dot {x} _ {2} - \dot {x} _ {3})$$

The dierence here is that we have a new unknown x2. This new unknown requires a new EOM however $m _ { 2 } = 0 .$ . The EOMS for the system of Figure 2.4 are thus:

$$K (x _ {1} - x _ {2}) = f0 \ddot {x} _ {2} + K (x _ {2} - x _ {1}) + B (\dot {x} _ {2} - \dot {x} _ {3}) = 0B (\dot {x} _ {3} - \dot {x} _ {2}) = f$$

![](image/e9c41099ff5355ff2592ab4cd18053d1a83681ff9f5b359daa140c59e031c72e.jpg)

<details>
<summary>text_image</summary>

f
K
x₁
x₂
B
x₃
</details>

Figure 2.4: If a spring and damper are connected in series, a new EOM must be constructed for the node in between (x2).
