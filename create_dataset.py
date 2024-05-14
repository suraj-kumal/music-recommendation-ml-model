import csv

data = [
    (9, 0, 'Electronic'),
    (55, 1, 'Jazz'),
    (17, 0, 'Electronic'),
    (63, 1, 'Jazz'),
    (25, 1, 'Hip Hop'),
    (47, 0, 'Electronic'),
    (34, 1, 'Hip Hop'),
    (42, 0, 'Electronic'),
    (18, 1, 'Hip Hop'),
    (70, 0, 'Classical'),
    (30, 1, 'Rock'),
    (38, 0, 'Electronic'),
    (14, 1, 'Hip Hop'),
    (65, 0, 'Classical'),
    (20, 1, 'Rock'),
    (53, 0, 'Electronic'),
    (27, 1, 'Electronic'),
    (58, 0, 'Jazz'),
    (16, 1, 'Dance'),
    (68, 0, 'Classical'),
    (22, 1, 'Rock'),
    (45, 0, 'Jazz'),
    (13, 1, 'Electronic'),
    (50, 0, 'Electronic'),
    (67, 0, 'Classical'),
    (19, 1, 'Rock'),
    (40, 0, 'Classical'),
    (11, 1, 'Electronic'),
    (52, 0, 'Electronic'),
    (48, 0, 'Classical'),
    (31, 1, 'Electronic'),
    (64, 0, 'Jazz'),
    (28, 1, 'Electronic'),
    (57, 0, 'Classical'),
    (15, 1, 'Rock'),
    (60, 0, 'Classical'),
    (26, 1, 'Electronic'),
    (56, 0, 'Classical'),
    (12, 1, 'Electronic'),
    (62, 0, 'Classical'),
    (49, 0, 'Electronic'),
    (33, 1, 'Rock'),
    (69, 0, 'Classical'),
    (23, 1, 'R&B'),
    (66, 0, 'Classical'),
    (29, 1, 'Electronic'),
    (54, 0, 'Classical'),
    (35, 1, 'Dance'),
    (59, 0, 'Classical'),
    (32, 1, 'Electronic'),
    (51, 0, 'Electronic')
] 

with open('music_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Age', 'Gender', 'Genre'])
    writer.writerows(data)

print("CSV file generated successfully.")
