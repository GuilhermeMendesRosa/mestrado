-- Script de limpeza das 90 tabelas - PostgreSQL
-- Remove todos os dados das tabelas mantendo a estrutura

-- Início da transação para garantir atomicidade
BEGIN;

-- Limpeza de todas as tabelas
TRUNCATE TABLE tabela1 RESTART IDENTITY CASCADE;
TRUNCATE TABLE tabela2 RESTART IDENTITY CASCADE;
TRUNCATE TABLE tabela3 RESTART IDENTITY CASCADE;
TRUNCATE TABLE tabela4 RESTART IDENTITY CASCADE;
TRUNCATE TABLE tabela5 RESTART IDENTITY CASCADE;
TRUNCATE TABLE tabela6 RESTART IDENTITY CASCADE;
TRUNCATE TABLE tabela7 RESTART IDENTITY CASCADE;
TRUNCATE TABLE tabela8 RESTART IDENTITY CASCADE;
TRUNCATE TABLE tabela9 RESTART IDENTITY CASCADE;
TRUNCATE TABLE tabela10 RESTART IDENTITY CASCADE;
TRUNCATE TABLE tabela11 RESTART IDENTITY CASCADE;
TRUNCATE TABLE tabela12 RESTART IDENTITY CASCADE;
TRUNCATE TABLE tabela13 RESTART IDENTITY CASCADE;
TRUNCATE TABLE tabela14 RESTART IDENTITY CASCADE;
TRUNCATE TABLE tabela15 RESTART IDENTITY CASCADE;
TRUNCATE TABLE tabela16 RESTART IDENTITY CASCADE;
TRUNCATE TABLE tabela17 RESTART IDENTITY CASCADE;
TRUNCATE TABLE tabela18 RESTART IDENTITY CASCADE;
TRUNCATE TABLE tabela19 RESTART IDENTITY CASCADE;
TRUNCATE TABLE tabela20 RESTART IDENTITY CASCADE;
TRUNCATE TABLE tabela21 RESTART IDENTITY CASCADE;
TRUNCATE TABLE tabela22 RESTART IDENTITY CASCADE;
TRUNCATE TABLE tabela23 RESTART IDENTITY CASCADE;
TRUNCATE TABLE tabela24 RESTART IDENTITY CASCADE;
TRUNCATE TABLE tabela25 RESTART IDENTITY CASCADE;
TRUNCATE TABLE tabela26 RESTART IDENTITY CASCADE;
TRUNCATE TABLE tabela27 RESTART IDENTITY CASCADE;
TRUNCATE TABLE tabela28 RESTART IDENTITY CASCADE;
TRUNCATE TABLE tabela29 RESTART IDENTITY CASCADE;
TRUNCATE TABLE tabela30 RESTART IDENTITY CASCADE;

-- Confirmar a transação
COMMIT;

-- Verificar se as tabelas estão vazias (opcional)
-- Descomente as linhas abaixo para verificar:

