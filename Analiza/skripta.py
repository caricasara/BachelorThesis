from Bio import SeqIO
import statistics
import gzip

duljina = 0
referenca = "references/Pseudomonas_aeruginosa_complete_genome.fasta"

for record in SeqIO.parse(referenca, "fasta"):
    duljina = len(record.seq)

read = "zymo_binned_pseudomonas_aeruginosa.fastq.gz"

length = []
with gzip.open(read, "rt") as f:
    for record in SeqIO.parse(f, "fastq"):
        length.append(len(record.seq))
f.close()

zbroj = sum(length)
max_vrijednost = max(length)
min_vrijednost = min(length)
prosjek = zbroj / len(length)
medijan = statistics.median(length)
stdev = statistics.stdev(length)

izlazna_datoteka = "Pseudomonas_aeruginosa.txt"
g = open(izlazna_datoteka, "w")
g.write("Length of the reference sequence is -> %d\n" % duljina)
g.write("Length of the combined sequence of the reads is -> %d\n" % zbroj)
g.write("Coverage is -> %f\n" % (float(zbroj) / duljina))
g.write("Maximum value of the length of the reads is -> %d\n" % max_vrijednost)
g.write("Minimum value of the length of the reads is -> %d\n" % min_vrijednost)
g.write("Average value of the length of the reads is -> %f\n" % float(prosjek))
g.write("Median value of the length of the reads is -> %d\n" % medijan)
g.write("Standard deviation value of the length of the reads is -> %f\n" % float(stdev))
g.close()
