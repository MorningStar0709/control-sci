(1) Angle of attack and sideslip angle.   
(2) Lift and/or side force.   
(3) Mach number and/or Reynolds number (plays a role only in the drag force).   
(4) Center of gravity location.   
(5) Altitude.

As mentioned above, all the aerodynamic force coefficients are, in general, functions of the state variables and the control variables, so that one can write, for example,

$$C _ {D} = C _ {D} (\alpha , \beta , M, q, \dots).$$

![](image/c694f6ee8b4774fb017840ed9418b3316b0ff525b7ae4dfc83472c745c39e591.jpg)

<details>
<summary>text_image</summary>

-C_{Zb}
C_L
X_b
α
X_C
C_D
-C_{Xb}
Y_b
Z_b
X_E
-Z_E
C_D
-C_{Yb}
-C_{Yb}
Z_b
β
X_E
Y_E
</details>

Fig. 3.4. Wind tunnel representation of the aerodynamic coefficients.

By taking the partial derivatives, we have

$$d C _ {D} = (\partial C _ {D} / \partial \alpha) d \alpha + (\partial C _ {D} / \partial \beta) d \beta + (\partial C _ {D} / \partial M) d M + (\partial C _ {D} / \partial q) d q + \dots .$$

Therefore, the aerodynamic force coefficients $C _ { D } , C _ { L }$ , and $C _ { Y }$ may be expressed in terms of the aerodynamic derivatives as follows:

$$C _ {D} = C _ {D 0} + C _ {D \alpha} | \alpha | + C _ {D \alpha^ {2}} \alpha^ {2} + C _ {D \beta} | \beta | + C _ {D \beta^ {2}} \beta^ {2} + C _ {D \alpha \beta} | \alpha | | \beta |, (3. 1 2)C _ {L} = C _ {L 0} + C _ {L \alpha} | \alpha | + C _ {L \alpha^ {2}} \alpha^ {2} + C _ {L \beta} | \beta | + C _ {L \beta^ {2}} \beta^ {2} + C _ {L \alpha \beta} | \alpha | | \beta |, (3. 1 3)C _ {Y} = C _ {Y 0} + C _ {Y \alpha} | \alpha | + C _ {Y \alpha^ {2}} \alpha^ {2} + C _ {Y \beta} | \beta | + C _ {Y \beta^ {2}} \beta^ {2} + C _ {Y \alpha \beta} | \alpha | | \beta |, (3. 1 4)$$

where $C _ { D 0 } = ( \partial C _ { D } / \partial \alpha ) | _ { \alpha = 0 }$ (i.e., evaluated at $\alpha = 0 ) , C _ { D \alpha } = \partial C _ { D } / \partial \alpha$ , etc. For our purposes, the functional dependence of the aerodynamic force coefficients will be assumed to take the simpler form as follows [6], [8]:

Drag Coefficient $( C _ { D } )$

$$C _ {D} = C _ {D 0} + C _ {D \alpha} \alpha , \tag {3.15a}$$

where

CD0 = total drag coefficient evaluated at $\alpha = 0$ (or close to it) $\mathsf { \Pi } = ( \partial C _ { D } / \partial \alpha ) | _ { \alpha = 0 }$

$C _ { D \alpha }$ = total drag coefficient variation with angle of attack $= \partial C _ { D } / \partial \alpha .$ ,

α = angle of attack (in radians).

The derivatives are evaluated at constant Mach number and Reynold’s number. The drag polar is written in the form [4]

$$C _ {D} = C _ {D 0} + K C _ {L} ^ {2}, \tag {3.15b}$$

where
