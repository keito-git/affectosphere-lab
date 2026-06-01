# 日次ルーティン:Affectosphere Group 発信パイプライン

毎日決まったフローで「論文 → 記事 → サイト + note 公開」を回すための運用設計書。
井下さんが Claude Code に **「daily run」** と指示するだけで、以下が一連で動く。

---

## 0. 1 行サマリー

> 早川が毎朝 arXiv から 5 論文選定 → 三浦が 5 記事 (JP + EN + note) 化 → 画像生成 → サイト push。

---

## 1. 役割分担

| エージェント | 担当 |
|------------|------|
| メイン Claude | オーケストレーション、品質チェック、ビルド検証、エラーリカバリ |
| **早川** (paper-watcher) | arXiv 論文選定。タスクA(発信用5件)+タスクB(研究用5件) ── 詳細は [[feedback_paper_watcher_frequency]] |
| **三浦** (pr-column) | 5 論文を v2 文体で記事化(JP + EN + note)+ GitHub push |
| 必要に応じて subagent 並列 | 3-5 並列で記事執筆を分担(socket close 回避で 3-5 が安全) |

---

## 2. 早川のタスクA(発信用論文選定)

### 選定基準

- **対象**: arXiv 直近 24 時間の新規論文
- **カテゴリ**: cs.CL / cs.AI / cs.HC / cs.CY / cs.IR / cs.SI 中心、他カテゴリも可
- **件数**: 5 件/日
- **★構成ルール(2026-06-01 改定)**: 5 件の内訳を毎日固定する。
  - **感情枠 = 1 件(必須)**: AI × 感情(感情認識・生成・倫理・Well-being・人とのインタラクション)。毎日必ず 1 本入れる。
  - **ビジネス実装枠 = 4 件**: 「ビジネスに落とし込めそうな AI 論文」。マーケに限定せず、**HR・経営管理・組織マネジメント・人材育成・オペレーション・意思決定・コンプラ・リーガル・医療・自動車**等まで幅広く取る。
    - 選定の問い: 「**この論文はこういう形でビジネスに使えるのでは?**」という具体的な応用仮説が 1 つ以上立てられるか。立たない純粋理論論文は外す。
- **形式**: arXiv ID, URL, 著者, タイトル(日英併記), 要旨 3 行サマリ, 想定ビジネス読者層, **想定ビジネス応用仮説(1-2 行)**

### 重複排除

- `/Users/ishitatakashishou/Desktop/報告/早川/論文レポート/` の過去レポートと照合
- すでに記事化済み(`src/content/column-ja/*.md`)の論文も除外

### 出力先

メイン Claude にチャットで返却 + `docs/paper-picks/<YYYY-MM-DD>_task-a.md` に保存(その後 三浦に分配)。

### ★完了トリガー(2026-06-01 追加ルール)

**タスクA の 5 件選定が完了した時点を「トリガー」とする。**
選定完了後はただちに三浦へ引き渡し、

> 記事化(JP/EN/note) → 画像生成 → `npm run build` 検証 → **三浦がサイトへ push**

までを一連で自動実行する。

- **タスクB の完了は待たない**(A と B は独立。A が終わり次第 push パイプラインを起動)。
- push は公開(Netlify 自動デプロイ)を伴う対外アクションのため、**push 直前に井下さんへ最終確認を 1 回入れる**(初期運用)。確認不要の完全自動化に切り替える場合は本節を更新する。

---

## 3. 三浦による記事執筆

### 入力
早川から渡された 5 論文の slug + メタ情報 + 主要論点。

### 執筆ルール
- [[docs/column-writing-guide.md]] 完全準拠
- v2 文体(価値先・リスク後・フォーマット自由・感情 AI 視点)
- **★ビジネス提案型(2026-06-01 改定)**: ビジネス実装枠の 4 本は「**この研究はこういう形で現場(HR・経営管理・組織・マーケ等)に使えるのでは?**」という応用提案を記事の軸に置く。学術解説で終えず、想定ビジネス読者が「自社でどう試せるか」を持ち帰れる具体イメージ(ユースケース・部署・KPI 等)を必ず 1 つ以上提示する。感情枠の 1 本は従来通り感情 AI 視点で書く。
- 字数:JP 3000-3500 字、EN 同等
- 太字未使用、AI 注記末尾、参考論文セクション必須
- 著者表記は論文の元言語(英語論文 → Keito Inoshita 等)
- **査読中ジャーナル名は本文に書かない**([[docs/column-writing-guide.md]] セクション 5a)

