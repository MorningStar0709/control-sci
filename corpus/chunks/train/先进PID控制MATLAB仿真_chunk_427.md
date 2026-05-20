u_7=u_6;u_6=u_5;u_5=u_4;u_4=u_3;
u_3=u_2;u_2=u_1;u_1=u(k);

wkp_1=wkp(k);
wkd_1=wkd(k);
wiki_1=wki(k);

y_2=y_1;y_1=y(k); 
```

```matlab
end
figure(1);
plot(time,yd,'r',time,y,'k:',linewidth',2);
xlabel('time(s)');ylabel('yd,y');
legend('ideal position','position tracking');
figure(2);
plot(time,u,'r','linewidth',2);
xlabel('time(s)');ylabel('u');
figure(3);
subplot(311);
plot(time,wkp,'r','linewidth',2);
xlabel('time(s)');ylabel('wkp');
subplot(312);
plot(time,wki,'r','linewidth',2);
xlabel('time(s)');ylabel('wiki');
subplot(313);
plot(time,wkd,'r','linewidth',2);
xlabel('time(s)');ylabel('wkd'); 
```

注意：采用 Hebb 学习规则或梯度下降法来设计神经网络权值调节律，神经网络参数或控制参数都是按经验选取或试凑，闭环系统的稳定性得不到保障，如果神经网络参数或控制参数选择不当，闭环系统控制很容易发散。针对这一问题，出现了在线自适应神经网络控制方法，它是基于 Lyapunov 稳定性理论获得权值自适应律，从而获得闭环系统的稳定性。

![](image/b9eed2758d74c1765c8edb99e4595316565907f1f3b7fae3c8974da9aade047a.jpg)
