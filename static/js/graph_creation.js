function createPieGraph( data ) {
    nv.addGraph(function() {
      width = $(".pie_graph_container").width();
      height =$(".pie_graph_container").height();

      var chart = nv.models.pieChart()
          .x(function(d) { return d.label })
          .y(function(d) { return d.value })
          .showLabels(true)
          .labelType("percent")
          .donut(true)
          .width(width).height(height);

      d3.select("#pie_graph")
        .attr("width", "400px")
        .attr("height", "400px")
        .attr('viewBox','0 0 '+width+' '+height)
        .attr('preserveAspectRatio','xMinYMin')
        .datum(data)
        .transition().duration(350)
        .call(chart);

      return chart;
    });
}

function createChartGraph( data, date_display )
{
    nv.addGraph(function () {
        width = $(".chart_graph_container").width();
        height = 0.5 * width;

        var chart = nv.models.lineChart()
            .useInteractiveGuideline(true)
            .margin({left: 100})
            .duration(350)
            .showLegend(true)
            .showYAxis(true)
            .showXAxis(true)
            .width(width-40).height(height);

        chart.xAxis     //Chart x-axis settings
              .axisLabel('Day')
              .tickFormat(function(d) {
                return d3.time.format(date_display)(new Date(d))
              });

          chart.yAxis     //Chart y-axis settings
              .axisLabel('Routes')
              .tickFormat(d3.format('.0f'));


        d3.select('#chart_graph')
            .datum(data)
            .attr('preserveAspectRatio','xMinYMin')
            .attr('viewBox','0 0 '+width+' '+height)
            .call(chart)

        //Update the chart when window resizes.
        nv.utils.windowResize(chart.update());
        return chart;
    });
}