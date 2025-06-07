-- Script DDL para criação de 90 tabelas de sincronização - PostgreSQL
-- Cada tabela possui campos padrão para simulação de dados reais


-- Tabela 1
CREATE TABLE tabela1 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela1
CREATE INDEX idx_tabela1_codigo ON tabela1 (codigo);
CREATE INDEX idx_tabela1_nome ON tabela1 (nome);
CREATE INDEX idx_tabela1_data_criacao ON tabela1 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela1()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela1
    BEFORE UPDATE ON tabela1
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela1();


-- Tabela 2
CREATE TABLE tabela2 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela2
CREATE INDEX idx_tabela2_codigo ON tabela2 (codigo);
CREATE INDEX idx_tabela2_nome ON tabela2 (nome);
CREATE INDEX idx_tabela2_data_criacao ON tabela2 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela2()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela2
    BEFORE UPDATE ON tabela2
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela2();


-- Tabela 3
CREATE TABLE tabela3 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela3
CREATE INDEX idx_tabela3_codigo ON tabela3 (codigo);
CREATE INDEX idx_tabela3_nome ON tabela3 (nome);
CREATE INDEX idx_tabela3_data_criacao ON tabela3 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela3()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela3
    BEFORE UPDATE ON tabela3
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela3();


-- Tabela 4
CREATE TABLE tabela4 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela4
CREATE INDEX idx_tabela4_codigo ON tabela4 (codigo);
CREATE INDEX idx_tabela4_nome ON tabela4 (nome);
CREATE INDEX idx_tabela4_data_criacao ON tabela4 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela4()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela4
    BEFORE UPDATE ON tabela4
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela4();


-- Tabela 5
CREATE TABLE tabela5 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela5
CREATE INDEX idx_tabela5_codigo ON tabela5 (codigo);
CREATE INDEX idx_tabela5_nome ON tabela5 (nome);
CREATE INDEX idx_tabela5_data_criacao ON tabela5 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela5()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela5
    BEFORE UPDATE ON tabela5
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela5();


-- Tabela 6
CREATE TABLE tabela6 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela6
CREATE INDEX idx_tabela6_codigo ON tabela6 (codigo);
CREATE INDEX idx_tabela6_nome ON tabela6 (nome);
CREATE INDEX idx_tabela6_data_criacao ON tabela6 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela6()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela6
    BEFORE UPDATE ON tabela6
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela6();


-- Tabela 7
CREATE TABLE tabela7 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela7
CREATE INDEX idx_tabela7_codigo ON tabela7 (codigo);
CREATE INDEX idx_tabela7_nome ON tabela7 (nome);
CREATE INDEX idx_tabela7_data_criacao ON tabela7 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela7()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela7
    BEFORE UPDATE ON tabela7
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela7();


-- Tabela 8
CREATE TABLE tabela8 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela8
CREATE INDEX idx_tabela8_codigo ON tabela8 (codigo);
CREATE INDEX idx_tabela8_nome ON tabela8 (nome);
CREATE INDEX idx_tabela8_data_criacao ON tabela8 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela8()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela8
    BEFORE UPDATE ON tabela8
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela8();


-- Tabela 9
CREATE TABLE tabela9 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela9
CREATE INDEX idx_tabela9_codigo ON tabela9 (codigo);
CREATE INDEX idx_tabela9_nome ON tabela9 (nome);
CREATE INDEX idx_tabela9_data_criacao ON tabela9 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela9()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela9
    BEFORE UPDATE ON tabela9
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela9();


-- Tabela 10
CREATE TABLE tabela10 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela10
CREATE INDEX idx_tabela10_codigo ON tabela10 (codigo);
CREATE INDEX idx_tabela10_nome ON tabela10 (nome);
CREATE INDEX idx_tabela10_data_criacao ON tabela10 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela10()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela10
    BEFORE UPDATE ON tabela10
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela10();


-- Tabela 11
CREATE TABLE tabela11 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela11
CREATE INDEX idx_tabela11_codigo ON tabela11 (codigo);
CREATE INDEX idx_tabela11_nome ON tabela11 (nome);
CREATE INDEX idx_tabela11_data_criacao ON tabela11 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela11()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela11
    BEFORE UPDATE ON tabela11
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela11();


