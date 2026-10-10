
-- schema.sql – SQLite schema for HostelCare AI

PRAGMA foreign_keys = ON;

-- 1. Users and authentication
CREATE TABLE IF NOT EXISTS users (
    user_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL,
    block TEXT,
    room_number TEXT,
    mobile TEXT
);

-- 2. Departments
CREATE TABLE IF NOT EXISTS departments (
    department_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

-- 3. Authority hierarchy
CREATE TABLE IF NOT EXISTS authorities (
    authority_id INTEGER PRIMARY KEY AUTOINCREMENT,
    role TEXT NOT NULL,
    level INTEGER NOT NULL,
    department_id INTEGER NOT NULL,
    UNIQUE(role, department_id),
    FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);

-- 4. Complaints / tickets
CREATE TABLE IF NOT EXISTS complaints (
    ticket_id TEXT PRIMARY KEY,
    user_id TEXT,
    description TEXT NOT NULL,
    category TEXT NOT NULL,
    block TEXT NOT NULL,
    room_number TEXT,
    floor TEXT,
    duration TEXT,
    impact TEXT,
    priority TEXT NOT NULL,
    status TEXT NOT NULL,
    assigned_role TEXT,
    escalation_level INTEGER NOT NULL DEFAULT 1,
    resolution_notes TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    resolved_at TEXT
);

-- 5. Complaint update history
CREATE TABLE IF NOT EXISTS complaint_updates (
    update_id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticket_id TEXT NOT NULL,
    updated_by TEXT,
    old_status TEXT,
    new_status TEXT,
    update_note TEXT,
    timestamp TEXT NOT NULL,
    FOREIGN KEY (ticket_id)
        REFERENCES complaints(ticket_id),
    FOREIGN KEY (updated_by)
        REFERENCES users(user_id)
);

-- 6. Audit and escalation logs
CREATE TABLE IF NOT EXISTS action_logs (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticket_id TEXT NOT NULL,
    action TEXT NOT NULL,
    from_role TEXT,
    to_role TEXT,
    timestamp TEXT NOT NULL,
    FOREIGN KEY (ticket_id)
        REFERENCES complaints(ticket_id)
);

-- 7. Seed departments
INSERT OR IGNORE INTO departments (name) VALUES
    ('Plumbing'),
    ('Electrical'),
    ('Housekeeping'),
    ('Security');

-- 8. Seed authority hierarchy for each department
INSERT OR IGNORE INTO authorities (role, level, department_id)
SELECT roles.role, roles.level, departments.department_id
FROM departments
CROSS JOIN (
    SELECT 'Technician' AS role, 1 AS level
    UNION ALL SELECT 'Supervisor', 2
    UNION ALL SELECT 'Warden', 3
    UNION ALL SELECT 'Director', 4
) AS roles;

-- Demo user accounts are seeded by database.py.
-- Keep account details in one place to avoid conflicting demo users.

