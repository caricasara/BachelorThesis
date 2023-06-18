from Bio import SeqIO

referenca = input("Full path name of reference .fasta file: ")
lista = []
for record in SeqIO.parse(referenca, "fasta"):
    if "chromosome" in record.id:
        lista.append(record.id)
        lista.append(record.seq)

dubina = input("Input depth=")
opis = "depth=" + dubina + " circular=true"

filename = input("Full path name of edited reference .fasta file: ")
nova = []
for j in range(0, len(lista), 2):
    zapis = SeqIO.SeqRecord(seq=lista[j+1], id=lista[j], description=opis)
    nova.append(zapis)
SeqIO.write(nova, filename, "fasta")