-- Tabela 12
CREATE TABLE tabela12 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela12
CREATE INDEX idx_tabela12_codigo ON tabela12 (codigo);
CREATE INDEX idx_tabela12_nome ON tabela12 (nome);
CREATE INDEX idx_tabela12_data_criacao ON tabela12 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela12()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela12
    BEFORE UPDATE ON tabela12
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela12();


-- Tabela 13
CREATE TABLE tabela13 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela13
CREATE INDEX idx_tabela13_codigo ON tabela13 (codigo);
CREATE INDEX idx_tabela13_nome ON tabela13 (nome);
CREATE INDEX idx_tabela13_data_criacao ON tabela13 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela13()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela13
    BEFORE UPDATE ON tabela13
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela13();


-- Tabela 14
CREATE TABLE tabela14 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela14
CREATE INDEX idx_tabela14_codigo ON tabela14 (codigo);
CREATE INDEX idx_tabela14_nome ON tabela14 (nome);
CREATE INDEX idx_tabela14_data_criacao ON tabela14 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela14()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela14
    BEFORE UPDATE ON tabela14
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela14();


-- Tabela 15
CREATE TABLE tabela15 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela15
CREATE INDEX idx_tabela15_codigo ON tabela15 (codigo);
CREATE INDEX idx_tabela15_nome ON tabela15 (nome);
CREATE INDEX idx_tabela15_data_criacao ON tabela15 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela15()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela15
    BEFORE UPDATE ON tabela15
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela15();


-- Tabela 16
CREATE TABLE tabela16 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela16
CREATE INDEX idx_tabela16_codigo ON tabela16 (codigo);
CREATE INDEX idx_tabela16_nome ON tabela16 (nome);
CREATE INDEX idx_tabela16_data_criacao ON tabela16 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela16()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela16
    BEFORE UPDATE ON tabela16
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela16();


-- Tabela 17
CREATE TABLE tabela17 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela17
CREATE INDEX idx_tabela17_codigo ON tabela17 (codigo);
CREATE INDEX idx_tabela17_nome ON tabela17 (nome);
CREATE INDEX idx_tabela17_data_criacao ON tabela17 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela17()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela17
    BEFORE UPDATE ON tabela17
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela17();


-- Tabela 18
CREATE TABLE tabela18 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela18
CREATE INDEX idx_tabela18_codigo ON tabela18 (codigo);
CREATE INDEX idx_tabela18_nome ON tabela18 (nome);
CREATE INDEX idx_tabela18_data_criacao ON tabela18 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela18()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela18
    BEFORE UPDATE ON tabela18
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela18();


-- Tabela 19
CREATE TABLE tabela19 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela19
CREATE INDEX idx_tabela19_codigo ON tabela19 (codigo);
CREATE INDEX idx_tabela19_nome ON tabela19 (nome);
CREATE INDEX idx_tabela19_data_criacao ON tabela19 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela19()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela19
    BEFORE UPDATE ON tabela19
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela19();


-- Tabela 20
CREATE TABLE tabela20 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela20
CREATE INDEX idx_tabela20_codigo ON tabela20 (codigo);
CREATE INDEX idx_tabela20_nome ON tabela20 (nome);
CREATE INDEX idx_tabela20_data_criacao ON tabela20 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela20()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela20
    BEFORE UPDATE ON tabela20
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela20();


-- Tabela 21
CREATE TABLE tabela21 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela21
CREATE INDEX idx_tabela21_codigo ON tabela21 (codigo);
CREATE INDEX idx_tabela21_nome ON tabela21 (nome);
CREATE INDEX idx_tabela21_data_criacao ON tabela21 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela21()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela21
    BEFORE UPDATE ON tabela21
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela21();


-- Tabela 22
CREATE TABLE tabela22 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela22
CREATE INDEX idx_tabela22_codigo ON tabela22 (codigo);
CREATE INDEX idx_tabela22_nome ON tabela22 (nome);
CREATE INDEX idx_tabela22_data_criacao ON tabela22 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela22()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela22
    BEFORE UPDATE ON tabela22
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela22();


-- Tabela 23
CREATE TABLE tabela23 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela23
CREATE INDEX idx_tabela23_codigo ON tabela23 (codigo);
CREATE INDEX idx_tabela23_nome ON tabela23 (nome);
CREATE INDEX idx_tabela23_data_criacao ON tabela23 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela23()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela23
    BEFORE UPDATE ON tabela23
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela23();


