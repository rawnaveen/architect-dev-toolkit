# Claude pricing snapshot (checked 2026-11-08 against platform.claude.com/docs/en/about-claude/pricing)

Per million tokens, USD.

| Model | Input | Output | 5m cache write | 1h cache write | Cache read |
|---|---|---|---|---|---|
| Fable 5.1 (`claude-fable-5-1`) | 10 | 50 | 12.50 | 20 | 0.25 |
| Opus 5.5 (`claude-opus-5-5`) | 4 | 20 | 5 | 8 | 0.20 |
| Sonnet 5.5 (`claude-sonnet-5-5`) | 2 | 10 | 2.50 | 4 | 0.10 |
| Haiku 5.5 (`claude-haiku-5-5`), prompt <=100k | 0.10 | 0.50 | 0.125 | 0.20 | 0.01 |
| Haiku 5.5, prompt >100k | 0.50 | 2.50 | 0.625 | 1 | 0.05 |
| Opus 5 / 4.8 / 4.7 / 4.6 / 4.5 | 5 | 25 | 6.25 | 10 | 0.50 |
| Sonnet 4.6 / 4.5 | 3 | 15 | 3.75 | 6 | 0.30 |
| Haiku 4.5 | 1 | 5 | 1.25 | 2 | 0.10 |

- Batch: 50% off input and output; stacks with caching.
- Fast mode Opus 5.5: $8 / $40. Not available in batch.
- Data residency `inference_geo: "us"`: 1.1x on all categories.
- Web search $10 / 1,000 searches + tokens. Web fetch: tokens only. Code execution: 1,550 free hours / org / month, then $0.05 per container-hour.
- Claude 4.7+ tokenizer yields ~30% more tokens than older models for the same text.
- Default effort: `medium` on Opus 5.5 and Haiku 5.5, `high` elsewhere.
