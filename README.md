# Lung Mechanics Lab

An interactive teaching app for exploring lung and chest wall mechanics, pressure relationships, airflow, airway resistance, compliance, and illustrative hysteresis.

Teaching concept and instructional design: **David Julian**. Developed with assistance from **Codex (OpenAI)**.

**Open the app:** [Lung Mechanics Lab](https://davidjulian.github.io/Lung_Mechanics_Lab)

## Use the app

Drag the large **Set volume** slider to inflate or deflate the lungs. The aligned **Actual volume** display changes continuously according to the modeled pressure gradient and airway resistance. Pressure bars and six simultaneous graphs show the resulting relationships. Volume controls, breathing actions, app controls, anatomy, and graphs are visually grouped for easier navigation.

The six graphs are arranged in two rows on a laptop: Across lung pressure, Elastic balance, and Alveolar & intrapleural above Flow volume loop, Pressures over time, and Relative muscle effort. The combined pressure graph uses one scale for both pressures; its hover readout also gives their difference.

**Relative muscle effort** is a continuous pressure-demand indicator: the magnitude of signed muscle pressure divided by a fixed reference pressure of 10 cm H₂O. It is zero at rest at FRC or after Relax muscles and remains elevated while holding a volume away from the elastic balance. Both inspiratory and expiratory muscle effort contribute. These relative units are not measured force, mechanical work, power, or metabolic energy expenditure. Its recent time window matches Pressures over time; it does not accumulate across trials.

The Play buttons increase inspiratory support over 2.5 seconds, then use a rapid initial release followed by a smaller, slower decay. Residual inspiratory activity brakes elastic recoil during early expiration, as occurs in quiet breathing. An illustrative blend of fast and slow exponential decays tapers to zero 2.75 seconds after the inspiratory request peaks. With compensation off, a breath started at rest then has zero muscle effort during the remaining passive emptying. Emptying time depends on resistance and compliance. The six-second sequence may be followed by additional settling. A breath started at a held volume retains the support needed to return to that held baseline. Relax muscles removes support immediately. Manual slider control continues to support the selected held volume.

**Maintain breathing pattern** illustrates the compensatory increase in respiratory muscle activity when airway resistance rises. Generating a larger pressure difference helps preserve airflow and the amount of air moved with each breath. Students can observe greater relative effort while breath size and timing stay similar. Compensation is limited by muscle pressure capacity, and maintaining expiration against increased resistance can require expiratory muscle activity. The option is off by default and applies to Play tidal breath and Play deep breath. Reset and Restart turn it off.

- **Mechanics settings** changes resistance, lung and chest wall compliance, hysteresis, and maximum muscle pressure. Its Reset restores baseline settings while preserving volume and recorded comparisons.
- **Clear graphs** removes recorded graph history. Volume trajectories and elastic balance paths otherwise accumulate across breaths and settings changes.
- **Restart** returns to baseline FRC, restores all mechanics, and clears traces.
- The **expand icon** opens a larger view of any graph; its accessible label and tooltip name the graph.
- **Anatomical view** selects Frontal or Lateral. Recoil arrows are always shown, with a legend for lung recoil, chest wall recoil, and airflow.
- **About** includes © 2026 David Julian, development credits, and an explanation of the volume, recoil, pressure, flow, hysteresis, relative effort, and breathing compensation calculations.

Hysteresis is Off by default for introductory experiments. The optional control introduces illustrative history dependent recoil, allowing comparisons between inflation and deflation at the same volume. Both Reset and Restart return hysteresis to Off. The app represents a conceptual model; its values are intended for teaching rather than clinical prediction. Extra expiratory resistance is fixed. Dynamic airway collapse and effort independent flow limitation are deferred.

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
