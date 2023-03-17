lista = ["bacillus_subtilis_chimeric.txt", "cryptococcus_neoformans_chimeric.txt", "enterococcus_faecalis_chimeric.txt", "escherichia_coli_chimeric.txt", "lactobacillus_fermentum_chimeric.txt", "listeria_monocytogenes_chimeric.txt", "pseudomonas_aeruginosa_chimeric.txt", "saccharomyces_cerevisiae_chimeric.txt", "salmonella_enterica_chimeric.txt", "staphylococcus_aureus_chimeric.txt"]

f = open("all.txt", "w")
for element in lista:
    f.write("%s\n" % element)
    g = open(element, "r")
    procitano = g.readlines()
    for line in procitano:
        f.write("%s" % line)
    f.write("\n")
    g.close()
f.close()
