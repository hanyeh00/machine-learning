clc;
close all;
clear all;

num=200;
epoch=10;
n1=2;
n2=8;
n3=3;
n4=1;

x=unifrnd(-0.5,0.5,[num,n1]);

y=zeros(num,1);

for i=1:num
    y(i)=(sin(x(i,1))/x(i,1))+x(i,2);
end
%%train data
etaw=0.1;
w1=unifrnd(-1,1,[n2,n1]);
w2=unifrnd(-1,1,[n3,n2]);
w3=unifrnd(-1,1,[n4,n3]);

o1=zeros(n2,1);
o2=zeros(n3,1);
o3=zeros(n4,1);

etab=0.1;
b1=unifrnd(0,1,[n2,1]);
b2=unifrnd(0,1,[n3,1]);
b3=unifrnd(0,1,[n4,1]);


f1=zeros(n2,n2);
f2=zeros(n3,n3);
f3=zeros(n4,n4);

etag=0.01;
g1=zeros(n2,1);
for i=1:n2
    g1(i,i)=unifrnd(0,1,[1,1]);
end

g2=zeros(n3,1);
for i=1:n3
    g2(i,i)=unifrnd(0,1,[1,1]);
end

F1=zeros(n2,1);
F2=zeros(n3,1);
F3=zeros(n4,1);

trsize=ceil(0.75*num); % train size
tssize=num-trsize;  %test size

error=zeros(trsize,1);
error_mse=zeros(epoch,1);

trw1=zeros(trsize,1);
trw2=zeros(trsize,1);
trw3=zeros(trsize,1);

for step=1:epoch
    for t=1:trsize
        %************** feed forward ****************
           trw1(t,1)=w1(2,1);

          net1=w1*x(t,:)'+b1;
          o1=logsig(g1*net1);
          
          net2=w2*o1+b2;
          o2=logsig(g2*net2);
          
          net3=w3*o2+b3;
          o3=purelin(net3);
          
          error(t)=y(t)-o3;
          
         %************** back propagation ***********
           for i=1:n4
               f3(i,i)=1;
           end
           
           for i=1:n3
               f2(i,i)=g2(i,i)*o2(i)*(1-o2(i));
           end
           
           for i=1:n2
               f1(i,i)=g1(i,i)*o1(i)*(1-o1(i));
           end
           
           for i=1:n3
               F2(i,1)=net2(i)*o2(i)*(1-o2(i));
           end
           
           for i=1:n2
               F1(i,1)=net1(i)*o1(i)*(1-o1(i));
           end
           
           save_w2=w2;
           save_w3=w3;
           
           w1=w1+etaw*error(t)*f3*((w3*f2)*w2*f1)'*x(t,:);
           w2=w2+etaw*error(t)*f3*(w3*f2)'*o1';
           w3=w3+etaw*error(t)*f3*o2';
     
           
           b1=b1+etaw*error(t)*f3*((save_w3*f2)*save_w2*f1)';
           b2=b2+etaw*error(t)*f3*(save_w3*f2)';
           b3=b3+etab*error(t)*f3;
           
           g1=g1+etag*error(t)*f3*(save_w3*f2*save_w2*F1)';
           g2=g2+etag*error(t)*f3*(save_w3*F2)';
    end
    error_mse(step)=mse(error);
end

%*********************** train *********************
target1=zeros(trsize,1);
output_train=zeros(trsize,1);
for t=1:trsize
             net1=w1*x(trsize,:)'+b1;
             o1=logsig(g1*net1);
             net2=w2*o1+b2;
             o2=logsig(g2*net2);
             net3=w3*o2+b3;
             o3=purelin(net3);
             output_train(t)=o3;
             target1(t)=y(t);
end
%*********************** test **********************
target=zeros(tssize,1);
mlp=zeros(tssize,1);
mse_ts=zeros(tssize,1);

for t=1:tssize
          net1=w1*x(t+trsize,:)'+b1;
          o1=logsig(g1*net1);
          net2=w2*o1+b2;
          o2=logsig(g2*net2);
          net3=w3*o2+b3;
          o3=purelin(net3);
          mlp(t)=o3;
          target(t)=y(t+trsize);
          
end
mse_ts(t)=mse(y(t+trsize)-mlp(t));

subplot(2,2,1),semilogy(error_mse,'--b');
xlabel('Epoch');
ylabel('Error Mse');
title('Train Error Mse');

subplot(2,2,2),plot(mlp,'-*b');
hold on;
plot(target,'-or');
xlabel('Test Samples');
ylabel('outputs');
title('Comparision of MLP and Real Target');
legend('MLP','Target');

plot(SG2,'-*b');

xlabel('iteration');
ylabel('F-score');
title('F-score over 50 iteration');
legend('F-score');

subplot(2,2,4),semilogy(trw1,'--b');
xlabel('Train Samples');
ylabel('Value');
title('Train w1(1,1)');

figure(2);
x1=mlp;
y1=target;
hand=plotregression(x1,y1,'Regression');
h=get(hand,'Children');
hh=get(h(2),'Children');
delete(hh(3))
set(hh(1),'Marker','o')
legend('Target','MLP','Location','Northwest');