%{
#include <stdio.h>
%}

%%
[aA]plicar       { printf("Verbo (Aplicación): %s\n", yytext); }
[uU]sar          { printf("Verbo (Aplicación): %s\n", yytext); }
[dD]emostrar     { printf("Verbo (Aplicación): %s\n", yytext); }
[cC]onstruir     { printf("Verbo (Aplicación): %s\n", yytext); }
[mM]odificar     { printf("Verbo (Aplicación): %s\n", yytext); }
[oO]perar        { printf("Verbo (Aplicación): %s\n", yytext); }
[cC]alcular      { printf("Verbo (Aplicación): %s\n", yytext); }
[aA]justar       { printf("Verbo (Aplicación): %s\n", yytext); }
[aA]plicando     { printf("Verbo (Aplicación): %s\n", yytext); }
.|\n             ;
%%

int main() {
    yylex();
    return 0;
}
