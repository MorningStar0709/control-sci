# 5. 建立模糊控制表

上述描写的模糊控制规则可采用模糊规则表4-5来描述，表中共有49条模糊规则，各个模糊语句之间是“或”的关系，由第一条语句所确定的控制规则可以计算出 $u_{1}$ 。同理，可以由其余各条语句分别求出控制量 $u_{2},\cdots,u_{49}$ ，则控制量为模糊集合U，可表示为

$$U = u _ {1} + u _ {2} + \dots + u _ {4 9} \tag {4.4}$$

表 4-5 模糊规则表

<table><tr><td rowspan="2" colspan="2">U</td><td colspan="7">e</td></tr><tr><td>NB</td><td>NM</td><td>NS</td><td>ZO</td><td>PS</td><td>PM</td><td>PB</td></tr><tr><td rowspan="7">ec</td><td>NB</td><td>NB</td><td>NB</td><td>NM</td><td>NM</td><td>NS</td><td>NS</td><td>ZO</td></tr><tr><td>NM</td><td>NB</td><td>NM</td><td>NM</td><td>NS</td><td>NS</td><td>ZO</td><td>PS</td></tr><tr><td>NS</td><td>NM</td><td>NB</td><td>NS</td><td>NS</td><td>ZO</td><td>PS</td><td>PS</td></tr><tr><td>ZO</td><td>NM</td><td>NS</td><td>NS</td><td>ZO</td><td>PS</td><td>PS</td><td>PM</td></tr><tr><td>PS</td><td>NS</td><td>NS</td><td>ZO</td><td>PS</td><td>PS</td><td>PM</td><td>PM</td></tr><tr><td>PM</td><td>NS</td><td>ZO</td><td>PS</td><td>PM</td><td>PM</td><td>PM</td><td>PB</td></tr><tr><td>PB</td><td>ZO</td><td>PS</td><td>PS</td><td>PM</td><td>PM</td><td>PB</td><td>PB</td></tr></table>
