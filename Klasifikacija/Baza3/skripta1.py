from Bio import SeqIO

file = open("kraken.out", "r")
d_kraken = {}
unclassified = []
for line in file:
    if line.startswith("C"):
        id = line.split("\t")[1]
        oznaka_krakena = line.split("\t")[2].split("(")[0][:-1]
        taxid = line.split("\t")[2].split("(")[1].split(" ")[1][:-1]
        d_kraken[id] = [oznaka_krakena, taxid]
    elif line.startswith("U"):
        neklasificiran = line.split("\t")[1]
        if neklasificiran not in unclassified:
            unclassified.append(neklasificiran)
file.close()
#print(d_kraken)
#print(unclassified)
print("KLASIFICIRANI: ", len(d_kraken))
print("NEKLASIFICIRANI (FALSE NEGATIVE): ", len(unclassified))

d_fastq = {}
with open("rez95.fastq", "r") as f:
    for record in SeqIO.parse(f, "fastq"):
        id_reada = record.id
        opis = record.description.split(" ")[1].split(",")[0]
        if opis == 'BS.pilon.polished.v3.ST170922':
            d_fastq[id_reada] = [opis, "1423"]
        elif opis == 'Enterococcus_faecalis_complete_genome':
            d_fastq[id_reada] = [opis, "1351"]
        elif opis == 'Escherichia_coli_chromosome':
            d_fastq[id_reada] = [opis, "562"]
        elif opis == 'Lactobacillus_fermentum_complete_genome':
            d_fastq[id_reada] = [opis, "1613"]
        elif opis == 'Listeria_monocytogenes_complete_genome':
            d_fastq[id_reada] = [opis, "1639"]
        elif opis == 'Pseudomonas_aeruginosa_complete_genome':
            d_fastq[id_reada] = [opis, "287"]
        elif opis == 'Salmonella_enterica_chromosome':
            d_fastq[id_reada] = [opis, "28901"]
        elif opis == 'Staphylococcus_aureus_chromosome':
            d_fastq[id_reada] = [opis, "1280"]
        else:
            d_fastq[id_reada] = [opis, "?"]
f.close()
#print(d_fastq)
#print(len(d_fastq))

tocno = []
rod = []
krivo = []
taksonomija_iznad = []
for key, value in d_kraken.items():
    if d_fastq[key][1] == value[1]:
        tocno.append(key)
    elif d_fastq[key] == ['junk_seq', '?'] or d_fastq[key] == ['random_seq', '?']:
        krivo.append(key)
    elif d_fastq[key][0] == 'BS.pilon.polished.v3.ST170922':
        if value[1] in ['1386', '653685']:
            rod.append(key)
        elif value[1] in ['1239', '91061', '1385', '186817']:
            taksonomija_iznad.append(key)
    elif d_fastq[key][0] == 'Enterococcus_faecalis_complete_genome':
        if value[1] == '1350':
            rod.append(key)
        elif value[1] in ['1239', '91061', '186826', '81852']:
            taksonomija_iznad.append(key)
    elif d_fastq[key][0] == 'Escherichia_coli_chromosome':
        if value[1] in ['1224', '1236', '91347', '543']:
            taksonomija_iznad.append(key)
    elif d_fastq[key][0] == 'Lactobacillus_fermentum_complete_genome':
        if value[1] == '2742598':
            rod.append(key)
        elif value[1] in ['1239', '91061', '186826', '33958']:
            taksonomija_iznad.append(key)
    elif d_fastq[key][0] == 'Listeria_monocytogenes_complete_genome':
        if value[1] == '1637':
            rod.append(key)
        elif value[1] in ['1239', '91061', '1385', '186820']:
            taksonomija_iznad.append(key)
    elif d_fastq[key][0] == 'Pseudomonas_aeruginosa_complete_genome':
        if value[1] in ['286', '136841']:
            rod.append(key)
        elif value[1] in ['1224', '1236', '72274', '135621']:
            taksonomija_iznad.append(key)
    elif d_fastq[key][0] == 'Salmonella_enterica_chromosome':
        if value[1] == '590':
            rod.append(key)
        elif value[1] in ['1224', '1236', '91347', '543']:
            taksonomija_iznad.append(key)
    elif d_fastq[key][0] == 'Staphylococcus_aureus_chromosome':
        if value[1] == '1279':
            rod.append(key)
        elif value[1] in ['1239', '91061', '1385', '90964']:
            taksonomija_iznad.append(key)
print("TOČNO KLASIFICIRANE VRSTE (TRUE POSITIVE): ", len(tocno))
#print("TOČNI SOJEVI VRSTA: ", len(soj))
#print("TRUE POSITIVE -> TOČNI SOJEVI I VRSTE: ", len(tocno)+len(soj))
print("TOČAN ROD VRSTE: ", len(rod))
print("TOČNA TAKSONOMIJA KOLJENA, RAZREDA, REDA I PORODICE: ", len(taksonomija_iznad))
for t in tocno:
    del d_kraken[t]
#for s in soj:
    #del d_kraken[s]
for r in rod:
    del d_kraken[r]
for i in taksonomija_iznad:
    del d_kraken[i]
for k in krivo:
    del d_kraken[k]

for key, value in d_kraken.items():
    krivo.append(key)
print("FALSE POSITIVE (POGREŠNI): ", len(krivo))

