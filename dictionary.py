# # dictionary can store any types of data
colors={
    "B":"Blue",
    "R":"Red",
    "G":"Green"
}

print(colors.get("G","stop"))


employee={
    140:"nameA",
    150:"nameB",
    160:"nameC",
}

print(employee.get(140, "it's not present"))