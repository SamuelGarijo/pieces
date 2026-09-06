# Step 1 — archive extraction, run 2026-09-06

Method: `content-creation-engine/references/archive-extraction.md`. Order of operations:
bucket → score → flag contradictions → cut → keep-classes → story sentence → spec.

## Bucket pass (Quesenbery & Brooks, p. 162)

| Bucket | draft-2026-08-27 | summary-2026-09-06 |
|---|---|---|
| Who | the author, as archivist (§7); no persona | none — the piece speaks as "esta publicación" |
| Said, verbatim | rich: the author's own phrasing throughout | official quotes (Herzog, Lieberman) — third-party |
| Did, in order | the study's method (count, normalize); the proposed structure | procedures: the waiver → escort → censor → publish |
| Needs | "enseñar al lector a *ver* el mecanismo en su propio consumo" (§4.3) | "por qué ciertas narrativas encuentran eco" |

The draft is the voice source; the summary is the evidence list. Neither has a protagonist
with a face — see story sentence below.

## Scoring — the five signals

| # | Fragment | redundancy | action | grounding | focus | surprise | verified | Record |
|---|---|---|---|---|---|---|---|---|
| F01 | The denominator — the ratio's trap | ● both sources | ○ | ● | ● | ● contradicts own headline | ✅ re-checked; figures are CNN+MSNBC combined | `F01-el-denominador.md` |
| F02 | The sentence without a subject — passive voice | ● both | ● a verb form | ● | ● | ● | ◐ no paired active/passive study exists; NewsCord: BBC 77% passive for Palestinian deaths (one side only); CfMM "died" 50 v 7 | `F02-la-frase-sin-sujeto.md` |
| F03 | The eleven-page form — the waiver | ○ | ● sign, escort, censor, publish | ● 11 pp. | ● | ● | ✅ primary form found — **8 pages, not 11**; review is of raw footage, not final story | `F03-el-formulario.md` |
| F04 | "Militant" in the style guide, "terrorist" on air | ○ | ● | ● 560/488 | ● | ● say/do inside the subject | ✅ found (El Masry et al. 2025) — **BBC alone**; CNN is the reverse; counts include attributed uses | `F04-la-guia-de-estilo.md` |
| F05 | "Hamas-run" 915 times, "Knesset-run" never | ○ | ○ | ● | ● | ● one phrase | ✅ arXiv 2510.06453 — but 915 (v3: 951) = all doubt phrases, not the one tag; CfMM: the tag in 1,155 articles vs 119 without | `F05-la-etiqueta.md` |
| F06 | Eight years, fourteen thousand dead, and nobody knows — the Donbás hole | ● both | ○ | ● | ● hook only | ● | ✅ OHCHR figures | `F06-el-hueco.md` |
| F07 | The archive as attention — the bridge that makes it his | ● draft §4.5, §7 | ○ | ○ | ● | ○ | n/a (voice) | in this file, below |
| F08 | "No hay inocentes" — the justification quotes, Bandura | ○ summary only | ○ | ● | ◐ scope B or C? | ● | ⚠️ Law for Palestine DB, *Le Monde*; quotes are third-party | in this file, below |
| F09 | The numbers block (16,126 / 74,582 / 4–5×) | ● both | ○ | ● | ● | ○ | ◐ OHCHR yes; Gaza MoH+Israeli combined — state the sample | in this file, below |
| F10 | Two US channels ≠ "Western media" — the author's own caution vs the summary's generalization | ● (draft) vs summary | ○ | ○ | ● | ● self-correction across time | n/a | contradiction, below |
| F11 | Image warning — no victim photos; the data is the illustration | ● draft §8 | ○ | ○ | ● | ● | n/a | constraint → run log |

Legend: ● fires · ◐ partial · ○ no. Six records written (F01–F06); F07–F11 are kept here.

## Contradictions flagged (before any cut)

1. **The author's own** — F01: the headline ratio (16.1 vs 0.36, ~45×) against the raw
   mentions (4,223 vs 3,632, +33.4%). Self-correction in the draft: "hay que decirla antes
   de que la diga otro." Kept as the piece's honesty beat and its `planted-detail` /
   `rupture` candidate.
2. **The subject's** — F04: newsroom policy says "militant", output says "terrorist" 560 to
   488. An `antifrasis` written by the newsroom itself. Blocked on verification.
3. **The archive's, across time** — F10: the draft (Aug 27) says don't generalize from CNN
   and MSNBC; the summary (Sep 6) says "cobertura occidental". The later text loosened the
   earlier discipline. The piece keeps the earlier one.

## Cut list (Pulizzi), after flagging

- Throat-clearing: "Esta publicación no busca determinar quién tiene más razón…",
  "Durante la conversación se plantearon objeciones…" — cut from any copy; the *content*
  of the objections stays (counter-arguments are built in, draft §6).
- R.O.T.: the Mearsheimer / McFaul debate — the summary itself says "para contexto, no
  como conclusión"; outside argument B. Cut from the piece, kept in sources.
- Sales speak (= naming the thesis): "La tesis central es que la atención mediática…",
  "Esa asimetría de encuadre revela más sobre…" — flagged. They go to `takeaways`; never
  into a frame or a caption (`figures/alegoria.md`).

