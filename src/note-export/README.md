# note 投稿用エクスポート

Affectosphere Group の Column 14 本を、note 投稿用に整形したテキストファイル群です。

## 投稿の全体フロー

### Step 1: note アカウント作成(初回のみ)

1. https://note.com/signup にアクセス
2. メールアドレス: `inosita.2865@gmail.com`(または運用ご希望のもの)で登録
3. クリエイター名: **Affectosphere Group**
4. note ID(URL になる文字列): `affectosphere-group`(推奨。空きがあれば)
   - URL は `https://note.com/affectosphere-group` になる
5. プロフィール画像: `/public/logo/mark.png` をアップロード
6. プロフィール文:
   > 関西大学 井下敬翔研究室(Affectosphere Group)の公式 note。感情 AI 研究の最新成果を、ビジネスマン向けに 5 分で読めるコラムとして発信しています。本サイト: https://affectosphere-group.netlify.app

### Step 2: マガジンを作成(初回のみ)

1. note にログイン後、画面右上のアイコン → 「マガジン管理」または `https://note.com/affectosphere-group/m/new` に直接アクセス
2. マガジン名: **Affectosphere Group ── 感情 AI をビジネスの言葉で**
3. 説明文(例):
   > 関西大学 井下敬翔研究室の感情 AI 研究を、リスク管理・価値創出・実行可能なアクションの観点でビジネスマン向けに書き直したコラム集です。1 本 5 分で読めます。
4. カバー画像: 任意(後で `/public/logo/mark-light.png` などを使用可)
5. 公開設定: **無料・公開**
6. 「マガジンを作成」

### Step 3: 各記事を投稿

1. note 右上の **「投稿」** → **「テキスト」**
2. 本フォルダの該当 `.md` ファイルを開く
3. ファイル冒頭の `# タイトル` をコピー → note の「タイトル」欄に貼り付け
4. 本文(タイトル行以下すべて)をコピー → note の本文欄に貼り付け
5. **ヘッダ画像**:`/public/column-images/<slug>.svg` を 1200x630 程度の PNG に変換してアップロード(SVG は note 非対応)
   - 当面のプレースホルダ: ラボロゴ `/public/logo/mark.png` でも可
6. **マガジンに追加**: 投稿画面の右側「公開設定」内「マガジン」セクションで、Step 2 で作成したマガジンを選択
7. **ハッシュタグ**: 各記事ファイルの冒頭にあるハッシュタグ候補を貼り付け
8. **「公開」** をクリック

### Step 4: 本サイトとの相互リンク(任意・推奨)

各記事末尾に既に「元記事 / ラボサイトへのリンク」を入れてあります。逆方向(ラボサイト Column から note 記事へのリンク)を貼るなら:
- `src/content/column-ja/<slug>.md` の frontmatter に `noteUrl: "..."` を追加するなどの拡張を依頼してください。

## 投稿の順番(推奨)

最新研究 → 古い研究の順、もしくは話題性が高いものから:

1. nationality-llm-bias (汎用性・話題性高)
2. ai-homogenization (HR/教育に強い読者層)
3. trustworthy-emotion-ai (技術寄り読者向け)
4. five-silos (戦略・経営層向け)
5. workplace-emotion-ai (HR 全般)
6. customer-sarcasm (CX 系)
7. emotion-tempering (広告・メディア)
8. synthetic-emotion-data (データ運用)
9. llm-political-bias (PR/国際)
10. llm-governance (経営・コンプラ)
11. llm-legal-exams (リーガル)
12. ai-co-driver (自動車)
13. tourism-emotion-ai (観光)
14. personal-organizational-ai (HR テック)

**頻度の目安**: 週 2 本ペース(7 週間で全部公開)、または週 1 本ペース(14 週間)。一気に出すよりは定期投稿の方が読者育成に良い。

## 注意事項

- 各記事は本サイトと同じ内容です(SEO 観点で「同一コンテンツ」になる可能性あり)。note は canonical タグを自分でいじれないので、Google からは note 版が「コピー」扱いされる場合があります。
- 対策として、各記事末尾に「元記事は Affectosphere Group 公式サイトに掲載されています」と明示。これで重複ペナルティのリスクを下げます。
- note 内での評価(スキ・シェア)はそのまま note 内のシグナルとして機能します。
