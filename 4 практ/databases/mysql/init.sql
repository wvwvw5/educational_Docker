CREATE TABLE IF NOT EXISTS energy_usage (
    id INT AUTO_INCREMENT PRIMARY KEY,
    recorded_at DATETIME NOT NULL,
    kilowatt_hours DECIMAL(6,2) NOT NULL,
    location VARCHAR(64) NOT NULL
);

INSERT INTO energy_usage (recorded_at, kilowatt_hours, location) VALUES
    ('2025-10-20 08:00:00', 12.5, 'Office'),
    ('2025-10-20 12:00:00', 18.1, 'Office'),
    ('2025-10-20 16:00:00', 16.3, 'Office'),
    ('2025-10-21 08:00:00', 13.8, 'Office'),
    ('2025-10-21 12:00:00', 17.9, 'Office');