## Keep-classes

- **voice** (unguarded phrasing, draft only): "se cae en el primer comentario" · "la
  normalización es la tesis, no un detalle técnico" · "Sólo el hueco." · "Escríbelo como
  comentarista geopolítico y es uno más." · "Un archivo decide a qué le da espacio."
- **pain** (the imbalance): a reader who cannot see the mechanism in her own feed; a
  newsroom that cannot see it in its own sentences.
- **analogy** (raw metaphors, anti-adefesio check pending): the archive as coverage / the
  coverage as the collective archive (draft §7 — *not* a cliché, it is the author's own
  practice); "gold in river sediment" (mine, from the method — reject, cliché). The
  material is short on similes: the piece's figures will come from the *mechanism's
  objects* (a form, a tag, a verb with no subject, two bars), i.e. metonymy, not metaphor.

## Story sentence — three candidates

Q&B's pattern: *A [person] in [place] needs help doing [activity] because [motivation].*
The material has no protagonist with a face; each candidate supplies one.

- **(a) The newsroom.** *A newsroom in London needs help counting the dead, because its
  style guide says "militant" and its output says "terrorist".* — the say/do subject.
  Depends on F04's verification.
- **(b) The reader.** *A reader in Madrid needs help seeing what she isn't shown, because
  the sentences she reads have lost their subject.* — the mechanism (F02), and the draft's
  stated need (§4.3: teach the reader to see it in her own consumption).
- **(c) The archivist.** *A man with a personal archive needs help deciding what gets
  space, because the same decision, made by newsrooms, decides who gets mourned.* — the
  draft's §7, "el ángulo que lo hace tuyo": literally the same problem at two scales. The
  archivist is the author, elided (`figures/elipsis.md`).

**Recommendation (mine):** (c) as the piece's frame — it is the only candidate that is a
*story* rather than an analysis, which Golden's thought-piece test demands and the draft
itself demands ("escríbelo desde ahí y es un texto tuyo") — with (b) as the mechanism of
Act II. (a) waits for F04. **Decision for Samuel** — see `../02-strategy.md`.

## Spec handoff (Q&B tech-spec, p. 220)

- **Presumptions.** Attention and magnitude are independent variables (F06). The object
  of study is newsrooms, not victims (draft §6.4). Normalizing per death is the thesis,
  not a technicality (F01). Two channels are a sample, not "the media" (F10).
- **Word images** (candidate frames, one line each):
  1. Eight years. Fourteen thousand. An empty shelf where the story should be.
  2. Two bars: 16.1 and 0.36 — and, small beside them, the two raw numbers that are only
     a third apart.
  3. A sentence with its subject cut out: "fueron matados ___".
  4. An eleven-page form, a signature line, a stamp; the camera is on the other side of it.
  5. A two-word tag stuck to a number: *Hamas-run*. Beside it, a number with no tag.
  6. A personal archive: a hand deciding which of two things gets the shelf.
- **Goals.** The reader can name one mechanism (the missing subject, the tag, the form)
  and catch it in tomorrow's news. That is the third-circle test: forwardable because it
  teaches a *move*, not an opinion.
- **References.** ✅ verified: Johnson & Ali, *The Nation* (Oct 2024); Slovic 2007;
  OHCHR/HRMMU. ⚠️ to verify before use: Intercept; CMM/BBC report; arXiv "Journalistic
  Biases…"; *Journalism Research* "The Press and Gaza"; Law for Palestine; *Le Monde* on
  Channel 14; the terrorist/militant study (unnamed — find or drop). Canonical framing
  (draft §5): Herman & Chomsky (worthy/unworthy victims), Entman (framing), Slovic
  (psychic numbing). Cut: Mearsheimer debate.
- **Takeaways** (the claim — never in the image): the attention a victim receives tracks
  resemblance and alignment, not magnitude; the mechanism is grammatical and procedural
  before it is ideological; a person's archive and a society's coverage are the same
  decision at two scales.

## What the miner learned (for the `extract-fragments` skill)

- The draft (the author's own brief) was worth more than the summary (the AI synthesis):
  voice, structure, verification status, counter-arguments and the image constraint all
  came from it. **Rule for the skill: rank the author's own prior drafts above any
  synthesis, and diff later syntheses against earlier drafts for loosened discipline
  (F10).**
- Essay material has no protagonist; the story sentence had to be *supplied*, not found.
  The skill should emit candidates and stop, not pick.
- The `verified:` field did real work: of eleven fragments, three were usable before
  verification, one was blocked. After the verification pass (2026-09-06, see
  `verification-2026-09-06.md`): every checked figure in the AI summary was **off in a way
  that matters** — 11 pages → 8; "BBC and CNN" 560/488 → BBC alone, CNN the reverse; "915
  uses of Hamas-run" → 915/951 of all doubt phrases, the tag itself 1,155; "active vs
  passive by side" → no such study, one side measured. The primary numbers are *stronger*
  than the summary's in three of four cases, and the summary would have gotten the piece
  called out on all four. **Rule for the skill: an AI synthesis is a lead list, never a
  source; every figure re-anchored to its primary before it can enter a frame.** A miner
  that doesn't carry verification status hands the forge a piece that fails at step 7.
