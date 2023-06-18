from Bio import SeqIO

file = open("newkraken.out", "r")
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

ukupni_rijecnik = {}
with open("zymo_binned_bacillus_subtilis.fastq", "r") as f:
    for record in SeqIO.parse(f, "fastq"):
        ukupni_rijecnik[record.id] = ["Bacillus subtilis", "1423"]
f.close()
with open("zymo_binned_enterococcus_faecalis.fastq", "r") as f:
    for record in SeqIO.parse(f, "fastq"):
        ukupni_rijecnik[record.id] = ["Enterococcus faecalis", "1351"]
f.close()
with open("zymo_binned_escherichia_coli.fastq", "r") as f:
    for record in SeqIO.parse(f, "fastq"):
        ukupni_rijecnik[record.id] = ["Escherichia coli", "562"]
f.close()
with open("zymo_binned_lactobacillus_fermentum.fastq", "r") as f:
    for record in SeqIO.parse(f, "fastq"):
        ukupni_rijecnik[record.id] = ["Lactobacillus fermentum", "1613"]
f.close()
with open("zymo_binned_listeria_monocytogenes.fastq", "r") as f:
    for record in SeqIO.parse(f, "fastq"):
        ukupni_rijecnik[record.id] = ["Listeria monocytogenes", "1639"]
f.close()
with open("zymo_binned_pseudomonas_aeruginosa.fastq", "r") as f:
    for record in SeqIO.parse(f, "fastq"):
        ukupni_rijecnik[record.id] = ["Pseudomonas aeruginosa", "287"]
f.close()
with open("zymo_binned_salmonella_enterica.fastq", "r") as f:
    for record in SeqIO.parse(f, "fastq"):
        ukupni_rijecnik[record.id] = ["Salmonella enterica", "28901"]
f.close()
with open("zymo_binned_staphylococcus_aureus.fastq", "r") as f:
    for record in SeqIO.parse(f, "fastq"):
        ukupni_rijecnik[record.id] = ["Staphylococcus aureus", "1280"]
f.close()

d_fastq = {}
with open("zymo_binned_all.fastq", "r") as f:
    for record in SeqIO.parse(f, "fastq"):
        id_reada = record.id
        if id_reada in ukupni_rijecnik:
            d_fastq[id_reada] = ukupni_rijecnik[id_reada]
        else:
            print("Tu sam")
            d_fastq[id_reada] = ["Error", "?"]
f.close()

tocno = []
rod = []
krivo = []
taksonomija_iznad = []
for key, value in d_kraken.items():
    if d_fastq[key][1] == value[1]:
        tocno.append(key)
    elif d_fastq[key][1] == '?':
        krivo.append(key)
    elif d_fastq[key][0] == 'Bacillus subtilis':
        if value[1] in ['1386', '653685']:
            rod.append(key)
        elif value[1] in ['1239', '91061', '1385', '186817']:
            taksonomija_iznad.append(key)
    elif d_fastq[key][0] == 'Enterococcus faecalis':
        if value[1] == '1350':
            rod.append(key)
        elif value[1] in ['1239', '91061', '186826', '81852']:
            taksonomija_iznad.append(key)
    elif d_fastq[key][0] == 'Escherichia coli':
        if value[1] == '561':
            rod.append(key)
        elif value[1] in ['1224', '1236', '91347', '543']:
            taksonomija_iznad.append(key)
    elif d_fastq[key][0] == 'Lactobacillus fermentum':
        if value[1] == '2742598':
            rod.append(key)
        elif value[1] in ['1239', '91061', '186826', '33958']:
            taksonomija_iznad.append(key)
    elif d_fastq[key][0] == 'Listeria monocytogenes':
        if value[1] == '1637':
            rod.append(key)
        elif value[1] in ['1239', '91061', '1385', '186820']:
            taksonomija_iznad.append(key)
    elif d_fastq[key][0] == 'Pseudomonas aeruginosa':
        if value[1] in ['286', '136841']:
            rod.append(key)
        elif value[1] in ['1224', '1236', '72274', '135621']:
            taksonomija_iznad.append(key)
    elif d_fastq[key][0] == 'Salmonella enterica':
        if value[1] == '590':
            rod.append(key)
        elif value[1] in ['1224', '1236', '91347', '543']:
            taksonomija_iznad.append(key)
    elif d_fastq[key][0] == 'Staphylococcus aureus':
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
print(len(krivo))
for k in krivo:
    del d_kraken[k]
print(len(d_kraken))
for key, value in d_kraken.items():
    krivo.append(key)
print("FALSE POSITIVE (POGREŠNI): ", len(krivo))
