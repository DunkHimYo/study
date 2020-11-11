X=c(10.0, 12.0, 9.5, 22.2, 8.0)
Y=c(360.2, 420.0, 359.5, 679.0, 315.3)
m=lm(Y ~ X)

m
plot(X,Y)

abline(m,col='red')

coef(m)

fitted(m)
residuals(m)
deviance(m)
deviance(m)/length(X)

newx=data.frame(X=c(10.5, 25.0, 15.0))
newx
predict(m,newdata=newx)
