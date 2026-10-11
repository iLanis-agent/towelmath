# Towel math

What 500 GSM actually weighs, how many bath towels a 7 kg machine really takes, and what the weekly towel habit costs a year. Exact arithmetic in the browser, every borrowed number labeled.

Live site: https://ilanis-agent.github.io/towelmath/

## The three tools

- **Weight plan** - `weightPlan(widthCm, heightCm, gsm)`: size and GSM become grams.
- **Load plan** - `loadPlan(towelG, count, machineKg)`: towels per load and loads per pile, with an honest too-heavy error.
- **Cost plan** - `costPlan(loadsWeek, costPerLoad)`: a weekly habit becomes loads and cost per year.

## Labeled norms (illustrative references, not rules)

- GSM: about 350-450 for everyday towels, 500-700 for heavy ones.
- Machine: 7-9 kg for a household washer. Load cost: about 0.9 for water and energy.

The towel's label and your machine's manual carry the real numbers.

## Files

- `index.html` / `app.html` - landing and calculators (static, no dependencies)
- `engine.js` - pure arithmetic + renderers, runs in browser and node
- `oracle.py` - python mirror of the engine; regenerates `expected.json`
- `test.js` - compares engine output to the oracle: `node test.js` (35 cases, 105 checks)

Regenerate the oracle expectations: `python3 oracle.py`
