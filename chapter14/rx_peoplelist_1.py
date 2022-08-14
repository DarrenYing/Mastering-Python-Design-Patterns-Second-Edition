from rx import interval, operators, from_


def firstnames_from_db(file_name):
    file = open(file_name)
    # collect and push stored people firstnames
    return from_(file).pipe(
        operators.flat_map(lambda content: content.split(', ')),
        operators.filter(lambda name: name != ''),
        operators.map(lambda name: name.split()[0]),
        operators.group_by(lambda firstname: firstname),
        operators.flat_map(lambda grp: grp.count().map(lambda ct: (grp.key, ct)))
    )


db_file = "people.txt"

# Emit data every 5 seconds
interval(1).pipe(
    operators.flat_map(lambda i: firstnames_from_db(db_file))
).subscribe(lambda value: print(str(value)))

# Keep alive until user presses any key
input("Starting... Press any key to quit\n")
