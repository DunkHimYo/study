x=c(3,6,9,12)
y=c(3,4,5.5,6.7)

ex_model=function(x)
  return(0.3*x+2)

pred_y=vector()

for(i in 1:length(x)){
  pred_y=append(pred_y,ex_model(x[i]))
}
pred_y
y
y-pred_y
(y-pred_y)^2
sum((y-pred_y)^2)
mse=sum((y-pred_y)^2)/length(y)
mse

library(ggplot2)
result=data.frame(x,y,pred_y)
result
ggplot(result,aes(x=x))+geom_line(aes(y=y,colour='y'))+geom_point(aes(y=pred_y,colour='pred_y'))
