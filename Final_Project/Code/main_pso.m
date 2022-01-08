clc;
close;
clear all;
load position.txt
pso_position = zeros(size(position,1),3);
best_angle = zeros(1,6);
i = 1;
tic;
while(i<=size(position,1))
    [JointAngle] = pso(position(i,:),best_angle');
    [ ~, ~ , Pbas ] = ForwardKinemetics(JointAngle );
    best_angle(:) = JointAngle(:);
    pso_position(i,:) = Pbas(:);
    i = i + 1
end   
toc;
%%
figure(1)
plot3(pso_position(:,1),pso_position(:,2),pso_position(:,3))
xlabel('x Axis')
ylabel('y Axis')
zlabel('z Axis')
hold on;
plot3(position(:,1),position(:,2),position(:,3))
legend({'desired position','BAS'},'Location','northwest')
title('Trajectory')
grid on

figure(2)
t = 1:1:size(position,1);
plot(t,position(:,1)-pso_position(:,1),t,position(:,2)-pso_position(:,2),t,position(:,3)-pso_position(:,3))
ylim([-1 1])
title('PSO ERROR')
xlabel('time step') 
ylabel('error(x,y,z)') 
legend({'Ex','Ey','Ez'},'Location','southwest')
grid on