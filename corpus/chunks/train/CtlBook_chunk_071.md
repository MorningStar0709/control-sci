# Example 2.10

Car Suspension Example

![](image/e6232c061f880e23e76e6334a3a992af6841d5ff89bc39b8fe5e683b9987b2ca.jpg)

<details>
<summary>text_image</summary>

x₃
Mᵥ
← car body
Kₛ
Bₛ
x₂
Mᵥ
← wheel height
Kf
← road profile
x₁
</details>

Find the transfer function from road $\left( x _ { 1 } ( s ) \right)$ to body $\left( x _ { 3 } ( s ) \right)$ .

Normalize the denominator.

$$E O M ^ {s}M _ {w}: \quad M _ {w} \ddot {X} _ {2} + B _ {s} (\dot {X} _ {2} - \dot {X} _ {3}) + K _ {s} (x _ {2} - x _ {3}) + K _ {T} (x _ {2} - x _ {1}) = 0M _ {v}: \quad M _ {v} \ddot {x} _ {3} + B _ {s} (\dot {x} _ {3} - \dot {x} _ {2}) + K _ {s} (x _ {3} - x _ {2}) = 0\text { Collect variables } X _ {3} (s) X _ {2} (s), X _ {1} (s)\mathrm{MW:} \quad M _ {w} \dot {X} _ {2} + B _ {s} \dot {X} _ {2} + (K _ {T} + K _ {S}) (X _ {2}) + B _ {s} (- \dot {X} _ {3}) + K _ {s} (- X _ {2}) + K _ {T} (- X _ {1}) = 0\mu \nu : \quad \mu_ {v} \dot {X} _ {3} + B _ {s} \dot {X} _ {3} - B _ {s} \dot {X} _ {2} + K _ {s} (X _ {3} - X _ {2}) = 0\text { Laplace Transform }M _ {w}: \quad X _ {2} (s) \left(M _ {w} s ^ {2} + B _ {s} s + K _ {T} + K _ {s}\right) + X _ {3} (s) \left(B _ {s} s - K _ {s}\right) + X _ {1} (s) (K _ {T}) = 0M _ {V}: \quad X _ {3} (s) \left(M _ {v} s ^ {2} + B _ {s} s + K _ {s}\right) + \quad X _ {2} (s) \left(- B _ {s} s - K _ {s}\right) = 0\text { Sub } \quad \text { to } \quad \text { eliminate } \quad X _ {2} (s)X _ {2} (s) = X _ {3} (s) \frac {(m v s ^ {2} + B _ {s} s + K _ {s})}{B _ {s} s + K _ {s}}$$
