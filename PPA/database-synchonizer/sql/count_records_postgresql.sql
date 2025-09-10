-- Contagem total de registros em todas as tabelas
SELECT 
    'TOTAL GERAL' as resumo,
    SUM(registros) as total_registros
FROM (
    SELECT COUNT(*) as registros FROM tabela1
    UNION ALL
    SELECT COUNT(*) as registros FROM tabela2
    UNION ALL
    SELECT COUNT(*) as registros FROM tabela3
    UNION ALL
    SELECT COUNT(*) as registros FROM tabela4
    UNION ALL
    SELECT COUNT(*) as registros FROM tabela5
    UNION ALL
    SELECT COUNT(*) as registros FROM tabela6
    UNION ALL
    SELECT COUNT(*) as registros FROM tabela7
    UNION ALL
    SELECT COUNT(*) as registros FROM tabela8
    UNION ALL
    SELECT COUNT(*) as registros FROM tabela9
    UNION ALL
    SELECT COUNT(*) as registros FROM tabela10
    UNION ALL
    SELECT COUNT(*) as registros FROM tabela11
    UNION ALL
    SELECT COUNT(*) as registros FROM tabela12
    UNION ALL
    SELECT COUNT(*) as registros FROM tabela13
    UNION ALL
    SELECT COUNT(*) as registros FROM tabela14
    UNION ALL
    SELECT COUNT(*) as registros FROM tabela15
    UNION ALL
    SELECT COUNT(*) as registros FROM tabela16
    UNION ALL
    SELECT COUNT(*) as registros FROM tabela17
    UNION ALL
    SELECT COUNT(*) as registros FROM tabela18
    UNION ALL
    SELECT COUNT(*) as registros FROM tabela19
    UNION ALL
    SELECT COUNT(*) as registros FROM tabela20
    UNION ALL
    SELECT COUNT(*) as registros FROM tabela21
    UNION ALL
    SELECT COUNT(*) as registros FROM tabela22
    UNION ALL
    SELECT COUNT(*) as registros FROM tabela23
    UNION ALL
    SELECT COUNT(*) as registros FROM tabela24
    UNION ALL
    SELECT COUNT(*) as registros FROM tabela25
    UNION ALL
    SELECT COUNT(*) as registros FROM tabela26
    UNION ALL
    SELECT COUNT(*) as registros FROM tabela27
    UNION ALL
    SELECT COUNT(*) as registros FROM tabela28
    UNION ALL
    SELECT COUNT(*) as registros FROM tabela29
    UNION ALL
    SELECT COUNT(*) as registros FROM tabela30	
) as contagens;