### 各記事の出力ファイル(5 セット)

| 種別 | パス |
|------|------|
| サイト JP 本文 | `src/content/column-ja/<slug>.md` |
| サイト EN 本文 | `src/content/column-en/<slug>.md` |
| サイト ヘッダ画像 | `public/column-images/<slug>.svg` |
| **note 本文** | `src/note-export/<YYYY-MM-DD>/<slug>.md` |
| **note 画像 SVG** | `src/note-export/<YYYY-MM-DD>/<slug>.svg` |
| **note 画像 PNG** | `src/note-export/<YYYY-MM-DD>/<slug>.png` (生成は次節) |

`<YYYY-MM-DD>` フォルダは毎日新規作成、5 セット格納。

### subagent 並列実行
- 5 論文を 3-5 個の general-purpose subagent に分配
- 各 subagent が担当論文の 5 ファイル(JP/EN/note md + SVG)を作成
- 並列度は 3-5 を上限(過去 4 並列以上で socket close 発生実績あり)

---

## 4. 画像生成(SVG → PNG)

### SVG プレースホルダ
各 subagent が記事執筆時に同時に `<slug>.svg` を生成する。テーマに合わせて
ivory/cream/amber/charcoal カラーパレットで 16:9 (1600x900) の抽象ビジュアル。

### PNG 一括変換
記事執筆完了後、メイン Claude が以下を実行:

```bash
# src/note-export/*.svg を src/note-export/*.png に変換
node scripts/svg-to-png.mjs
```

(スクリプトは `src/note-export/` 以下を**再帰探索**するため、
日付フォルダ内の SVG も自動で拾う。)

### 将来:本番画像
gpt-image-2-2026-04-21 等で本番 PNG を生成して `.svg` を `.png` に差し替える運用。
当面は SVG プレースホルダで運用。

---

## 5. ビルド検証 + push

### 実行
```bash
npm run build  # 全 77+ ページ build、エラーなければ次へ
```

### 三浦が push
```bash
git status --short
git add -A src/content/column-ja/ src/content/column-en/ src/note-export/ public/column-images/
git commit -m "Daily column drop YYYY-MM-DD: 5 papers"
git push origin main
```

### Netlify が自動デプロイ(2-3 分)

---

## 6. note 投稿(井下さん手動)

サイト本体は自動で公開。**note は井下さん手動コピペ運用**:

1. `src/note-export/<YYYY-MM-DD>/` フォルダを開く
2. 5 記事を順に note にコピペ投稿
   - 1 ファイルの 1 行目 `# タイトル` → note のタイトル欄
   - 2 行目以降 → 本文欄
   - 画像 = 同じディレクトリの `<slug>.png` をアップロード
   - マガジン「Affectosphere Group ── 感情 AI をビジネスの言葉で」に紐付け
3. 公開タイミングは適宜(全 5 件まとめて公開 / 1 日 1 件ずつ予約投稿 / 等)

詳細は [[src/note-export/README.md]] 参照。

---

## 7. 早川のタスクB(研究本人向けレポート)

タスクA とは別に、井下さん本人の研究用に毎日 5 件レポートを書く。

- 対象:井下さんの研究テーマ(感情 AI、不確実性、感情主権、サイロ論等)に直結する論文
- 件数:5 件/日
- 出力先:`/Users/ishitatakashishou/Desktop/報告/早川/論文レポート/`
- 形式:既存レポートに従う(早川の判断)

タスクA と独立。記事化はしない。サイト発信ともリンクしない。

---

## 8. 失敗時のリカバリ

| 失敗箇所 | 対応 |
|---------|------|
| 早川が 5 件取れない | 4 件で進める(無理に増やさない) |
| subagent が socket close | 失敗した subagent の担当だけ再実行 |
| ビルドエラー | エラー特定 → 該当 subagent に修正依頼 → 再ビルド |
| 三浦の push 失敗 | 通常は手動 git status で原因確認 → 再 push |

---

## 9. 運用開始判断

- **試運転**: 1 日だけ手動で全フロー回して、所要時間と品質を確認
- **本運用**: 試運転 OK なら、毎朝井下さんが「daily run」コマンドで起動

完全自動化(cron)は別途設計が必要。現状は半自動運用が現実解。

---

最終更新:2026-06-01(タスクA完了トリガー → 三浦 push のルールを明文化)
