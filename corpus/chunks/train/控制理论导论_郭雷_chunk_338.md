A4. $\{w_{k}\}$ 是 iid 正态向量 $\in \mathcal{N}(0, I)$ , 并和 $\left[ \begin{array}{c} x_{0} \\ y_{0} \end{array} \right]$ 独立.

引理 4.4.6 设 A1\~A4 成立. 对任意 $k=0,1,2,\cdots$ 在 $y^{k}$ 条件下， $\begin{bmatrix}x_{k+1}\\y_{k+1}\end{bmatrix}$ 和 $x_{k}$ 都是条件正态向量，这时称 $(x_{k},y_{k})$ 为条件正态过程.

证明 A3 及引理 4.4.1 保证了引理对 $k = 0$ 成立。今设引理对 $k$ 成立。我们来证对 $k + 1$ 也对。求条件特征函数

$$
\begin{array}{l} E [ \exp (\mathrm{i} (\lambda^ {\mathrm{T}} x _ {k + 1} + \mu^ {\mathrm{T}} y _ {k + 1})) | y ^ {k} ] \\ = E \left\{\exp \left[ i \left(\lambda^ {T} + \mu^ {T} C _ {k + 1}\right) x _ {k + 1} \right] \cdot \exp \left[ i \left(\mu^ {T} H _ {k + 1} v _ {k} + \mu^ {T} F _ {k + 1} w _ {k + 1} \right\rbrack \mid y ^ {k} \right. \right\} \\ = E \left\{\exp \left[ i \left(\lambda^ {T} + \mu^ {T} C _ {k + 1}\right) \Phi_ {k + 1, k} x _ {k} \right] \cdot \exp \left[ i \left(\lambda^ {T} + \mu^ {T} C _ {k + 1}\right) B _ {k} u _ {k} + i \mu^ {T} H _ {k + 1} v _ {k} \right] \right. \\ \cdot \exp [ i (\lambda^ {T} + \mu^ {T} C _ {k + 1}) D _ {k + 1} + i \mu^ {T} F _ {k + 1} ] w _ {k + 1} | y ^ {k} \} \\ \end{array}

\begin{array}{l} = E \left\{\exp \left[ i \left(\lambda^ {T} + \mu^ {T} C _ {k + 1}\right) \Phi_ {k + 1, k} x _ {k} \right] \cdot \exp \left[ i \left(\lambda^ {T} + \mu^ {T} C _ {k + 1}\right) B _ {k} u _ {k} + i \mu^ {T} H _ {k + 1} v _ {k} \right] \right. \\ \cdot E \left[ \left(\mathrm{i} \left(\lambda^ {\mathrm{T}} + \mu^ {\mathrm{T}} C _ {k + 1}\right) D _ {k + 1} + \mathrm{i} \mu^ {\mathrm{T}} F _ {k + 1}\right) w _ {k + 1} \mid x _ {k}, y ^ {k} \right] \mid y ^ {k} \}. \tag {4.4.32} \\ \end{array}
$$

注意到 $w_{k + 1}$ 和 $(x_{k},y^{k})$ 独立， $C_{k + 1},D_{k + 1},F_{k + 1}$ 对 $y^{k}$ 可测，所以

$$
\begin{array}{l} E \left\{\exp \left(\mathrm{i} \left(\lambda^ {\mathrm{T}} + \mu^ {\mathrm{T}} C _ {k + 1}\right) D _ {k + 1} + \mathrm{i} \mu^ {\mathrm{T}} F _ {k + 1}\right) w _ {k + 1} \mid x _ {k}, y ^ {k} \right\} \\ = \exp \left(- \frac {1}{2} \| (\lambda^ {\mathrm{T}} + \mu^ {\mathrm{T}} C _ {k + 1}) D _ {k + 1} + \mu^ {\mathrm{T}} F _ {k + 1} \| ^ {2}\right), \tag {4.4.33} \\ \end{array}
$$

它是对 $y^{k}$ 可测的条件正态特征函数.

据归纳法假设，在 $y^{k}$ 条件下， $x_{k}$ 条件正态，所以 (4.4.32) 右端为三个对 $y^{k}$ 可测的条件正态特征函数，因此它本身是条件正态特征函数。
