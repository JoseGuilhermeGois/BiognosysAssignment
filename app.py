"""Biognosys interview assignment"""

from flask import Flask, jsonify, render_template

from utils.file_handler import read_file_path
from utils.json_utils import convert_to_json_format
from utils.data_processing import get_proteins_per_sample, get_peptides_per_sample, apply_welch_test


app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    """Check if the app is running."""
    return render_template('index.html', port=port_value)


@app.route('/proteins-per-sample', methods=['GET'])
def proteins_per_sample():
    """1st endpoint to return aggregated number of proteins per sample."""
    proteins_per_sample_values = get_proteins_per_sample(data)
    return jsonify(convert_to_json_format(proteins_per_sample_values))


@app.route('/peptides-per-sample', methods=['GET'])
def peptides_per_sample():
    """2nd endpoint to return aggregated number of peptides per sample."""
    peptides_per_sample_values = get_peptides_per_sample(data)
    return jsonify(convert_to_json_format(peptides_per_sample_values))


@app.route('/statistical-test', methods=['GET'])
def statistical_test():
    """3rd endpoint to perform a statistical test (Welch's t-test)."""
    t_statistic, p_value = apply_welch_test(data)
    return jsonify({
        't_statistic': t_statistic,
        'p_value': p_value
    })


if __name__ == '__main__':
    data = read_file_path()
    port_value = 8080
    app.run(debug=True, port=port_value)
