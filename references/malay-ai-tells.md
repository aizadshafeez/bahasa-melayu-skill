# Malay AI Tells — Humanizer Pass for Malay

How machine-generated Malay gives itself away, and how to fix each case. Run this after drafting in any register. The English humanizer already covers the structural patterns; this file maps them onto Malay and adds the Malay-only tells (translation artefacts, Indonesian leakage, register mismatch).

Sources:
- DBP PRPM Khidmat Nasihat rulings, cited as [KN:kw] (URL pattern and dates in baku.md).
- MalayPrag (arXiv:2605.28782) on LLM particle failure [MP].
- `dbp-translator-claude` [DBPT] and `localize-ms` [LMS], both MIT.
- Everything else is native-speaker observation of LLM Malay output [NK]. No published catalogue of Malay AI tells exists as of Nov 2026.

---

## A. Structural tells, in Malay form

| Tell | Typical Malay form | Before → After |
|---|---|---|
| Not-X-but-Y contrast | `Ini bukan sekadar X, tetapi Y.` / `Bukan hanya… malah…` | `Ini bukan sekadar sebuah kedai kopi, tetapi sebuah ruang komuniti.` → `Kedai kopi ni jadi tempat orang kampung berkumpul tiap petang.` |
| Escalation opener | `Bukan itu sahaja,` / `Lebih menarik lagi,` / `Apa yang lebih penting,` | `Bukan itu sahaja, aplikasi ini juga menyokong bayaran DuitNow.` → `Boleh bayar guna DuitNow juga.` |
| Summary closer | `Kesimpulannya,` / `Secara keseluruhannya,` / `Akhir kata,` | `Kesimpulannya, produk ini merupakan pilihan terbaik untuk anda.` → delete the line, or end with a concrete fact: `Harga RM89, pos percuma Semenanjung.` |
| Era opener | `Dalam era digital ini,` / `Dalam dunia yang serba pantas ini,` / `Pada zaman globalisasi ini,` | `Dalam era digital ini, perniagaan dalam talian semakin popular.` → `Tahun lepas jualan online kami naik dua kali ganda.` |
| Inflated significance | `memainkan peranan penting`, `amat signifikan`, `tidak dapat dinafikan`, `sememangnya`, `sesungguhnya` | `Tidak dapat dinafikan bahawa pendidikan memainkan peranan yang amat penting dalam pembangunan negara.` → `Sekolah yang bagus boleh ubah nasib budak-budak kampung.` |
| Forced triad | `cepat, mudah dan selamat` / `inovatif, dinamik dan holistik` | `Proses yang cepat, mudah dan selamat.` → `Siap dalam 5 minit.` (keep the one claim you can prove) |
| Connector chains (SPM-essay voice) | `Selain itu,` … `Di samping itu,` … `Seterusnya,` … `Tambahan pula,` … `Oleh hal yang demikian,` | Cut most connectors. Malay prose flows with short sentences and `pun`, `juga`, `jadi`. |
| Rhetorical hooks | `Tahukah anda?` / `Bayangkan…` / `Pernahkah anda terfikir…` | `Tahukah anda bahawa 70% rakyat Malaysia…` → `70% rakyat Malaysia…` |
| Sales hype | `pengalaman yang tidak dapat dilupakan`, `permata tersembunyi`, `syurga makanan`, `menawarkan pelbagai…`, `jangan lepaskan peluang` | `Kafe ini merupakan permata tersembunyi yang menawarkan pengalaman yang tidak dapat dilupakan.` → `Kafe kecil belakang Masjid India. Nasi lemak dia RM6, sambal pedas manis.` |
| AI vocabulary | `menyelami`, `merungkai`, `meneroka`, `landskap`, `ekosistem`, `holistik`, `sinergi`, `transformasi`, `memperkasakan`, `lancar` (seamless), `komprehensif`, `dinamik` | Replace with plain verbs: `tengok`, `faham`, `cuba`, `bantu`, `senang`. |
| `pelbagai` everywhere | `menawarkan pelbagai produk`, `pelbagai cabaran`, `pelbagai jenis` | Name the items, or use `macam-macam` (casual) or `banyak`. DBP also flags `pelbagai jenis` as redundant [KN:pelbagai]. |
| `amatlah` / `sangat penting untuk` | `Adalah amat penting untuk…` / `Amatlah dihargai` | `Adalah sangat penting untuk anda menyemak dokumen.` → `Sila semak dokumen ni dulu.` |
| `justeru` as "therefore" | `Justeru, kita perlu…` | `Oleh itu, kita perlu…` / casual `Jadi, kena…`. DBP (2013) says justeru ≠ oleh itu [KN:justeru]. |
| Em dash and colon labels | `Harga — berpatutan`, `**Kelebihan:**` lists | Malay writing barely uses em dashes. Use a comma or full stop. Drop the bold labels. |
| Chatbot residue | `Semoga membantu!`, `Jangan ragu untuk bertanya`, `Sudah tentu!`, `Berikut adalah…`, `Mari kita terokai…`, `Saya harap maklumat ini berguna`, `Soalan yang bagus!` | Delete. Start with the answer. |
| Over-validation | `Saya faham perasaan anda.` / `Kebimbangan anda adalah sah.` | `Faham, memang menyakitkan hati.` or just answer. |

