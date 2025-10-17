%{
#include <stdio.h>
%}

%%
"//".*                        { printf("Comentario (una línea): %s\n", yytext); }
"/*"([^*]|\*+[^*/])*\*+"/"    { printf("Comentario (multilínea)\n"); }
printf\(\"([^\\\"]|\\.)*\"\)  { printf("Texto en pantalla: %s\n", yytext); }
.|\n                          ;
%%

int main() {
    yylex();
    return 0;
}
