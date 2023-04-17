import * as d3 from "d3";
import DotPlot from "./dotPlot";
import { calculatedPercents } from "./dotPlotData";
import Legend from "./legend";

const viewWidth = document.documentElement.clientWidth;

let legend = Legend(
  d3.scaleOrdinal(
    [
      "<10",
      "10-19",
      "20-29",
      "30-39",
      "40-49",
      "50-59",
      "60-69",
      "70-79",
      "≥80",
    ],
    d3.schemeSpectral[10]
  ),
  {
    title: "Age (years)",
    tickSize: 0,
  }
);

let chart = DotPlot(calculatedPercents, {
  x: (d) => d.population,
  y: (d) => d.name,
  z: (d) => d.age,
  xFormat: "%",
  xLabel: "Sample Size →",
  width: viewWidth,
  marginLeft: 360,
  marginRight: 100,
});

const containerDiv = document.querySelector(".visualization");
const legendContainer = document.querySelector(".legendContainer");
legendContainer.appendChild(legend);
legendContainer.style.marginBottom = "20px";
containerDiv.appendChild(chart);
