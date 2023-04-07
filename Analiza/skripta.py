from Bio import SeqIO
import numpy as np
import gzip

duljina = 0
referenca = input("Full path name of reference .fasta file: ")

for record in SeqIO.parse(referenca, "fasta"):
    duljina = len(record.seq)

read = input("Full path name of read .fastq.gz file: ")

length = []
with gzip.open(read, "rt") as f:
    for record in SeqIO.parse(f, "fastq"):
        length.append(len(record.seq))
f.close()

kolicina = len(length)
summation = np.sum(length)
minimum = np.min(length)
maximum = np.max(length)
mean = np.mean(length)
median = np.median(length)
std_dev = np.std(length)
quartiles = np.percentile(length, [25, 75])
q1 = quartiles[0]
q3 = quartiles[1]

izlazna_datoteka = input("Name the output .txt file: ")
g = open(izlazna_datoteka, "w")
g.write("Length of the reference sequence is -> %d\n" % duljina)
g.write("Length of the combined sequence of the reads is -> %d\n" % summation)
g.write("Coverage is -> %f\n" % (float(summation) / duljina))
g.write("Average value of the length of the reads is -> %f\n" % float(mean))
g.write("Minimum value of the length of the reads is -> %d\n" % minimum)
g.write("First quartile value of the length of the reads is -> %f\n" % q1)
g.write("Median value of the length of the reads is -> %f\n" % median)
g.write("Third quartile value of the length of the reads is -> %f\n" % q3)
g.write("Maximum value of the length of the reads is -> %d\n" % maximum)
g.write("Total number of the reads is -> %d\n" % kolicina)
g.write("Standard deviation value of the length of the reads is -> %f\n" % float(std_dev))
g.close()
