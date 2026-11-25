# Third-party notices

This skill includes material adapted from the two MIT-licensed works below. Their notices are reproduced as the licence requires.

## dbp-translator-claude

- Source: https://github.com/keemanxp/dbp-translator-claude
- What was used: the register notes, Indonesian false friends, DBP term preferences, and the warnings against passive overuse and literal idioms.
- What was changed: the guidance on stiff, over-formal phrasing was replaced, because the original's own example sentence reads as machine Malay.

```
MIT License

Copyright (c) 2026 Kee-Man Chuah

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## i18nstack (localize-ms)

- Source: https://github.com/i18n-agent/i18nstack
- What was used: Malaysian vs Indonesian technical vocabulary, the false friends (`butuh`, `pusing`, `sulit`, `punggung`), number and RM formats, the affix rules for UI strings, and the D-M examples.
- What was changed, with the DBP basis for each:
  - `keretapi` → `kereta api` (DBP Khidmat Nasihat, 14 Sep 2012)
  - `kamu` is no longer listed as the friendly "you"; in Malaysia it is teacher-to-child or exhortative.
  - The advice to put a comma before `yang` was dropped.

```
MIT License

Copyright (c) 2026 i18nagent.ai

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Other sources

- **Dewan Bahasa dan Pustaka, PRPM Khidmat Nasihat** (prpm.dbp.gov.my): rulings are cited by keyword and date and paraphrased. Only short set phrases are quoted, such as the letter formulas and short example corrections.
- **MalayPrag** (arXiv:2605.28782) and the other academic works listed in `references/basahan.md`, cited for their findings.

## Fonts in the README images

The SVGs in `assets/` embed **Cairo** (Copyright 2009 The Cairo Project Authors) and **Instrument Serif** (Copyright 2022 The Instrument Serif Project Authors), both under the SIL Open Font License 1.1. The font files and their licences are in `assets/fonts/`.
