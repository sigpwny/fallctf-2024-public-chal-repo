```
area[name="Zürich"]({{bbox}})->.zurich;
node[natural=peak](area.zurich)->.peaks;
node(around.peaks:500)[railway=station](if:number(t["ele"])>="750");

out;
```