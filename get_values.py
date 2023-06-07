import csv

def process():
    names = ["H2B_sequence", "H2A_sequence", "H3_sequence", "H4_sequence"]
    namesfiles = ["c.elegans", "ciliate", "drosophila", "e.coli",
                  "human", "methanocaldococcus", "mouse",
                  "thermococcus", "tuberculosis", "yeast", "zebrafish"]
    
    # Create a CSV file
    with open('results.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write the header row with namesfiles as column names
        writer.writerow([""] + namesfiles)
        
        # Iterate over each name
        for name in names:
            row_data = []
            row_data.append(name)
            
            # Iterate over each filename
            for filename in namesfiles:
                with open("{name}.{filename}.blast".format(name=name, filename=filename)) as file:
                    for i, line in enumerate(file):
                        if i == 5:
                            splitted = line.split("\t")
                            row_data.append(splitted[-2])
                            break
            
            # Write the row to the CSV file
            writer.writerow(row_data)

# Call the process function
process()
