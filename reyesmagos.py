#include <stdio.h>
#include <string.h>
#include<stdlib.h>
//Almacena los nombre de los tres reyes magos en una lista de punteros
//que apuntan a 3 palabras cuyo tamaño es distinto

int main(void) {
//Reservamos memoria para los 3 punteros  
  char *magos[3];
  char nombreaux[10];
  int longitud;
  int cont;
  for(cont=0;cont<3;cont++){
      printf("\nRey mago numero %d: ",cont+1);
      scanf(" %s",nombreaux);
      longitud=strlen(nombreaux);//Cuento las letras del nombre
      magos[cont]=(char *) malloc(sizeof(char)*longitud);
     
  }
  return 0;
}
