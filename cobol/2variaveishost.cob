DATA DIVISION.
WORKING-STORAGE SECTION.
EXEC SQL 
INCLUDE NOME-TABELA 
END-EXEC.

EXEC SQL BEGIN DECLARE SECTION
END-EXEC.
01 ESTUDANTES-REC.
     05 ESTUDANTE-ID PIC 9(4).
     05 ESTUDANTE-NOME PIC X(25).
     05 ESTUDANTE-ENDERECO X(50).
EXEC SQL END DECLARE SECTION
END-EXEC.