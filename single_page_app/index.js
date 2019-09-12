function draw_points_on_map(longitudes, latitudes, names) {
    let data = [{
        type: 'scattermapbox',
        lat: latitudes,
        lon: longitudes,
        mode: 'markers',
        marker: {
            size: 15
        },
        text: names
    }];

    let layout = {
        autosize: true,
        hovermode: 'closest',
        mapbox: {
            bearing: 0,
            center: {
                lat: 49.25,
                lon: -123.133333
            },
            pitch: 0,
            zoom: 12
        },
    };

    Plotly.setPlotConfig({
        mapboxAccessToken: 'pk.eyJ1IjoidGNoYW5iYyIsImEiOiJjazBnNnlvYzQwNGhzM2JzMTQ5cWY4MGphIn0.aJM_vtB9yDD7LIz0Hl_Obw'
    });

    Plotly.plot('mapDiv', data, layout);
}

function parse_data(data) {
    // If the API returned multiple points I would be parsing them as an Array
    let location = data.location;
    let longitudes = [location[0]];
    let latitudes = [location[1]];
    let names = [data.name];
    draw_points_on_map(longitudes, latitudes, names)
}

function query_poi() {
    $.get('http://ce-env.fxrhvmyt8y.us-west-2.elasticbeanstalk.com/api/').done(function (data) {
        parse_data(data)
    });
}

$(function () {
    query_poi();
});