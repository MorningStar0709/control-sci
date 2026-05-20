# Constructing the Root Locus Using MATLAB

As previously stated, several textbooks present rules for sketching the root locus. It is this author’s opinion that it is more important for the control engineer to know how to use and interpret the root locus than it is to know how to sketch the root locus. This opinion is reinforced by the fact that the root locus can be easily constructed by a single MATLAB command. To illustrate, let us again consider the simple closed-loop control system present in Fig. 10.31, where the P-controller gain $K _ { P }$ is in the forward path. The open-loop transfer function is

$$G (s) H (s) = \frac {1}{s (s + 3)} \tag {10.42}$$

In this example, the feedback transfer function H(s) is unity. The required MATLAB commands to create the root locus are

```matlab
>> sysGH = tf(1, [1 3 0])
% create the open-loop transfer function G(s)H(s)
>> rlocus(sysGH)
% create and draw the root locus 
```

The rlocus command draws the root locus to the screen. Executing these commands creates the root-locus plot shown in Fig. 10.34, which matches the diagram in Fig. 10.32. We can also use the basic rlocus command to determine the specific closed-loop poles (roots) for a desired gain; for example, $K _ { P } = 2$ :

>> sysGH = tf(1, [1 3 0])
    % create G(s)H(s)
>> KP = 2
    % set the desired gain $K_{P}$ >> CL_roots = rlocus(sysGH, KP)
    % compute closed-loop roots (no plot)

In this case where gain $K _ { P } = 2$ , the two closed-loop poles are $s _ { 1 } = - 1$ and $s _ { 2 } = - 2$ .

![](image/ef13e9eac5a54a1b8441612993f38c4bc92debe671f3fd2ae3132450aa76a132.jpg)

<details>
<summary>line</summary>

| Real Axis | Imaginary Axis |
| --- | --- |
| -3.0 | 0.0 |
| 0.0 | 0.0 |
</details>

Figure 10.34 Root-locus plot created by MATLAB for $G ( s ) H ( s ) = 1 / ( s ^ { 2 } + 3 s )$ .

Another extremely useful MATLAB command is rlocfind, which draws the root locus and then allows the user to place a “cross-hair target” cursor on a desired closed-loop root on the root locus. When the user clicks the mouse, the rlocfind command returns the gain K that produces the desired closed-loop root as well as the complete set of n closed-loop roots for gain K. Using the simple closed-loop system from Fig. 10.31, the following MATLAB commands illustrate the use of rlocfind

```erlang
>> sysGH = tf(1, [1 3 0])    % create G(s)H(s)
>> rlocus(sysGH)    % create and draw the root locus
>> [KP, CL_roots] = rlocfind(sysGH)    % allow cross-hair target on root locus 
```
