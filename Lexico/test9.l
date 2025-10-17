%{
#include <stdio.h>
%}

%%
[eE]xaminar      { printf("Verbo (Analizar): %s\n", yytext); }
[aA]nalisar      { printf("Verbo (Analizar): %s\n", yytext); }
[cC]omparar      { printf("Verbo (Analizar): %s\n", yytext); }
[cC]lasificar    { printf("Verbo (Analizar): %s\n", yytext); }
[dD]istinguir    { printf("Verbo (Analizar): %s\n", yytext); }

[bB]ueno|[eE]xcelente|[pP]ositivo|[aA]gradable|[iI]ncreíble {
    printf("Adjetivo positivo: %s\n", yytext);
}

[yY]|[oO]|[pP]ero|[sS]ino|[qQ]ue|[mM]ientras {
    printf("Conjunción: %s\n", yytext);
}

[aA]|[dD]e|[eE]n|[cC]on|[pP]or|[sS]obre|[hH]acia {
    printf("Preposición: %s\n", yytext);
}

[yY]o|[tT]ú|[eE]l|[eE]lla|[nN]osotros|[uU]stedes|[eE]llos {
    printf("Pronombre: %s\n", yytext);
}

.|\n ;
%%

int main() {
    yylex();
    return 0;
}
