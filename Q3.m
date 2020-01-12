A=[2 4 6]; 
M=50000;
N=10000;
sum_time = 0;

for j= 1:M
    for i=1:N
        R=randperm(3);  
        n=A(R(1));
        if (n == 2)
              sum_time =sum_time+2;
            break;
        else
            sum_time=sum_time+n;
        end
    end
end
sum_time=sum_time/M;
