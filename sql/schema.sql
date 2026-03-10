-- Tenants and their leases at a small commercial building.
CREATE TABLE tenants (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  unit TEXT NOT NULL
);

CREATE TABLE leases (
  id INTEGER PRIMARY KEY,
  tenant_id INTEGER NOT NULL REFERENCES tenants(id),
  start_date TEXT NOT NULL,  -- YYYY-MM-DD
  end_date TEXT NOT NULL,    -- YYYY-MM-DD
  monthly_rent INTEGER NOT NULL
);

INSERT INTO tenants (id, name, unit) VALUES
  (1, 'Bright Bakery', 'G-01'),
  (2, 'Kiosk Nine', 'G-09'),
  (3, 'Lumen Optical', '2-04'),
  (4, 'Northwind Pharmacy', 'G-03'),
  (5, 'Tala Coffee', '2-01');

INSERT INTO leases (id, tenant_id, start_date, end_date, monthly_rent) VALUES
  (1, 1, '2023-01-01', '2024-12-31', 45000),
  (2, 1, '2025-01-01', '2027-12-31', 52000),
  (3, 2, '2024-06-01', '2026-05-31', 18000),
  (4, 3, '2025-03-01', '2028-02-29', 61000),
  (5, 4, '2022-01-01', '2025-12-31', 58000);
