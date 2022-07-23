"""
Copyright (c) 2022, Oracle and/or its affiliates.
Copyright (c) 2020, Vitor Avancini

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

     https://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
"""

# https://docs.oracle.com/en/database/oracle/oracle-database/21/zzpre/Oracle-reserved-words-keywords-namespaces.html#GUID-25FE5FB4-5B17-4AFA-9B59-77B6036EF579
RESERVED_KEYWORDS = {
        "ACCESS"
        "ELSE",
        "MODIFY",
        "START",
        "ADD",
        "EXCLUSIVE",
        "NOAUDIT",
        "SELECT",
        "ALL",
        "EXISTS",
        "NOCOMPRESS",
        "SESSION",
        "ALTER",
        "FILE",
        "NOT",
        "SET",
        "AND",
        "FLOAT",
        "NOTFOUND",
        "SHARE",
        "ANY",
        "FOR",
        "NOWAIT",
        "SIZE",
        "ARRAYLEN",
        "FROM",
        "NULL",
        "SMALLINT",
        "AS",
        "GRANT",
        "NUMBER",
        "SQLBUF",
        "ASC",
        "GROUP",
        "OF",
        "SUCCESSFUL",
        "AUDIT",
        "HAVING",
        "OFFLINE",
        "SYNONYM",
        "BETWEEN",
        "IDENTIFIED",
        "ON",
        "SYSDATE",
        "BY",
        "IMMEDIATE",
        "ONLINE",
        "TABLE",
        "CHAR",
        "IN",
        "OPTION",
        "THEN",
        "CHECK",
        "INCREMENT",
        "OR",
        "TO",
        "CLUSTER",
        "INDEX",
        "ORDER",
        "TRIGGER",
        "COLUMN",
        "INITIAL",
        "PCTFREE",
        "UID",
        "COMMENT",
        "INSERT",
        "PRIOR",
        "UNION",
        "COMPRESS",
        "INTEGER",
        "PRIVILEGES",
        "UNIQUE",
        "CONNECT",
        "INTERSECT",
        "PUBLIC",
        "UPDATE",
        "CREATE",
        "INTO",
        "RAW",
        "USER",
        "CURRENT",
        "IS",
        "RENAME",
        "VALIDATE",
        "DATE",
        "LEVEL",
        "RESOURCE",
        "VALUES",
        "DECIMAL",
        "LIKE",
        "REVOKE",
        "VARCHAR",
        "DEFAULT",
        "LOCK",
        "ROW",
        "VARCHAR2",
        "DELETE",
        "LONG",
        "ROWID",
        "VIEW",
        "DESC",
        "MAXEXTENTS",
        "ROWLABEL",
        "WHENEVER",
        "DISTINCT",
        "MINUS",
        "ROWNUM",
        "WHERE",
        "DROP",
        "MODE",
        "ROWS",
        "WITH"
}

NON_RESERVED_KEYWORDS = {
        "ADMIN",
        "CURSOR",
        "FOUND",
        "MOUNT",
        "AFTER",
        "CYCLE",
        "FUNCTION",
        "NEXT",
        "ALLOCATE",
        "DATABASE",
        "GO",
        "NEW",
        "ANALYZE",
        "DATAFILE",
        "GOTO",
        "NOARCHIVELOG",
        "ARCHIVE",
        "DBA",
        "GROUPS",
        "NOCACHE",
        "ARCHIVELOG",
        "DEC",
        "INCLUDING",
        "NOCYCLE",
        "AUTHORIZATION",
        "DECLARE",
        "INDICATOR",
        "NOMAXVALUE",
        "AVG",
        "DISABLE",
        "INITRANS",
        "NOMINVALUE",
        "BACKUP",
        "DISMOUNT",
        "INSTANCE",
        "NONE",
        "BEGIN",
        "DOUBLE",
        "INT",
        "NOORDER",
        "BECOME",
        "DUMP",
        "KEY",
        "NORESETLOGS",
        "BEFORE",
        "EACH",
        "LANGUAGE",
        "NORMAL",
        "BLOCK",
        "ENABLE",
        "LAYER",
        "NOSORT",
        "BODY",
        "END",
        "LINK",
        "NUMERIC",
        "CACHE",
        "ESCAPE",
        "LISTS",
        "OFF",
        "CANCEL",
        "EVENTS",
        "LOGFILE",
        "OLD",
        "CASCADE",
        "EXCEPT",
        "MANAGE",
        "ONLY",
        "CHANGE",
        "EXCEPTIONS",
        "MANUAL",
        "OPEN",
        "CHARACTER",
        "EXEC",
        "MAX",
        "OPTIMAL",
        "CHECKPOINT",
        "EXPLAIN",
        "MAXDATAFILES",
        "OWN",
        "CLOSE",
        "EXECUTE",
        "MAXINSTANCES",
        "PACKAGE",
        "COBOL",
        "EXTENT",
        "MAXLOGFILES",
        "PARALLEL",
        "COMMIT",
        "EXTERNALLY",
        "MAXLOGHISTORY",
        "PCTINCREASE",
        "COMPILE",
        "FETCH",
        "MAXLOGMEMBERS",
        "PCTUSED",
        "CONSTRAINT",
        "FLUSH",
        "MAXTRANS",
        "PLAN",
        "CONSTRAINTS",
        "FREELIST",
        "MAXVALUE",
        "PLI",
        "CONTENTS",
        "FREELISTS",
        "MIN",
        "PRECISION",
        "CONTINUE",
        "FORCE",
        "MINEXTENTS",
        "PRIMARY",
        "CONTROLFILE",
        "FOREIGN",
        "MINVALUE",
        "PRIVATE",
        "COUNT",
        "FORTRAN",
        "MODULE",
        "PROCEDURE",
        "PROFILE",
        "SAVEPOINT",
        "SQLSTATE",
        "TRACING",
        "QUOTA",
        "SCHEMA",
        "STATEMENT_ID",
        "TRANSACTION",
        "READ",
        "SCN",
        "STATISTICS",
        "TRIGGERS",
        "REAL",
        "SECTION",
        "STOP",
        "TRUNCATE",
        "RECOVER",
        "SEGMENT",
        "STORAGE",
        "UNDER",
        "REFERENCES",
        "SEQUENCE",
        "SUM",
        "UNLIMITED",
        "REFERENCING",
        "SHARED",
        "SWITCH",
        "UNTIL",
        "RESETLOGS",
        "SNAPSHOT",
        "SYSTEM",
        "USE",
        "RESTRICTED",
        "SOME",
        "TABLES",
        "USING",
        "REUSE",
        "SORT",
        "TABLESPACE",
        "WHEN",
        "ROLE",
        "SQL",
        "TEMPORARY",
        "WRITE",
        "ROLES",
        "SQLCODE",
        "THREAD",
        "WORK",
        "ROLLBACK",
        "SQLERROR",
        "TIME"
}

KEYWORDS = RESERVED_KEYWORDS | NON_RESERVED_KEYWORDS
