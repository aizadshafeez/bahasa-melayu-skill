# bahasa-melayu

An agent skill (Claude Code, Codex and any tool that reads `SKILL.md`) that writes **natural Malaysian Malay** in the right register, then checks it for the habits that make AI Malay sound like AI.

It covers both registers Malaysians actually use:

- **Bahasa baku** follows Dewan Bahasa dan Pustaka (DBP) rulings. Use it for letters, formal email, CVs, reports and UI text.
- **Bahasa pasar** is everyday Malay. Use it for WhatsApp, customer DMs, captions, and chat with family and friends.

## Why

Language models write Malay that is grammatical but obviously not human:

- `anda` in a message to your wife
- `Ia adalah penting untuk…` (an English sentence in Malay words)
- `Semoga membantu!` at the end of everything
- `lah` on every sentence when the model tries to sound casual
- Indonesian words leaking in (`bisa`, `aja`, `banget`)

Some Indonesian leaks are offensive in Malaysia (`butuh`, `gampang`). As of November 2026 no public skill covered both registers with a Malay-specific humanizer pass.

## What's inside

| File | What it holds |
|---|---|
| `SKILL.md` | The workflow: pick the register, fix the pronouns, think in Malay, draft, run a two-layer humanizer pass, read it aloud. |
| `references/register-guide.md` | Situation → register (R1 official → R4 close friends), with pronouns, particles, code-switching, spelling, and 9 worked scenarios. |
| `references/baku.md` | DBP grammar: sentence patterns, hukum D-M, active/passive, affixes, prepositions (`dari`/`daripada`), common errors, spelling, Malaysian vs Indonesian vocabulary, letter and email conventions. About 80 DBP rulings are cited by keyword and date. |
| `references/pasar.md` | Particles (`la, kan, ke, je, pun, kot, pulak, tau…`) with meaning and position, short forms, pronouns by relationship, code-switching, slang, regional markers, tone ladders. §8a has measured norms from about 12,000 real adult chat messages. |
| `references/malay-ai-tells.md` | The Malay humanizer: structural tells in their Malay form, translation artefacts, Indonesian leakage, register mismatch, fake-pasar overcorrection, and a final checklist. |

## Install

**Claude Code**

```bash
git clone https://github.com/aizad1125/bahasa-melayu-skill ~/.claude/skills/bahasa-melayu
```

**Codex / other agents:** clone it into your agent's skills folder (e.g. `~/.agents/skills/bahasa-melayu`).

The skill triggers on its own whenever you ask for anything in Malay. Optionally, install a general humanizer skill too; this skill runs it as its first check if present, and falls back to its own Malay checklist if not.

## Make it sound like you (optional)

Create a `voice.md` next to `SKILL.md` describing how you write Malay to specific people: which pronouns, how much you shorten, your particles and emoji. The skill uses it whenever it drafts as you. `voice.md` is listed in `.gitignore`, so it stays on your machine.

## Sources and honesty

Every rule is tagged with where it came from:

- `[KN:keyword date]`: a DBP Khidmat Nasihat ruling (prpm.dbp.gov.my)
- `[NK]`: native-speaker convention, with no published source
- `[CORPUS]`: measured from a consenting native speaker's own chats, aggregates only, no real messages
- `(perlu semakan)`: the sources conflict; the file says which form is safer

A few findings differ from school textbooks. DBP accepts `sangat … sekali`. It allows `adalah` before an adjective phrase. And a 2013 ruling says `justeru` does not mean `oleh itu`.

Most of the pasar material is native judgement, because DBP treats colloquial Malay as non-standard and academic work covers only a few particles. It was reviewed by a native KL speaker. Corrections are very welcome.

Not affiliated with or endorsed by Dewan Bahasa dan Pustaka.

## Contributing

Open an issue or a pull request, especially for:

- a rule that sounds wrong to a native ear (say where you're from)
- dialect sections (northern, Kelantan/Terengganu, Negeri Sembilan, Sabah, Sarawak), kept separate from the KL default
- newer DBP rulings that settle a `perlu semakan` item

## Credits

Material was taken and corrected from two MIT-licensed skills: [`dbp-translator-claude`](https://github.com/keemanxp/dbp-translator-claude) by Kee-Man Chuah, and [`i18nstack` `localize-ms`](https://github.com/i18n-agent/i18nstack) by i18nagent.ai. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

---

## Ringkasan (BM)

Skill ini membantu AI menulis Bahasa Melayu Malaysia yang bunyinya macam orang betul-betul tulis: baku untuk surat dan e-mel rasmi, pasar untuk WhatsApp dan media sosial. Lepas tu ia semak tulisan tu supaya tak bunyi macam terjemahan mesin atau bahasa Indonesia.

Peraturan baku merujuk Khidmat Nasihat DBP. Bahagian pasar pula disemak oleh penutur asli dari KL. Kalau ada yang tak kena, buka issue ye.

## License

MIT. See [LICENSE](LICENSE).
