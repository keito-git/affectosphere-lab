# Affectosphere Group サイト開発ログ

サイトの主要マイルストーンと判断ポイントを時系列で記録。
詳細は `git log` を参照。**新しい意思決定は冒頭に追記する**(逆時系列)。

---

## 2026-06-01

### Services ページ追加 + Nav 12 タブ化(commit: TBD)

- 収益化強化のため `src/pages/services.astro` を新設(JP/EN 両言語)
- メニュー: ① 企業内研修・勉強会、② 講演・登壇、③ コンサルティング
- 単価表記:メニュー内容のみ掲載、料金は「要相談」(初回 30 分無料相談 → 見積もり)
- AI for Science は「学際的研究共同」、Services は「企業向けサービス」と棲み分け
- nav は 11 → 12 タブ化、位置は AI for Science の隣
- note 投稿用 `src/note-export/` に各記事の SVG 画像をコピー(記事と画像をセットで管理する運用に統一)

### ドキュメント整備(本ファイル)

- `docs/column-writing-guide.md` ── けんすう・DOWM 風のラフな文体エッセンスを採用、新規記事はストーリー型構成へ
- `docs/development-log.md` ── 本ファイル。今後の意思決定をここに残す

---

## 2026-05-31

### 参考論文セクション正規化(commit: 1132820 / 0780476)

- 各 Column 記事の出典 blockquote を削除、`## 参考論文` セクションに置換
- publications.ts から正確な引用情報を取得(著者・タイトル・出版先・年)
- 著者表記は**論文の元言語に従う**:英語論文は Keito Inoshita 表記、日本語論文は井下敬翔 表記
- 複数論文ベースの記事は全部列挙
- frontmatter `basedOnPaper` は主要論文 1 本のタイトル(原言語)

### note 投稿用エクスポート(commit: be293ef)

- `src/note-export/` に全 14 記事を note 投稿用に整形
- 整形ルール:frontmatter 除去、ハッシュタグ追加、チェックリスト変換、HTML 除去、フッターに元記事リンクと Affectosphere Group 紹介
- README.md にアカウント作成 + マガジン作成 + 投稿手順を記載
- マガジン設計: A 案(1 マガジン集約「Affectosphere Group ── 感情 AI をビジネスの言葉で」)
- アカウント: ラボ名「Affectosphere Group」で新規

### SEO Package A(commit: ea0b76b / 939ee97)

- `@astrojs/sitemap@3.2.1` 導入(3.7.3 は Astro 4 系で reduce エラー出たためダウングレード)
- astro.config.mjs に `site: "https://affectosphere-group.netlify.app"`
- BaseLayout に追加:canonical / hreflang (ja/en/x-default) / og:url / og:locale / per-page ogImage prop / jsonLd prop
- Column 個別記事に Article JSON-LD 構造化データ
- robots.txt に Sitemap URL 明示
- Google Search Console 認証メタタグ追加

### Column 第 2 弾 13 本(commit: debaaae / b09ceb1)

- 最新論文から順に 13 本追加(計 14 本)
- subagent 並列で執筆、3 並列を採用(前回 4 並列で全 socket close した経緯)
- 各記事:JP + EN + SVG プレースホルダのセット

### Column 1 本目: nationality-llm-bias(commit: 0215395 / b3d34fc / b58aa45)

- Astro Content Collection を新規導入(`src/content/config.ts`)
- 2 collection:`column-ja` / `column-en`
- 個別記事ページ `src/pages/column/[slug].astro` / `src/pages/en/column/[slug].astro`
- 一覧ページを Content Collection 駆動に書き換え
- 構成方針:
  - 第 1 版「リスク + 4 つの問い」→ ユーザフィードバックでビジネス強化リライト
  - 太字未使用、AI 注記末尾追加、本文幅広げ(max-w-3xl → 5xl)
  - SVG プレースホルダ画像(`/public/column-images/`)

---

## 2026-05-30

### 英語版サイト一括構築(commit: ba76767)

- `/en/` ルートで英語版全 23 ページ
- 言語切替トグル(ヘッダ右上に JP/EN)
- 全データを `src/data/*.en.ts` に複製・英訳
- `MANIFESTO.en.md` 追加
- 英語版フォーム:`en-contact` / `en-ai-for-science`

### サイト本体の調整(commit: 5a4eb10 / 6ad53fb / cf82459)

- Hero 中央寄せ + 改行統合
- 本文幅広げ(`max-w-prose` → 撤廃して全幅)
- 研究領域タイトル中央寄せ
- Member カード縮小(役職・所属を一段小さく)
- Awards / Grants の説明文削除

### Netlify Forms 検出修正(commit: 02a964e)

- `public/__forms.html` に hidden フォームスケルトン追加(Astro + Netlify Forms の検出取りこぼし対策)

---

## 2026-05-27 〜 2026-05-29

### 初期構築(commit: 9129d64 〜 開発期間)

- Astro + Tailwind CSS の静的サイトとして start
- カラーパレット: ivory / cream / amber / charcoal / slate
- フォント: Times New Roman + Noto Serif JP
- ラボ名: Affectosphere Group(関西大学・井下敬翔研究室)
- 全 23 ページのスケルトン作成
- データ層: `src/data/*.ts` に research-domains, publications, awards, grants, people, news, ai-for-science, column 等
- MANIFESTO.md(Vision エッセイ)を `?raw` import で `/affectosphere/` ページに埋め込み
- ナビゲーション 11 タブ(英語ラベル)
- GitHub 連携: keito-git/affectosphere-lab(三浦 = pr-column subagent が GitHub 操作を独占)
- Netlify デプロイ: affectosphere-group.netlify.app

---

## 主要な設計判断

### なぜ Astro?
- 静的サイトで十分(SSR 不要)、ビルド速度が速い、Markdown と TS のミックスがしやすい

### なぜ Content Collection?
- Column 記事を Markdown で書きたい(エディタが軽快、git diff が読みやすい)
- frontmatter の型保証が欲しい
- ファイル数が増えても自動取り込み

### なぜ subagent に GitHub 操作を独占させた?
- ユーザの明示的セキュリティ要件「GitHub の権限ですが、三浦にのみあります」
- メイン Claude は git/gh コマンドを直接実行しない、すべて pr-column 経由

### なぜ note 投稿用は別ファイルにしている?
- note は SVG 非対応、HTML タグ非対応、脚注非対応
- サイト本体と同一 Markdown のままだと表示崩れ
- 整形済みファイルを別途用意することで、井下さんはコピペ投稿のみで済む

### なぜ SVG プレースホルダ?
- gpt-image での本番画像生成までの繋ぎ
- ファイル名が決まっているので、井下さんは PNG 生成後に同名で差し替えるだけで済む

---

最終更新: 2026-06-01
