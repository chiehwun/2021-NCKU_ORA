function [xbest] = pso(d_x,theta)
    % clear; clc; close all;
    PosLimit = [  170    -170  ;
                    82.79  -135  ;
                    104    -74.88  ;
                    190    -190  ;
                    118.88 -118.88  ;
                    360    -360  ]* pi / 180;
    CostFunction = @(x) f_obj(x, d_x);  % Cost Function
    xbest = zeros(6,1);
    %% Assignment Aquirement
    MaxRun = 1;    % 50
    MAXIT = 1000;


    %% PSO-AC Properties
    nPop = 10;      % Particle number: 50
    w_max = 2.0;
    w_min = 0.1;
    phi1 = 2.05;     % Personal Learning Coefficient
    phi2 = 4.05;     % Global Learning Coefficient
    VelRatio = 0.9;  % % Velocity Limits Ratio

    %% Parameters Calculation
    phi = phi1 + phi2;
    assert(phi > 4, 'phi = %.4f must > 4', phi)
    chi = 2/abs(phi - 2 + sqrt(phi^2 - 4*phi)) ;         % Constriction factor
    c1 = chi*phi1;
    c2 = chi*phi2;

    %% Initialize particles
    empty_particle.Pos = [];
    empty_particle.Cost = [];
    empty_particle.Vel = [];
    empty_particle.Best.Pos = [];
    empty_particle.Best.Cost = [];
    empty_particle.Best.LastCost = [];

    fileID = fopen(sprintf('result\\pso_result.txt'), 'w');
    %% Choose Benchmark Function Code
    nVar = 6;
    VarMin = -pi;
    VarMax = pi;
    AnsPos = zeros(nVar,1);
    Opt = 0;
    VarSize = [nVar 1];
    VelMax = VelRatio*(VarMax - VarMin);
    VelMin = -VelMax;
    PSO_paras = {nPop, nVar, phi1, phi2, chi, VelRatio};    % package parameters

    BestCost = zeros(MaxRun, MAXIT, 1); % Best-so-far record
    MeanFit = zeros(MaxRun, 1);         % Mean fitness at MAXIT
    for run=1:MaxRun
        particle = repmat(empty_particle, nPop, 1);
        GlobalBest.Cost = inf;  % Make GlobalBest = particle(1).Best
        for i = 1:nPop
%             particle(i).Pos = unifrnd(VarMin, VarMax, VarSize);
            d = rands(nVar,1);
            particle(i).Pos = theta + (d/(sqrt(sum(d.^2)))).*0.05*sqrt(f_obj(theta,d_x));
            particle(i).Vel = VelMin + rand(VarSize).*(VelMax - VelMax);

            % Evaluation (needless to check boundary)
            particle(i).Cost = CostFunction(particle(i).Pos);

            % Update Personal Best
            particle(i).Best.Pos      = particle(i).Pos;
            particle(i).Best.Cost     = particle(i).Cost;
            particle(i).Best.LastCost = particle(i).Cost;
            % Update Global Best
            if particle(i).Best.Cost < GlobalBest.Cost
                GlobalBest = particle(i).Best;
            end
        end

        %% PSO Iteration
        succ_percent = ones(MAXIT, 1);  % w_a = w_max when it == 1
        succ_particles = nPop; % Every particle success at first
        w_a = zeros(MAXIT, 1);
        w   = zeros(MAXIT, 1);
        for it = 1:MAXIT
            succ_percent(it) = succ_particles / nPop;   % success percentage of the swarm
            succ_particles = 0;
            % Calculate w_a
            w_a(it) = (w_max - w_min)*succ_percent(it) + w_min;
            w(it) = w_a(it)*chi;
            for i = 1:nPop
                % Update Velocity
                particle(i).Vel = w(it)*particle(i).Vel ...
                    + c1*rand(VarSize).*(particle(i).Best.Pos - particle(i).Pos) ...
                    + c2*rand(VarSize).*(GlobalBest.Pos - particle(i).Pos);

                % Apply Velocity Limits
                particle(i).Vel = max(particle(i).Vel, VelMin);
                particle(i).Vel = min(particle(i).Vel, VelMax);

                % Update Position
                particle(i).Pos = particle(i).Pos + particle(i).Vel;

                % Velocity Mirror Effect: bounce back when hitting the boundary
                IsOutside = (particle(i).Pos < VarMin | particle(i).Pos>VarMax); % logic array
                particle(i).Vel(IsOutside) = -particle(i).Vel(IsOutside);

                % Apply Position Limits
                particle(i).Pos(:) = max(particle(i).Pos(:), PosLimit(:,2));
                particle(i).Pos(:) = min(particle(i).Pos(:), PosLimit(:,1));

                % === Evaluation === %
                particle(i).Cost = CostFunction(particle(i).Pos);

                % Update Personal Best
                if particle(i).Cost < particle(i).Best.Cost
                    particle(i).Best.Pos = particle(i).Pos;
                    % Update Personal Best Cost
                    particle(i).Best.LastCost = particle(i).Best.Cost;
                    particle(i).Best.Cost = particle(i).Cost;
                    % Update Global Best
                    if particle(i).Best.Cost < GlobalBest.Cost
                        GlobalBest = particle(i).Best;
                    end
                else
                    % Update Last Personal Best
                    particle(i).Best.LastCost = particle(i).Best.Cost;
                end

                % Calculate success particles of the swarm
                if particle(i).Best.Cost < particle(i).Best.LastCost
                    succ_particles = succ_particles + 1;
                end
            end % nPop

            BestCost(run, it) = GlobalBest.Cost; % Best-so-far
            if GlobalBest.Cost < 0.005
                xbest(:) = GlobalBest.Pos(:);
                break;
            end
        end % iteration
        MeanFit(run) = mean([particle.Cost]);   % last iteration
    end % run
    % fclose(fileID);
%     figure(1)
%     t = (1:1:200);
%     plot(t,BestCost(1,:))
%     xlabel('iteration')
%     ylabel('error')
%     title('PSO')


    % Pb4
    %% Show PSO-CW parameters

%     show_pso_parameters(PSO_paras{:})
%     GlobalBest.Cost
end
%% Local Function Definition
function x = show_pso_parameters(nPop, nVar, phi1, phi2, chi, VelRatio)
    disp('======= PSO Parameters =======')
    fprintf('nPop     = %d\n', nPop)
    fprintf('nVar     = %d\n', nVar)
    fprintf('phi1     = %.4f\n', phi1)
    fprintf('phi2     = %.4f\n', phi2)
    fprintf('chi      = %.4f\n', chi)
    fprintf('VelRatio = %.4f\n', VelRatio)
end