-- Tabela 24
CREATE TABLE tabela24 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela24
CREATE INDEX idx_tabela24_codigo ON tabela24 (codigo);
CREATE INDEX idx_tabela24_nome ON tabela24 (nome);
CREATE INDEX idx_tabela24_data_criacao ON tabela24 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela24()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela24
    BEFORE UPDATE ON tabela24
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela24();


-- Tabela 25
CREATE TABLE tabela25 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela25
CREATE INDEX idx_tabela25_codigo ON tabela25 (codigo);
CREATE INDEX idx_tabela25_nome ON tabela25 (nome);
CREATE INDEX idx_tabela25_data_criacao ON tabela25 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela25()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela25
    BEFORE UPDATE ON tabela25
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela25();


-- Tabela 26
CREATE TABLE tabela26 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela26
CREATE INDEX idx_tabela26_codigo ON tabela26 (codigo);
CREATE INDEX idx_tabela26_nome ON tabela26 (nome);
CREATE INDEX idx_tabela26_data_criacao ON tabela26 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela26()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela26
    BEFORE UPDATE ON tabela26
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela26();


-- Tabela 27
CREATE TABLE tabela27 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela27
CREATE INDEX idx_tabela27_codigo ON tabela27 (codigo);
CREATE INDEX idx_tabela27_nome ON tabela27 (nome);
CREATE INDEX idx_tabela27_data_criacao ON tabela27 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela27()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela27
    BEFORE UPDATE ON tabela27
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela27();


-- Tabela 28
CREATE TABLE tabela28 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela28
CREATE INDEX idx_tabela28_codigo ON tabela28 (codigo);
CREATE INDEX idx_tabela28_nome ON tabela28 (nome);
CREATE INDEX idx_tabela28_data_criacao ON tabela28 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela28()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela28
    BEFORE UPDATE ON tabela28
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela28();


-- Tabela 29
CREATE TABLE tabela29 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela29
CREATE INDEX idx_tabela29_codigo ON tabela29 (codigo);
CREATE INDEX idx_tabela29_nome ON tabela29 (nome);
CREATE INDEX idx_tabela29_data_criacao ON tabela29 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela29()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela29
    BEFORE UPDATE ON tabela29
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela29();


-- Tabela 30
CREATE TABLE tabela30 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela30
CREATE INDEX idx_tabela30_codigo ON tabela30 (codigo);
CREATE INDEX idx_tabela30_nome ON tabela30 (nome);
CREATE INDEX idx_tabela30_data_criacao ON tabela30 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela30()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela30
    BEFORE UPDATE ON tabela30
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela30();


-- Tabela 31
CREATE TABLE tabela31 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela31
CREATE INDEX idx_tabela31_codigo ON tabela31 (codigo);
CREATE INDEX idx_tabela31_nome ON tabela31 (nome);
CREATE INDEX idx_tabela31_data_criacao ON tabela31 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela31()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela31
    BEFORE UPDATE ON tabela31
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela31();


-- Tabela 32
CREATE TABLE tabela32 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela32
CREATE INDEX idx_tabela32_codigo ON tabela32 (codigo);
CREATE INDEX idx_tabela32_nome ON tabela32 (nome);
CREATE INDEX idx_tabela32_data_criacao ON tabela32 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela32()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela32
    BEFORE UPDATE ON tabela32
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela32();


-- Tabela 33
CREATE TABLE tabela33 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela33
CREATE INDEX idx_tabela33_codigo ON tabela33 (codigo);
CREATE INDEX idx_tabela33_nome ON tabela33 (nome);
CREATE INDEX idx_tabela33_data_criacao ON tabela33 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela33()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela33
    BEFORE UPDATE ON tabela33
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela33();


-- Tabela 34
CREATE TABLE tabela34 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela34
CREATE INDEX idx_tabela34_codigo ON tabela34 (codigo);
CREATE INDEX idx_tabela34_nome ON tabela34 (nome);
CREATE INDEX idx_tabela34_data_criacao ON tabela34 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela34()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela34
    BEFORE UPDATE ON tabela34
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela34();


