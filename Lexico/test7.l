%{
#include <stdio.h>
#include <ctype.h>
%}

%%
.   { putchar(tolower(yytext[0])); }
\n  { putchar('\n'); }
%%

int main() {
    yylex();
    return 0;
}
