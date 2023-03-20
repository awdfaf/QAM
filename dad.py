generator=[1 1 1;1 0 1];   %다항식 생성
[n,K] = size(generator);
m = K-1;%레지스터 숫자 / M is the number of shift registers
state = zeros(1,m);%제로스 설정 
inputtt=[1 0 0 1 1 0 1 0 1 1];%입력 소스 코드 
[trash,h]=size(inputtt);
outputttt=[];
for x=1:h              %h=비트 숫자 
    input=inputtt(1,x);
for i=1:n
   output(i) = generator(i,1)*input;
   for j = 2:K
       z=generator(i,j)*state(j-1);
      output(i) = xor(output(i),z);
   end;
end
state = [input, state(1:m-1)];
outputttt=[outputttt,output];%새로운 코드 생성 
end
inputtt    %입력 출력 
outputttt   %결과 출력 
% 201811723 박건우  