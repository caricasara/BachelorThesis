from Bio import SeqIO

ulazna_datoteka = input("Full path name of .fasta file: ")
list_of_records = []
prvi_kvartil = int(input("Write the number of the first quartile: "))
for record in SeqIO.parse(ulazna_datoteka, "fasta"):
    if len(record.seq) < prvi_kvartil:
        list_of_records.append(record)

##prosjek = int(input("Write the average number: "))
##prvi_kvartil = int(input("Write the number of the first quartile: "))
##read = input("Full path name of read .fasta file: ")
##manji_od_prosjeka = []
##manji_od_prvog_kvartila = []
##with open(read, "rt") as f:
##    for record in SeqIO.parse(f, "fasta"):
##        if len(record.seq) < prosjek:
##            manji_od_prosjeka.append(len(record.seq))
##        if len(record.seq) < prvi_kvartil:
##            manji_od_prvog_kvartila.append(len(record.seq))
##f.close()
##print(len(manji_od_prosjeka))
##print(len(manji_od_prvog_kvartila))

print(len(list_of_records))

izlazna_datoteka = input("Full path name of .txt file: ")
with open(izlazna_datoteka, "w") as output_handle:
    SeqIO.write(list_of_records, output_handle, "fasta")

