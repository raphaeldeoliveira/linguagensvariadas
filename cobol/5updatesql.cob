IDENTIFICATION DIVISION
PROGRAM_ID. UP-SQL.

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
MOVE 'Belo Horizonte' TO WS-ESTUDANTE-ENDERECO.
EXEC SQL
    UPDATE ESTUDANTE SET ESTUDANTE-ENDERECO=:WS-ESTUDANTE-ENDERECO
    WHERE ESTUDANTE-ID = 1--3
END-EXEC.
IF SQLCODE = 0
    DISPLAY 'Registro atualizado com sucesso'
ELSE DISPLAY 'Erro'
END-IF.
STOP RUN.