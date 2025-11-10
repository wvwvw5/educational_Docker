CREATE TABLE IF NOT EXISTS sensor_readings (
    id SERIAL PRIMARY KEY,
    ts TIMESTAMPTZ NOT NULL,
    temperature NUMERIC(5,2) NOT NULL,
    humidity NUMERIC(5,2) NOT NULL
);

INSERT INTO sensor_readings (ts, temperature, humidity) VALUES
    ('2025-10-20 09:00:00+03', 21.5, 45.2),
    ('2025-10-20 12:00:00+03', 23.1, 42.8),
    ('2025-10-20 15:00:00+03', 24.4, 40.5),
    ('2025-10-20 18:00:00+03', 22.7, 44.1),
    ('2025-10-21 09:00:00+03', 20.9, 48.3);