-- Tabela 35
CREATE TABLE tabela35 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela35
CREATE INDEX idx_tabela35_codigo ON tabela35 (codigo);
CREATE INDEX idx_tabela35_nome ON tabela35 (nome);
CREATE INDEX idx_tabela35_data_criacao ON tabela35 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela35()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela35
    BEFORE UPDATE ON tabela35
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela35();


-- Tabela 36
CREATE TABLE tabela36 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela36
CREATE INDEX idx_tabela36_codigo ON tabela36 (codigo);
CREATE INDEX idx_tabela36_nome ON tabela36 (nome);
CREATE INDEX idx_tabela36_data_criacao ON tabela36 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela36()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela36
    BEFORE UPDATE ON tabela36
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela36();


-- Tabela 37
CREATE TABLE tabela37 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela37
CREATE INDEX idx_tabela37_codigo ON tabela37 (codigo);
CREATE INDEX idx_tabela37_nome ON tabela37 (nome);
CREATE INDEX idx_tabela37_data_criacao ON tabela37 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela37()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela37
    BEFORE UPDATE ON tabela37
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela37();


-- Tabela 38
CREATE TABLE tabela38 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela38
CREATE INDEX idx_tabela38_codigo ON tabela38 (codigo);
CREATE INDEX idx_tabela38_nome ON tabela38 (nome);
CREATE INDEX idx_tabela38_data_criacao ON tabela38 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela38()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela38
    BEFORE UPDATE ON tabela38
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela38();


-- Tabela 39
CREATE TABLE tabela39 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela39
CREATE INDEX idx_tabela39_codigo ON tabela39 (codigo);
CREATE INDEX idx_tabela39_nome ON tabela39 (nome);
CREATE INDEX idx_tabela39_data_criacao ON tabela39 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela39()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela39
    BEFORE UPDATE ON tabela39
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela39();


-- Tabela 40
CREATE TABLE tabela40 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela40
CREATE INDEX idx_tabela40_codigo ON tabela40 (codigo);
CREATE INDEX idx_tabela40_nome ON tabela40 (nome);
CREATE INDEX idx_tabela40_data_criacao ON tabela40 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela40()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela40
    BEFORE UPDATE ON tabela40
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela40();


-- Tabela 41
CREATE TABLE tabela41 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela41
CREATE INDEX idx_tabela41_codigo ON tabela41 (codigo);
CREATE INDEX idx_tabela41_nome ON tabela41 (nome);
CREATE INDEX idx_tabela41_data_criacao ON tabela41 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela41()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela41
    BEFORE UPDATE ON tabela41
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela41();


-- Tabela 42
CREATE TABLE tabela42 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela42
CREATE INDEX idx_tabela42_codigo ON tabela42 (codigo);
CREATE INDEX idx_tabela42_nome ON tabela42 (nome);
CREATE INDEX idx_tabela42_data_criacao ON tabela42 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela42()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela42
    BEFORE UPDATE ON tabela42
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela42();


-- Tabela 43
CREATE TABLE tabela43 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela43
CREATE INDEX idx_tabela43_codigo ON tabela43 (codigo);
CREATE INDEX idx_tabela43_nome ON tabela43 (nome);
CREATE INDEX idx_tabela43_data_criacao ON tabela43 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela43()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela43
    BEFORE UPDATE ON tabela43
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela43();


-- Tabela 44
CREATE TABLE tabela44 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela44
CREATE INDEX idx_tabela44_codigo ON tabela44 (codigo);
CREATE INDEX idx_tabela44_nome ON tabela44 (nome);
CREATE INDEX idx_tabela44_data_criacao ON tabela44 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela44()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela44
    BEFORE UPDATE ON tabela44
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela44();


-- Tabela 45
CREATE TABLE tabela45 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela45
CREATE INDEX idx_tabela45_codigo ON tabela45 (codigo);
CREATE INDEX idx_tabela45_nome ON tabela45 (nome);
CREATE INDEX idx_tabela45_data_criacao ON tabela45 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela45()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela45
    BEFORE UPDATE ON tabela45
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela45();


-- Tabela 46
CREATE TABLE tabela46 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela46
CREATE INDEX idx_tabela46_codigo ON tabela46 (codigo);
CREATE INDEX idx_tabela46_nome ON tabela46 (nome);
CREATE INDEX idx_tabela46_data_criacao ON tabela46 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela46()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela46
    BEFORE UPDATE ON tabela46
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela46();


