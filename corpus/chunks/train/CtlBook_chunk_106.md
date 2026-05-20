# Example 3.8

Nick Baroody (Sp25) proposed an alternate method, which can be easier in some problems.

Consider the same system as the rst diagram in Example 3.7.

Part 1: Eliminate the gears and draw the transformed system. As an alternate transformation-based method, leave $J _ { 2 } , K _ { 2 } , B _ { 2 } , J _ { 3 } , K _ { 3 } , B _ { 3 }$ as they are and transform only $J _ { 1 }$ into the $\theta _ { 2 }$ variables!

Solution: This time our gear ratio is inverted:

$$N = 2 5 / 1 0 0 = 1 / 4$$

and we have only one transform,

$$\hat {J} _ {1} = n ^ {2} J _ {1} = \frac {1}{1 6} J _ {1}$$

We also need to transform $\tau _ { 1 } , \theta _ { 1 }$ according to

$$\hat {\tau} _ {1} = n \tau_ {1} = \tau_ {1} / 4 \quad \mathrm{and} \quad \hat {\theta} _ {1} = 1 / n \theta_ {1} = 4 \theta_ {1}$$

Our rst mass is therefore

$$J _ {T} = J _ {2} + \hat {J}$$

and the transformed system is

![](image/855b69f26e8357810399137676d2ac31d68036543b3253e634ab017aa59867e7.jpg)

<details>
<summary>text_image</summary>

B₂
Jₜ
θ₂
K₂
J₃
B₃
K₃
τ̂, θ̂₁
</details>

Part 2: Write the EOM(s) Writing the EOM's for the above gure,

Solution:

Inertia $J _ { T } \colon$

$$J _ {T} \ddot {\hat {\theta}} _ {1} + B _ {2} \dot {\hat {\theta}} _ {1} + K _ {2} (\hat {\theta} _ {1} - \theta_ {2}) = \hat {\tau}$$

Inertia $J _ { 3 } { \mathrm { : } }$

$$J _ {3} \ddot {\theta} _ {2} + B _ {3} \dot {\theta} _ {2} + K _ {2} (\theta_ {2} - \hat {\theta_ {1}}) + K _ {3} \theta_ {2} = 0$$

Part 3: Substitute to eliminate all hats", and $N \mathrm { { s } }$ in your answer

Solution:

$J _ { T } ;$

$$\left(\frac {1}{1 6} J _ {1} + J _ {2}\right) 4 \ddot {\theta} _ {1} + B _ {2} 4 \dot {\theta} _ {1} + K _ {2} (4 \theta_ {1} - \theta_ {2}) = \frac {1}{4} \tau\left(J _ {1} + 1 6 J _ {2}\right) \ddot {\theta} _ {1} + 1 6 B _ {2} \dot {\theta} _ {1} + 1 6 K _ {2} \left(\theta_ {1} - \frac {1}{4} \theta_ {2}\right) = \tau$$

J3:

$$J _ {3} \ddot {\theta} _ {2} + B _ {3} \dot {\theta} _ {2} + K _ {2} (\theta_ {2} - 4 \theta_ {1}) + K _ {3} \theta_ {2} = 0$$

Note: These are the same EOMs as the earlier method of Example 3.7

![](image/e21230bba42e73753b26031638f29680fa30e460ae75fec45e1dc938fcf72ebb.jpg)

<details>
<summary>text_image</summary>

r
F
x
z, θ
</details>

Figure 3.6: Rack and Pinion gear system converts rotary to linear motion and force to torque (and vice versa).
