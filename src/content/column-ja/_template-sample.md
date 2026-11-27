---
# 研究ブログ記事のテンプレート。draft: true のあいだはサイトに出ない。
# 新しい記事はこのファイルをコピーして、ファイル名（= URL）を英数字で付け直す。
title: "記事タイトル（論文の主張を一文で）"
subtitle: "サブタイトル（論文の正式な題目など）"
date: "2026-11-27"
excerpt: "一覧に出る要約。2〜3文。"
readingMinutes: 15
# image: "/column-images/sample.png"   # 一覧のサムネイルと冒頭の図
# imageAlt: "図の説明"
authors:
  - name: "井下 敬翔"
    url: "/about/"
    affiliation: "関西大学"
tldr: "ここに3〜4文の要約。何を問い、何をして、何がわかったか。"
links:
  - label: "Paper"
    url: "https://example.com/"
  - label: "Code"
    url: "https://github.com/keito-git/"
citation: |
  @article{key2026,
    title   = {Title},
    author  = {Inoshita, Keito},
    journal = {Journal},
    year    = {2026}
  }
draft: false
---

<div class="teaser">
<div>

Read

ひとつめの要点（図や数字を1つ）。

</div>
<div>

Fix

ふたつめの要点。

</div>
<div>

Improve

みっつめの要点。

</div>
</div>

## 背景

本文。リンクは [このように](https://example.com/) 書く。

## 実験 1：問いの形で見出しを書く

<p class="experiment-label">Experiment 1</p>

<div class="setup">

**Setup**

- データ：
- モデル：
- 評価：

</div>

<figure>
  <img src="/favicon.svg" alt="図の説明" />
  <figcaption><strong>Figure 1.</strong> 図の読み方を1〜2文で書く。</figcaption>
</figure>

| 手法 | 指標A | 指標B |
|---|---|---|
| ベースライン | 0.00 | 0.00 |
| 提案手法 | 0.00 | 0.00 |

## 次にやること

## 謝辞
