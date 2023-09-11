### Read in the avocado data

# Read tab-delimited data
import pandas as pd
avocado = pd.read_csv('data/avocado.csv', sep='\t')

# Subset large DataFrame to include only relevant columns
subset_columns = [ 'code', 'lc', 'product_name_en', 'quantity', 'serving_size', 'packaging_tags', 'brands', 'brands_tags', 'categories_tags', 'labels_tags', 'countries', 'countries_tags', 'origins','origins_tags']
avocado = avocado[subset_columns]

# Gather relevant categories data for avocados
with open("data/relevant_avocado_categories.txt", "r") as file:
    relevant_avocado_categories = file.read().splitlines()
    file.close()
    
### Filter avocado data using relevant category tags

# Turn a column of comma-separated tags into a column of lists
avocado['categories_list'] = avocado['categories_tags'].str.split(',')

# Drop rows with null values in a particular column
avocado = avocado.dropna(subset = 'categories_list')

# Filter a DataFrame based on a column of lists
avocado = avocado[avocado['categories_list'].apply(lambda x: any([i for i in x if i in relevant_avocado_categories]))]

### Where do most avocados come from?

# Filter DataFrame for UK data
avocados_uk = avocado[(avocado['countries']=='United Kingdom')]

# Find most common country for avocado origin
avocado_origin = (avocados_uk['origins_tags'].value_counts().index[0])
avocado_origin = avocado_origin.lstrip("en:")


### Create a general function to read and filter data for a particular ingredient, 
###    and return the top origin country for that food item

def read_and_filter_data(filename, relevant_categories):
  df = pd.read_csv('data/' + filename, sep='\t')
  
  # Subset large DataFrame to include only relevant columns
  subset_columns = [ 'code', 'lc', 'product_name_en', 'quantity', 'serving_size', 'packaging_tags', 'brands', 'brands_tags', 'categories_tags', 'labels_tags', 'countries', 'countries_tags', 'origins','origins_tags']
  df = df[subset_columns]

  # Split tags into lists
  df['categories_list'] = df['categories_tags'].str.split(',')

  # Drop rows with null categories data
  df = df.dropna(subset = 'categories_list')

  # Filter data for relevant categories
  df = df[df['categories_list'].apply(lambda x: any([i for i in x if i in relevant_categories]))]
    
  # Filter data for the UK
  df_uk = df[(df['countries']=='United Kingdom')]

  # Find top origin country string with the highest count
  top_origin_string = (df_uk['origins_tags'].value_counts().index[0])

  # Clean up top origin country string
  top_origin_country = top_origin_string.lstrip("en:")
  top_origin_country = top_origin_country.replace('-', ' ')

  print(f'**{filename[:-4]} origins**','\n', top_origin_country, '\n')

  print ("Top origin country: ", top_origin_country)
  print ("\n")

  # End of function - return top origin country for this ingredient
  return top_origin_country


# Analyze avocado origins again, this time by calling function
top_avocado_origin = read_and_filter_data('avocado.csv',relevant_avocado_categories)

### Repeat process above with new function for the other 2 ingredients

# Gather relevant categories data for olive oil
with open("data/relevant_olive_oil_categories.txt", "r") as file:
    relevant_olive_oil_categories = file.read().splitlines()
    file.close()

# Call user-defined function on olive_oil.csv
top_olive_oil_origin = read_and_filter_data('olive_oil.csv',relevant_olive_oil_categories)

# Gather relevant categories data for sourdough
with open("data/relevant_sourdough_categories.txt", "r") as file:
    relevant_sourdough_categories = file.read().splitlines()
    file.close()

# Call user-defined function on sourdough.csv
top_sourdough_origin = read_and_filter_data('sourdough.csv',relevant_sourdough_categories)

