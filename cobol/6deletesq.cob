IDENTIFICATION DIVISION
PROGRAM_ID. DEL-SQL.

DATA DIVISION.
WORKING-STORAGE SECTION.
EXEC SQL
INCLUDE SQLCA
END-EXEC.
EXEC SQL
INCLUDE ESTUDANTE
END EXEC.
EXEC SQL BEGIN DECLARE SECTION
END EXEC.
    01 WS-ESTUDANTE-REC.
        05 WS-ESTUDANTE-ID PIC 9(4)
        05 WS-ESTUDANTE-NOME PIC X(25)
        05 WS-ESTUDANTE-ENDERECO X(50)
EXEC SQL END DECLASE SECTION
END EXEC.

PROCEDURE DIVISION.
MOVE 1005 TO WS-ESTUDANTE-ID.
EXEC SQL
    DELETE FROM ESTUDANTE
    WHERE ESTUDANTE-ID=:WS-ESTUDANTE-ID
END-EXEC.
IF SQLCODE = 0
    DISPLAY 'Registro excluido com sucesso'
ELSE DISPLAY 'Erro'
END-IF.
STOP RUN.