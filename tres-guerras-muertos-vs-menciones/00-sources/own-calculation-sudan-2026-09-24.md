# Own calculation — Sudan, first 100 days (2026-09-24)

Samuel asked to fill Sudan's column on frame 1 ourselves. Done by replicating The Nation's
method exactly, not by approximating it.

## Mentions (CNN + MSNBC, 15 Apr – 23 Jul 2023)

Method: The Nation's own query, read from their public dataset
(github.com/nationmag/Gaza-Media-Bias, header of `Ukrainian Civilians - 100 days.csv`):
the people-terms in the same 15-second clip, GDELT TV API, raw counts. Script:
`method/gdelt_civilian_mentions.py`.

**Validation before use** (run 2026-09-24):

| Series | The Nation | Our run | Diff |
|---|---:|---:|---:|
| Ukraine, CNN + MSNBC | 29,534 (15,593 + 13,941) | 29,534 (15,593 + 13,941) | 0 — exact |
| Gaza, CNN + MSNBC | 15,062 | 15,050 (7,564 + 7,486) | −12 (0.08 %) — likely archive re-indexing |

**Sudan:**

| Query | CNN | MSNBC | Total |
|---|---:|---:|---:|
| Same shape as Ukraine's (includes bare "sudanese") | 512 | 70 | **582** |
| Strict (bare "sudanese" removed) | 116 | 20 | **136** |

Why two numbers: Ukraine's bare term is "ukrainians" (a plural noun, people only). In
English "Sudanese" is both the noun and the adjective, so the bare term also counts
"Sudanese army", "Sudanese military" — this war is between two armed forces. 582 therefore
overstates civilian mentions; 136 understates them slightly. The chart shows **≤ 582** —
the figure most generous to Sudan's coverage, so the gap shown is the smallest defensible.

## Deaths

**ACLED, July 2023 Sudan situation update:** "over 3,900 fatalities" since 15 Apr, cut-off
14 Jul 2023 (day 91). All fatalities from political violence — combatants included, not
civilians only. ACLED's own caveat: "a minimum documented count of deaths directly caused
by political violence", "a conservative estimate". Other figures in the window: Sudan's
health ministry 1,136 (June, officials expect higher); Al Jazeera "at least 3,000" (no
attribution). No civilian-only count for the first 100 days was found.

Denominators are therefore NOT homogeneous across the three groups and the slide says so:
Ukraine = civilians (UN estimate via The Nation), Gaza = all deaths (official), Sudan = all
deaths (ACLED minimum).

## Ratios (for the caption or the article, not the chart)

| | Mentions | Deaths | Mentions per 1,000 deaths |
|---|---:|---:|---:|
| Ukraine | 29,534 | ≈4,000 civilians | 7,384 |
| Gaza | 15,062 | >24,000 all | ≤ 628 |
| Sudan | ≤ 582 | >3,900 all | ≤ 149 (strict: ≤ 35) |

Sudan: ≥ 50× fewer mentions per death than Ukraine; ≥ 4× fewer than Gaza — on the query
most generous to Sudan.

Sources: acleddata.com/update/sudan-situation-update-july-2023-saf-faces-setbacks-armed-groups-overtake-territory-across ·
acleddata.com/methodology/how-interpret-acleds-fatality-records-sudan ·
aljazeera.com/news/2023/7/24/100-days-of-conflict-in-sudan-a-timeline ·
thenation.com/article/society/cnn-msnbc-gaza-media-bias-study/ · github.com/nationmag/Gaza-Media-Bias
