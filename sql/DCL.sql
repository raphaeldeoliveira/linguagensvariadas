-- GRANT
-- sintaxe
-- GRANT privilégios ON objeto TO usuários
--[WITH GRANT OPTION]

GRANT insert, delete ON funcionario, departamento TO joao;
GRANT select ON funcionario, departamento TO joana WITH GRANT OPTION;
GRANT select ON funcionario TO MARCOS;

-- REVOKE
-- sintaxe
-- REVOKE [WITH GRANT OPTION] prvilégios ON objeto FROM
-- usuários [RESTRICT/CASCADE]

GRANT select ON funcionario TO maria WITH GRANT OPTION;
GRANT select ON funcionario TO renata WITH GRANT OPTION;
REVOKE select ON funcionario FROM maria CASCADE;