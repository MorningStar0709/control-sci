# Example 9.14 cont.

However when we compute the root-locus using python it does not pass through or close to the targets (red dots added to the plot).

Root locus plot for ECE 447 Example   
Example 9.14,Original Attempt   
![](image/18cf6992aa79cb4c482ef035392fc3fcae7cfb0b1a42bca6b7bd185f0b1b4a58.jpg)

<details>
<summary>radar</summary>

| Real | Imaginary |
| --- | --- |
| 3.0 | 4.5 |
| 0.5 | 4.5 |
| 1.5 | 0.0 |
</details>

Also, the computed RL is qualitatively dierent from the manual one because the two CC poles do not go directly to the zeros (if you move the zeros closer to the jω axis, they do). This can sometimes happen even if you follow the hand drawing rules correctly (though rules 5 and 6 can reduce these errors). Either way, the RL does not hit the targets!

Trying dierent zero locations we nd better results with two real zeros: $s = \{ - 1 , - 5 . 5 \}$ the new Root Locus is

Root locus plot for ECE 447 Example   
Example 9.14, Inproved Attempt   
![](image/32941bfe4857c3e145a08d126942dfca6023399d5d0b4241c4c74e12132a72cb.jpg)

<details>
<summary>radar</summary>

| Real | Imaginary |
| --- | --- |
| 3.0 | 4.5 |
| 0.5 | 4.5 |
</details>

Note that now we now have two zeros at $s = - 1 ,$ , one from the plant and one from the PID controller. Then clicking on the root locus curve at or very near the target location, we nd $g a i n = 4 . 5 8$ (let's round it to 4.6 - this is only a rough computation).
