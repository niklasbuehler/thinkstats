import survey
import thinkstats
import math

pregnancies = survey.Pregnancies()
pregnancies.ReadRecords()
print 'Number of pregnancies', len(pregnancies.records)
print

preg_lengths_first = []
preg_lengths_others = []

for preg in pregnancies.records:
    if preg.outcome != 1:
        continue
    if preg.birthord == 1:
        preg_lengths_first.append(preg.prglength)
    else:
        preg_lengths_others.append(preg.prglength)

pregs_first = len(preg_lengths_first)
mean_length_first, var_length_first = thinkstats.MeanVar(preg_lengths_first)
std_length_first = math.sqrt(var_length_first)

pregs_others = len(preg_lengths_others)
mean_length_others, var_length_others = thinkstats.MeanVar(preg_lengths_others)
std_length_others = math.sqrt(var_length_others)

print 'Number of live births, first child', pregs_first
print 'Mean pregnancy length (weeks), first child', mean_length_first
print 'Variance of gestation time, first child', var_length_first
print 'Standard deviation of gestation time, first child', std_length_first
print
print 'Number of live births, other children', pregs_others
print 'Mean pregnancy length (weeks), other children', mean_length_others
print 'Variance of gestation time, other children', var_length_others
print 'Standard deviation of gestation time, other children', std_length_others