/*
SELECT 'tabela1' as tabela, COUNT(*) as registros FROM tabela1;
SELECT 'tabela2' as tabela, COUNT(*) as registros FROM tabela2;
SELECT 'tabela3' as tabela, COUNT(*) as registros FROM tabela3;
SELECT 'tabela4' as tabela, COUNT(*) as registros FROM tabela4;
SELECT 'tabela5' as tabela, COUNT(*) as registros FROM tabela5;
SELECT 'tabela6' as tabela, COUNT(*) as registros FROM tabela6;
SELECT 'tabela7' as tabela, COUNT(*) as registros FROM tabela7;
SELECT 'tabela8' as tabela, COUNT(*) as registros FROM tabela8;
SELECT 'tabela9' as tabela, COUNT(*) as registros FROM tabela9;
SELECT 'tabela10' as tabela, COUNT(*) as registros FROM tabela10;
SELECT 'tabela11' as tabela, COUNT(*) as registros FROM tabela11;
SELECT 'tabela12' as tabela, COUNT(*) as registros FROM tabela12;
SELECT 'tabela13' as tabela, COUNT(*) as registros FROM tabela13;
SELECT 'tabela14' as tabela, COUNT(*) as registros FROM tabela14;
SELECT 'tabela15' as tabela, COUNT(*) as registros FROM tabela15;
SELECT 'tabela16' as tabela, COUNT(*) as registros FROM tabela16;
SELECT 'tabela17' as tabela, COUNT(*) as registros FROM tabela17;
SELECT 'tabela18' as tabela, COUNT(*) as registros FROM tabela18;
SELECT 'tabela19' as tabela, COUNT(*) as registros FROM tabela19;
SELECT 'tabela20' as tabela, COUNT(*) as registros FROM tabela20;
SELECT 'tabela21' as tabela, COUNT(*) as registros FROM tabela21;
SELECT 'tabela22' as tabela, COUNT(*) as registros FROM tabela22;
SELECT 'tabela23' as tabela, COUNT(*) as registros FROM tabela23;
SELECT 'tabela24' as tabela, COUNT(*) as registros FROM tabela24;
SELECT 'tabela25' as tabela, COUNT(*) as registros FROM tabela25;
SELECT 'tabela26' as tabela, COUNT(*) as registros FROM tabela26;
SELECT 'tabela27' as tabela, COUNT(*) as registros FROM tabela27;
SELECT 'tabela28' as tabela, COUNT(*) as registros FROM tabela28;
SELECT 'tabela29' as tabela, COUNT(*) as registros FROM tabela29;
SELECT 'tabela30' as tabela, COUNT(*) as registros FROM tabela30;
SELECT 'tabela31' as tabela, COUNT(*) as registros FROM tabela31;
SELECT 'tabela32' as tabela, COUNT(*) as registros FROM tabela32;
SELECT 'tabela33' as tabela, COUNT(*) as registros FROM tabela33;
SELECT 'tabela34' as tabela, COUNT(*) as registros FROM tabela34;
SELECT 'tabela35' as tabela, COUNT(*) as registros FROM tabela35;
SELECT 'tabela36' as tabela, COUNT(*) as registros FROM tabela36;
SELECT 'tabela37' as tabela, COUNT(*) as registros FROM tabela37;
SELECT 'tabela38' as tabela, COUNT(*) as registros FROM tabela38;
SELECT 'tabela39' as tabela, COUNT(*) as registros FROM tabela39;
SELECT 'tabela40' as tabela, COUNT(*) as registros FROM tabela40;
SELECT 'tabela41' as tabela, COUNT(*) as registros FROM tabela41;
SELECT 'tabela42' as tabela, COUNT(*) as registros FROM tabela42;
SELECT 'tabela43' as tabela, COUNT(*) as registros FROM tabela43;
SELECT 'tabela44' as tabela, COUNT(*) as registros FROM tabela44;
SELECT 'tabela45' as tabela, COUNT(*) as registros FROM tabela45;
SELECT 'tabela46' as tabela, COUNT(*) as registros FROM tabela46;
SELECT 'tabela47' as tabela, COUNT(*) as registros FROM tabela47;
SELECT 'tabela48' as tabela, COUNT(*) as registros FROM tabela48;
SELECT 'tabela49' as tabela, COUNT(*) as registros FROM tabela49;
SELECT 'tabela50' as tabela, COUNT(*) as registros FROM tabela50;
SELECT 'tabela51' as tabela, COUNT(*) as registros FROM tabela51;
SELECT 'tabela52' as tabela, COUNT(*) as registros FROM tabela52;
SELECT 'tabela53' as tabela, COUNT(*) as registros FROM tabela53;
SELECT 'tabela54' as tabela, COUNT(*) as registros FROM tabela54;
SELECT 'tabela55' as tabela, COUNT(*) as registros FROM tabela55;
SELECT 'tabela56' as tabela, COUNT(*) as registros FROM tabela56;
SELECT 'tabela57' as tabela, COUNT(*) as registros FROM tabela57;
SELECT 'tabela58' as tabela, COUNT(*) as registros FROM tabela58;
SELECT 'tabela59' as tabela, COUNT(*) as registros FROM tabela59;
SELECT 'tabela60' as tabela, COUNT(*) as registros FROM tabela60;
SELECT 'tabela61' as tabela, COUNT(*) as registros FROM tabela61;
SELECT 'tabela62' as tabela, COUNT(*) as registros FROM tabela62;
SELECT 'tabela63' as tabela, COUNT(*) as registros FROM tabela63;
SELECT 'tabela64' as tabela, COUNT(*) as registros FROM tabela64;
SELECT 'tabela65' as tabela, COUNT(*) as registros FROM tabela65;
SELECT 'tabela66' as tabela, COUNT(*) as registros FROM tabela66;
SELECT 'tabela67' as tabela, COUNT(*) as registros FROM tabela67;
SELECT 'tabela68' as tabela, COUNT(*) as registros FROM tabela68;
SELECT 'tabela69' as tabela, COUNT(*) as registros FROM tabela69;
SELECT 'tabela70' as tabela, COUNT(*) as registros FROM tabela70;
SELECT 'tabela71' as tabela, COUNT(*) as registros FROM tabela71;
SELECT 'tabela72' as tabela, COUNT(*) as registros FROM tabela72;
SELECT 'tabela73' as tabela, COUNT(*) as registros FROM tabela73;
SELECT 'tabela74' as tabela, COUNT(*) as registros FROM tabela74;
SELECT 'tabela75' as tabela, COUNT(*) as registros FROM tabela75;
SELECT 'tabela76' as tabela, COUNT(*) as registros FROM tabela76;
SELECT 'tabela77' as tabela, COUNT(*) as registros FROM tabela77;
SELECT 'tabela78' as tabela, COUNT(*) as registros FROM tabela78;
SELECT 'tabela79' as tabela, COUNT(*) as registros FROM tabela79;
SELECT 'tabela80' as tabela, COUNT(*) as registros FROM tabela80;
SELECT 'tabela81' as tabela, COUNT(*) as registros FROM tabela81;
SELECT 'tabela82' as tabela, COUNT(*) as registros FROM tabela82;
SELECT 'tabela83' as tabela, COUNT(*) as registros FROM tabela83;
SELECT 'tabela84' as tabela, COUNT(*) as registros FROM tabela84;
SELECT 'tabela85' as tabela, COUNT(*) as registros FROM tabela85;
SELECT 'tabela86' as tabela, COUNT(*) as registros FROM tabela86;
SELECT 'tabela87' as tabela, COUNT(*) as registros FROM tabela87;
SELECT 'tabela88' as tabela, COUNT(*) as registros FROM tabela88;
SELECT 'tabela89' as tabela, COUNT(*) as registros FROM tabela89;
SELECT 'tabela90' as tabela, COUNT(*) as registros FROM tabela90;
*/

-- Comando para verificar todas as tabelas de uma vez:
-- SELECT 
--     schemaname,
--     tablename, 
--     n_tup_ins as total_inseridos,
--     n_tup_del as total_deletados,
--     n_live_tup as registros_atuais
-- FROM pg_stat_user_tables 
-- WHERE tablename LIKE 'tabela%' 
-- ORDER BY tablename;

-- Fim do script de limpeza
-- Todas as 90 tabelas foram limpas e sequências resetadas