-- Tabela 47
CREATE TABLE tabela47 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela47
CREATE INDEX idx_tabela47_codigo ON tabela47 (codigo);
CREATE INDEX idx_tabela47_nome ON tabela47 (nome);
CREATE INDEX idx_tabela47_data_criacao ON tabela47 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela47()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela47
    BEFORE UPDATE ON tabela47
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela47();


-- Tabela 48
CREATE TABLE tabela48 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela48
CREATE INDEX idx_tabela48_codigo ON tabela48 (codigo);
CREATE INDEX idx_tabela48_nome ON tabela48 (nome);
CREATE INDEX idx_tabela48_data_criacao ON tabela48 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela48()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela48
    BEFORE UPDATE ON tabela48
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela48();


-- Tabela 49
CREATE TABLE tabela49 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela49
CREATE INDEX idx_tabela49_codigo ON tabela49 (codigo);
CREATE INDEX idx_tabela49_nome ON tabela49 (nome);
CREATE INDEX idx_tabela49_data_criacao ON tabela49 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela49()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela49
    BEFORE UPDATE ON tabela49
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela49();


-- Tabela 50
CREATE TABLE tabela50 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela50
CREATE INDEX idx_tabela50_codigo ON tabela50 (codigo);
CREATE INDEX idx_tabela50_nome ON tabela50 (nome);
CREATE INDEX idx_tabela50_data_criacao ON tabela50 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela50()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela50
    BEFORE UPDATE ON tabela50
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela50();


-- Tabela 51
CREATE TABLE tabela51 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela51
CREATE INDEX idx_tabela51_codigo ON tabela51 (codigo);
CREATE INDEX idx_tabela51_nome ON tabela51 (nome);
CREATE INDEX idx_tabela51_data_criacao ON tabela51 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela51()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela51
    BEFORE UPDATE ON tabela51
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela51();


-- Tabela 52
CREATE TABLE tabela52 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela52
CREATE INDEX idx_tabela52_codigo ON tabela52 (codigo);
CREATE INDEX idx_tabela52_nome ON tabela52 (nome);
CREATE INDEX idx_tabela52_data_criacao ON tabela52 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela52()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela52
    BEFORE UPDATE ON tabela52
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela52();


-- Tabela 53
CREATE TABLE tabela53 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela53
CREATE INDEX idx_tabela53_codigo ON tabela53 (codigo);
CREATE INDEX idx_tabela53_nome ON tabela53 (nome);
CREATE INDEX idx_tabela53_data_criacao ON tabela53 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela53()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela53
    BEFORE UPDATE ON tabela53
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela53();


-- Tabela 54
CREATE TABLE tabela54 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela54
CREATE INDEX idx_tabela54_codigo ON tabela54 (codigo);
CREATE INDEX idx_tabela54_nome ON tabela54 (nome);
CREATE INDEX idx_tabela54_data_criacao ON tabela54 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela54()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela54
    BEFORE UPDATE ON tabela54
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela54();


-- Tabela 55
CREATE TABLE tabela55 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela55
CREATE INDEX idx_tabela55_codigo ON tabela55 (codigo);
CREATE INDEX idx_tabela55_nome ON tabela55 (nome);
CREATE INDEX idx_tabela55_data_criacao ON tabela55 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela55()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela55
    BEFORE UPDATE ON tabela55
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela55();


-- Tabela 56
CREATE TABLE tabela56 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela56
CREATE INDEX idx_tabela56_codigo ON tabela56 (codigo);
CREATE INDEX idx_tabela56_nome ON tabela56 (nome);
CREATE INDEX idx_tabela56_data_criacao ON tabela56 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela56()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela56
    BEFORE UPDATE ON tabela56
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela56();


-- Tabela 57
CREATE TABLE tabela57 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela57
CREATE INDEX idx_tabela57_codigo ON tabela57 (codigo);
CREATE INDEX idx_tabela57_nome ON tabela57 (nome);
CREATE INDEX idx_tabela57_data_criacao ON tabela57 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela57()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela57
    BEFORE UPDATE ON tabela57
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela57();


