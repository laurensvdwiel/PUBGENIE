import subprocess
from html import escape

def gene_query(user_input, filename):
    command = f"head -1 {filename} && zgrep {user_input} {filename}"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()

    if error:
        print(f"Error: {error}")
        return f"Error: {escape(error.decode('utf-8'))}"

    lines = output.decode('utf-8').split('\n')
    headers = lines[0].split('\t')
    data_rows = [line.split('\t') for line in lines[1:] if line]

    table_html = '<h2><a href="https://www.nature.com/articles/s41586-020-2832-5" target="_blank">Kaplanis <i>et al.</i> Nature 2020</a></h2>'
    table_html += '<table>\n'
    table_html += '<tr>' + ''.join(f'<th>{escape(header)}</th>' for header in headers) + '</tr>\n'
    for row in data_rows:
        table_html += '<tr>' + ''.join(f'<td>{escape(cell)}</td>' for cell in row) + '</tr>\n'
    table_html += '</table>'

    return table_html