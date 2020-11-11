x=c(3,6,3,6,7.7)
u=c(10,10,20,20,14.8)
y=c(4.65,5.9,6.7,8.02,7.7)
m=lm(y~x+u)

nx=c(7.5, 15.0)
nu= c(5.0, 12.0)

new_data=data.frame(x=nx,u=nu)
ny=predict(m,new_data)
ny

library(scatterplot3d)
s=scatterplot3d(nx,nu,ny,zlim=0:11,pch=20,type='h',color='red',angle=70)
s$plane3d(m)
