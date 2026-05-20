# Example 9.15 cont.

Root locus plot for ECE 447 Example

Example 9.15, Original Attempt

![](image/396e6fe330f70f9a69ae76c8de63de89d68903888df3314e99e6f66c29d65fe0.jpg)

<details>
<summary>radar</summary>

| Real | Imaginary |
| --- | --- |
| 3.2 | 1.0 |
| 0.8 | 0.8 |
| 0.0 | 0.0 |
</details>

Unfortunately, while some of the poles move into the region of acceptable performancea, the two origin poles will never get to the left of σ = −1!

Try 2: Move the two zeros to {−4, −4}

```lisp
// 2nd guess controller
pp=25;
c1 = pp * ((s+4)*(s+4))/(s*(s+pp));
Sys = syslin('c', c1*p); // loop gain system
clf();
evans(Sys,2000); // experiment with gain range (200)
a1=get(('current_axes')); //get the handle of the newly created axesctl
a1.data_bounds=[-5,1, -3,3];
sgrid; // helps for the % overshoot performance line
} 
```

aThis can be seen by changing the plotting limits
