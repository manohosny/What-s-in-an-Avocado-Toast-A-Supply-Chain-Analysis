# Avocado Data Analysis README

## Overview
This project provides a Python script to analyze the origins of various food items, starting with avocados. The main goal is to determine the top origin country for a given food item in the UK. The script is modular and can be adapted to analyze other food items as well.

## Dependencies
- Python 3.x
- pandas

## Dataset
The data is expected to be in tab-delimited CSV format with the following columns:
- code
- lc
- product_name_en
- quantity
- serving_size
- packaging_tags
- brands
- brands_tags
- categories_tags
- labels_tags
- countries
- countries_tags
- origins
- origins_tags

The dataset should be placed in a folder named `data` in the root directory of the project.

## Usage

1. Place your data files (e.g., `avocado.csv`, `olive_oil.csv`, `sourdough.csv`) in the `data` directory.
2. For each food item, create a text file (e.g., `relevant_avocado_categories.txt`, `relevant_olive_oil_categories.txt`, `relevant_sourdough_categories.txt`) in the `data` directory containing the relevant category tags, one per line.
3. Run the script. The script will:
   - Read the data.
   - Filter the data based on the relevant category tags.
   - Determine the top origin country for the food item in the UK.
   - Print the results.

## Functions

- `read_and_filter_data(filename, relevant_categories)`: This function reads and filters data for a particular ingredient and returns the top origin country for that food item in the UK.

## Example

After running the script, you might get output similar to:

```
**avocado origins** 
 Mexico 

Top origin country:  Mexico

**olive_oil origins** 
 Spain 

Top origin country:  Spain

**sourdough origins** 
 France 

Top origin country:  France
```

## Future Improvements

- Extend the script to analyze data from other countries, not just the UK.
- Visualize the data using graphs and charts.
- Integrate with a database for more efficient data storage and retrieval.

## Contributing

If you'd like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
