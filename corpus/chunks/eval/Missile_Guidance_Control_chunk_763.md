$$
\begin{array}{l} \begin{array}{c} M A D _ {k, m} = \text { the   value   of   the   mean   absolute   difference   between   the   kth   terrain } \\ \text { elevation   file   and   the   mth   reference   matrix   column }, \end{array} \\ \begin{array}{l} N = \text { the   number   of   samples   in   the   measured   terrain   elevation   file   and } \\ \text { usually   it   is   also   equal   to   the   number   of   rows   in   the   reference   matrix, } \end{array} \\ M = \text { the   number   of   reference   matrix   columns }, \\ \begin{array}{l} K = \text { the   number   of   measured   terrain   elevation   files   used   in   the   correlation } \\ \text { process   (for   the   SSLM   technique   K = 1) }, \end{array} \\ | \quad | = \text { the   absolute   value   of   the   argument }, \\ \end{array}
n, m, k = \text { row }, \text { column }, \text { and terrain elevation file indices },H _ {m, n} = \text { the stored reference matrix data: } 1 \leq m \leq M, 1 \leq n \leq N,h _ {k, m} = \text { the } k \text { th measured terrain elevation file: } 1 \leq k \leq K.
$$

The MSD algorithm can be expressed in terms of the profile in question. Mathematically, the expression for MSD is

$$M S D _ {j k} = (1 / N) \sum_ {i = 1} ^ {N} (S _ {i j} - S _ {i k}) ^ {2}, \tag {7.14}$$

where

$$S _ {j}, S _ {k} = j \text { th and } k \text { th profiles },N = \text { length of each profile. }$$

Note that for uniformity, we can also express the MAD algorithm as in the expression for the MSD. Thus,

$$M A D _ {j k} = (1 / N) \sum_ {i = 1} ^ {N} | S _ {i j} - S _ {i k} |. \tag {7.15}$$

Examination of the expressions for the MAD and MSD processors indicates that both of these correlators can be viewed as distance measures, where the dimensions of the space for which these distances are defined correspond to the number of elements in the profiles. From (7.14) and (7.15), we note that the ambiguity between any two profiles is defined as the probability (P ) that sensed data corresponding to one of the profiles will be closer (in terms of the distance measure) to the other profile than to the one from which it was taken. Mathematically, the ambiguity ξ can be expressed as

$$
\xi_ {j k} = \left\{ \begin{array}{l} P [ C _ {j k} <   C _ {j j} ], \text {   where   a   minimum   of   } C _ {j k} \text {   is   sought }, \\ P [ C _ {j k} > C _ {j j} ], \text {   where   a   maximum   of   } C _ {j k} \text {   is   sought }. \end{array} \right.
$$

![](image/f5802aee15789263f0d282a18d3a60f815f5a4327bebb5540bdb8ddebc9b0535.jpg)

<details>
<summary>text_image</summary>

Radar altimeter
Profile of
path flown
Stored matrix
</details>
