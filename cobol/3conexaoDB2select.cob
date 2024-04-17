IDENTIFICATION DIVISION.
PROGRAM-ID. EXE-SELECT-SQL.

DATA DIVISION.
WORKING-STORAGE SECTION.
EXEC SQL
    INCLUDE SQLCA
END-EXEC.
EXEC SQL
    INCLUDE ESTUDANTE
END-EXEC.
EXEC SQL BEGIN DECLARE SECTION
END-EXEC.
    01 WS-ESTUDANTE-REG.
        05 WS-ESTUDANTE-ID PIC 9(4).
        05 WS-ESTUDANTE-NOME PIC X(25).
        05 WS-ESTUDANTE-ENDERECO X(50).
EXEC SQL END DECLARE SECTION
END EXEC.
PROCEDURE DIVISION.
EXEC SQL
    SELECT ESTUDANTE-ID, ESTUDANTE-NOME, ESTUDANTE-ENDERECO
    INTO :WS-ESTUDANTE-ID, :WS-ESTUDANTE-NOME, :WS-ESTUDANTE-ENDERECO FROM ESTUDANTE
    WHERE ESTUDANTE-ID=1004
END-EXEC.

IF SQLCODE = 0
    DISPLAY WS-ESTUDANTE-REG
ELSE DISPLAY 'ERRO'
END-IF.
STOP RUN.