-- Tabela 58
CREATE TABLE tabela58 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela58
CREATE INDEX idx_tabela58_codigo ON tabela58 (codigo);
CREATE INDEX idx_tabela58_nome ON tabela58 (nome);
CREATE INDEX idx_tabela58_data_criacao ON tabela58 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela58()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela58
    BEFORE UPDATE ON tabela58
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela58();


-- Tabela 59
CREATE TABLE tabela59 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela59
CREATE INDEX idx_tabela59_codigo ON tabela59 (codigo);
CREATE INDEX idx_tabela59_nome ON tabela59 (nome);
CREATE INDEX idx_tabela59_data_criacao ON tabela59 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela59()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela59
    BEFORE UPDATE ON tabela59
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela59();


-- Tabela 60
CREATE TABLE tabela60 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela60
CREATE INDEX idx_tabela60_codigo ON tabela60 (codigo);
CREATE INDEX idx_tabela60_nome ON tabela60 (nome);
CREATE INDEX idx_tabela60_data_criacao ON tabela60 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela60()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela60
    BEFORE UPDATE ON tabela60
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela60();


-- Tabela 61
CREATE TABLE tabela61 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela61
CREATE INDEX idx_tabela61_codigo ON tabela61 (codigo);
CREATE INDEX idx_tabela61_nome ON tabela61 (nome);
CREATE INDEX idx_tabela61_data_criacao ON tabela61 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela61()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela61
    BEFORE UPDATE ON tabela61
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela61();


-- Tabela 62
CREATE TABLE tabela62 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela62
CREATE INDEX idx_tabela62_codigo ON tabela62 (codigo);
CREATE INDEX idx_tabela62_nome ON tabela62 (nome);
CREATE INDEX idx_tabela62_data_criacao ON tabela62 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela62()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela62
    BEFORE UPDATE ON tabela62
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela62();


-- Tabela 63
CREATE TABLE tabela63 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela63
CREATE INDEX idx_tabela63_codigo ON tabela63 (codigo);
CREATE INDEX idx_tabela63_nome ON tabela63 (nome);
CREATE INDEX idx_tabela63_data_criacao ON tabela63 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela63()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela63
    BEFORE UPDATE ON tabela63
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela63();


-- Tabela 64
CREATE TABLE tabela64 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela64
CREATE INDEX idx_tabela64_codigo ON tabela64 (codigo);
CREATE INDEX idx_tabela64_nome ON tabela64 (nome);
CREATE INDEX idx_tabela64_data_criacao ON tabela64 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela64()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela64
    BEFORE UPDATE ON tabela64
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela64();


-- Tabela 65
CREATE TABLE tabela65 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela65
CREATE INDEX idx_tabela65_codigo ON tabela65 (codigo);
CREATE INDEX idx_tabela65_nome ON tabela65 (nome);
CREATE INDEX idx_tabela65_data_criacao ON tabela65 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela65()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela65
    BEFORE UPDATE ON tabela65
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela65();


-- Tabela 66
CREATE TABLE tabela66 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela66
CREATE INDEX idx_tabela66_codigo ON tabela66 (codigo);
CREATE INDEX idx_tabela66_nome ON tabela66 (nome);
CREATE INDEX idx_tabela66_data_criacao ON tabela66 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela66()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela66
    BEFORE UPDATE ON tabela66
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela66();


-- Tabela 67
CREATE TABLE tabela67 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela67
CREATE INDEX idx_tabela67_codigo ON tabela67 (codigo);
CREATE INDEX idx_tabela67_nome ON tabela67 (nome);
CREATE INDEX idx_tabela67_data_criacao ON tabela67 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela67()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela67
    BEFORE UPDATE ON tabela67
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela67();


-- Tabela 68
CREATE TABLE tabela68 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela68
CREATE INDEX idx_tabela68_codigo ON tabela68 (codigo);
CREATE INDEX idx_tabela68_nome ON tabela68 (nome);
CREATE INDEX idx_tabela68_data_criacao ON tabela68 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela68()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela68
    BEFORE UPDATE ON tabela68
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela68();


-- Tabela 69
CREATE TABLE tabela69 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela69
CREATE INDEX idx_tabela69_codigo ON tabela69 (codigo);
CREATE INDEX idx_tabela69_nome ON tabela69 (nome);
CREATE INDEX idx_tabela69_data_criacao ON tabela69 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela69()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela69
    BEFORE UPDATE ON tabela69
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela69();


