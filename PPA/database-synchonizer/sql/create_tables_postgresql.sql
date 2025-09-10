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

