albums = [
    ('blawededed', 'sgjngnonwo', 1989),
    ('blidwoed', 'sikuikik', 192324),
    ('blabddsdnaidwoed', 'sikiuuinonwo', 193389),
    ('blab33ddwoed', 'sdggfonwo', 43249),
    ('blabd2dsdfwoed', 'gfdnwo', 192439),
    ('blablagthfgwoed', 'siniwgsdwo', 1989333),
]
print(len(albums))

# Unpaking tuple in loop
for name, artist, year in albums:
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))

for album in albums:
    name, artist, year = album
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))