package br.com.udesc.sequential_database_synchonizer.sequential;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import java.sql.*;

@Service
public class DatabaseSynchronizationService {

    private static final Logger logger = LoggerFactory.getLogger(DatabaseSynchronizationService.class);

    @Value("${database.source.url}")
    private String sourceUrl;

    @Value("${database.target.url}")
    private String targetUrl;

    @Value("${database.username:postgres}")
    private String username;

    @Value("${database.password:postgres}")
    private String password;

    static {
        try {
            Class.forName("org.postgresql.Driver");
            System.out.println("Driver PostgreSQL carregado com sucesso");
        } catch (ClassNotFoundException e) {
            System.err.println("Erro ao carregar driver PostgreSQL: " + e.getMessage());
            throw new RuntimeException("Driver PostgreSQL não encontrado", e);
        }
    }

    public void synchronizeTable(String tableName) throws SQLException {
        logger.info("Iniciando sincronização da tabela: {}", tableName);

        try (Connection sourceConn = getSourceConnection();
             Connection targetConn = getTargetConnection()) {

            long startTime = System.currentTimeMillis();

            int sourceCount = countRecords(sourceConn, tableName);
            logger.info("Tabela {} possui {} registros no banco source", tableName, sourceCount);

            if (sourceCount > 0) {
                copyTableData(sourceConn, targetConn, tableName);

                int targetCount = countRecords(targetConn, tableName);
                logger.info("Sincronização da tabela {} concluída: {} registros copiados", tableName, targetCount);

                if (sourceCount != targetCount) {
                    throw new SQLException(String.format("Falha na sincronização: source=%d, target=%d", sourceCount, targetCount));
                }
            } else {
                logger.info("Tabela {} está vazia no source, apenas limpeza do target realizada", tableName);
            }

            long duration = System.currentTimeMillis() - startTime;
            logger.info("Sincronização da tabela {} finalizada em {}ms", tableName, duration);

        } catch (SQLException e) {
            logger.error("Erro durante sincronização da tabela {}: {}", tableName, e.getMessage(), e);
            throw e;
        }
    }

    private Connection getSourceConnection() throws SQLException {
        return DriverManager.getConnection(sourceUrl, username, password);
    }

    private Connection getTargetConnection() throws SQLException {
        return DriverManager.getConnection(targetUrl, username, password);
    }

    private int countRecords(Connection conn, String tableName) throws SQLException {
        String countSQL = "SELECT COUNT(*) FROM " + tableName;

        try (Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(countSQL)) {

            if (rs.next()) {
                return rs.getInt(1);
            }
            return 0;
        }
    }

    private void copyTableData(Connection sourceConn, Connection targetConn, String tableName) throws SQLException {
        logger.debug("Iniciando cópia de dados da tabela: {}", tableName);

        String selectSQL = buildSelectQuery(sourceConn, tableName);
        String insertSQL = buildInsertQuery(sourceConn, tableName);

        logger.debug("Query SELECT: {}", selectSQL);
        logger.debug("Query INSERT: {}", insertSQL);

        try (PreparedStatement selectStmt = sourceConn.prepareStatement(selectSQL);
             PreparedStatement insertStmt = targetConn.prepareStatement(insertSQL);
             ResultSet rs = selectStmt.executeQuery()) {

            int batchSize = 1000;
            int batchCount = 0;
            int totalRecords = 0;

            targetConn.setAutoCommit(false);

            while (rs.next()) {
                copyRowData(rs, insertStmt, sourceConn, tableName);
                insertStmt.addBatch();
                batchCount++;
                totalRecords++;

                if (batchCount == batchSize) {
                    insertStmt.executeBatch();
                    targetConn.commit();
                    logger.debug("Lote de {} registros inserido. Total: {}", batchSize, totalRecords);
                    batchCount = 0;
                }
            }

            if (batchCount > 0) {
                insertStmt.executeBatch();
                targetConn.commit();
                logger.debug("Lote final de {} registros inserido", batchCount);
            }

            targetConn.setAutoCommit(true);
            logger.debug("Cópia de dados finalizada: {} registros", totalRecords);
        }
    }

    private String buildSelectQuery(Connection conn, String tableName) throws SQLException {
        StringBuilder selectBuilder = new StringBuilder("SELECT ");

        DatabaseMetaData metaData = conn.getMetaData();
        try (ResultSet columns = metaData.getColumns(null, null, tableName, null)) {
            boolean first = true;
            while (columns.next()) {
                String columnName = columns.getString("COLUMN_NAME");
                if (!first) {
                    selectBuilder.append(", ");
                }
                selectBuilder.append(columnName);
                first = false;
            }
        }

        selectBuilder.append(" FROM ").append(tableName);
        return selectBuilder.toString();
    }

    private String buildInsertQuery(Connection conn, String tableName) throws SQLException {
        StringBuilder insertBuilder = new StringBuilder("INSERT INTO ").append(tableName).append(" (");
        StringBuilder valuesBuilder = new StringBuilder(" VALUES (");

        DatabaseMetaData metaData = conn.getMetaData();
        try (ResultSet columns = metaData.getColumns(null, null, tableName, null)) {
            boolean first = true;
            while (columns.next()) {
                String columnName = columns.getString("COLUMN_NAME");
                if (!first) {
                    insertBuilder.append(", ");
                    valuesBuilder.append(", ");
                }
                insertBuilder.append(columnName);
                valuesBuilder.append("?");
                first = false;
            }
        }

        insertBuilder.append(")").append(valuesBuilder).append(")");
        return insertBuilder.toString();
    }

    private void copyRowData(ResultSet rs, PreparedStatement insertStmt, Connection sourceConn, String tableName) throws SQLException {
        DatabaseMetaData metaData = sourceConn.getMetaData();
        try (ResultSet columns = metaData.getColumns(null, null, tableName, null)) {
            int paramIndex = 1;
            while (columns.next()) {
                String columnName = columns.getString("COLUMN_NAME");
                int columnType = columns.getInt("DATA_TYPE");

                Object value = rs.getObject(columnName);
                if (value == null) {
                    insertStmt.setNull(paramIndex, columnType);
                } else {
                    insertStmt.setObject(paramIndex, value);
                }
                paramIndex++;
            }
        }
    }
}