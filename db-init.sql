GRANT ALL PRIVILEGES ON DATABASE perf_metrics TO postgres;

CREATE TABLE measurements (
    version INT,
    timestamp TIMESTAMP NOT NULL,
    value NUMERIC NOT NULL
);

INSERT INTO measurements (version, timestamp, value)
VALUES
    (1, '2023-09-20 00:00:00', 10.5),
    (2, '2023-09-21 01:00:00', 11.2),
    (3, '2023-09-22 02:00:00', 9.8),
    (4, '2023-09-23 03:00:00', 12.1),
    (5, '2023-09-24 04:00:00', 8.9),
    (6, '2023-09-25 05:00:00', 10.3),
    (7, '2023-09-26 06:00:00', 11.5),
    (8, '2023-09-27 07:00:00', 9.7),
    (9, '2023-09-28 08:00:00', 12.3),
    (10, '2023-09-29 09:00:00', 8.5),
    (11, '2023-09-30 10:00:00', 11.1),
    (12, '2023-10-01 11:00:00', 9.9),
    (13, '2023-10-02 12:00:00', 12.2),
    (14, '2023-10-03 13:00:00', 8.8),
    (15, '2023-10-04 14:00:00', 10.4),
    (16, '2023-10-05 15:00:00', 11.4),
    (17, '2023-10-06 16:00:00', 9.6),
    (18, '2023-10-07 17:00:00', 12.4),
    (19, '2023-10-08 18:00:00', 8.4),
    (20, '2023-10-09 19:00:00', 11.0);
