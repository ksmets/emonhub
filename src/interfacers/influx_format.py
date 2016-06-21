from influxdb.line_protocol import make_lines


def convert_cargo_to_influx_line_format(cargo):
    data = {}
    data['tags'] = {'nodeid': cargo.nodeid, 'nodename': cargo.nodename}
    points = []
    timestamp = int(cargo.timestamp * 1e9)
    for i, value in enumerate(cargo.realdata):
        if not cargo.enabled or cargo.enabled[i]:
            value = int(value) if isinstance(cargo.scales[i], int) else float(value)
            points.append({'measurement': cargo.names[i], 'fields': {'value': value}, 'time': timestamp})
    points.append({'measurement': 'rssi', 'fields': {'value': int(cargo.rssi)}, 'time': timestamp})
    data['points'] = points
    return make_lines(data)

