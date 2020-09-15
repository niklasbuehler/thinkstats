import survey

table = survey.Pregnancies()
table.ReadRecords()
print 'Number of pregnancies', len(table.records)

pregs_first = 0
pregs_others = 0
length_first = 0
length_others = 0

for record in table.records:
    if record.outcome != 1:
        continue
    if record.birthord == 1:
        pregs_first += 1
        length_first += record.prglength
    else:
        pregs_others += 1
        length_others += record.prglength

length_first /= pregs_first
length_others /= pregs_others

print 'Number of live births, first child', pregs_first
print 'Average pregnancy length (weeks), first child', length_first
print 'Number of live births, other children', pregs_others
print 'Average pregnancy length (weeks), other children', length_others
