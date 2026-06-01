# /daily — Affectosphere Daily Run

毎朝の論文取得 → 記事化 → サイト公開を一連で回すスラッシュコマンド。
詳細フローは `docs/daily-routine.md`、文体ルールは `docs/column-writing-guide.md` を参照。

---

## 実行手順(順番に進める)

### Step 1: 早川に論文選定を依頼(タスクA)

`paper-watcher` サブエージェント(早川)を呼び出し、以下を依頼する:

> 今日の Affectosphere サイト発信用に、arXiv 直近 24 時間の新規論文から 5 件を選定してください。基準:
> - cs.CL / cs.AI / cs.HC / cs.CY / cs.IR / cs.SI 中心
> - AI × 感情、または ビジネス応用可能性ある AI 論文
> - 重複排除:`/Users/ishitatakashishou/Desktop/報告/早川/論文レポート/` の過去レポートと `src/content/column-ja/*.md` の既存記事と照合
> - 各論文について arXiv ID、URL、著者、タイトル(日英併記)、要旨 3 行サマリ、想定ビジネス読者層を返答
> - Affectosphere 発信用 (タスクA) のみ。タスクB(研究本人向け)は別途。

### Step 2: subagent 並列で記事執筆

早川の返答を受けたら、5 論文を 3-5 個の `general-purpose` サブエージェントに分配する。各 subagent に以下を指示:

> 担当論文を、`docs/column-writing-guide.md` の v2 文体で 1 記事化してください。
>
> 必読(まず Read):
> - `docs/column-writing-guide.md` ── ライティングガイド(全章、特に 5a 査読中誌名ルール)
> - `src/content/column-ja/nationality-llm-bias.md` ── JP v2 サンプル
> - `src/note-export/nationality-llm-bias.md` ── note 整形サンプル
>
> 出力先 5 ファイル:
> - `src/content/column-ja/<slug>.md`
> - `src/content/column-en/<slug>.md`
> - `public/column-images/<slug>.svg`(amber+ivory トーンの抽象 16:9 SVG)
> - `src/note-export/<YYYY-MM-DD>/<slug>.md`
> - `src/note-export/<YYYY-MM-DD>/<slug>.svg`(↑ と同じ SVG をコピー)
>
> `<YYYY-MM-DD>` は今日の日付。subagent 自身でフォルダ作成。
>
> 厳守:
> - 太字 `**` 禁止
> - 著者表記は論文元言語(英語論文 → Keito Inoshita 等)
> - 査読中ジャーナル名は本文に書かない(arXiv / SSRN のみ可)
> - AI 注記末尾必須
> - 字数 JP 3000-3500 字、EN 同等

並列度は 3-5 を上限(過去 4 並列以上で socket close 実績あり)。記事数が 5 なら 3+2 / 2+2+1 などで分割。

### Step 3: 画像 PNG 化

```bash
npm run notes:images
```

`scripts/svg-to-png.mjs` が `src/note-export/` 配下を再帰探索して全 SVG を PNG 化。

### Step 4: ビルド検証

```bash
npm run build
```

エラーが出たら、該当 subagent に修正依頼してリトライ。

### Step 5: 三浦に push 依頼

`pr-column` サブエージェント(三浦)に以下を依頼:

> Affectosphere Daily Run YYYY-MM-DD 分の記事 5 本(JP/EN/note + 画像)を push してください。
>
> 実行:
> ```bash
> cd /Users/ishitatakashishou/Desktop/研究/affectosphere-lab/
> git status --short
> git add -A src/content/column-ja/ src/content/column-en/ src/note-export/ public/column-images/
> git commit -m "Daily column drop YYYY-MM-DD: 5 papers"
> git push origin main
> ```
>
> 完了後、commit ハッシュと公開 URL リストを報告。

### Step 6: 井下さんに完了報告

- 公開された記事 5 本の URL リスト(サイト本体)
- `src/note-export/<YYYY-MM-DD>/` フォルダパス(井下さんが note 投稿時に開く)
- 所要時間
- エラーや要確認事項

---

## 失敗時のリカバリ

- 早川が 5 件取れない → 4 件で進める
- subagent が socket close → 該当 subagent の担当だけ再実行
- ビルドエラー → エラー特定 → 該当 subagent に修正依頼 → 再ビルド
- 三浦の push 失敗 → git status で原因確認 → 必要なら手動介入

---

## メモ

- 完全自動化(cron + launchd)は別途要設計。現状は井下さんが `/daily` と打つ半自動運用
- タスクB(早川の研究本人向けレポート、`/Desktop/報告/早川/論文レポート/`)はこのコマンドの対象外
