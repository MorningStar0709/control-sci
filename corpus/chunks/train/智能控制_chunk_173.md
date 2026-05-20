# 3. 模糊规则的描述

根据日常的经验,设计以下模糊规则:

(1)“若 e 负大,则 u 负大”;   
(2)“若 e 负小,则 u 负小”;   
(3)“若 e 为零,则 u 为零”;  
(4)“若 e 正小,则 u 正小”;  
(5)“若 e 正大, 则 u 正大”。

其中,排水时 u 为负,注水时 u 为正。

将上述规则采用“IF A THEN B”的形式来描述,则模糊规范表示为

(1) if e = NB then u = NB   
(2) if e = NS then u = NS   
(3) if e = ZO then u = ZO   
(4) if e = PS then u = PS   
(5) if e = PB then u = PB

根据上述经验规则,可得模糊控制规则表,见表 4-3。

表 4-3 模糊控制规则表

<table><tr><td>若(IF)</td><td>NBe</td><td>NSe</td><td>ZOe</td><td>PSe</td><td>PBe</td></tr><tr><td>则(THEN)</td><td>NBu</td><td>NSu</td><td>ZOu</td><td>PSu</td><td>PBu</td></tr></table>
