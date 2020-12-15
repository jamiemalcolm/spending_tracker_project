DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS merchants;



CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    active BOOLEAN
);

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    category VARCHAR(255),
    active BOOLEAN
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    merchant_id INT REFERENCES merchants(id) ON DELETE CASCADE,
    amount FLOAT,
    time_stamp TIMESTAMP NOT NULL DEFAULT NOW(),
    tag_id INT REFERENCES tags(id) ON DELETE CASCADE
);