---

## B. Translation artefacts (English skeleton, Malay words)

| Tell | Before → After | Note |
|---|---|---|
| Dummy `Ia` subject (it is…) | `Ia adalah penting untuk kita menjaga kesihatan.` → `Kita kena jaga kesihatan.` / baku: `Menjaga kesihatan itu penting.` | DBP accepts `Ia` for things [KN:ia benda]; the tell is `Ia` as an empty subject |
| `ianya` | `Ianya mudah digunakan.` → `Mudah digunakan.` / `Ia mudah digunakan.` | DBP error [KN:ianya] |
| `di mana` / `yang mana` relative | `Ini kedai di mana saya beli kek itu.` → `Ini kedai tempat saya beli kek tu.` / `Kat kedai ni la aku beli kek tu.` | DBP error [KN:di mana] |
| `adalah` padding | `Saya adalah gembira dengan keputusan ini.` → `Saya gembira dengan keputusan ni.` | calque of "I am"; DBP forbids `adalah` before FN or FK [KN:adalah] |
| `satu` as article "a" | `Ini adalah satu idea yang bagus.` → `Idea yang bagus.` / `Bagus idea ni.` | |
| `merupakan` overuse | `Kuala Lumpur merupakan sebuah bandar yang merupakan pusat…` → `Kuala Lumpur pusat…` | one `merupakan` per page at most |
| Overuse of `anda` | `Anda boleh menghubungi kami jika anda mempunyai sebarang soalan tentang pesanan anda.` → `Ada apa-apa soalan pasal order, WhatsApp je kami ye.` | three `anda` in a sentence is the clearest robot tell |
| Passive chains with `oleh` | `Laporan telah disediakan oleh saya dan akan dihantar oleh pengurus.` → `Saya dah siapkan laporan, nanti pengurus hantar.` | first person can't take `di-…oleh` [KN:pasif diri pertama] |
| English adjective order (M-D) | `Jaya Klinik`, `pengguna-mesra`, `cili sos` → `Klinik Jaya`, `mesra pengguna`, `sos cili` | Hukum D-M [USM; LMS] |
| Literal idioms | `Patahkan kaki!` → `Semoga berjaya!` / `Di penghujung hari` → `Akhirnya` / `Sekeping kek` → `Senang je` / `mengambil tempat` → `berlangsung` | [LMS; DBPT] |
| `untuk` for every "to" | `Saya pergi ke kedai untuk membeli roti untuk sarapan untuk anak.` → `Aku singgah kedai beli roti, sarapan budak-budak.` | |
| `seseorang` for "someone" | `Jika seseorang memerlukan bantuan…` → `Kalau ada sesiapa perlukan bantuan…` / casual `Kalau ada orang nak minta tolong…` | |
| `pada masa yang sama` for "at the same time" | Use `dalam masa sama` or restructure | |
| Double plural | `banyak pelanggan-pelanggan`, `para peserta-peserta` → `banyak pelanggan`, `para peserta` | DBP error [KN:para] |
| `Adakah` / `Apakah` questions in chat | `Adakah awak sudah makan?` → `Dah makan?` / `Apakah yang awak mahu?` → `Nak apa?` | baku question forms in casual chat |

---

## C. Indonesian leakage (never acceptable in Malaysian text)

| Indonesian | Malaysian | Note |
|---|---|---|
| bisa | boleh | `bisa` = venom in MY [LMS] |
| butuh | perlu | **vulgar in MY** [LMS] |
| gampang | senang, mudah | **serious insult in MY** [NK] |
| nggak / ngga / gak (as "no") | tak | `gak` exists in MY only as `jugak` |
| aja | je | |
| banget | sangat, gila, sungguh | |
| gimana | macam mana, camne | |
| sih, dong, kok, deh, loh | — | no Malaysian equivalent; drop |
| kamu (to an adult peer) | awak, kau, you | [NK] |
| mengerti | faham | |
| sulit (difficult) | susah | `sulit` = confidential [LMS] |
| pusing (dizzy) | pening | [LMS] |
| kantor, karyawan, rapat | pejabat, pekerja/kakitangan, mesyuarat | [DBPT; LMS] |
| unggah, unduh, pengaturan, hapus | muat naik, muat turun, tetapan, padam | [LMS] |
| Senin, Minggu (Sunday), Agustus | Isnin, Ahad, Ogos | [LMS] |
| uang, mobil, bioskop, apotek | duit/wang, kereta, pawagam, farmasi | [LMS] |
| analisa, sistim | analisis, sistem | |
| ketemu | jumpa | |
| capek | penat | |

---

