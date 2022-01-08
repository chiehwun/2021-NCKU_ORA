function [xbest] = bas(d_x,theta)
    PosLimit = [  170    -170  ;
                        82.79  -135  ;
                        104    -74.88  ;
                        190    -19  ;
                        118.88 -118.88  ;
                        360    -360  ]* pi / 180;
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %初始化部分
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    c1 = 0.25;
    c2 = 0.2;%ratio between delta and lambda
    n=1;%iterations
    k=6;%space dimension
    lambda = c1*sqrt(f_obj(theta,d_x));
    delta = lambda * c2;
    x = theta;
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %迭代部分
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%     rng('shuffle');
    for i=1:n
        dir=rands(k,1);
        dir=dir/(norm(dir));
        xleft=x+dir*lambda;
        fleft=f_obj(xleft,d_x);
        xright=x-dir*lambda;
        fright=f_obj(xright,d_x);
        x=x-delta*dir*sign(fleft-fright);
        x(:) = min(x(:), PosLimit(:,1));
        x(:) = max(x(:), PosLimit(:,2));
        xbest=x;
        break;
    end
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %數據顯示部分
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%     figure(1),clf(1),
%     plot(x_store(1,:),x_store(end,:),'r-o')
%     hold on,
%     plot(x_store(1,:),fbest_store,'b-.')
%     legend("x_store","fbest_store")
%     xlabel('iteration')
%     ylabel('error')
%     title('BAS')
end