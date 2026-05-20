# Example 7.2

![](image/112cb905ebf7c2b3394747811bff5ee8e000fce483701fd4ead2e34e083687d4.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    X --> A["Summing Junction"]
    A --> B["C: K(s+4)(s+5)"]
    B --> C["P: 1/(s+1+3j)(s+1-3j)"]
    C --> Y
    Y --> D["Feedback Loop H=1"]
```
</details>

Use the computer to plot a Root Locus diagram for the system above.

Here we have two blocks around the loop. C which represents a controller, and P which represents a plant. The closed loop system does not care how many blocks are in the loop, just the loop gain which is the product of all blocks around the loop.

$$G (s) = C P H (s) = C (s) P (s) = \frac {K (s + 4) (s + 5)}{(s + 1 + 3 j) (s + 1 - 3 j)}$$

Using python.control (Listing 7.2)

![](image/cef8e9b4a20cff6193019dfdee598c1bb6d96fda54ed7fdd775d7e59383a9137.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| -5 | 0 |
| -4 | 0 |
| -1 | 3 |
| -1 | -3 |
</details>

This time the closed loop poles migrate toward the two zeros in the controller. First they leave the loop gain poles (x's) and then join up at the real axis. After that they split again and migrate along the real axis until they hit the zeros.
