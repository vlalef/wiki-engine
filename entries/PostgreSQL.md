# PostgreSQL

PostgreSQL is a powerful, open-source object-relational database system with over 30 years of active development.

## Overview

PostgreSQL emphasizes extensibility and standards compliance, providing robust features for complex queries, foreign keys, triggers, views, and transactional integrity.

### Key Features

- **ACID Compliance**: Atomicity, Consistency, Isolation, Durability
- **Complex Queries**: Advanced query optimization
- **Multi-Version Concurrency Control (MVCC)**
- **Extensible**: Custom functions and procedures
- **Data Types**: Rich set of native data types

## History

- **1986**: POSTGRES project begins
- **1995**: Postgres95 released
- **1996**: PostgreSQL 6.0 released
- **2020**: PostgreSQL 13 released

## Basic Commands

    -- Create database
    CREATE DATABASE mydatabase;

    -- Create table
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    -- Insert data
    INSERT INTO users (username) VALUES ('john_doe');

## Core Features

### Data Types
- Numeric types
- Character types
- Date/Time types
- Arrays
- JSON/JSONB
- Custom types

### Advanced Features
- Indexes (B-tree, Hash, GiST)
- Full-text search
- Table partitioning
- Replication
- Foreign data wrappers

## Common Uses

### Web Applications
- Data persistence
- User management
- Content management

### Enterprise Systems
- Transaction processing
- Data warehousing
- Analytics

### Geographic Systems
- Spatial data storage
- Geographic queries
- PostGIS extension

## See Also
- [Django](/wiki/Django)
- [Database](/wiki/Database)
- [SQL](/wiki/SQL)