## D. Register mismatch (baku words in casual chat)

The single most common tell in Claude's WhatsApp-style Malay is formal vocabulary in casual chat [NK].

| Formal word in chat | Chat form | Before → After |
|---|---|---|
| tidak | tak | `Saya tidak dapat datang.` → `Tak dapat datang la.` |
| sudah | dah | `Saya sudah sampai.` → `Dah sampai.` |
| hendak / mahu / ingin | nak | `Awak hendak makan apa?` → `Nak makan apa?` |
| sahaja | je | `Sedikit sahaja.` → `Sikit je.` |
| sebentar | kejap, jap | `Tunggu sebentar.` → `Jap.` / `Kejap ye.` |
| tersebut | tu | `Barang tersebut sudah dihantar.` → `Barang tu dah pos.` |
| oleh itu / oleh yang demikian | so, jadi, sebab tu | `Oleh itu, kita batalkan.` → `So kita cancel je la.` |
| bagaimanapun / walau bagaimanapun | tapi | `Walau bagaimanapun, saya akan cuba.` → `Tapi aku try la.` |
| bagaimana | macam mana | `Bagaimana keadaan awak?` → `Macam mana, okay?` |
| mengapa | kenapa | `Mengapa awak lambat?` → `Kenapa lambat?` |
| ini / itu | ni / tu | `Kedai ini tutup.` → `Kedai ni tutup.` |
| baiklah | okay, ok, baik | `Baiklah, saya faham.` → `Ok faham.` |
| terima kasih kerana… | thanks, tq, terima kasih ye | `Terima kasih kerana memaklumkan.` → `Ok thanks bagitau.` |
| di (place) | kat | `Saya di rumah.` → `Aku kat rumah.` |
| sedang | tengah | `Saya sedang memandu.` → `Tengah drive.` |

Chat-shape tells:
- Perfect capitalisation, full stops and complete sentences in every WhatsApp bubble.
- Paragraph-long replies where people send two short lines.
- No dropped subjects (`Saya…`, `Saya…`, `Saya…`).
- Zero English in a KL office chat.
- No `InsyaAllah` / `Alhamdulillah` where a Malay family chat would have one.

Before:
> Baiklah sayang. Saya sudah sampai di pejabat. Saya akan pulang lewat sedikit pada malam ini kerana terdapat mesyuarat. Jangan lupa untuk makan ya.

After:
> Ok yang, dah sampai office. Malam ni balik lambat sikit, ada meeting. Jangan lupa makan tau.

---

## E. Fake-pasar tells (overcorrection)

When Claude tries to sound casual, it often overshoots [MP shows LLMs misjudge ke/kan/none more than half the time; the rest NK]:

| Tell | Before → After |
|---|---|
| `lah` on every sentence | `Okay lah. Saya pergi dulu lah. Jumpa esok lah.` → `Ok, gerak dulu. Jumpa esok.` |
| Particles in baku sentences | `Saya tidak tahu lah.` → `Tak tahu la.` |
| Wrong ke/kan | `Awak dah makan, ke?` (as an assumption) → `Awak dah makan, kan?`; `Kedai tu buka kan?` (genuinely unsure) → `Kedai tu buka ke?` |
| Chinese particles from a Malay voice | `Takpe lor, nanti saya buat mah.` → `Takpe la, nanti saya buat.` |
| Slang pile-up | `Weh bro, gempak gila doh, padu la wei, syok giler!` → `Gempak gila weh.` |
| Regional mix | `Hang nak gi mana, bah?` (northern + Sabah) → `Ko nak pergi mana?` |
| aku/kau to a customer or elder | `Kau nak saiz apa?` → `Sis nak saiz apa ye?` |
| English verbs in baku | `Saya akan proceed dengan permohonan tersebut.` → baku `Saya akan meneruskan permohonan ini.` / casual `Saya proceed dulu ye.` |
| Chat abbreviations in a formal email | `Sy dh hntr dokumen tu.` → `Saya telah menghantar dokumen berkenaan.` |

---

## F. Final pass checklist

1. Delete chatbot openers and closers (`Sudah tentu!`, `Semoga membantu!`, `Kesimpulannya,`).
2. Remove `ianya`, relative `di mana` / `yang mana`, and `adalah` before verbs or nouns.
3. Count `anda`: in one-to-one text it should be zero.
4. Kill `Ini bukan sekadar…`, `Bukan itu sahaja,`, `Dalam era…`, `memainkan peranan penting`, `tidak dapat dinafikan`.
5. Check register: any `tidak/sahaja/sudah/tersebut` in R3–R4, or any `x/yg/weh/la` in R1–R2?
6. Scan for Indonesian (`bisa`, `butuh`, `aja`, `nggak`, `banget`, `gimana`, `sih`).
7. Particles: at most one per short sentence; check every `ke` vs `kan`.
8. Read it aloud as a KL native. Would a real person send this? If it sounds like a Berita Harian press release in a family chat, rewrite.
