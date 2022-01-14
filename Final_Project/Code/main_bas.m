clc;
close;
clear all;
load position.txt
n = 10 ;%number of bas;
% bas_trajectory = zeros(size(position,1),3);
bas_trajectory = zeros(4420,3);
best_bas_angle = zeros(1,6);
i = 1;
k = 1;
tic;
while(i<=size(position,1))
    error = zeros(n,1);
    three_bas_position = zeros(n,3);
    three_bas_angle = zeros(n,6);
    for j = 1:1:n
        [JointAngle] = bas(position(i,:),best_bas_angle');
        [ ~, ~ , Pbas ] = ForwardKinemetics(JointAngle );
        error(j) = f_obj(JointAngle,position(i,:));
        three_bas_angle(j,:) =  (JointAngle)';
        three_bas_position(j,:) = Pbas(:);
    end
    for j = 1:1:n
        if error(j) <= 0.005
            bas_trajectory(i,:) = three_bas_position(j,:);
            best_bas_angle(:) = three_bas_angle(j,:);
%             if i == 4419
%                i = i + 1; 
%             else
%                 i = i + 2;
%             end
%             k = k+1;
            i = i + 1; 
            break;
        end
    end
    i
end   
toc;
% disp(['運行時間: ',num2str(toc)]);
%%
figure(1)
plot3(bas_trajectory(:,1),bas_trajectory(:,2),bas_trajectory(:,3))
xlabel('x Axis')
ylabel('y Axis')
zlabel('z Axis')
hold on;
plot3(position(:,1),position(:,2),position(:,3))
title('Trajectory')
legend({'desired position','BAS'},'Location','northwest')
grid on

figure(2)
t = 1:1:size(position,1);
plot(t,position(:,1)-bas_trajectory(:,1),t,position(:,2)-bas_trajectory(:,2),t,position(:,3)-bas_trajectory(:,3))
ylim([-1 1])
title('BAS ERROR (threshold = 0.005)')
xlabel('time step') 
ylabel('error(x,y,z)') 
legend({'Ex','Ey','Ez'},'Location','southwest')
grid on
%%
dx = position(:,1)-bas_trajectory(:,1);
dy = position(:,2)-bas_trajectory(:,2);
dz = position(:,3)-bas_trajectory(:,3);
RMSE_x = sqrt(sum(dx.^2))
RMSE_y = sqrt(sum(dy.^2))
RMSE_z = sqrt(sum(dz.^2))