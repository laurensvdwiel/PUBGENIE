from pubgenie.domain.model.satterstrom_et_al_2020 import gene_query as satterstrom_gene_query
from pubgenie.domain.model.kaplanis_et_al_2020 import gene_query as kaplanis_gene_query
from pubgenie.domain.model.de_novo_db import gene_query as denovo_db_query

def execute_gene_query(user_input):
    # the return value of this function is a string of HTML
    table_html = ''

    # Query the Kaplanis de novo variants
    kaplanis_html = kaplanis_gene_query(user_input, '/data/41586_2020_2832_MOESM3_ESM.txt')
    table_html += kaplanis_html

    # Query the Satterstrom de novo variants
    satterstrom_html = satterstrom_gene_query(user_input, '/data/1-s2.0-S0092867419313984-mmc1.xlsx', 4)
    table_html += satterstrom_html

    # Query the de novo db
    denovo_db_html = denovo_db_query(user_input, '/data/denovo-db.non-ssc-samples.variants.tsv.gz')
    table_html += denovo_db_html

    return table_html
