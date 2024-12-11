#include <stdio.h>

void fibonacci(int n) {
	int a = 0, b = 1, next;
	
	if (n <= 0) {
		printf("Por favor ingresa un numero positivo.\n");
		return;
	}
	
	printf("Secuencia de Fibonacci con %d elementos:\n", n);
	
	for (int i = 0; i < n; i++) {
		if (i == 0) {
			printf("%d", a);
		} else if (i == 1) {
			printf(", %d", b);
		} else {
			next = a + b;
			a = b;
			b = next;
			printf(", %d", next);
		}
	}
	printf("\n");
}

int main() {
	int num;
	
	printf("Cuantos numeros de la secuencia de Fibonacci deseas generar? ");
	scanf("%d", &num);
	
	fibonacci(num);
	
	return 0;
}
