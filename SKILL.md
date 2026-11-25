---
name: bahasa-melayu
description: Write natural Malaysian Malay in the right register, from DBP-standard bahasa baku (letters, formal email, CV, UI, reports) to everyday bahasa pasar (WhatsApp, customer DMs, IG/Threads captions, family and friends chat), then run a Malay humanizer pass so it never reads like machine Malay or Indonesian. Use whenever the user asks for anything in Malay, replies in Malay, asks to translate into Malay, or wants Malay text checked or fixed, or says "BM", "bahasa", "Melayu", "baku", "pasar", "tulis dalam BM".
---

# Bahasa Melayu: baku + pasar, humanized

Every Malay reply must pass a KL native's ear. Grammar alone is not enough. Most machine Malay comes from three faults: the **wrong register** (baku in a WhatsApp, `anda` to a spouse), English sentence shapes built from Malay words, or Indonesian leaking in.

## References (read what the job needs)

| File | Read when |
|---|---|
| `references/register-guide.md` | **Always, first.** It maps the situation to a register (R1–R4) and sets pronouns, particles, code-switching and spelling. |
| `references/baku.md` | R1–R2 text: DBP grammar, imbuhan, kata sendi, D-M, pasif, spelling, surat rasmi, modern email. |
| `references/pasar.md` | R3–R4 text: particles, short forms, pronouns by relationship, code-switching, measured adult chat norms (§8a), tone ladders. |
| `references/malay-ai-tells.md` | **Always, last.** The Malay humanizer checklist. |
| `voice.md` (optional, yours) | If it exists in this folder, it describes how *you* write Malay to specific people. It overrides the generic defaults when drafting as you. See README. |

Each rule carries a source tag:
- `[KN:…]` is a DBP Khidmat Nasihat ruling.
- `[NK]` is native-speaker convention.
- `[CORPUS]` is measured from real chat.
- `(perlu semakan)` means the sources conflict, so prefer the safer form the file names.

## How to write

1. **Pick the register before writing a word.** Identify the recipient, the relationship, the channel and whether the text goes to one person or to many. Use the decision table in `register-guide.md`.
   - If the other person wrote first, mirror their pronouns, their level of English and how much they abbreviate.
   - If unsure, go one step more polite: R3 for chat, R2 for email.
2. **Fix the pronoun pair** for the whole message (e.g. `abang ↔ yang`, `saya ↔ Encik Hafiz`, `saya ↔ sis`). Use `anda` only in text for many readers (UI, ads, forms). Never use `aku/kau` up the hierarchy or to customers.
3. **Think in Malay, not in English.** Don't draft in English and translate. Build the sentence the Malay way:
   - topic first
   - subject dropped when obvious
   - D-M order
   - natural passive (`saya tulis`, `kena marah`)
   - no dummy `Ia adalah…`
4. **Draft at the register's vocabulary.**
   - **R1–R2:** full baku (`tidak, sudah, hendak, sahaja`), DBP spelling, correct `dari/daripada` and `ialah/adalah`. No particles, no chat abbreviations.
   - **R3:** full words plus `tak, dah, nak, je, tu, ni` and a light `ye`. Work English is allowed; `x/yg/weh` are not.
   - **R4:** write the way that person types. Use particles as seasoning: `la` appears in only about 1 adult message in 20 (`pasar.md` §8a). Put English content words in a Malay frame.
   - **Shortening:** shorten long common words (`sbb, tp, mcm, yg`). Keep short core words in full (`tak, dah, nak, boleh`) unless you're mirroring someone who shortens everything.
5. **Humanizer pass, in two layers.**
   - **Layer 1, structure.** Check the draft for not-X-but-Y contrasts, one-line closers, staged openers, forced triads, dashes, inflated significance, sales language, bold labels, chatbot residue, and re-explaining what the reader already knows. If a `humanizer` skill is installed, run it in embedded mode; otherwise use the Malay forms in `malay-ai-tells.md` §A.
   - **Layer 2, Malay.** Go through the `malay-ai-tells.md` §F checklist: translation artefacts, Indonesian leakage, register mismatch, and fake-pasar overcorrection.
6. **Read it aloud as a KL native.** Would a real person send this, to this person, on this channel? If it sounds like a Berita Harian press release in a family chat, or a Gen Z TikTok comment in an email to HR, rewrite from step 1.

## Hard rules

- Malaysian Malay only, never Indonesian (`bisa, butuh, gampang, aja, nggak, banget, gimana, sih, kantor, unggah`). `butuh` and `gampang` are offensive in Malaysia.
- Never write `ianya`. Never use `di mana` or `yang mana` as relative pronouns ("the house where", "the one which").
- Don't put `adalah` before a noun phrase (use `ialah`) or before a verb phrase.
  - Write `walaupun …,` with no `tetapi`.
  - Write `antara A dengan B`.
  - Write `dalam kalangan`, not `di kalangan`.
- No double plurals (`banyak buku-buku`, `para guru-guru`).
- Never put particles inside a full baku sentence. `Saya tidak tahu lah` is wrong in every register.
- Don't stack regional markers. KL/Selangor is the default unless the user asks for a dialect.
- Religious expressions (`InsyaAllah, Alhamdulillah, Assalamualaikum`) are normal everyday Malay for Malay Muslim recipients. Don't push them onto non-Muslim recipients.
- No em dashes in Malay prose. Malay writing barely uses them.

## Output

- **Drafting or replying:** give only the final Malay text. Add a one-line English note only when the user needs to know a register choice, e.g. "kept it R3 because it's your boss".
- **Writing as the user:** follow `voice.md` if it exists. Use their real pronoun habits with that person.
- **Checking someone's Malay:** list the fixes (✗ → ✓ with the rule), then give the corrected text.
- **Translating:** translate the meaning, not the words, at the register the target reader needs.

## Sources and credits

- **DBP rulings:** about 80 dated rulings from the PRPM Khidmat Nasihat archive (prpm.dbp.gov.my), cited in `baku.md`. *Tatabahasa Dewan* is cited only through the page numbers DBP officers give in those rulings.
- **Particle research:** the MalayPrag paper, arXiv:2605.28782 (ke/kan), plus Malay discourse-particle and code-switching studies cited in `pasar.md`.
- **Chat norms:** `pasar.md` §8a is measured from a consenting native speaker's own chat history, reported as aggregates only.
- **Adapted skills:** material taken and corrected from two MIT-licensed skills, `dbp-translator-claude` by Kee-Man Chuah and i18nstack `localize-ms` by i18nagent.ai. See `THIRD_PARTY_NOTICES.md`.

Not affiliated with or endorsed by Dewan Bahasa dan Pustaka.
