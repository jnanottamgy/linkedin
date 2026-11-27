# RUMIN: LinkedIn post

Images: `rumin-1.jpg` to `rumin-6.jpg`, uploaded in order as one multi-image post, or `rumin-carousel.pdf` uploaded as a document (carousel).

## Post text

```
A 20% jump in crude oil took an airline's operating margin from 8.33% to −0.54% in 12 months.

The airline is fictional and I typed the figures in myself. What matters is what the software did with them: it drew every step from the oil price to the profit line, and labelled which numbers were my inputs, which were model assumptions and which were simulated.

That's RUMIN, a financial-intelligence and economic-simulation platform I built over six days in September.

It maps how companies, industries, countries and economic variables connect, then lets you run "what if?" on that network. Every number on screen is tagged as an observation, an assumption, a scenario input, a simulated output or an uncertainty.

The rule I protected hardest was the boring one: never invent a figure. When I asked its AI analyst about a 20% crude shock without giving it the airline's numbers, it didn't guess. It listed the six figures it needed.

10 build phases, 105 commits, 1,771 passing tests. FastAPI and PostgreSQL underneath, React and Three.js for the 3D view of the knowledge graph.

It's ready for internal testing, not for a public launch. No model has been back-tested yet, and I'd rather say that up front than have someone find out later.

If you could stress-test one company against one shock, which would you pick?

#FinTech #BuildInPublic
```

## First comment (post it yourself right after publishing)

```
Code: github.com/jnanottamgy/Rumin-
```

Note: the repo's `main` branch only has an empty README. The code is on the
`claude/rumin-phase-1-foundation-m6zluw` branch. Merge it into `main` before sharing the link.

## Alt text (one per image)

1. RUMIN's 3D knowledge graph: economic drivers, industries, companies and places on stacked layers. Stat cards: 6 days, 10 build phases, 105 commits, 1,771 passing tests.
2. The five kinds of knowledge RUMIN labels (observation, assumption, scenario input, simulated output, uncertainty) above its knowledge-graph map of 39 records and 82 relationships.
3. Scenario Lab: Brent crude +20% on a fictional airline takes operating margin from 8.33% to −0.54%, with the pathway from oil price to profit drawn.
4. Stress test: operating profit change for crude +10%, +20%, +25% and +40%; at +40% the margin falls to −9.42%. Fictional airline, illustrative figures.
5. The AI Analyst declining to compute a crude shock without company figures and listing the six numbers it needs.
6. Status slide: ready for internal testing, not for public launch. 1,183 backend, 444 frontend, 76 integration and 68 browser tests.

## Notes

- Best window: Tue/Wed/Thu, 7:30 to 9:00 AM IST.
- Screenshots are from RUMIN running locally on its built-in sample dataset. The airline figures
  (₹180 B revenue, ₹165 B operating costs, 1.5 M kL fuel, $2.40/gal, ₹84/$) were entered for the demo.
