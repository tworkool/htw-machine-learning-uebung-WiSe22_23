import IPython
import numpy as np

str_style = '''
<style>
table {
  border-collapse: collapse;
}

td {
  border: 3px solid #666666;
  min-width:30px;
  height: 30px;
  position: relative; 
  text-align:center; 
  color: #474747;
  font-size:20px;
  font-weight: bolder;
  padding: 19px;
}

.up{
  position: absolute; 
  right: 0;
  top: 0;
  background: white;
  text-align: right;
  font-size: 16px;
  font-family: Courier;
  font-weight: bolder;
  color: blue;
  opacity: 1.0;
  background-color:rgba(0, 0, 0, 0.0);
}

.down{
  position: absolute; 
  right: 0;
  bottom: 0;
  background: white;
  text-align: right;
  font-size: 16px;
  font-family: Courier;
  font-weight: bolder;
  color: red;
  opacity: 0.9;
  background-color:rgba(0, 0, 0, 0.0);
}
</style>
'''

# background-color:rgba(0, 0, 0, 0.0);


""" def write_html(html_content):
    _html = html_content
    with open('html_file.html', 'w+') as f:
        f.write(_html) """


def enclose_element(element, idx_up, idx_down):
    return ('\t<td>' + str(element) + '<span class="up">'
                     + str(idx_up) + '</span><span class="down">'
                     + str(idx_down) + '</span></td>')


def horizontal_tbl(array, color):
    result = '<table bgcolor="' + color + '"><tr>\n'
    max_count = len(array)
    for idx, e in enumerate(array):
        result += enclose_element(e, idx, idx - max_count) + '\n'
    result += '</tr></table>\n'
    return result


def vertical_tbl(array, color):
    result = '<table bgcolor="' + color + '">\n'
    max_count = len(array)
    for idx, e in enumerate(array):
        result += '<tr>' + enclose_element(e, idx, idx - max_count) + '</tr>\n'
    result += '</table>\n'
    return result


def recursive_tbl(array, parity, max_levels, level=0, color_A=[150, 200, 255], color_B=[75, 100, 170]):
    if len(array.shape) == 1:
        return horizontal_tbl(array, "".join(["%02x" % int(c) for c in color_A]))
    mix = np.array(color_A) * (level/max_levels) + \
        np.array(color_B) * (1.0 - level/max_levels)
    color = "".join(["%02x" % int(c) for c in mix])
    if parity:
        return horizontal_tbl([recursive_tbl(x, not parity, max_levels, level+1, color_A, color_B) for x in array], color)
    else:
        return vertical_tbl([recursive_tbl(x, not parity, max_levels, level+1, color_A, color_B) for x in array], color)


def array_to_html(array):
    return str_style + recursive_tbl(array, len(array.shape) % 2, len(array.shape)-1)


def visualize_array(array):
    array_str = array_to_html(array)
    html = IPython.display.HTML(array_str).data
    with open('html_file.html', 'w+') as f:
        f.write(html)


str_style_bigtbl = '''
<style>
.bigtable {
  border-collapse: collapse;
}

.bigtd {
  border: 3px solid #ffd4d3ff;
  min-width:30px;
  height: 30px;
  position: relative; 
  text-align:center; 
  color: #474747;
  font-size:20px;
  font-weight: bolder;
  padding: 19px;
}

</style>
'''


def envelope_tbl(lst):
    result = '<table class="bigtable">\n'
    for row in lst:
        result += '<tr>\n\t'
        for e in row:
            if isinstance(e, dict):
                result += '<td class="bigtd" '
                for key in e:
                    if key != 'text':
                        result += str(key) + '="' + str(e[key]) + '" '
                result += '>' + str(e['text']) + '</td>'
            else:
                result += '<td class="bigtd">' + str(e) + '</td>'
        result += '\n</tr>\n'
    result += '</table>'
    return result


def draw_tbl(lst):
    result = envelope_tbl(lst)
    html = IPython.display.HTML(str_style_bigtbl + result).data
    with open('html_file.html', 'w+') as f:
        f.write(html)


def how_broadcast(a, b):
    x, y = np.broadcast_arrays(a, b)
    draw_tbl([[{'text': 'ORIGINAL ARRAYS', 'colspan': 2}],
              [array_to_html(a), array_to_html(b)],
              [{'text': 'BROADCASTED', 'colspan': 2}],
              [array_to_html(x), array_to_html(y)]])
