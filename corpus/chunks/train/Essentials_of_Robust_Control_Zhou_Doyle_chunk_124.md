# 5.2 Well-Posedness of Feedback Loop

Assume that the plant P and the controller K in Figure 5.1 are fixed real rational proper transfer matrices. Then the first question one would ask is whether the feedback interconnection makes sense or is physically realizable. To be more specific, consider a simple example where

$$P = - \frac {s - 1}{s + 2}, \quad K = 1$$

are both proper transfer functions. However,

$$u = \frac {(s + 2)}{3} (r - n - d) + \frac {s - 1}{3} d _ {i}.$$

That is, the transfer functions from the external signals $r - n - d$ and $d _ { i }$ to u are not proper. Hence, the feedback system is not physically realizable.

Definition 5.1 A feedback system is said to be well-posed if all closed-loop transfer matrices are well-defined and proper.

Now suppose that all the external signals $r , n , d ,$ and $d _ { i }$ are specified and that the closed-loop transfer matrices from them to u are, respectively, well-defined and proper. Then $y$ and all other signals are also well-defined and the related transfer matrices are proper. Furthermore, since the transfer matrices from d and n to u are the same and differ from the transfer matrix from r to u by only a sign, the system is well-posed if and only if the transfer matrix from $\left[ \begin{array} { l } { d _ { i } } \\ { d } \end{array} \right]$ to u exists and is proper.

To be consistent with the notation used in the rest of this book, we shall denote

$$\hat {K} := - K \tag {5.1}$$

and regroup the external input signals into the feedback loop as $w _ { 1 }$ and $w _ { 2 }$ and regroup the input signals of the plant and the controller as $e _ { 1 }$ and $e _ { 2 }$ . Then the feedback loop with the plant and the controller can be simply represented as in Figure 5.2 and the system is well-posed if and only if the transfer matrix from $\left[ \begin{array} { l } { w _ { 1 } } \\ { w _ { 2 } } \end{array} \right]$ to $e _ { 1 }$ exists and is proper.

![](image/725e59eeda7b6b07464f3fc9747abb75afc741d0b46596a43503b9313cae1410.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    w1["w₁"] -->|+| sum((+))
    sum --> e1["e₁"]
    e1 --> P["P"]
    P --> sum
    w2["w₂"] -->|+| sum
    sum --> K["K̂"]
    K̂ --> e2["e₂"]
    e2 --> sum
```
</details>

Figure 5.2: Internal stability analysis diagram

Lemma 5.1 The feedback system in Figure 5.2 is well-posed if and only if

$$I - \hat {K} (\infty) P (\infty) \tag {5.2}$$

is invertible.

Proof. The system in Figure 5.2 can be represented in equation form as
