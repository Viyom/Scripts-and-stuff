

%plot(0.005,0.0,0.005, 1.0, '--','LineWidth',1.5);

% load target_5.dat
% [n,p] = size(target_5);
% n= 12429;
% p =2;
% t=1:n;
% 
% 
% 
% y=target_5(:,2);
%  cdfplot(mtupdate_1ms);
% 
hold on
x=0:1:350;
pdnorm=fitdist(Qlength1,'normal');
f=normcdf(x,pdnorm.mu,pdnorm.sigma);
plot(x,f,'b');
legend('BLUE');
grid on
box on
hold off
xlabel ('Queue Length')
ylabel ('CDF')
hold off

% cdfplot(Qlength1);
% hold on
% x=0:0.001:0.04;
% pdnorm=fitdist(mtupdate_1ms,'normal');
% pdnorm1=fitdist(tar_5,'normal');
% f=normcdf(x,pdnorm.mu,pdnorm.sigma);
% f1=normcdf(x,pdnorm1.mu,pdnorm1.sigma);
% plot(x,f,'r');
%plot(x,f1,'b');
%y=evcdf(x,0,3);
%plot(x,y,'m');





