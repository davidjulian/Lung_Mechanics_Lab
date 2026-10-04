# Lung Mechanics Lab

An interactive teaching app for exploring lung and chest wall mechanics, pressure relationships, airflow, airway resistance, compliance, and illustrative hysteresis.

Teaching concept and instructional design: **David Julian**. Developed with assistance from **Codex (OpenAI)**.

**Open the app:** [Lung Mechanics Lab](https://davidjulian.github.io/Lung_Mechanics_Lab)

## Use the app

Drag the large desired volume slider to inflate or deflate the lungs. The actual volume changes continuously according to the modeled pressure gradient and airway resistance. Pressure bars and six simultaneous graphs show the resulting relationships.

- **Mechanics settings** changes resistance, lung and chest wall compliance, hysteresis, and maximum muscle pressure. Its Reset restores baseline settings while preserving volume and recorded comparisons.
- **Clear traces** removes recorded graph history. Volume trajectories and elastic balance traces otherwise accumulate across breaths and settings changes.
- **Restart** returns to baseline FRC, restores all mechanics, and clears traces.
- **Expand** opens a larger view of any graph.
- **About** credits the teaching design and development assistance.

The baseline includes modest illustrative hysteresis: up to ±10% recoil modulation. The app represents a conceptual model; its values are intended for teaching rather than clinical prediction. Extra expiratory resistance is fixed. Dynamic airway collapse and effort independent flow limitation are deferred.

## Files and local development

- `src/lung-mechanics.html`: editable app, diagrams, graphs, and continuous simulation.
- `dist/index.html`: self-contained deployable page.
- `tools/export_app.py`: rebuilds the deployable page from the source and bundled interface styles.

Rebuild with Python 3:

```sh
python tools/export_app.py
```

Serve the finished page locally:

```sh
python -m http.server 8000 --directory dist
```

Then open `http://localhost:8000`. No account or server backend is required. D3 and the tooltip positioning library load from version pinned public CDNs. Settings are saved only in the visitor's browser; graph trajectories stay in memory.

## Online publication

GitHub Pages hosts the public app at `https://davidjulian.github.io/Lung_Mechanics_Lab`. The publication workflow rebuilds and deploys `dist` automatically when changes are pushed to `main`. Only the finished app is included in the deployed website.

## Verification

Browser checks covered the six simultaneous graphs, moving volume and elastic balance traces, graph expansion, About credits, settings persistence, restart, and narrow screen layout. The optional read-only browser agent interface is feature detected; it could not be exercised in the available browser because that browser does not implement WebMCP.
