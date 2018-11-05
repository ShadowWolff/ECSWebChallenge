function createPieGraph( data, id, container, type = "percent" ) {
    nv.addGraph(function() {
      width = $("." + container).width();
      height =$("." + container).height();

      var chart = nv.models.pieChart()
          .x(function(d) { return d.label })
          .y(function(d) { return d.value })
          .showLabels(true)
          .width(width).height(height);

      if(type != "number")
          chart.labelType("percent");
      else
          chart.labelType("value");

      d3.select("#"+id)
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

function createChartGraph( data, date_display, chart_id, container, display_date=true )
{
    nv.addGraph(function () {
        width = $("." + container).width();
        height = 0.5 * width;

        var chart = nv.models.lineChart()
            .useInteractiveGuideline(true)
            .margin({left: 100})
            .duration(350)
            .showLegend(true)
            .showYAxis(true)
            .showXAxis(true)
            .width(width-40).height(height);

        if(display_date) {
            chart.xAxis     //Chart x-axis settings
                .axisLabel('Day')
                .tickFormat(function (d) {
                    return d3.time.format(date_display)(new Date(d))
                });
        }else{
          chart.xAxis     //Chart x-axis settings
              .axisLabel('Hour')
              .tickFormat(d3.format(',r'));
        }

          chart.yAxis     //Chart y-axis settings
              .axisLabel('Routes')
              .tickFormat(d3.format('.0f'));


        d3.select('#'+chart_id)
            .datum(data)
            .attr('preserveAspectRatio','xMinYMin')
            .attr('viewBox','0 0 '+width+' '+height)
            .call(chart)

        //Update the chart when window resizes.
        nv.utils.windowResize(chart.update());
        return chart;
    });
}