-- Tabela 70
CREATE TABLE tabela70 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela70
CREATE INDEX idx_tabela70_codigo ON tabela70 (codigo);
CREATE INDEX idx_tabela70_nome ON tabela70 (nome);
CREATE INDEX idx_tabela70_data_criacao ON tabela70 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela70()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela70
    BEFORE UPDATE ON tabela70
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela70();


-- Tabela 71
CREATE TABLE tabela71 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela71
CREATE INDEX idx_tabela71_codigo ON tabela71 (codigo);
CREATE INDEX idx_tabela71_nome ON tabela71 (nome);
CREATE INDEX idx_tabela71_data_criacao ON tabela71 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela71()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela71
    BEFORE UPDATE ON tabela71
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela71();


-- Tabela 72
CREATE TABLE tabela72 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela72
CREATE INDEX idx_tabela72_codigo ON tabela72 (codigo);
CREATE INDEX idx_tabela72_nome ON tabela72 (nome);
CREATE INDEX idx_tabela72_data_criacao ON tabela72 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela72()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela72
    BEFORE UPDATE ON tabela72
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela72();


-- Tabela 73
CREATE TABLE tabela73 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela73
CREATE INDEX idx_tabela73_codigo ON tabela73 (codigo);
CREATE INDEX idx_tabela73_nome ON tabela73 (nome);
CREATE INDEX idx_tabela73_data_criacao ON tabela73 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela73()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela73
    BEFORE UPDATE ON tabela73
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela73();


-- Tabela 74
CREATE TABLE tabela74 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela74
CREATE INDEX idx_tabela74_codigo ON tabela74 (codigo);
CREATE INDEX idx_tabela74_nome ON tabela74 (nome);
CREATE INDEX idx_tabela74_data_criacao ON tabela74 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela74()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela74
    BEFORE UPDATE ON tabela74
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela74();


-- Tabela 75
CREATE TABLE tabela75 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela75
CREATE INDEX idx_tabela75_codigo ON tabela75 (codigo);
CREATE INDEX idx_tabela75_nome ON tabela75 (nome);
CREATE INDEX idx_tabela75_data_criacao ON tabela75 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela75()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela75
    BEFORE UPDATE ON tabela75
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela75();


-- Tabela 76
CREATE TABLE tabela76 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela76
CREATE INDEX idx_tabela76_codigo ON tabela76 (codigo);
CREATE INDEX idx_tabela76_nome ON tabela76 (nome);
CREATE INDEX idx_tabela76_data_criacao ON tabela76 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela76()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela76
    BEFORE UPDATE ON tabela76
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela76();


-- Tabela 77
CREATE TABLE tabela77 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela77
CREATE INDEX idx_tabela77_codigo ON tabela77 (codigo);
CREATE INDEX idx_tabela77_nome ON tabela77 (nome);
CREATE INDEX idx_tabela77_data_criacao ON tabela77 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela77()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela77
    BEFORE UPDATE ON tabela77
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela77();


-- Tabela 78
CREATE TABLE tabela78 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela78
CREATE INDEX idx_tabela78_codigo ON tabela78 (codigo);
CREATE INDEX idx_tabela78_nome ON tabela78 (nome);
CREATE INDEX idx_tabela78_data_criacao ON tabela78 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela78()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela78
    BEFORE UPDATE ON tabela78
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela78();


-- Tabela 79
CREATE TABLE tabela79 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela79
CREATE INDEX idx_tabela79_codigo ON tabela79 (codigo);
CREATE INDEX idx_tabela79_nome ON tabela79 (nome);
CREATE INDEX idx_tabela79_data_criacao ON tabela79 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela79()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela79
    BEFORE UPDATE ON tabela79
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela79();


-- Tabela 80
CREATE TABLE tabela80 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela80
CREATE INDEX idx_tabela80_codigo ON tabela80 (codigo);
CREATE INDEX idx_tabela80_nome ON tabela80 (nome);
CREATE INDEX idx_tabela80_data_criacao ON tabela80 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela80()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela80
    BEFORE UPDATE ON tabela80
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela80();


