# Sales ETL Pipeline

"Sales ETL Pipeline" is a comprehensive data processing system that extracts, transforms, and loads data from a single CSV file. The system prepares the data for a relational database by performing several transformations, ensuring the data is clean, well-structured, and ready for analysis. In addition to the ETL process, the project includes a sentiment analysis module that analyzes customer reviews, providing insights into customer sentiment. The transformed and analyzed data is then inserted into a relational database, enabling efficient querying and analysis of the data. This project demonstrates the practical application of ETL pipelines and sentiment analysis in data preparation for a relational database.

## Motivation

"Sales ETL Pipeline", stems from a desire to gain hands-on experience with ETL pipeline stages and relational databases. This project offers an opportunity to apply these skills in a real-world scenario, extracting data from a CSV file, transforming it, and loading it into a relational database. The ability to load this data into a relational database provides easy access to the data for future use, which is a key aspect of data management. This project serves as a platform for me to apply and expand my knowledge in ETL pipeline stages and relational databases, providing me with a comprehensive understanding of these key aspects of data management.

## 🚀 Quick Start

### 1) Download source data file [amazon.csv](https://www.kaggle.com/datasets/karkavelrajaj/amazon-sales-dataset)
### 2) Install required packages to run the files.

```bash
pip install -r requirements.txt
```

### 3) Adjust connection parameters in [db_tasks.py](https://github.com/yasarsultan/salesETL/blob/main/db_tasks.py) file.

### 4) Run the [etl.py](https://github.com/yasarsultan/salesETL/blob/main/etl.py) file.

```bash
python3 etl.py
```
