-- Inserting in to "flat_details" Table

INSERT INTO private_data.flat_details (flatno, floorno, furnished, facilities, propertytype, area_in_m2, price_range, available_from) VALUES
(32, 3, 'Yes', '{"wash-machine","dishwasher","cupboard","sofa"}', '2BHK', 70, '[29000,35001)', '2026-02-01'),
(34, 3, 'Yes', '{"wash-machine","dishwasher","cupboard","sofa"}', '2BHK', 70, '[29000,35001)', '2024-06-01'),
(12, 1, 'No', '{"wash-machine","cupboard","sofa"}', '1BHK', 60, '[14000,20001)', '2025-02-01'),
(11, 1, 'No', '{}', '2BHK', 88, '[19000,25001)', '2025-02-01'),
(4, 0, 'No', '{}', 'SHOP', 550, '[49000,55001)', '2025-01-01');