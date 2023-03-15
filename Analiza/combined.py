lista = ["Bacillus_subtilis.txt", "Cryptococcus_neoformans.txt", "Enterococcus_faecalis.txt", "Escherichia_coli.txt", "Lactobacillus_fermentum.txt", "Listeria_monocytogenes.txt", "Pseudomonas_aeruginosa.txt", "Saccharomyces_cerevisiae.txt", "Salmonella_enterica.txt", "Staphylococcus_aureus.txt"]

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