-- Tabela 81
CREATE TABLE tabela81 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela81
CREATE INDEX idx_tabela81_codigo ON tabela81 (codigo);
CREATE INDEX idx_tabela81_nome ON tabela81 (nome);
CREATE INDEX idx_tabela81_data_criacao ON tabela81 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela81()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela81
    BEFORE UPDATE ON tabela81
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela81();


-- Tabela 82
CREATE TABLE tabela82 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela82
CREATE INDEX idx_tabela82_codigo ON tabela82 (codigo);
CREATE INDEX idx_tabela82_nome ON tabela82 (nome);
CREATE INDEX idx_tabela82_data_criacao ON tabela82 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela82()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela82
    BEFORE UPDATE ON tabela82
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela82();


-- Tabela 83
CREATE TABLE tabela83 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela83
CREATE INDEX idx_tabela83_codigo ON tabela83 (codigo);
CREATE INDEX idx_tabela83_nome ON tabela83 (nome);
CREATE INDEX idx_tabela83_data_criacao ON tabela83 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela83()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela83
    BEFORE UPDATE ON tabela83
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela83();


-- Tabela 84
CREATE TABLE tabela84 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela84
CREATE INDEX idx_tabela84_codigo ON tabela84 (codigo);
CREATE INDEX idx_tabela84_nome ON tabela84 (nome);
CREATE INDEX idx_tabela84_data_criacao ON tabela84 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela84()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela84
    BEFORE UPDATE ON tabela84
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela84();


-- Tabela 85
CREATE TABLE tabela85 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela85
CREATE INDEX idx_tabela85_codigo ON tabela85 (codigo);
CREATE INDEX idx_tabela85_nome ON tabela85 (nome);
CREATE INDEX idx_tabela85_data_criacao ON tabela85 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela85()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela85
    BEFORE UPDATE ON tabela85
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela85();


-- Tabela 86
CREATE TABLE tabela86 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela86
CREATE INDEX idx_tabela86_codigo ON tabela86 (codigo);
CREATE INDEX idx_tabela86_nome ON tabela86 (nome);
CREATE INDEX idx_tabela86_data_criacao ON tabela86 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela86()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela86
    BEFORE UPDATE ON tabela86
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela86();


-- Tabela 87
CREATE TABLE tabela87 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela87
CREATE INDEX idx_tabela87_codigo ON tabela87 (codigo);
CREATE INDEX idx_tabela87_nome ON tabela87 (nome);
CREATE INDEX idx_tabela87_data_criacao ON tabela87 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela87()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela87
    BEFORE UPDATE ON tabela87
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela87();


-- Tabela 88
CREATE TABLE tabela88 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela88
CREATE INDEX idx_tabela88_codigo ON tabela88 (codigo);
CREATE INDEX idx_tabela88_nome ON tabela88 (nome);
CREATE INDEX idx_tabela88_data_criacao ON tabela88 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela88()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela88
    BEFORE UPDATE ON tabela88
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela88();


-- Tabela 89
CREATE TABLE tabela89 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela89
CREATE INDEX idx_tabela89_codigo ON tabela89 (codigo);
CREATE INDEX idx_tabela89_nome ON tabela89 (nome);
CREATE INDEX idx_tabela89_data_criacao ON tabela89 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela89()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela89
    BEFORE UPDATE ON tabela89
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela89();


-- Tabela 90
CREATE TABLE tabela90 (
    id BIGSERIAL PRIMARY KEY,
    codigo VARCHAR(50) NOT NULL,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    valor DECIMAL(15,2),
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ativo BOOLEAN DEFAULT TRUE,
    categoria VARCHAR(100),
    observacoes TEXT
);

-- Índices para tabela90
CREATE INDEX idx_tabela90_codigo ON tabela90 (codigo);
CREATE INDEX idx_tabela90_nome ON tabela90 (nome);
CREATE INDEX idx_tabela90_data_criacao ON tabela90 (data_criacao);

-- Trigger para atualizar data_atualizacao automaticamente
CREATE OR REPLACE FUNCTION update_data_atualizacao_tabela90()
RETURNS TRIGGER AS $$
BEGIN
    NEW.data_atualizacao = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_update_data_atualizacao_tabela90
    BEFORE UPDATE ON tabela90
    FOR EACH ROW
    EXECUTE FUNCTION update_data_atualizacao_tabela90();

