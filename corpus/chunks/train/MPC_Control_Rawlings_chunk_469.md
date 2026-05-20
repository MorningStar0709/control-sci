Next we create a single estimate sequence by concatenating MHE sequences from times $N , 2 N , 3 N , \ldots$ This gives the state sequence and corresponding $\overline { { \mathbf { w } } } _ { 1 }$ and $\overline { { \mathbf { W } } } _ { 2 }$ sequences listed in the following table so that

$$\overline {{{x}}} ^ {+} = f (\overline {{{x}}}, \overline {{{w}}} _ {1}) + \overline {{{w}}} _ {2} \quad \text { for } k \geq 0 \quad y = h (\overline {{{x}}}) + \overline {{{v}}}$$

![](image/96f6272435b3f31c10d2b02278b2a43e5ec585f89b23ba5f50b58d5b6b630789.jpg)

<details>
<summary>text_image</summary>

x
0
N
k
2N
\hat{x}(0|N)
\hat{x}(1|N)
...
\hat{x}(N-1|N)
\hat{x}(N|N)
\hat{x}(N+1|2N)
\hat{x}(2N-1|2N)
\hat{x}(2N|2N)
\hat{w}(0|N)
\hat{w}(N-1|N)
\hat{w}(N|2N)
\hat{w}(2N-1|2N)
</details>

Figure 4.2: Concatenating two MHE sequences to create a single state estimate sequence from time 0 to 2N.

<table><tr><td> $\overline{\mathbf{x}}$ </td><td> $\overline{\mathbf{w}}_{1}$ </td><td> $\overline{\mathbf{w}}_{2}$ </td><td> $\overline{\mathbf{v}}$ </td></tr><tr><td> $\hat{x}(0|N)$ </td><td> $\hat{w}(0|N)$ </td><td>0</td><td> $\hat{v}(0|N)$ </td></tr><tr><td> $\hat{x}(1|N)$ </td><td> $\hat{w}(1|N)$ </td><td>0</td><td> $\hat{v}(1|N)$ </td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td> $\hat{x}(N-1|N)$ </td><td> $\hat{w}(N-1|N)$ </td><td> $\hat{x}(N|2N)-\hat{x}(N|N)$ </td><td> $\hat{v}(N-1|N)$ </td></tr><tr><td> $\hat{x}(N|2N)$ </td><td> $\hat{w}(N|2N)$ </td><td>0</td><td> $\hat{v}(N|2N)$ </td></tr><tr><td> $\hat{x}(N+1|2N)$ </td><td> $\hat{w}(N+1|2N)$ </td><td>0</td><td> $\hat{v}(N+1|2N)$ </td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td></tr><tr><td> $\hat{x}(2N-1|2N)$ </td><td> $\hat{w}(2N-1|2N)$ </td><td> $\hat{x}(2N|3N)-\hat{x}(2N|2N)$ </td><td> $\hat{v}(2N-1|2N)$ </td></tr><tr><td> $\hat{x}(2N|3N)$ </td><td> $\hat{w}(2N|3N)$ </td><td>0</td><td> $\hat{v}(2N|3N)$ </td></tr><tr><td> $\hat{x}(2N+1|3N)$ </td><td> $\hat{w}(2N+1|3N)$ </td><td>0</td><td> $\hat{v}(2N+1|3N)$ </td></tr><tr><td>...</td><td>...</td><td>...</td><td>...</td></tr></table>
