# Example 9.15

For the following system:

$$P (s) = \frac {(s + 3)}{s (s + 1 + 1 . 5 j) (s + 1 - 1 . 5 j)} \quad H (s) = 1$$

design a PID controller to achieve:

$$T _ {S} \leq 1. 3 3 \quad \% O S \leq 1 \% \quad (34 ^ {\circ}, \zeta = 0. 8 3)$$

Plotting the performance specs in the complex plane:

![](image/ca30c6e313689700a906a67a09108d9cbbfd64f0198d1f9a86f0332691726697.jpg)

<details>
<summary>text_image</summary>

90%OS =
1970
3j
2j
j
340°
-4 -3 -2 -1
-j
-x
-2j
T_s = 1.33
</details>

The PID controller adds 2 zeros and a pole at the origin. We hope that with some value of gain, it will move the closed loop poles to the left of the shaded region.

Try 1: a double zero at s = −1 and a pole at the origin. The resulting controller is

$$C _ {1} (s) = \frac {(s + 1) (s + 1)}{s}$$

However, this cannot be simulated properly. Using Section 9.5.3, we add a regularization pole at 20:

$$C _ {1} (s) = 2 0 \frac {(s + 1) (s + 1)}{s (s + 2 0)}$$

Now we place this system into a python script and we add a little bit of code to draw the performance lines

```txt
