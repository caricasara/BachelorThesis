from Bio import SeqIO
import gzip

duljina = 0
referenca = input("Full path name of reference .fasta file: ")

for record in SeqIO.parse(referenca, "fasta"):
    duljina = len(record.seq)

zbroj = 0
read = input("Full path name of read .fastq.gz file: ")

with gzip.open(read, "rt") as f:
    for record in SeqIO.parse(f, "fastq"):
        zbroj += len(record.seq)
f.close()

izlazna_datoteka = input("Name the output .txt file: ")
g = open(izlazna_datoteka, "w")
g.write("Length of the reference sequence is -> %d\n" % duljina)
g.write("Length of the combined sequence of the reads is -> %d\n" % zbroj)
g.write("Coverage is -> %f" % (float(zbroj) / duljina))
g.close()
