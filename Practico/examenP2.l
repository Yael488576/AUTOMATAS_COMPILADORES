%option noyywrap
%{
	#include<stdio.h>
	int comentarios = 0;
%}

DIGITO [0-9]
LETRA  [a-zA-Z]
VARIABLE {LETRA}({LETRA}|{DIGITO})*
NUMERO {DIGITO}+(\.DIGITO}+)?
COMENTARIO "//".*

%%
"if"|"else"|"while"|"for"|"return"|"int"|"float"|"double"|"char"|"void"|"main" {
    printf("Palabra reservada: %s\n", yytext);
}

"("|")"|"{"|"}"|"["|"]"|";"|","|"."|":"|"#"|"?"|"!"|"@"|"$"|"&"|"|"|"~"|"^" {
    printf("Simbolo especial: %s\n", yytext);
}

"+"|"-"|"*"|"/" {
    printf("Operadores aritmeticos: %s\n", yytext);
}

"=="|"!="|"<"|">"|"&&"|"||"|"!" {
    printf("Operador logico: %s\n", yytext);
}

{NUMERO} {
    printf("Numero: %s\n", yytext);
}

{VARIABLE} {
    printf("Variable: %s\n", yytext);
}

{LETRA} {
    printf("Letra: %s\n", yytext);
}

{COMENTARIO} {
    comentarios++;
    printf("Comentario: %s\n", yytext);
}

[ \t\n]  ;

.        ;

%%
int main(int argc, char *argv[]){
    if (argc < 2) {
        printf("Uso: %s codigo.cpp\n", argv[0]);
        return 1;
    }

FILE *archivo = fopen(argv[1], "r");
    if (archivo == NULL) {
        printf("Error al intentar abrir el archivo: %s\n", argv[1]);
        return 1;
    }
    
    yyin = archivo;
    
    printf("=== ANALIZANDO ARCHIVO: %s ===\n\n", argv[1]);
    yylex();
    
    printf("\n=== RESULTADOS ===\n");
    printf("Total comentarios: %d\n", comentarios);
    
    fclose(archivo);
    return 0;
}

int yywrap() {
    return 1;
}