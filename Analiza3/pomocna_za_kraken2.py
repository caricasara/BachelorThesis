from Bio import SeqIO

referenca = "jedna_fali.fasta"
pom = []
#fali "edited_escherichia_coli.fasta" u lista
lista = ["edited_bacillus_subtilis_complete_genome.fasta", "edited_enterococcus_faecalis_complete_genome.fasta", "edited_lactobacillus_fermentum_complete_genome.fasta", "edited_listeria_monocytogenes_complete_genome.fasta", "edited_pseudomonas_aeruginosa_complete_genome.fasta", "edited_salmonella_enterica_complete_genome.fasta", "edited_staphylococcus_aureus_complete_genome.fasta"]
for l in lista:
    for record in SeqIO.parse(l, "fasta"):
        pom.append(record.id)
        pom.append(record.seq)

final = []
for x in range(0, 2, 2):
    y = SeqIO.SeqRecord(seq=pom[x+1], id=pom[x]+"|kraken:taxid|1423", description='')
    final.append(y)
for x in range(2, 4, 2):
    y = SeqIO.SeqRecord(seq=pom[x+1], id=pom[x]+"|kraken:taxid|1351", description='')
    final.append(y)
#for x in range(4, 6, 2):
    #y = SeqIO.SeqRecord(seq=pom[x+1], id=pom[x]+"|kraken:taxid|562", description='')
    #final.append(y)
for x in range(4, 6, 2):
    y = SeqIO.SeqRecord(seq=pom[x+1], id=pom[x]+"|kraken:taxid|1613", description='')
    final.append(y)
for x in range(6, 8, 2):
    y = SeqIO.SeqRecord(seq=pom[x+1], id=pom[x]+"|kraken:taxid|1639", description='')
    final.append(y)
for x in range(8, 10, 2):
    y = SeqIO.SeqRecord(seq=pom[x+1], id=pom[x]+"|kraken:taxid|287", description='')
    final.append(y)
for x in range(10, 12, 2):
    y = SeqIO.SeqRecord(seq=pom[x+1], id=pom[x]+"|kraken:taxid|28901", description='')
    final.append(y)
for x in range(12, 14, 2):
    y = SeqIO.SeqRecord(seq=pom[x+1], id=pom[x]+"|kraken:taxid|1280", description='')
    final.append(y)
SeqIO.write(final, referenca, "fasta")
