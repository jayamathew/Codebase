# Renaming the output file to include date to prevent overwriting output from a pipeline

output_filename = 'filename.csv'
print(output_filename)
dt = str(time.strftime("%m_%d_%Y"))
print(dt)
output_filename = 'filename_' + dt + '.csv'
print(output_filename)

# Write output to a file
final.to_csv(output_filename, index=False)

