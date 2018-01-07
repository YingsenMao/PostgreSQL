var svg = d3.select("svg"),
margin = {top: 20, right: 20, bottom: 30, left: 50},
width = +svg.attr("width") - margin.left - margin.right,
height = +svg.attr("height") - margin.top - margin.bottom,
g = svg.append("g").attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var parseTime = d3.timeParse("%Y");

var x = d3.scaleTime()
    .rangeRound([0, width]);

var y = d3.scaleLinear()
    .rangeRound([height, 0]);

var line = d3.line()
    .x(function(d) { return x(d.year); })
    .y(function(d) { return y(d.total); });

var slider = document.getElementById("myRange");
var output = document.getElementById("demo");

var searchRequest = null;
var lrRequest = null;

$(document).ready(function() {
    var minlength = 2;
    $('#your_name').keyup(function() {
        value = $(this).val();

        if (value.length >= minlength ) {
            if (searchRequest != null) {
                searchRequest.abort();
            }        
            searchRequest = $.ajax({
                url: 'api/' + value + '/' + $("#myRange").val(),
                type: "GET",
                dataType : "json",
                })
                .done(function( json ) {
                    var post_data = json;
                    drawChart(post_data);
            })
        }    
    });

    $('#myRange').on('input', function() {
        value = $(this).val();

        if (lrRequest != null) {
            lrRequest.abort();
        }    

        lrRequest = $.ajax({
                url: 'api/' + $('#your_name').val() + '/' + value,
                type: "GET",
                dataType : "json",
                })
                .done(function( json ) {
                    var cof = json["coeff"];
                    document.getElementById("coef").innerHTML = cof;
            })   
    });
});


output.innerHTML = slider.value;

slider.oninput = function() {
  output.innerHTML = this.value;
}


function drawChart(dt){
    coef = dt["coeff"];
    data = dt["data"];

    document.getElementById("coef").innerHTML = coef;

    for(var i = 0; i < data.length; i++) {
        data[i]['year'] = parseTime(data[i]['year']);
    }

    d3.selectAll("g > *").remove();

    x.domain(d3.extent(data, function(d) { return d.year; }));
    y.domain(d3.extent(data, function(d) { return d.total; }));

    g.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));

    g.append("g")
        .call(d3.axisLeft(y))
        .append("text")
        .attr("fill", "#000")
        .attr("transform", "rotate(-90)")
        .attr("y", 6)
        .attr("dy", "0.71em")
        .attr("text-anchor", "end")
        .text("Number");

    g.append("path")
        .datum(data)
        .attr("fill", "none")
        .attr("stroke", "steelblue")
        .attr("stroke-linejoin", "round")
        .attr("stroke-linecap", "round")
        .attr("stroke-width", 1.5)
        .attr("d", line);
}

