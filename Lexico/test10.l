%{
#include <stdio.h>
%}

%%
(auto|break|case|char|const|continue|default|do|double|else|enum|
extern|float|for|goto|if|int|long|register|return|short|signed|
sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while)
    { printf("Palabra reservada: %s\n", yytext); }

(int|float|double|char|void)
    { printf("Tipo de dato: %s\n", yytext); }

[a-zA-Z_][a-zA-Z0-9_]* { printf("Variable: %s\n", yytext); }

[0-9]+                 { printf("Número: %s\n", yytext); }
.|\n ;
%%

int main() {
    yylex();
    return 0;
}
