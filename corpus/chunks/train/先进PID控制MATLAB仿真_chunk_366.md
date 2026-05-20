```javascript
xlabel('time(s)');ylabel('speed tracking for link 1'); 
```

```javascript
legend('Ideal speed signal','Speed signal tracking'); 
```

```javascript
figure(3); 
```

```txt
subplot(211); 
```

```javascript
plot(t,toll(:,1),'r','linewidth',2); 
```

```javascript
xlabel('time(s)');ylabel('control input of link 1'); 
```

```txt
subplot(212); 
```

```javascript
plot(t,tol2(:,1),'r','linewidth',2); 
```

```javascript
xlabel('time(s)');ylabel('control input of link 2'); 
```

![](image/a3800097e84eec59c3d93ac2d0cef9fe704a70c49003d3c29116f42186cc0d2f.jpg)
