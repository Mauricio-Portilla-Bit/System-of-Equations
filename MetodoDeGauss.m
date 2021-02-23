%Codigo para resolver sistemas de ecuaciones con una longitud de nxn

prompt = 'Introduce el Número de Variables';
numeroDeVariables =input(prompt);

Ecuaciones = zeros(numeroDeVariables);
Soluciones = zeros(numeroDeVariables,1);

Valores = zeros(numeroDeVariables,1);

%Iniciar las Matrices  
for i=1:numeroDeVariables
    % Iniciar las variables
    for j=1:numeroDeVariables
        fprintf('Ecuacion # %d Variable # %d.\n',i,j);
        prompt = 'Introduce el Valor:';
        Ecuaciones(i,j) = input(prompt);
    end
    %Iniciar las soluciones
    fprintf('Ecuación %d \n',i);
    prompt = 'Solución:';
    Soluciones(i) = input(prompt);
end

for i=1:(numeroDeVariables-1)
    %fprintf('Diagonal %d \n',Ecuaciones(i,i))
    Soluciones(i) = Soluciones(i) / Ecuaciones(i,i);
    Ecuaciones(i,:) = Ecuaciones(i,:) / Ecuaciones(i,i);
    
    for j=(i+1):(numeroDeVariables)
        %fprintf('Inicio %d \n',j)
        if (Ecuaciones(j,i) > 0);
        Soluciones(j) = Soluciones(j) - abs(Ecuaciones(j,i))*Soluciones(i);
        Ecuaciones(j,:) = Ecuaciones(j,:) - abs(Ecuaciones(j,i))*Ecuaciones(i,:);
        end
        if(Ecuaciones(j,i) < 0)
        Soluciones(j) = Soluciones(j) + abs(Ecuaciones(j,i))*Soluciones(i);
        Ecuaciones(j,:) = Ecuaciones(j,:) + abs(Ecuaciones(j,i))*Ecuaciones(i,:);
        end
    end
    
end

%Despejar las Ecuaciones
for i=0: numeroDeVariables-1
    %Inicio
    Valores(numeroDeVariables-i) = Soluciones(numeroDeVariables-i);
    %Resta
    for j=0: i-1        
        Valores(numeroDeVariables-i) = Valores(numeroDeVariables-i) - Valores(numeroDeVariables-j)*Ecuaciones(numeroDeVariables-i,numeroDeVariables-j);
    end
    %División
    Valores(numeroDeVariables-i) = Valores(numeroDeVariables-i)/Ecuaciones(numeroDeVariables-i,numeroDeVariables-i);
end

%Respuestas
Valores()
