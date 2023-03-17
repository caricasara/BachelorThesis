from Bio import SeqIO
import statistics
import gzip

ulazna_datoteka = input("Full path name of .fasta file: ")

length = []
for record in SeqIO.parse(ulazna_datoteka, "fasta"):
    length.append(len(record.seq))

zbroj = sum(length)
max_vrijednost = max(length)
min_vrijednost = min(length)
prosjek = zbroj / len(length)
medijan = statistics.median(length)
stdev = statistics.stdev(length)

izlazna_datoteka = input("Name the output .txt file: ")
f = open(izlazna_datoteka, "w")
f.write("Length in total is -> %d\n" % zbroj)
f.write("Maximum value of the length is -> %d\n" % max_vrijednost)
f.write("Minimum value of the length is -> %d\n" % min_vrijednost)
f.write("Average value of the length is -> %f\n" % float(prosjek))
f.write("Median value of the length is -> %d\n" % medijan)
f.write("Standard deviation value is -> %f\n" % float(stdev))
f.close()
