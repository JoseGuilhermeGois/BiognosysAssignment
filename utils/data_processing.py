from pandas import DataFrame
from scipy.stats import ttest_ind


def get_number_of_proteins_per_row(protein_accesions: str) -> int:
    """Count the number of protein accessions split by ';'."""
    return len(protein_accesions.split(";"))


def get_proteins_per_sample(data: DataFrame) -> DataFrame:
    """Get number of proteins per sample."""
    number_of_proteins_per_sample = lambda x: x.apply(get_number_of_proteins_per_row).sum()
    result = data.groupby("R.FileName")['PG.ProteinAccessions'].apply(number_of_proteins_per_sample).reset_index()
    
    return result[["R.FileName", "PG.ProteinAccessions"]].sort_values(by="PG.ProteinAccessions", ascending=False)


def get_peptides_per_sample(data: DataFrame) -> DataFrame:
    """Get number of peptides per sample."""
    return data.groupby('R.FileName')['PEP.GroupingKey'].nunique().reset_index()


def apply_welch_test(data: DataFrame) -> set:
    """Serform statistical test (Welch's t-test) comparing two groups of data."""
    # create the two groups based on the presence of 'NewCol' in the R.FileName column
    newcol_group = data[data['R.FileName'].str.contains('NewCol')]
    nonewcol_group = data[~data['R.FileName'].str.contains('NewCol')]
    # perform the Welch's t-test using 'ttest_ind' function from the 'scipy.stats' library
    # 'equal_var = False' to perfrom the Welch's test, which does not assume equal population variance
    return ttest_ind(newcol_group['EG.TargetQuantity (Settings)'],
                     nonewcol_group['EG.TargetQuantity (Settings)'],
                     equal_var=False)
