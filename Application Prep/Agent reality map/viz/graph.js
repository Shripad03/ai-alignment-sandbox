const svg = d3.select("#svg");
const detail = document.getElementById("detail");
const fileInput = document.getElementById("file");

fileInput.addEventListener("change", async (e) => {
  const file = e.target.files[0];
  const text = await file.text();
  const lines = text.trim().split("\n").map(JSON.parse);

  // build nodes/links in step order
  const nodes = lines.map(d => ({
    id: String(d.step),
    label: `#${d.step}`,
    raw: d
  }));
  const links = lines.slice(1).map((d, i) => ({
    source: String(i+1),
    target: String(i+2)
  }));

  render(nodes, links);
});

function render(nodes, links) {
  svg.selectAll("*").remove();
  const width = +svg.attr("width") || 900;
  const height = +svg.attr("height") || 520;

  const simulation = d3.forceSimulation(nodes)
    .force("link", d3.forceLink(links).id(d => d.id).distance(120))
    .force("charge", d3.forceManyBody().strength(-300))
    .force("center", d3.forceCenter(width/2, height/2));

  const link = svg.append("g").attr("stroke-width", 1.5)
    .selectAll("line").data(links).enter().append("line")
    .attr("class", "link");

  const node = svg.append("g").selectAll("g").data(nodes).enter().append("g")
    .attr("class", "node")
    .on("click", (_, d) => detail.textContent = JSON.stringify(d.raw, null, 2));

  node.append("circle").attr("r", 16);
  node.append("text").text(d => d.label).attr("dy", 2);

  simulation.on("tick", () => {
    link.attr("x1", d => d.source.x)
        .attr("y1", d => d.source.y)
        .attr("x2", d => d.target.x)
        .attr("y2", d => d.target.y);

    node.attr("transform", d => `translate(${d.x},${d.y})`);
  });
}