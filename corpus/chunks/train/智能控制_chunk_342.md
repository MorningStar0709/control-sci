# 3. 函数型

有代表性的有 Sigmoid 型和高斯型函数。Sigmoid 型函数表达式为

$$f \left(\mathrm{net} _ {i}\right) = \frac {1}{1 + \mathrm{e} ^ {- \frac {\mathrm{net} _ {i}}{T}}} \tag {7.6}$$

Sigmoid 型函数如图 7-4 所示。

![](image/3238f395390250bee196fe1398817467d2e95c23da58b062e8c409872e33f561.jpg)

<details>
<summary>line</summary>

| ent_i | f |
| --- | --- |
| 0 | 1.0 |
| 1 | 1.0 |
</details>

图 7-2 阈值型函数

![](image/1c55f43ad2a2ed9f415a463c4c8dd59937487ef5301c4f9ac596e77b417b3fd0.jpg)

<details>
<summary>line</summary>

| Time Point | f_max |
| --- | --- |
| ent₀ | 0 |
| ent₁ | f_max |
| ent₂ | f_max |
</details>

图 7-3 分段线性型函数

![](image/5b791940e53d3e4c56ae9f188129dcc5a07fe0ee601f9c2a75d8c64a68f8ff69.jpg)

<details>
<summary>line</summary>

| net_i | f |
| --- | --- |
| -2.0 | 0.0 |
| -1.0 | 0.2 |
| 0.0 | 0.5 |
| 1.0 | 0.8 |
| 2.0 | 1.0 |
</details>

图 7-4 Sigmoid 型函数
